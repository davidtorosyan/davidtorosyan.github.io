"""Generate the icon family for the portfolio site and its projects.

One dark tile, one glyph per property:
  site   >_ terminal prompt (green)
  hood   jigsaw puzzle piece (amber)
  ti-js  calculator (blue)

Each glyph also has a hand-authored favicon.svg next to its PNGs;
keep the geometry here in sync with those files.

Requires Pillow:  pip install pillow
Run:              python scripts/gen_icons.py
"""
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
ICONS = ROOT / "assets" / "icons"

BG = (13, 17, 23, 255)        # #0d1117 — site dark background
GREEN = (74, 222, 128, 255)   # #4ade80 — site accent
AMBER = (251, 191, 36, 255)   # #fbbf24 — hood
BLUE = (88, 166, 255, 255)    # #58a6ff — ti-js

S = 8  # supersample factor; draw at 512*S, downscale with Lanczos
C = 512 * S


def transform(scale):
    """Map 512-space coords to the supersampled canvas, scaling about center."""
    def t(x, y):
        return ((256 + (x - 256) * scale) * S, (256 + (y - 256) * scale) * S)
    return t


def glyph_prompt(d, t, k, color):
    """>_ terminal prompt."""
    w = 54 * S * k
    a, b, c = t(148, 168), t(258, 256), t(148, 344)
    d.line([a, b], fill=color, width=int(w))
    d.line([b, c], fill=color, width=int(w))
    for p in (a, b, c):
        r = w / 2
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=color)
    d.rounded_rectangle([*t(300, 317), *t(412, 371)], radius=27 * S * k, fill=color)


def glyph_puzzle(d, t, k, color):
    """Jigsaw piece: body, knob on top, notch cut from the right edge."""
    d.rounded_rectangle([*t(138, 156), *t(390, 408)], radius=28 * S * k, fill=color)
    for cx, cy, fill in ((264, 156, color), (390, 282, BG)):
        x, y = t(cx, cy)
        r = 52 * S * k
        d.ellipse([x - r, y - r, x + r, y + r], fill=fill)


def glyph_calc(d, t, k, color):
    """Calculator: body, screen, 3x3 button grid."""
    d.rounded_rectangle([*t(168, 116), *t(344, 396)], radius=32 * S * k, fill=color)
    d.rounded_rectangle([*t(196, 150), *t(316, 212)], radius=12 * S * k, fill=BG)
    r = 16 * S * k
    for cx in (212, 256, 300):
        for cy in (256, 310, 364):
            x, y = t(cx, cy)
            d.ellipse([x - r, y - r, x + r, y + r], fill=BG)


def render(glyph, color, rounded=True, scale=1.0):
    img = Image.new("RGBA", (C, C), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if rounded:
        d.rounded_rectangle([0, 0, C - 1, C - 1], radius=int(C * 0.22), fill=BG)
    else:
        d.rectangle([0, 0, C, C], fill=BG)
    glyph(d, transform(scale), scale, color)
    return img


def save(img, path, size):
    path.parent.mkdir(parents=True, exist_ok=True)
    img.resize((size, size), Image.LANCZOS).save(path)
    print(f"wrote {path.relative_to(ROOT)}")


def project_set(name, glyph, color):
    """favicon.ico + apple-touch-icon.png for a project, under assets/icons/<name>/."""
    out = ICONS / name
    tile = render(glyph, color)
    out.mkdir(parents=True, exist_ok=True)
    tile.resize((48, 48), Image.LANCZOS).save(
        out / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)]
    )
    print(f"wrote {(out / 'favicon.ico').relative_to(ROOT)}")
    # iOS rounds corners itself: full-bleed square, glyph slightly smaller
    save(render(glyph, color, rounded=False, scale=0.82), out / "apple-touch-icon.png", 180)


# --- site (>_ prompt, green) ---
site = render(glyph_prompt, GREEN)
save(site, ICONS / "favicon-16x16.png", 16)
save(site, ICONS / "favicon-32x32.png", 32)
save(site, ICONS / "android-chrome-192x192.png", 192)
save(site, ICONS / "android-chrome-256x256.png", 256)
site.resize((48, 48), Image.LANCZOS).save(
    ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)]
)
print("wrote favicon.ico")
save(render(glyph_prompt, GREEN, rounded=False, scale=0.82), ICONS / "apple-touch-icon.png", 180)

mstile = Image.new("RGBA", (C, C), (0, 0, 0, 0))
glyph_prompt(ImageDraw.Draw(mstile), transform(0.72), 0.72, (255, 255, 255, 255))
save(mstile, ICONS / "mstile-150x150.png", 150)

# --- projects ---
project_set("hood", glyph_puzzle, AMBER)
project_set("ti-js", glyph_calc, BLUE)
