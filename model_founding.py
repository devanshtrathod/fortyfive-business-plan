"""Model v4 (15 Oct 2026): the founding-partner launch and the under-18 rate, on top of model.py's maths.

Fee tiers (what the tutor keeps of the price; FortyFive's fee is the rest, GST inside):
  founding partner, launch period : adult 50%, under 18 40%
  founding partner, after launch  : adult 92%, under 18 82%   (a better rate for life)
  standard                        : adult 90% (coaching 85%), under 18 80%
Year one is Dec 2026 to Nov 2027 with 8 paid months (Feb to Sep 2027); the launch period is the first
LAUNCH_MONTHS of them. Run: python model_founding.py"""
from model import GST, GW, TR, BASE, run

TIERS = {
    'Founding partner, launch period (adult)': 0.50,
    'Founding partner, launch period (under 18)': 0.40,
    'Founding partner, after launch (adult)': 0.92,
    'Founding partner, after launch (under 18)': 0.82,
    'Standard tutor (adult)': 0.90,
    'Standard graduate tutor (under 18)': 0.80,
}


def receipt(price, keep):
    tutor = price * keep
    fee = price - tutor
    gst = fee * GST / (1 + GST)
    pay = price * GW + tutor * TR
    return dict(price=price, tutor=tutor, fee=fee, gst=gst, pay=pay, kept=fee - gst - pay)


def lessons(groups):
    """groups: list of (tutors, hours/month, rate, months, keep share). Returns GMV, tutor pay, FortyFive's
    fee, GST on the fee, payment fees and what FortyFive keeps from lessons."""
    t = dict(gmv=0.0, tutor=0.0, fee=0.0, gst=0.0, pay=0.0)
    for n, h, rate, m, keep in groups:
        g = n * h * rate * m
        r = receipt(g, keep) if g else dict(tutor=0, fee=0, gst=0, pay=0)
        t['gmv'] += g
        for k in ('tutor', 'fee', 'gst', 'pay'):
            t[k] += r[k]
    t['kept'] = t['fee'] - t['gst'] - t['pay']
    return t


def year_one(name, adults, minors, later_adults, later_minors, hours, rate_a, rate_m, launch_months, months, s):
    after = months - launch_months
    groups = [
        (adults, hours, rate_a, launch_months, 0.50), (minors, hours, rate_m, launch_months, 0.40),
        (adults, hours, rate_a, after, 0.92), (minors, hours, rate_m, after, 0.82),
        (later_adults, hours, rate_a, after, 0.90), (later_minors, hours, rate_m, after, 0.80),
    ]
    L = lessons(groups)
    # courses and running costs come from model.py with lessons switched off
    c = run(dict(s, tutors=0))
    course_kept = c['course_sales'] - c['course_sales'] * GST / (1 + GST) - c['course_sales'] * GW - c['author_pay'] * (1 + TR)
    running = sum(c['running'].values())
    oneoff = sum(c['oneoff'].values())
    # background checks are charged per tutor checked, so recount them for the real number of tutors
    checks = round((adults + minors + later_adults + later_minors) * 1.5) * s['check']
    running = running - c['running']['Background checks on new tutors'] + checks
    net = L['kept'] + course_kept - running - oneoff
    return dict(name=name, L=L, course_kept=course_kept, running=running, oneoff=oneoff, net=net,
                tutors=adults + minors + later_adults + later_minors)


SCEN = [
    # name, founding adults, founding under-18s, later adults, later under-18s, hours/month, adult rate, under-18 rate
    ('Small', 5, 1, 2, 0, 6, 1000, 700, 6, 8, dict(BASE, enrol=40, scholar=25, authored=0, hosting=2500, video=500,
                                                  ca=24000, marketing=0, legal=15000, equipment=8000)),
    ('Base', 8, 2, 5, 1, 8, 1200, 800, 6, 8, BASE),
    ('Big', 15, 5, 20, 5, 12, 1400, 900, 6, 8, dict(BASE, enrol=600, hosting=10000, video=3000, ca=48000,
                                                   marketing=60000, legal=30000, equipment=25000)),
]

if __name__ == '__main__':
    print('Receipt for a Rs 1,000 lesson:')
    for k, keep in TIERS.items():
        r = receipt(1000, keep)
        print(f"  {k:44s} tutor {r['tutor']:7.2f} | fee {r['fee']:6.2f} | GST {r['gst']:6.2f} | payment {r['pay']:5.2f} | kept {r['kept']:7.2f}")
    print()
    for sc in SCEN:
        y = year_one(*sc)
        L = y['L']
        print(f"{y['name']:5} tutors {y['tutors']:2d} | GMV {L['gmv']:>10,.0f} | to tutors {L['tutor']:>10,.0f} | lessons kept {L['kept']:>9,.0f} "
              f"| courses kept {y['course_kept']:>8,.0f} | running {y['running']:>8,.0f} | one-off {y['oneoff']:>6,.0f} | NET {y['net']:>9,.0f}")
