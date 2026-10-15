"""Build the FortyFive pitch deck: deck_template.html -> deck.html (fonts embedded) -> FortyFive Pitch Deck.pdf.

Fonts are Latin Modern (the LaTeX font), embedded as base64 so the HTML works from file:// and the PDF carries them.
Numbers about schools come from ../schools/summary.json (written by build_schools.py); the model numbers
come from ../model.py.
Run: python build_deck.py
"""
import base64
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LM = r'C:\Users\USER\AppData\Local\Programs\MiKTeX\fonts\opentype\public\lm'
CH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
sys.path.insert(0, ROOT)
import model  # noqa: E402

FONTS = [('LM Roman', 'lmroman12-regular.otf', 400, 'normal'), ('LM Roman', 'lmroman12-bold.otf', 700, 'normal'),
         ('LM Roman', 'lmroman12-italic.otf', 400, 'italic'), ('LM Roman Display', 'lmroman17-regular.otf', 400, 'normal'),
         ('LM Roman Caps', 'lmromancaps10-regular.otf', 400, 'normal')]


def font_css():
    out = []
    for fam, f, w, st in FONTS:
        b = base64.b64encode(open(os.path.join(LM, f), 'rb').read()).decode('ascii')
        out.append('@font-face{font-family:"%s";src:url(data:font/otf;base64,%s) format("opentype");font-weight:%d;font-style:%s}' % (fam, b, w, st))
    return '\n'.join(out)


def inr(n):
    n = int(round(n))
    s = str(abs(n))
    last3, rest = s[-3:], s[:-3]
    parts = []
    while len(rest) > 2:
        parts.insert(0, rest[-2:])
        rest = rest[:-2]
    if rest:
        parts.insert(0, rest)
    return ('\u2212' if n < 0 else '') + '\u20b9' + ','.join(parts + [last3]) if parts else ('\u2212' if n < 0 else '') + '\u20b9' + last3


def bars(rows, maxv, fmt):
    """Single-series horizontal bars; the emphasised row is blue, the rest grey."""
    h = []
    for label, v, ours in rows:
        w = 0 if maxv == 0 else v / maxv * 100
        lab = '<b>%s</b>' % label if ours else label
        h.append('<div class="brow"><div class="bl">%s</div><div class="track"><div class="bar" style="width:%.2f%%;background:%s"></div>'
                 '<span class="bval num">%s</span></div></div>' % (lab, w * 0.82, 'var(--blue)' if ours else 'var(--grey-bar)', fmt(v)))
    return '\n'.join(h)


def be_svg():
    r = model.run(model.BASE)
    W, H = 640, 300
    ml, mr, mt, mb = 70, 18, 28, 46
    pw, ph = W - ml - mr, H - mt - mb
    x1, y1 = 200, 25000
    X = lambda h: ml + h / x1 * pw
    Y = lambda v: mt + (y1 - v) / y1 * ph
    inc = lambda h: r['course_month'] + r['per_hour'] * h
    o = ['<svg viewBox="0 0 %d %d" width="%d" height="%d" role="img" aria-label="Income and running costs a month by lesson hours">' % (W, H, W, H)]
    for v in range(0, y1 + 1, 5000):
        o.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="#e4e2da" stroke-width="1"/>' % (ml, W - mr, Y(v), Y(v)))
        o.append('<text x="%d" y="%.1f" text-anchor="end" font-size="15" fill="#7a7873">%s</text>' % (ml - 10, Y(v) + 5, '\u20b90' if v == 0 else '\u20b9%dk' % (v // 1000)))
    o.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="#c3c2b7" stroke-width="1"/>' % (ml, W - mr, Y(0), Y(0)))
    for h in range(0, x1 + 1, 50):
        o.append('<text x="%.1f" y="%d" text-anchor="middle" font-size="15" fill="#7a7873">%d</text>' % (X(h), mt + ph + 20, h))
    o.append('<text x="%.1f" y="%d" text-anchor="middle" font-size="15" fill="#7a7873">Lesson hours a month</text>' % (ml + pw / 2, H - 4))
    now = r['hours_now']
    o.append('<line x1="%.1f" x2="%.1f" y1="%d" y2="%d" stroke="#c3c2b7" stroke-width="1"/>' % (X(now), X(now), mt, mt + ph))
    o.append('<text x="%.1f" y="%d" text-anchor="middle" font-size="15" fill="#4a4945">Base case: %d h</text>' % (X(now), mt - 9, now))
    o.append('<path d="M%.1f %.1f H%.1f" stroke="#eb6834" stroke-width="2.5" fill="none" stroke-linecap="round"/>' % (X(0), Y(r['monthly_running']), X(x1)))
    o.append('<path d="M%.1f %.1f L%.1f %.1f" stroke="#2a78d6" stroke-width="2.5" fill="none" stroke-linecap="round"/>' % (X(0), Y(inc(0)), X(x1), Y(inc(x1))))
    need = r['hours_needed']
    o.append('<circle cx="%.1f" cy="%.1f" r="6" fill="#121211" stroke="#fffffe" stroke-width="2"/>' % (X(need), Y(r['monthly_running'])))
    o.append('<text x="%.1f" y="%.1f" text-anchor="end" font-size="16" fill="#121211">Pays for itself at %d h</text>' % (X(need) - 12, Y(r['monthly_running']) - 12, round(need)))
    o.append('<text x="%d" y="%.1f" text-anchor="end" font-size="16" fill="#4a4945">Income</text>' % (W - mr, Y(inc(x1)) - 10))
    o.append('<text x="%d" y="%.1f" text-anchor="end" font-size="16" fill="#4a4945">Running costs</text>' % (W - mr, Y(r['monthly_running']) + 22))
    o.append('</svg>')
    return '\n'.join(o)


def main():
    s = open(os.path.join(HERE, 'deck_template.html'), encoding='utf-8').read()
    summ_path = os.path.join(ROOT, 'schools', 'summary.json')
    summ = json.load(open(summ_path, encoding='utf-8')) if os.path.exists(summ_path) else {}
    s = s.replace('%%FONTS%%', font_css())
    # the logo's monogram, outlined (brand/final), so the cover matches the logo exactly
    s = s.replace('%%MONOGRAM%%', open(os.path.join(ROOT, 'brand', 'final', 'fortyfive-monogram.svg'), encoding='utf-8').read())
    s = s.replace('%%IN_DP%%', str(summ.get('in_dp', 196)))
    s = s.replace('%%IN_NOV%%', str(summ.get('in_nov', '?')))
    s = s.replace('%%INTL_DP%%', format(summ.get('intl_dp', 0), ','))
    s = s.replace('%%INTL_NOV%%', format(summ.get('intl_nov', 0), ','))
    countries = summ.get('by_country', [])[:7]
    cmax = max([c['dp'] for c in countries] or [1])
    s = s.replace('%%COUNTRY_BARS%%', bars([(c['name'], c['dp'], c['cc'] == 'IN') for c in countries], cmax, lambda v: str(v)))
    keeps = [('FortyFive', 900, True), ('Superprof, paid on the site', 900, False), ('Preply, after 400+ hours', 820, False),
             ('Wyzant', 750, False), ('Preply, a new tutor', 670, False), ('Preply, first lesson', 0, False)]
    s = s.replace('%%KEEP_BARS%%', bars(keeps, 1000, lambda v: '%s (%d%%)' % (inr(v), v // 10)))
    s = s.replace('%%BE_SVG%%', be_svg())
    # slide numbers: each %%N%% becomes the number of the slide it sits in
    parts = s.split('<section class="slide')
    s = parts[0] + ''.join('<section class="slide' + p.replace('%%N%%', str(k)) for k, p in enumerate(parts[1:], 1))
    left = [t for t in ('%%IN_NOV%%', '%%INTL_DP%%', '%%COUNTRY_BARS%%', '%%BE_SVG%%') if t in s]
    if left:
        print('unfilled tokens:', left)
    out = os.path.join(HERE, 'deck.html')
    open(out, 'w', encoding='utf-8').write(s)
    pdf = os.path.join(ROOT, 'FortyFive Pitch Deck.pdf')
    subprocess.run([CH, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--window-size=1400,900',
                    '--virtual-time-budget=6000', '--print-to-pdf=' + pdf, 'file:///' + out.replace('\\', '/')],
                   capture_output=True, timeout=120)
    print('wrote', out, 'and', pdf, os.path.getsize(pdf) if os.path.exists(pdf) else 'NO PDF')


if __name__ == '__main__':
    main()
