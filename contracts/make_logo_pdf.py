"""Turn the brand lockup SVG into a vector PDF that pdflatex can include. Run: python make_logo_pdf.py"""
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
SVG = HERE.parent / "brand" / "final" / "fortyfive-lockup.svg"
OUT = HERE / "fortyfive-lockup.pdf"

svg = SVG.read_text(encoding="utf-8")
w, h = 679.7, 132.2  # viewBox of the lockup, in px
html = f"""<!doctype html><html><head><style>@page {{ size: {w}px {h}px; margin: 0 }} html,body {{ margin:0 }} svg {{ display:block; width:{w}px; height:{h}px }}</style></head><body>{svg}</body></html>"""

with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")
    pg = b.new_page()
    pg.set_content(html)
    pg.pdf(path=str(OUT), width=f"{w}px", height=f"{h}px", print_background=True, page_ranges="1")
    b.close()
print("wrote", OUT)
