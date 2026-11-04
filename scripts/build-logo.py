#!/usr/bin/env python3
"""Build the UNSW-NLP logo: one bubble per group member, coloured by region
(teal top-left, yellow top-right, purple bottom-left, coral bottom-right) and
blending where bubbles overlap, with the official UNSW logo on top.

    python3 scripts/build-logo.py            # default: 33 people, layout seed 7
    python3 scripts/build-logo.py --people 40 --seed 7
    python3 scripts/build-logo.py --people 150 --seed 60 --logo-width 50 --opacity 50 --all   # current logo

Writes static/brand/unsw-nlp-mark.{svg,png} and a preview to the scratch path
given by --preview (optional). Requires Pillow.
"""
import argparse, base64, io, math
from PIL import Image, ImageDraw

TL, TR, BL, BR = (76, 195, 198), (247, 220, 62), (199, 123, 214), (242, 117, 139)
OPACITY = 0.68         # bubbles are see-through, so overlaps mix colours
HALF, ROUND = 54, 40   # rounded-square outline the bubbles stay inside (200-unit canvas)
LOGO_W = 0.60          # UNSW logo width as a share of the canvas
LOGO_Y = 0.50          # vertical centre of the UNSW logo


class LCG:
    """Same generator as the in-browser preview, so a seed reproduces a layout."""
    def __init__(self, seed): self.s = seed
    def __call__(self):
        self.s = (self.s * 16807) % 2147483647
        return (self.s - 1) / 2147483646


def _to_oklab(c):
    r, g, b = (((v / 255 + 0.055) / 1.055) ** 2.4 if v / 255 > 0.04045 else v / 255 / 12.92 for v in c)
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    return (0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
            1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
            0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s)


def _from_oklab(c):
    L, A, B = c
    l = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3
    m = (L - 0.1055613458 * A - 0.0638541728 * B) ** 3
    s = (L - 0.0894841775 * A - 1.2914855480 * B) ** 3
    rgb = (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
           -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
           -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)
    out = []
    for v in rgb:
        v = min(max(v, 0), 1)
        v = 1.055 * v ** (1 / 2.4) - 0.055 if v > 0.0031308 else 12.92 * v
        out.append(round(v * 255))
    return tuple(out)


def colour_at(x, y):
    """Each corner keeps its region colour; colours blend only near the seams.
    Blending happens in OKLab so mixes stay vivid instead of turning grey."""
    u, v = min(max(x / 200, 0), 1), min(max(y / 200, 0), 1)
    sm = lambda t: t * t * (3 - 2 * t)
    sharp = lambda t: sm(sm(t))          # hold the region colour, then blend at the seam
    lerp = lambda a, b, t: tuple(p + (q - p) * t for p, q in zip(a, b))
    tl, tr, bl, br = map(_to_oklab, (TL, TR, BL, BR))
    return _from_oklab(lerp(lerp(tl, tr, sharp(u)), lerp(bl, br, sharp(u)), sharp(v)))


def fits(x, y, r):
    dx, dy = abs(x - 100) - HALF, abs(y - 100) - HALF
    return math.hypot(max(dx, 0), max(dy, 0)) + r <= ROUND


def layout(n, seed):
    rnd, pts, tries = LCG(seed), [], 0
    r0 = max(7, 40 / math.sqrt(n / 8))
    while len(pts) < n and tries < 40000:
        tries += 1
        r = r0 * (0.75 + rnd() * 0.5)
        x, y = 4 + rnd() * 192, 4 + rnd() * 192
        if not fits(x, y, r):
            continue
        if all(math.hypot(px - x, py - y) >= (pr + r) * 0.62 for px, py, pr in pts):
            pts.append((x, y, r))
    return pts


def build(people, seed, logo_path, out_svg, out_png, size=1200):
    pts = layout(people, seed)
    logo = Image.open(logo_path).convert('RGBA')
    lw = LOGO_W * 200
    lh = lw * logo.height / logo.width
    lx, ly = 100 - lw / 2, LOGO_Y * 200 - lh / 2

    # SVG: vector bubbles + embedded official logo
    buf = io.BytesIO(); logo.save(buf, 'PNG', optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode()
    circles = ''.join(
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="rgb{colour_at(x, y)}" fill-opacity="{OPACITY}"/>'
        for x, y, r in pts)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="{size}" height="{size}" '
           f'role="img" aria-labelledby="t"><title id="t">UNSW-NLP</title>{circles}'
           f'<image href="data:image/png;base64,{b64}" x="{lx:.2f}" y="{ly:.2f}" width="{lw:.2f}" height="{lh:.2f}"/></svg>\n')
    open(out_svg, 'w').write(svg)

    # PNG: render bubbles at 2x then downsample for smooth edges
    S = size * 2; k = S / 200
    canvas = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    for x, y, r in pts:
        layer = Image.new('RGBA', (S, S), (0, 0, 0, 0))
        ImageDraw.Draw(layer).ellipse([(x - r) * k, (y - r) * k, (x + r) * k, (y + r) * k],
                                      fill=colour_at(x, y) + (round(255 * OPACITY),))
        canvas = Image.alpha_composite(canvas, layer)
    lg = logo.resize((round(lw * k), round(lh * k)), Image.LANCZOS)
    canvas.alpha_composite(lg, (round(lx * k), round(ly * k)))
    canvas = canvas.resize((size, size), Image.LANCZOS)
    canvas.save(out_png, optimize=True)
    return canvas


# ── Derived assets: everything the site uses, built from the mark ─────────────
def build_all(mark_png='static/brand/unsw-nlp-mark.png'):
    """Lockup (mark | UNSW-NLP) as SVG/PNG in black and white, navbar mark,
    favicons, legacy logo files and the link-preview image."""
    from fontTools.ttLib import TTFont
    from fontTools.pens.svgPathPen import SVGPathPen
    from fontTools.pens.transformPen import TransformPen
    from PIL import ImageFont

    mark = Image.open(mark_png).convert('RGBA')
    font_path = 'fonts-src/clancy/Clancy-Bold.otf'
    tt = TTFont(font_path); gs = tt.getGlyphSet(); cmap = tt.getBestCmap()
    upm = tt['head'].unitsPerEm; cap = tt['OS/2'].sCapHeight or 700

    # Proportions match the site header: mark 84, gap 11.9, bar 2.5 x 35.7, text 30.6 (x10)
    MARK, GAP, BARW, BARH, FS, TRACK = 840, 119, 25, 357, 306, 3.06
    scale = FS / upm
    paths, x = [], 0
    for ch in 'UNSW-NLP':
        g = gs[cmap[ord(ch)]]; pen = SVGPathPen(gs)
        g.draw(TransformPen(pen, (scale, 0, 0, -scale, x, 0)))
        paths.append(pen.getCommands()); x += g.width * scale + TRACK
    textx = MARK + GAP + BARW + GAP
    W, H = round(textx + x - TRACK + 4), MARK
    base = H / 2 + cap * scale / 2

    buf = io.BytesIO(); mark.resize((600, 600), Image.LANCZOS).save(buf, 'WEBP', quality=90, method=6)
    mark_b64 = base64.b64encode(buf.getvalue()).decode()
    for name, fill in (('unsw-nlp-logo', '#000000'), ('unsw-nlp-logo-white', '#ffffff')):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t">'
               f'<title id="t">UNSW-NLP</title>'
               f'<image href="data:image/webp;base64,{mark_b64}" x="0" y="0" width="{MARK}" height="{MARK}"/>'
               f'<rect x="{MARK + GAP}" y="{(H - BARH) / 2:.1f}" width="{BARW}" height="{BARH}" fill="{fill}"/>'
               f'<g transform="translate({textx:.1f} {base:.1f})" fill="{fill}">{"".join(f"<path d=\"{d}\"/>" for d in paths)}</g></svg>\n')
        open(f'static/brand/{name}.svg', 'w').write(svg)
        # PNG twin for tools that do not take SVG
        im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); im.alpha_composite(mark.resize((MARK, MARK), Image.LANCZOS))
        d = ImageDraw.Draw(im); pil_font = ImageFont.truetype(font_path, FS)
        d.rectangle([MARK + GAP, (H - BARH) // 2, MARK + GAP + BARW, (H + BARH) // 2], fill=fill)
        tx = textx
        for ch in 'UNSW-NLP':
            d.text((tx, base), ch, font=pil_font, fill=fill, anchor='ls'); tx += d.textlength(ch, font=pil_font) + TRACK
        im.save(f'static/brand/{name}.png', optimize=True)

    sq = lambda px: mark.resize((px, px), Image.LANCZOS)
    sq(112).save('static/logo-nav.webp', 'WEBP', quality=90, method=6)       # navbar mark (2x of 28px)
    sq(16).save('static/logo-16x16.png', optimize=True)
    sq(32).save('static/logo-32x32.png', optimize=True)
    sq(64).save('static/logo.ico', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    for f, px in (('static/logo.png', 256), ('static/prof-pic.png', 512)):          # legacy paths
        sq(px).quantize(colors=256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).save(f, optimize=True)

    # Link-preview image (1200x630): mark | UNSW-NLP and a strapline
    og = Image.new('RGB', (1200, 630), 'white'); d = ImageDraw.Draw(og)
    L = 300; title = ImageFont.truetype(font_path, 118)
    sub = ImageFont.truetype('fonts-src/roboto/Roboto-Regular.ttf', 34)
    bb = d.textbbox((0, 0), 'UNSW-NLP', font=title); tw, th = bb[2] - bb[0], bb[3] - bb[1]
    x0 = (1200 - (L + 44 + 7 + 44 + tw)) // 2; cy = 630 // 2 - 30
    og.paste(sq(L), (x0, cy - L // 2), sq(L))
    bx = x0 + L + 44; d.rectangle([bx, cy - th // 2 - 14, bx + 7, cy + th // 2 + 14], fill='black')
    d.text((bx + 7 + 44, cy - th // 2 - bb[1]), 'UNSW-NLP', font=title, fill='black')
    s = 'Natural language processing research group at UNSW Sydney'
    d.text(((1200 - d.textlength(s, font=sub)) / 2, cy + L // 2 + 40), s, font=sub, fill=(85, 85, 85))
    og.save('static/og-image.png', optimize=True)
    print('wrote lockups, navbar mark, favicons, legacy logos, og-image')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--people', type=int, default=33)
    ap.add_argument('--seed', type=int, default=7)
    ap.add_argument('--all', action='store_true', help='also rebuild the lockup, navbar mark, favicons and link-preview image')
    ap.add_argument('--logo-width', type=int, default=60, help='UNSW logo width, %% of the canvas')
    ap.add_argument('--opacity', type=int, default=68, help='bubble opacity, %%')
    ap.add_argument('--logo', default='scripts/brand-src/unsw-sydney-portrait.png')
    ap.add_argument('--svg', default='static/brand/unsw-nlp-mark.svg')
    ap.add_argument('--png', default='static/brand/unsw-nlp-mark.png')
    a = ap.parse_args()
    LOGO_W = a.logo_width / 100
    OPACITY = a.opacity / 100
    build(a.people, a.seed, a.logo, a.svg, a.png)
    print('wrote', a.svg, a.png)
    if a.all:
        build_all(a.png)
