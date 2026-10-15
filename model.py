"""Model v3: courses + honest tutor marketplace, passion-project lens, year one (Dec 2026 to Nov 2027), INR.
Adds what v2 left out: 18% GST on FortyFive's fee and on course sales (a platform that collects lesson
payments is an e-commerce operator, so it registers for GST from day one), Razorpay Route's transfer fee
on every payout, and one-off set-up costs kept apart from running costs.
Same formulas as the dashboard calculator."""
import math

GST = 0.18
GW = 0.02 * (1 + GST)      # payment gateway: 2% + GST, on the full amount paid
TR = 0.0025 * (1 + GST)    # Route transfer fee: 0.25% + GST, on what is passed to a tutor or author
ONBOARD_MULT = 1.5         # tutors checked per active tutor (some leave or never start)


def run(s):
    c = s['commission'] / 100
    gmv = s['tutors'] * s['hours'] * s['rate'] * s['months']
    fee = gmv * c                                  # FortyFive's fee, GST inside
    tutor_earn = gmv - fee
    paid = s['enrol'] * (1 - s['scholar'] / 100)
    course_sales = paid * s['price']               # GST inside
    gst = (fee + course_sales) * GST / (1 + GST)
    pay_fees = gmv * GW + tutor_earn * TR + course_sales * GW
    course_net = course_sales * (1 - GST / (1 + GST) - GW)
    author_pay = course_net * s['authored'] / 100 * s['author_share'] / 100
    pay_fees += author_pay * TR
    checks = math.ceil(s['tutors'] * ONBOARD_MULT) * s['check']
    running = {
        'Hosting and security': s['hosting'] * 12,
        'Video: course streaming and live rooms': s['video'] * 12,
        'Background checks on new tutors': checks,
        'CA: GST, TDS and filings': s['ca'],
        'Promotion': s['marketing'],
    }
    oneoff = {'Lawyer: terms, privacy, safeguarding': s['legal'], 'Recording kit': s['equipment']}
    money_in = fee + course_sales
    out = gst + pay_fees + author_pay + sum(running.values()) + sum(oneoff.values())
    per_hour = s['rate'] * (c / (1 + GST) - GW - (1 - c) * TR)
    monthly_running = sum(running.values()) / 12
    course_month = (course_net - author_pay * (1 + TR)) / 12
    need = (monthly_running - course_month) / per_hour if per_hour > 0 else float('inf')
    return dict(gmv=gmv, fee=fee, tutor_earn=tutor_earn, course_sales=course_sales, paid=paid, gst=gst,
                pay_fees=pay_fees, author_pay=author_pay, running=running, oneoff=oneoff, money_in=money_in,
                out=out, net=money_in - out, per_hour=per_hour, hours_now=s['tutors'] * s['hours'],
                hours_needed=max(0, need), monthly_running=monthly_running, course_month=course_month)


BASE = dict(tutors=15, hours=8, rate=1200, commission=10, months=8,
            enrol=120, price=1499, scholar=20, authored=50, author_share=70,
            hosting=5000, video=1500, check=1000, ca=30000, marketing=10000,
            legal=20000, equipment=15000)
SCEN = {
    'Small': dict(BASE, tutors=6, hours=6, rate=1000, months=6, enrol=40, scholar=25, authored=0,
                  hosting=2500, video=500, ca=24000, marketing=0, legal=15000, equipment=8000),
    'Base': BASE,
    'Big': dict(BASE, tutors=40, hours=12, rate=1400, months=10, enrol=600, hosting=10000, video=3000,
                ca=48000, marketing=60000, legal=30000, equipment=25000),
}

if __name__ == '__main__':
    # the receipt for one 1,000-rupee lesson at a 10% fee
    f = 100
    print(f"receipt: tutor 900 | GST {f*GST/(1+GST):.2f} | gateway {1000*GW:.2f} | transfer {900*TR:.2f} | "
          f"kept {f - f*GST/(1+GST) - 1000*GW - 900*TR:.2f}")
    for k, s in SCEN.items():
        r = run(s)
        print(f"{k:5} GMV {r['gmv']:>10,.0f} tutors {r['tutor_earn']:>10,.0f} fee {r['fee']:>8,.0f} | courses {r['course_sales']:>9,.0f} "
              f"({r['paid']:.0f} paid) authors {r['author_pay']:>8,.0f} | GST {r['gst']:>8,.0f} payfees {r['pay_fees']:>7,.0f} "
              f"running {sum(r['running'].values()):>8,.0f} oneoff {sum(r['oneoff'].values()):>6,.0f} | in {r['money_in']:>9,.0f} "
              f"net {r['net']:>9,.0f} | per hr {r['per_hour']:.2f} | hours now {r['hours_now']} need {r['hours_needed']:.1f} "
              f"| monthly run {r['monthly_running']:,.0f} course/mo {r['course_month']:,.0f}")
