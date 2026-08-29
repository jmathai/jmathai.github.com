#!/usr/bin/env python3
# Generates a post's 1200x630 social share image from its _posts frontmatter.
# Only used for posts that don't have an image.feature — those are used as-is
# (see the og_image capture in _layouts/nocturne.html).
import os, re, sys, glob, argparse
import yaml
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
POSTS_DIR = os.path.join(REPO, "_posts")
OUT_DIR = os.path.join(REPO, "images", "og")

FONT_REGULAR  = os.path.join(SKILL_DIR, "fonts", "Newsreader-Regular.ttf")
FONT_MEDIUM   = os.path.join(SKILL_DIR, "fonts", "Newsreader-Medium.ttf")
FONT_SEMIBOLD = os.path.join(SKILL_DIR, "fonts", "Newsreader-SemiBold.ttf")

W, H = 1200, 630
PAD = 90

# Palette lifted straight from assets/css/nocturne.css custom properties.
BG          = (0xF7, 0xF0, 0xE2)  # --color-bg
INK         = (0x2C, 0x25, 0x19)  # --color-text
ACCENT      = (0xC8, 0x87, 0x1F)  # --color-accent
ACCENT_100  = (0xF8, 0xEA, 0xD0)  # --color-accent-100
ACCENT_200  = (0xF1, 0xD5, 0xA3)  # --color-accent-200
ACCENT_700  = (0x87, 0x58, 0x11)  # --color-accent-700 (eyebrow text)
MUTED       = (0x8A, 0x7A, 0x5F)  # --color-neutral-600
DIVIDER     = (0x2C, 0x25, 0x19)  # --color-divider is ink at 12% — blended on paste

# _layouts/post.html's category -> eyebrow mapping, kept in sync by hand.
EYEBROW = {
    "generosity": "Generosity",
    "openphoto-trovebox": "Startup Journey",
    "faith-and-ai": "Faith and AI",
}


def font(path, size):
    return ImageFont.truetype(path, size)


def eyebrow_for(category):
    if not category:
        return "Writing"
    if category in EYEBROW:
        return EYEBROW[category]
    return category.replace("-", " ").capitalize()


def slug_for(path):
    name = os.path.splitext(os.path.basename(path))[0]
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", name)


def read_post(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise SystemExit(f"no frontmatter in {path}")
    fm = yaml.safe_load(m.group(1)) or {}
    title = fm.get("title")
    category = fm.get("category")
    feature = (fm.get("image") or {}).get("feature")
    if not title:
        raise SystemExit(f"no title in {path}")
    return title, category, feature


def radial_glow(size, color, alpha=160, blur_frac=0.22):
    """A soft blurred-ellipse glow that fades to true zero well inside its own
    layer (unlike Image.radial_gradient, whose corners never fully reach zero,
    which shows up as a hard rectangle when composited)."""
    layer = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(layer)
    blur = int(size * blur_frac)
    inset = blur * 1.6
    d.ellipse([inset, inset, size - inset, size - inset], fill=255)
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    layer = layer.point(lambda p: int(p / 255 * alpha))
    rgba = Image.new("RGBA", (size, size), color + (0,))
    rgba.putalpha(layer)
    return rgba


def draw_background():
    img = Image.new("RGBA", (W, H), BG + (255,))
    # top-right glow (mirrors the CSS radial-gradient at 86% -200px)
    glow1 = radial_glow(1200, ACCENT_200, alpha=170)
    img.alpha_composite(glow1, (W - 760, -560))
    # bottom-left glow (mirrors -12% 110%)
    glow2 = radial_glow(1100, ACCENT_100, alpha=170)
    img.alpha_composite(glow2, (-620, H - 560))
    return img.convert("RGB")


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_title(draw, title, max_w, start=72, min_size=40, max_lines=4):
    size = start
    while size > min_size:
        f = font(FONT_MEDIUM, size)
        lines = wrap(draw, title, f, max_w)
        if len(lines) <= max_lines:
            return f, size, lines
        size -= 2
    f = font(FONT_MEDIUM, min_size)
    return f, min_size, wrap(draw, title, f, max_w)


def tracked_text(draw, xy, text, fnt, fill, tracking=0):
    """Draw uppercase-style text with manual letter-spacing (Pillow has no kerning knob)."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking
    return x


def generate(path):
    title, category, feature = read_post(path)
    if feature:
        print(f"skip {os.path.basename(path)} — has image.feature ({feature})")
        return None

    slug = slug_for(path)
    img = draw_background()
    d = ImageDraw.Draw(img)

    # Eyebrow: short accent rule + uppercase label, mirrors .eyebrow-row/.eyebrow
    eyebrow = eyebrow_for(category).upper()
    line_y = PAD + 46
    d.line([(PAD, line_y), (PAD + 36, line_y)], fill=ACCENT, width=2)
    eb_font = font(FONT_SEMIBOLD, 20)
    tracked_text(d, (PAD + 52, line_y - 14), eyebrow, eb_font, ACCENT_700, tracking=2)

    # Title, vertically centered in the band between the eyebrow and the footer rule
    max_w = W - 2 * PAD
    title_font, tsize, lines = fit_title(d, title, max_w)
    line_h = int(tsize * 1.18)
    block_h = line_h * len(lines)
    band_top, band_bottom = line_y + 40, H - 130
    top = band_top + max(0, (band_bottom - band_top - block_h) // 2)
    for i, ln in enumerate(lines):
        d.text((PAD, top + i * line_h), ln, font=title_font, fill=INK)

    # Footer rule + wordmark, mirrors .peek-foot's border-top treatment
    foot_y = H - 96
    d.line([(PAD, foot_y), (W - PAD, foot_y)],
           fill=tuple(int(c * 0.12 + BG[i] * 0.88) for i, c in enumerate(DIVIDER)), width=1)
    d.text((PAD, foot_y + 22), "Jaisen Mathai", font=font(FONT_MEDIUM, 24), fill=INK)
    d.text((PAD, foot_y + 54), "jaisenmathai.com", font=font(FONT_REGULAR, 18), fill=MUTED)

    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, f"{slug}.png")
    img.save(out, "PNG")
    print(f"wrote {out}  ({W}x{H})  title={title!r}")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Generate OG share images for posts without an image.feature")
    ap.add_argument("slug", nargs="?", help="post filename or slug, e.g. the-risk-and-opportunity-of-ai-for-faith")
    ap.add_argument("--all", action="store_true", help="regenerate for every post missing image.feature")
    args = ap.parse_args()

    if args.all:
        for path in sorted(glob.glob(os.path.join(POSTS_DIR, "*.md"))):
            generate(path)
    elif args.slug:
        matches = [p for p in glob.glob(os.path.join(POSTS_DIR, "*.md")) if slug_for(p) == args.slug]
        if not matches:
            raise SystemExit(f"no post found with slug {args.slug!r}")
        generate(matches[0])
    else:
        ap.error("pass a slug or --all")
