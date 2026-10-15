"""First look: the wordmark and the numerals in every Latin Modern cut worth trying. Writes explore.html."""
import os

from outline import bounds, path

HERE = os.path.dirname(os.path.abspath(__file__))
CUTS = [('lmroman17-regular.otf', 'Roman 17'), ('lmroman12-regular.otf', 'Roman 12'), ('lmroman10-regular.otf', 'Roman 10'),
        ('lmromandunh10-regular.otf', 'Dunhill 10'), ('lmromandemi10-regular.otf', 'Demi 10'), ('lmroman10-bold.otf', 'Bold 10'),
        ('lmromancaps10-regular.otf', 'Caps 10'), ('lmroman10-italic.otf', 'Italic 10')]

rows = []
for f, label in CUTS:
    cells = []
    for text, size in (('FortyFive', 64), ('45', 96), ('45.', 96)):
        x0, y0, x1, y1 = bounds(f, text, size)
        pad = 10
        w, h = x1 - x0 + 2 * pad, y1 - y0 + 2 * pad
        d, _ = path(f, text, size, x=-x0 + pad, baseline=-y0 + pad)
        cells.append('<svg width="%.0f" height="%.0f" viewBox="0 0 %.1f %.1f"><path d="%s"/></svg>' % (w, h, w, h, d))
    rows.append('<tr><td class="l">%s</td><td>%s</td></tr>' % (label, '</td><td>'.join(cells)))
    if 'caps' in f:
        x0, y0, x1, y1 = bounds(f, 'FORTYFIVE', 54, tracking=0.12)
        d, _ = path(f, 'FORTYFIVE', 54, x=-x0 + 10, baseline=-y0 + 10, tracking=0.12)
        rows.append('<tr><td class="l">Caps, spaced</td><td colspan="3"><svg width="%.0f" height="%.0f"><path d="%s"/></svg></td></tr>'
                    % (x1 - x0 + 20, y1 - y0 + 20, d))

html = '''<!doctype html><meta charset="utf-8"><title>Logo exploration</title>
<style>body{margin:0;padding:24px;background:#f6f4ee;font:14px system-ui}table{border-collapse:collapse}
td{padding:10px 18px;border-bottom:1px solid #dcdad2;vertical-align:middle}td.l{color:#7a7873;width:110px}path{fill:#121211}</style>
<table>%s</table>''' % ''.join(rows)
open(os.path.join(HERE, 'explore.html'), 'w', encoding='utf-8').write(html)
print('ok')
