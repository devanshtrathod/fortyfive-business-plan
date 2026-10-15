"""Build the FortyFive logo options: outlined SVGs for three directions, plus a review sheet.

Every glyph is outlined from Latin Modern (GUST Font License), so nothing depends on fonts.
Run:  py -3.13 brand/make_logos.py
"""
import os

from outline import bounds, path

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'options')
INK, PAPER, BLUE = '#121211', '#f6f4ee', '#2a78d6'

ROMAN = 'lmroman10-regular.otf'
DEMI = 'lmromandemi10-regular.otf'
ITAL = 'lmroman10-italic.otf'
CAPS = 'lmromancaps10-regular.otf'
YF = {5: -18}  # nudge the second F towards the y, so FortyFive reads as one word with two capitals
S = 512        # monograms are drawn on a 512 square


def place(font, text, size, cx=None, cy=None, left=None, baseline=None, tracking=0.0, kern=None, colour=INK):
    """Outline text; centre its ink box on (cx, cy), or set it at (left, baseline)."""
    x0, y0, x1, y1 = bounds(font, text, size, tracking=tracking, kern_adjust=kern)
    if cx is not None:
        ox, by = cx - (x0 + x1) / 2, cy - (y0 + y1) / 2
    else:
        ox, by = left - x0, baseline
    d, _ = path(font, text, size, x=ox, baseline=by, tracking=tracking, kern_adjust=kern)
    return '<path fill="%s" d="%s"/>' % (colour, d), (x0 + ox, y0 + by, x1 + ox, y1 + by)


def svg(w, h, body, title):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %.1f %.1f" width="%.1f" height="%.1f" role="img" aria-label="%s">'
            '<title>%s</title>%s</svg>' % (w, h, w, h, title, title, body))


def svg_body(s):
    return s[s.index('</title>') + 8:-6]


# ---------- monograms ----------
def mono_tile(fg=PAPER, bg=INK):
    """Direction 1: 45. in Demi, paper on an ink square."""
    rect = '<rect width="%d" height="%d" fill="%s"/>' % (S, S, bg)
    num, _ = place(DEMI, '45.', 300, cx=S / 2 + 4, cy=S / 2 + 2, colour=fg)
    return svg(S, S, rect + num, 'FortyFive')


def mono_ring(fg=INK, bg=None):
    """Direction 2: italic 45 inside a ring, the way an examiner circles a total."""
    base = '<rect width="%d" height="%d" fill="%s"/>' % (S, S, bg) if bg else ''
    ring = '<circle cx="%d" cy="%d" r="%.1f" fill="none" stroke="%s" stroke-width="%.1f"/>' % (S / 2, S / 2, S * 0.44, fg, S * 0.026)
    num, _ = place(ITAL, '45', 300, cx=S / 2 - 2, cy=S / 2 + 3, colour=fg)
    return svg(S, S, base + ring + num, 'FortyFive')


def mono_box(fg=INK, bg=None):
    """Direction 3: 45 in a ruled box, like the total box on an exam paper."""
    base = '<rect width="%d" height="%d" fill="%s"/>' % (S, S, bg) if bg else ''
    box = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="none" stroke="%s" stroke-width="%.1f"/>' % (
        S * 0.07, S * 0.07, S * 0.86, S * 0.86, fg, S * 0.022)
    num, _ = place(ROMAN, '45', 318, cx=S / 2, cy=S / 2 + 2, colour=fg)
    return svg(S, S, base + box + num, 'FortyFive')


def monogram(direction, fg=INK, tile_fg=PAPER):
    if direction == 'tile':
        return mono_tile(fg=tile_fg, bg=fg)
    return mono_ring(fg=fg) if direction == 'ring' else mono_box(fg=fg)


def word_style(direction):
    """(font, text, tracking, kern) for each direction's wordmark."""
    if direction == 'caps':
        return CAPS, 'FORTYFIVE', 0.16, None
    return ROMAN, 'FortyFive', 0.0, YF


# ---------- wordmarks and lockups ----------
def wordmark(font=ROMAN, size=120, fg=INK, kern=YF, text='FortyFive', tracking=0.0):
    x0, y0, x1, y1 = bounds(font, text, size, tracking=tracking, kern_adjust=kern)
    pad = size * 0.04
    w, h = x1 - x0 + 2 * pad, y1 - y0 + 2 * pad
    p, _ = place(font, text, size, left=pad, baseline=-y0 + pad, tracking=tracking, kern=kern, colour=fg)
    return svg(w, h, p, 'FortyFive'), (w, h)


def lockup(direction, fg=INK, tile_fg=PAPER, size=120):
    """Monogram on the left, wordmark on the right, the capitals centred on the monogram."""
    font, text, tracking, kern = word_style(direction)
    cap = -bounds(font, 'F', size)[1]
    m = cap * (1.75 if direction == 'caps' else 1.62)   # monogram height
    gap = m * 0.36
    base_y = m * 0.5 + cap * 0.5
    g = '<g transform="scale(%.5f)">%s</g>' % (m / S, svg_body(monogram(direction, fg, tile_fg)))
    word, (_, _, wx1, wy1) = place(font, text, size, left=m + gap, baseline=base_y, tracking=tracking, kern=kern, colour=fg)
    return svg(wx1 + size * 0.02, max(m, wy1), g + word, 'FortyFive')


def stacked(direction, fg=INK, tile_fg=PAPER, size=120):
    """Monogram above the wordmark, centred."""
    font, text, tracking, kern = word_style(direction)
    x0, y0, x1, y1 = bounds(font, text, size, tracking=tracking, kern_adjust=kern)
    ww = x1 - x0
    m = ww * 0.42
    g = '<g transform="translate(%.2f,0) scale(%.5f)">%s</g>' % ((ww - m) / 2, m / S, svg_body(monogram(direction, fg, tile_fg)))
    gap = size * 0.42
    word, (_, _, _, by1) = place(font, text, size, left=0, baseline=m + gap - y0, tracking=tracking, kern=kern, colour=fg)
    return svg(ww + 2, by1 + 2, g + word, 'FortyFive')


DIRS = [('tile', '1. The full stop', '"45." in bold numerals on an ink square. The full stop is the idea: 45, full stop. Nothing else. It matches the line "Mastering the IB Diploma. Nothing else." and the tile already used in the deck and the dashboard.'),
        ('ring', "2. The examiner's ring", "An italic 45 inside a ring, the way an examiner circles the total at the top of a marked script. Warmer and more personal; thin lines need care at tiny sizes."),
        ('caps', '3. The title page', "FORTYFIVE in spaced capitals with the 45 in a ruled box, like the total box on an exam paper. The most formal and institutional, like a university press.")]


def img(name, h, extra=''):
    return '<img src="options/%s.svg" style="height:%dpx%s" alt="">' % (name, h, extra)


def main():
    os.makedirs(OUT, exist_ok=True)
    for key, _, _ in DIRS:
        files = {
            'monogram': monogram(key),
            'monogram-reversed': {'tile': mono_tile(fg=INK, bg=PAPER), 'ring': mono_ring(fg=PAPER, bg=INK),
                                  'caps': mono_box(fg=PAPER, bg=INK)}[key],
            'lockup': lockup(key),
            'lockup-reversed': lockup(key, fg=PAPER, tile_fg=INK),
            'stacked': stacked(key),
        }
        for name, content in files.items():
            open(os.path.join(OUT, '%s-%s.svg' % (key, name)), 'w', encoding='utf-8').write(content)
    open(os.path.join(OUT, 'wordmark-roman.svg'), 'w', encoding='utf-8').write(wordmark()[0])
    open(os.path.join(OUT, 'wordmark-caps.svg'), 'w', encoding='utf-8').write(
        wordmark(font=CAPS, text='FORTYFIVE', tracking=0.16, kern=None)[0])

    sections = []
    for key, title, note in DIRS:
        sections.append('''
<section class="dir">
  <h2>%s</h2><p class="note">%s</p>
  <div class="row big"><div class="paper">%s</div><div class="ink">%s</div></div>
  <div class="row"><div class="paper">%s</div><div class="paper">%s</div></div>
  <div class="row"><div class="paper sizes">%s %s %s %s</div>
    <div class="paper tab"><span class="fav">%s</span> FortyFive: Mastering the IB</div>
    <div class="paper app">%s</div></div>
  <div class="header"><span>%s</span><nav>Courses &nbsp; Tutors &nbsp; Coursework &nbsp; Free tools</nav><b>Join</b></div>
</section>''' % (title, note,
                 img(key + '-lockup', 64), img(key + '-lockup-reversed', 64),
                 img(key + '-stacked', 150), img(key + '-monogram', 150),
                 img(key + '-monogram', 64), img(key + '-monogram', 32), img(key + '-monogram', 24), img(key + '-monogram', 16),
                 img(key + '-monogram', 16), img(key + '-monogram', 96, ';border-radius:21px'), img(key + '-lockup', 30)))

    page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>FortyFive Logo Options</title>
<style>
body{margin:0;background:#e9e7e0;font:15px/1.5 system-ui,sans-serif;color:#121211}
main{max-width:1080px;margin:0 auto;padding:28px 16px 60px}
h1{font-size:28px;margin:0 0 6px} .lead{color:#4a4945;max-width:760px}
.dir{background:#fffffe;border:1px solid #dcdad2;border-radius:12px;padding:22px;margin:22px 0}
h2{margin:0 0 4px;font-size:20px} .note{color:#4a4945;margin:0 0 16px;max-width:820px}
.row{display:flex;gap:14px;flex-wrap:wrap;margin-top:14px}
.row > div{flex:1 1 300px;border-radius:10px;padding:22px;display:flex;align-items:center;justify-content:center;gap:18px;min-height:110px}
.paper{background:#f6f4ee}.ink{background:#121211}
.sizes img{display:block}.tab{justify-content:flex-start!important;font-size:13px;color:#4a4945}
.tab .fav{display:inline-flex;margin-right:8px}
.header{margin-top:14px;background:#f6f4ee;border-radius:10px;padding:14px 18px;display:flex;align-items:center;gap:24px;font-size:14px;color:#4a4945}
.header nav{flex:1}.header b{background:#121211;color:#f6f4ee;padding:8px 14px;font-weight:600}
</style></head><body><main>
<h1>FortyFive logo options</h1>
<p class="lead">Three formal, typographic directions, all set in Latin Modern (the font of the deck and every PDF) and outlined, so they never depend on a font being installed. Each is shown large, reversed, stacked, at favicon sizes, as an app icon and in a website header at real size. The recommended one, direction 1, is exported in full in brand/final.</p>
%s
</main></body></html>''' % ''.join(sections)
    open(os.path.join(HERE, 'LOGO OPTIONS.html'), 'w', encoding='utf-8').write(page)
    print('wrote', len(os.listdir(OUT)), 'svgs')


if __name__ == '__main__':
    main()
