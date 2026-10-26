"""Generate the icon family for the portfolio site and its projects.

One dark tile, one glyph per property. The site's >_ prompt is drawn in
code below and has hand-authored SVGs (favicon.svg, safari-pinned-tab.svg);
keep those in sync with glyph_prompt. Project glyphs are shape lists in
PROJECTS, and this script writes every project file from them, favicon.svg
included, so there is nothing to keep in sync by hand.

Requires Pillow:  pip install pillow
Run:              python scripts/gen_icons.py
"""
import math
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
ICONS = ROOT / "assets" / "icons"

BG = "#0d1117"     # site dark background
GREEN = "#4ade80"  # site accent

S = 8  # supersample factor; draw at 512*S, downscale with Lanczos
C = 512 * S


def transform(scale):
    """Map 512-space coords to the supersampled canvas, scaling about center."""
    def t(x, y):
        return ((256 + (x - 256) * scale) * S, (256 + (y - 256) * scale) * S)
    return t


def glyph_prompt(d, t, k, color=GREEN):
    """>_ terminal prompt."""
    w = 54 * S * k
    a, b, c = t(148, 168), t(258, 256), t(148, 344)
    d.line([a, b], fill=color, width=int(w))
    d.line([b, c], fill=color, width=int(w))
    for p in (a, b, c):
        r = w / 2
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=color)
    d.rounded_rectangle([*t(300, 317), *t(412, 371)], radius=27 * S * k, fill=color)


# --- project glyphs ---
#
# A glyph is a list of shapes in 512x512 space, drawn in order over the tile:
#   ("rect", x0, y0, x1, y1, radius, color)
#   ("circle", cx, cy, r, color)
#   ("ring", cx, cy, r, stroke, color)        r is the stroke's centerline
#   ("line", [(x, y), ...], stroke, color)    round caps and joins
#   ("poly", [(x, y), ...], color)
# Shapes in BG color cut holes. Everything is clipped to the tile.


def gear(cx, cy, teeth, r_body, r_tip, tooth_w, r_hole, color):
    out = [("circle", cx, cy, r_body, color)]
    for i in range(teeth):
        a = 2 * math.pi * i / teeth
        ux, uy = math.cos(a), math.sin(a)        # along the tooth
        vx, vy = -uy, ux                         # across it
        h = tooth_w / 2
        pts = [(cx + ux * r + vx * s, cy + uy * r + vy * s)
               for r, s in ((r_body - 10, -h), (r_tip, -h * 0.8), (r_tip, h * 0.8), (r_body - 10, h))]
        out.append(("poly", [(round(x, 1), round(y, 1)) for x, y in pts], color))
    out.append(("circle", cx, cy, r_hole, BG))
    return out


PROJECTS = {
    # jigsaw piece: knob on top, notch cut from the right edge
    "hood": [
        ("rect", 138, 156, 390, 408, 28, "#fbbf24"),
        ("circle", 264, 156, 52, "#fbbf24"),
        ("circle", 390, 282, 52, BG),
    ],
    # calculator: body, screen, 3x3 buttons
    "ti-js": [
        ("rect", 168, 116, 344, 396, 32, "#58a6ff"),
        ("rect", 196, 150, 316, 212, 12, BG),
    ] + [("circle", x, y, 16, BG) for y in (256, 310, 364) for x in (212, 256, 300)],
    # eye: ring around a pupil
    "consciousness-map": [
        ("ring", 256, 256, 124, 44, "#a78bfa"),
        ("circle", 256, 256, 54, "#a78bfa"),
    ],
    # gear
    "factorio-hub": gear(256, 256, 8, 112, 158, 50, 48, "#cbd5e1"),
    # level meter bars
    "resonate": [
        ("rect", x - 18, 256 - h / 2, x + 18, 256 + h / 2, 18, "#f472b6")
        for x, h in ((152, 96), (204, 196), (256, 280), (308, 168), (360, 88))
    ],
    # three color swatches
    "strooplang": [
        ("rect", 136, 140, 376, 204, 32, "#f87171"),
        ("rect", 136, 224, 376, 288, 32, "#4ade80"),
        ("rect", 136, 308, 376, 372, 32, "#60a5fa"),
    ],
    # open book
    "urth": [
        ("poly", [(108, 156), (244, 180), (244, 380), (108, 356)], "#2dd4bf"),
        ("poly", [(404, 156), (268, 180), (268, 380), (404, 356)], "#2dd4bf"),
    ],
    # license plate: two bolts, three characters
    "vanity": [
        ("rect", 88, 160, 424, 352, 36, "#22d3ee"),
        ("circle", 136, 196, 12, BG),
        ("circle", 376, 196, 12, BG),
    ] + [("rect", x, 228, x + 56, 316, 10, BG) for x in (150, 228, 306)],
    # 2x2 letter tiles
    "wordle": [
        ("rect", 140, 140, 248, 248, 18, "#4ade80"),
        ("rect", 264, 140, 372, 248, 18, "#facc15"),
        ("rect", 140, 264, 248, 372, 18, "#6b7280"),
        ("rect", 264, 264, 372, 372, 18, "#4ade80"),
    ],
    # basketball
    "madness": [
        ("circle", 256, 256, 152, "#f97316"),
        ("line", [(256, 104), (256, 408)], 14, BG),
        ("line", [(104, 256), (408, 256)], 14, BG),
        ("ring", 40, 256, 160, 14, BG),
        ("ring", 472, 256, 160, 14, BG),
    ],
    # question mark: three quarters of a ring, a stem, a dot
    "riddles": [
        ("ring", 256, 200, 84, 52, "#e879f9"),
        ("poly", [(256, 200), (140, 200), (140, 316), (256, 316)], BG),
        ("circle", 172, 200, 26, "#e879f9"),
        ("line", [(256, 284), (256, 312)], 52, "#e879f9"),
        ("circle", 256, 388, 30, "#e879f9"),
    ],
    # envelope with a flap
    "letteropener": [
        ("rect", 104, 156, 408, 356, 28, "#fb7185"),
        ("line", [(128, 184), (256, 280), (384, 184)], 24, BG),
    ],
    # crown
    "command.games": [
        ("poly", [(128, 344), (128, 168), (200, 256), (256, 148), (312, 256), (384, 168), (384, 344)], "#a3e635"),
        ("rect", 128, 364, 384, 396, 12, "#a3e635"),
    ],
    # arrows pointing in: narrow the page
    "wikiwidth": [
        ("poly", [(104, 168), (104, 344), (216, 256)], "#fde68a"),
        ("poly", [(408, 168), (408, 344), (296, 256)], "#fde68a"),
        ("rect", 244, 140, 268, 372, 12, "#fde68a"),
    ],
    # magnifying glass
    "ripgrep": [
        ("ring", 228, 228, 96, 48, "#dea584"),
        ("line", [(300, 300), (388, 388)], 56, "#dea584"),
    ],
}


def draw_shapes(d, t, k, shapes):
    for kind, *a in shapes:
        if kind == "rect":
            x0, y0, x1, y1, r, color = a
            d.rounded_rectangle([*t(x0, y0), *t(x1, y1)], radius=r * S * k, fill=color)
        elif kind == "circle":
            cx, cy, r, color = a
            x, y = t(cx, cy)
            r = r * S * k
            d.ellipse([x - r, y - r, x + r, y + r], fill=color)
        elif kind == "ring":
            cx, cy, r, w, color = a
            x, y = t(cx, cy)
            outer = (r + w / 2) * S * k
            d.ellipse([x - outer, y - outer, x + outer, y + outer], outline=color, width=round(w * S * k))
        elif kind == "line":
            pts, w, color = a
            pts = [t(*p) for p in pts]
            w = w * S * k
            d.line(pts, fill=color, width=round(w), joint="curve")
            for x, y in pts:
                d.ellipse([x - w / 2, y - w / 2, x + w / 2, y + w / 2], fill=color)
        elif kind == "poly":
            pts, color = a
            d.polygon([t(*p) for p in pts], fill=color)


def svg(shapes):
    """The same glyph as favicon.svg."""
    n = lambda v: f"{v:g}"
    out = []
    for kind, *a in shapes:
        if kind == "rect":
            x0, y0, x1, y1, r, color = a
            out.append(f'<rect x="{n(x0)}" y="{n(y0)}" width="{n(x1 - x0)}" height="{n(y1 - y0)}" rx="{n(r)}" fill="{color}"/>')
        elif kind == "circle":
            cx, cy, r, color = a
            out.append(f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}" fill="{color}"/>')
        elif kind == "ring":
            cx, cy, r, w, color = a
            out.append(f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}" fill="none" stroke="{color}" stroke-width="{n(w)}"/>')
        elif kind == "line":
            pts, w, color = a
            p = " ".join(f"{n(x)},{n(y)}" for x, y in pts)
            out.append(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{n(w)}" stroke-linecap="round" stroke-linejoin="round"/>')
        elif kind == "poly":
            pts, color = a
            p = " ".join(f"{n(x)},{n(y)}" for x, y in pts)
            out.append(f'<polygon points="{p}" fill="{color}"/>')
    body = "\n    ".join(out)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <clipPath id="tile"><rect width="512" height="512" rx="113"/></clipPath>
  <rect width="512" height="512" rx="113" fill="{BG}"/>
  <g clip-path="url(#tile)">
    {body}
  </g>
</svg>
"""


def render(glyph, rounded=True, scale=1.0):
    """glyph: a function (draw, transform, scale) or a list of shapes."""
    img = Image.new("RGBA", (C, C), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if rounded:
        d.rounded_rectangle([0, 0, C - 1, C - 1], radius=int(C * 0.22), fill=BG)
    else:
        d.rectangle([0, 0, C, C], fill=BG)
    if callable(glyph):
        glyph(d, transform(scale), scale)
    else:
        draw_shapes(d, transform(scale), scale, glyph)
    if rounded:  # clip anything drawn past the tile's rounded corners
        mask = Image.new("L", (C, C), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, C - 1, C - 1], radius=int(C * 0.22), fill=255)
        img.putalpha(ImageChops.multiply(img.getchannel("A"), mask))
    return img


def save(img, path, size):
    path.parent.mkdir(parents=True, exist_ok=True)
    img.resize((size, size), Image.LANCZOS).save(path)
    print(f"wrote {path.relative_to(ROOT)}")


def project_set(name, shapes):
    """favicon.svg, favicon.ico and apple-touch-icon.png under assets/icons/<name>/."""
    out = ICONS / name
    out.mkdir(parents=True, exist_ok=True)
    (out / "favicon.svg").write_text(svg(shapes), encoding="utf-8")
    print(f"wrote {(out / 'favicon.svg').relative_to(ROOT)}")
    render(shapes).resize((48, 48), Image.LANCZOS).save(
        out / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)]
    )
    print(f"wrote {(out / 'favicon.ico').relative_to(ROOT)}")
    # iOS rounds corners itself: full-bleed square, glyph slightly smaller
    save(render(shapes, rounded=False, scale=0.82), out / "apple-touch-icon.png", 180)


# --- site (>_ prompt, green) ---
site = render(glyph_prompt)
save(site, ICONS / "favicon-16x16.png", 16)
save(site, ICONS / "favicon-32x32.png", 32)
save(site, ICONS / "android-chrome-192x192.png", 192)
save(site, ICONS / "android-chrome-256x256.png", 256)
site.resize((48, 48), Image.LANCZOS).save(
    ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)]
)
print("wrote favicon.ico")
save(render(glyph_prompt, rounded=False, scale=0.82), ICONS / "apple-touch-icon.png", 180)

mstile = Image.new("RGBA", (C, C), (0, 0, 0, 0))
glyph_prompt(ImageDraw.Draw(mstile), transform(0.72), 0.72, color="#ffffff")
save(mstile, ICONS / "mstile-150x150.png", 150)

# --- projects ---
for name, shapes in PROJECTS.items():
    project_set(name, shapes)
