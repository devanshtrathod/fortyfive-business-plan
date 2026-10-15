"""Pull per-subject student counts out of the IB DP/CP final statistical bulletin.

pdftotext misaligns rows, so this works from word boxes: subject labels on the left,
the Students figure is the first number to the right whose vertical centre falls
inside the label's row band.
"""
import re
import sys

import pymupdf

doc = pymupdf.open(sys.argv[1])
dump = len(sys.argv) > 2
out = []
for pno, page in enumerate(doc):
    words = page.get_text('words')  # x0,y0,x1,y1,word,block,line,wno
    if not any(w[4] in ('HL', 'SL') for w in words):
        continue
    # group words into visual lines by block/line
    lines = {}
    for w in words:
        lines.setdefault((w[5], w[6]), []).append(w)
    segs = []
    for ws in lines.values():
        ws.sort(key=lambda w: w[0])
        segs.append((min(w[0] for w in ws), min(w[1] for w in ws), max(w[2] for w in ws), max(w[3] for w in ws),
                     ' '.join(w[4] for w in ws)))
    if dump and pno + 1 == int(sys.argv[2]):
        for s in sorted(segs, key=lambda s: (round(s[1]), s[0])):
            print(f'{s[0]:6.1f} {s[1]:6.1f} {s[3]:6.1f}  {s[4]}')
    # labels: segments in the left column ending in HL/SL (or followed by a lone HL/SL segment)
    left = [s for s in segs if s[0] < 200 and re.search(r'[A-Z]{3}', s[4])]
    nums = [s for s in segs if s[0] >= 150 and re.match(r'^[\d,]+\b', s[4])]
    for s in sorted(left, key=lambda s: s[1]):
        m = re.search(r'\b(HL|SL)$', s[4])
        label, y0, y1 = s[4], s[1], s[3]
        if not m:
            nxt = [t for t in segs if t[4] in ('HL', 'SL') and t[0] < 200 and 0 <= t[1] - y1 < 6]
            if not nxt:
                continue
            label = s[4] + ' ' + nxt[0][4]
            y1 = nxt[0][3]
        cands = [n for n in nums if y0 - 1 <= (n[1] + n[3]) / 2 <= y1 + 1]
        if cands:
            n = min(cands, key=lambda n: n[0])
            val = int(n[4].split()[0].replace(',', ''))
            out.append((pno + 1, label, val))

if not dump:
    for p, n, v in out:
        print(f'{p}\t{v}\t{n}')
