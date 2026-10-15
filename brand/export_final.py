"""Export the recommended logo (direction 1, the full stop) as a complete kit in brand/final/.

SVGs come from make_logos.py; PNGs are rendered by Chrome through Playwright at exact sizes;
favicon.ico is packed with Pillow. Run with the default python (it has Playwright):
    py -3.13 brand/make_logos.py && python brand/export_final.py
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FINAL = os.path.join(HERE, 'final')
os.makedirs(FINAL, exist_ok=True)

# 1. SVGs, made by the logo module under py -3.13 (it needs uharfbuzz)
code = r'''
import os, sys
sys.path.insert(0, r"%s")
from make_logos import mono_tile, lockup, stacked, wordmark, place, svg, ROMAN, INK, PAPER, S
F = r"%s"
def w(name, s): open(os.path.join(F, name), "w", encoding="utf-8").write(s)
w("fortyfive-monogram.svg", mono_tile())
w("fortyfive-monogram-reversed.svg", mono_tile(fg=INK, bg=PAPER))
w("fortyfive-lockup.svg", lockup("tile"))
w("fortyfive-lockup-reversed.svg", lockup("tile", fg=PAPER, tile_fg=INK))
w("fortyfive-stacked.svg", stacked("tile"))
w("fortyfive-wordmark.svg", wordmark()[0])
w("fortyfive-wordmark-display.svg", wordmark(font="lmroman17-regular.otf", kern={5: -14})[0])
w("favicon.svg", mono_tile())
w("fortyfive-tagline.svg", wordmark(font="lmroman12-regular.otf", size=72, text="Mastering the IB Diploma. Nothing else.", kern=None)[0])
# maskable icon: full-bleed ink, numerals inside the 80%% safe zone
num, _ = place("lmromandemi10-regular.otf", "45.", 236, cx=S / 2 + 3, cy=S / 2 + 2, colour=PAPER)
w("icon-maskable.svg", svg(S, S, '<rect width="%%d" height="%%d" fill="%%s"/>' %% (S, S, INK) + num, "FortyFive"))
print("svgs ok")
''' % (HERE, FINAL)
subprocess.run(['py', '-3.13', '-c', code], check=True)

# 2. PNGs at exact sizes
from playwright.sync_api import sync_playwright  # noqa: E402

PNGS = [('favicon.svg', 16, 'favicon-16.png'), ('favicon.svg', 32, 'favicon-32.png'), ('favicon.svg', 48, 'favicon-48.png'),
        ('favicon.svg', 180, 'apple-touch-icon.png'), ('favicon.svg', 192, 'icon-192.png'), ('favicon.svg', 512, 'icon-512.png'),
        ('icon-maskable.svg', 512, 'icon-maskable-512.png')]


def file_url(p):
    """A data URI: pages made with set_content can't load file:// images."""
    import base64
    return 'data:image/svg+xml;base64,' + base64.b64encode(open(p, 'rb').read()).decode('ascii')


with sync_playwright() as p:
    b = p.chromium.launch(channel='chrome')
    pg = b.new_page(device_scale_factor=1)
    for src, size, out in PNGS:
        pg.set_viewport_size({'width': size, 'height': size})
        pg.set_content('<html><body style="margin:0"><img src="%s" style="display:block;width:%dpx;height:%dpx"></body></html>'
                       % (file_url(os.path.join(FINAL, src)), size, size))
        pg.wait_for_timeout(150)
        pg.screenshot(path=os.path.join(FINAL, out), clip={'x': 0, 'y': 0, 'width': size, 'height': size})
    # social share card, 1200 x 630
    pg.set_viewport_size({'width': 1200, 'height': 630})
    pg.set_content('''<html><body style="margin:0;width:1200px;height:630px;background:#f6f4ee;display:flex;flex-direction:column;
justify-content:center;padding:0 96px;box-sizing:border-box;font-family:Georgia,serif">
<img src="%s" style="height:96px;width:auto;align-self:flex-start">
<div style="margin-top:44px;height:1px;background:#dcdad2"></div>
<img src="%s" style="height:auto;width:760px;margin-top:40px;align-self:flex-start">
</body></html>''' % (file_url(os.path.join(FINAL, 'fortyfive-lockup.svg')), file_url(os.path.join(FINAL, 'fortyfive-tagline.svg'))))
    pg.wait_for_timeout(200)
    pg.screenshot(path=os.path.join(FINAL, 'og-image.png'))
    b.close()

# 3. favicon.ico from the small PNGs
from PIL import Image  # noqa: E402

ims = [Image.open(os.path.join(FINAL, 'favicon-%d.png' % n)).convert('RGBA') for n in (16, 32, 48)]
ims[2].save(os.path.join(FINAL, 'favicon.ico'), sizes=[(16, 16), (32, 32), (48, 48)], append_images=ims[:2])
print('exported', sorted(os.listdir(FINAL)))
sys.exit(0)
