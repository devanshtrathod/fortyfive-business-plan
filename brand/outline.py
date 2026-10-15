"""Turn text set in Latin Modern into outlined SVG paths, kerned by HarfBuzz.

Latin Modern is under the GUST Font License (free to use and modify). Outlining the
glyphs means the logo files never depend on the font being installed.
"""
import os

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

LM = os.path.join(os.environ['LOCALAPPDATA'], 'Programs', 'MiKTeX', 'fonts', 'opentype', 'public', 'lm')
_cache = {}


def _load(name):
    if name not in _cache:
        path = os.path.join(LM, name)
        data = open(path, 'rb').read()
        face = hb.Face(data)
        font = hb.Font(face)
        tt = TTFont(path)
        _cache[name] = (font, tt, tt['head'].unitsPerEm, tt.getGlyphSet())
    return _cache[name]


def shape(name, text, tracking=0.0, features=None):
    """Return [(glyph_name, x_offset_units)], total advance in units, and the font's upem."""
    font, tt, upem, _ = _load(name)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, features or {'kern': True, 'liga': False})
    order = tt.getGlyphOrder()
    x, out = 0.0, []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        out.append((order[info.codepoint], x + pos.x_offset))
        x += pos.x_advance + tracking * upem
    return out, x - tracking * upem, upem


def path(name, text, size, x=0.0, baseline=0.0, tracking=0.0, features=None, kern_adjust=None):
    """SVG path data for `text` at `size` px, starting at (x, baseline). Returns (d, width_px).

    kern_adjust: optional {index: units} to nudge glyph i (and everything after it) by hand.
    """
    glyphs, adv, upem = shape(name, text, tracking, features)
    _, _, _, gs = _load(name)
    s = size / upem
    pen = SVGPathPen(gs, ntos=lambda v: ('%.2f' % v).rstrip('0').rstrip('.'))
    shift = 0.0
    for i, (g, gx) in enumerate(glyphs):
        if kern_adjust and i in kern_adjust:
            shift += kern_adjust[i]
        tp = TransformPen(pen, (s, 0, 0, -s, x + (gx + shift) * s, baseline))
        gs[g].draw(tp)
    return pen.getCommands(), (adv + shift) * s


def bounds(name, text, size, tracking=0.0, features=None, kern_adjust=None):
    """Ink bounds (x0, y0, x1, y1) in px for text drawn at baseline 0, y down."""
    from fontTools.pens.boundsPen import BoundsPen
    glyphs, adv, upem = shape(name, text, tracking, features)
    _, _, _, gs = _load(name)
    s = size / upem
    bp = BoundsPen(gs)
    shift = 0.0
    for i, (g, gx) in enumerate(glyphs):
        if kern_adjust and i in kern_adjust:
            shift += kern_adjust[i]
        gs[g].draw(TransformPen(bp, (s, 0, 0, -s, (gx + shift) * s, 0)))
    return bp.bounds
