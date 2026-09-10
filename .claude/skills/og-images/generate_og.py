#!/usr/bin/env python3
# Generates 1200x630 social share images in the site's own look.
#
# Two kinds of card, both driven by frontmatter (see the og_image capture in
# _layouts/nocturne.html):
#   posts        -> images/og/<slug>.png              eyebrow + title
#   collections  -> images/og/collections/<slug>.png  eyebrow + headline + description
# Posts with an image.feature are skipped — that photo is used as-is.
import os, re, sys, glob, html, argparse
import yaml
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
POSTS_DIR = os.path.join(REPO, "_posts")
OUT_DIR = os.path.join(REPO, "images", "og")
# Collection cards live in their own subdirectory so a collection slug can never
# collide with a post slug (e.g. a future post slugged "generosity").
COLLECTIONS_OUT_DIR = os.path.join(OUT_DIR, "collections")

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


def draw_eyebrow(d, label):
    """Short accent rule + uppercase label, mirrors .eyebrow-row/.eyebrow. Returns its baseline y."""
    line_y = PAD + 46
    d.line([(PAD, line_y), (PAD + 36, line_y)], fill=ACCENT, width=2)
    tracked_text(d, (PAD + 52, line_y - 14), label.upper(), font(FONT_SEMIBOLD, 20), ACCENT_700, tracking=2)
    return line_y


def draw_footer(d):
    """Footer rule + wordmark, mirrors .peek-foot's border-top treatment. Returns the rule's y."""
    foot_y = H - 96
    d.line([(PAD, foot_y), (W - PAD, foot_y)],
           fill=tuple(int(c * 0.12 + BG[i] * 0.88) for i, c in enumerate(DIVIDER)), width=1)
    d.text((PAD, foot_y + 22), "Jaisen Mathai", font=font(FONT_MEDIUM, 24), fill=INK)
    d.text((PAD, foot_y + 54), "jaisenmathai.com", font=font(FONT_REGULAR, 18), fill=MUTED)
    return foot_y


def generate(path):
    title, category, feature = read_post(path)
    if feature:
        print(f"skip {os.path.basename(path)} — has image.feature ({feature})")
        return None

    slug = slug_for(path)
    img = draw_background()
    d = ImageDraw.Draw(img)
    line_y = draw_eyebrow(d, eyebrow_for(category))

    # Title, vertically centered in the band between the eyebrow and the footer rule
    max_w = W - 2 * PAD
    title_font, tsize, lines = fit_title(d, title, max_w)
    line_h = int(tsize * 1.18)
    block_h = line_h * len(lines)
    band_top, band_bottom = line_y + 40, H - 130
    top = band_top + max(0, (band_bottom - band_top - block_h) // 2)
    for i, ln in enumerate(lines):
        d.text((PAD, top + i * line_h), ln, font=title_font, fill=INK)

    draw_footer(d)

    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, f"{slug}.png")
    img.save(out, "PNG")
    print(f"wrote {out}  ({W}x{H})  title={title!r}")
    return out


# ---------------------------------------------------------------------------
# Collection cards (the /articles/, /faith-and-ai/, /generosity/,
# /openphoto-trovebox/ archive pages)
# ---------------------------------------------------------------------------

def read_frontmatter(path):
    """Frontmatter dict, or None if the file has none."""
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    return yaml.safe_load(m.group(1)) or {}


def collection_slug(fm, path):
    """The permalink's last segment — matches `page.url | split: '/' | last` in the layout."""
    permalink = fm.get("permalink")
    if permalink:
        return permalink.strip("/").split("/")[-1]
    return os.path.splitext(os.path.basename(path))[0]


def find_collection_pages():
    """Root-level pages using the archive layout."""
    pages = []
    for path in sorted(glob.glob(os.path.join(REPO, "*.html")) + glob.glob(os.path.join(REPO, "*.md"))):
        fm = read_frontmatter(path)
        if fm and fm.get("layout") == "archive":
            pages.append((path, fm))
    return pages


def clean(text):
    """Frontmatter carries HTML entities (e.g. 'Articles &amp; essays') for the page title."""
    return html.unescape(str(text or "")).strip()


def fit_block(draw, text, font_path, max_w, start, min_size, max_lines):
    """Largest size at or below `start` whose wrap fits in max_lines."""
    size = start
    while size > min_size:
        f = font(font_path, size)
        lines = wrap(draw, text, f, max_w)
        if len(lines) <= max_lines:
            return f, size, lines
        size -= 2
    f = font(font_path, min_size)
    return f, min_size, wrap(draw, text, f, max_w)[:max_lines]


def generate_collection(path, fm):
    headline = clean(fm.get("headline") or fm.get("title"))
    if not headline:
        raise SystemExit(f"no headline or title in {path}")
    eyebrow = clean(fm.get("eyebrow")) or "Writing"
    description = clean(fm.get("description"))
    slug = collection_slug(fm, path)

    img = draw_background()
    d = ImageDraw.Draw(img)
    line_y = draw_eyebrow(d, eyebrow)
    foot_y = draw_footer(d)

    max_w = W - 2 * PAD
    # The description sets in a narrower measure than the headline, the way the
    # archive page's .page-head p does against its h1.
    desc_w = int(max_w * 0.86)

    # Everything between the eyebrow and the footer rule has to fit in this band.
    # A long headline and a long description together can overflow it, so the two
    # are fitted against it together rather than to fixed sizes.
    band_top, band_bottom = line_y + 44, foot_y - 46
    band_h = band_bottom - band_top

    gap = 34 if description else 0

    def fit_headline(size):
        f = font(FONT_MEDIUM, size)
        lines = wrap(d, headline, f, max_w)
        return (f, lines, int(size * 1.14) * len(lines)) if len(lines) <= 2 else None

    def fit_description(room):
        """Largest size that sets the whole description in <=3 lines within `room`."""
        for size in range(30, 21, -2):
            f = font(FONT_REGULAR, size)
            lines = wrap(d, description, f, desc_w)
            lh = int(size * 1.42)
            if len(lines) <= 3 and lh * len(lines) <= room:
                return f, lh, lines
        return None

    # Headline and description compete for one fixed band, so they're fitted
    # together: take the largest headline that still leaves room to set the
    # description in full. A big headline that would elide the description is
    # worse than a slightly smaller one that doesn't.
    head_font = head_lines = None
    head_h = 0
    desc_font, desc_line_h, desc_lines = None, 0, []
    for size in range(86, 55, -2):
        head = fit_headline(size)
        if not head:
            continue
        if not description:
            head_font, head_lines, head_h = head
            break
        desc = fit_description(band_h - head[2] - gap)
        if desc:
            head_font, head_lines, head_h = head
            desc_font, desc_line_h, desc_lines = desc
            break

    if head_font is None:
        # Nothing fit cleanly (an unusually long description) — set the headline
        # as large as it will go and elide the description to the room left.
        for size in range(86, 39, -2):
            head = fit_headline(size)
            if head:
                head_font, head_lines, head_h = head
                break
        if description:
            desc_font = font(FONT_REGULAR, 22)
            desc_line_h = int(22 * 1.42)
            lines = wrap(d, description, desc_font, desc_w)
            keep = max(1, min(len(lines), (band_h - head_h - gap) // desc_line_h))
            desc_lines = lines[:keep]
            if keep < len(lines):
                desc_lines[-1] = desc_lines[-1].rstrip(" ,;:.") + "\u2026"

    head_line_h = head_h // max(1, len(head_lines))
    desc_h = desc_line_h * len(desc_lines)

    block_h = head_h + gap + desc_h
    top = band_top + max(0, (band_h - block_h) // 2)

    for i, ln in enumerate(head_lines):
        d.text((PAD, top + i * head_line_h), ln, font=head_font, fill=INK)
    if desc_lines:
        dy = top + head_h + gap
        for i, ln in enumerate(desc_lines):
            d.text((PAD, dy + i * desc_line_h), ln, font=desc_font, fill=MUTED)

    os.makedirs(COLLECTIONS_OUT_DIR, exist_ok=True)
    out = os.path.join(COLLECTIONS_OUT_DIR, f"{slug}.png")
    img.save(out, "PNG")
    print(f"wrote {out}  ({W}x{H})  headline={headline!r}")
    return out


def run_collections(only=None):
    pages = find_collection_pages()
    if only:
        pages = [(path, fm) for path, fm in pages if collection_slug(fm, path) == only]
        if not pages:
            known = ", ".join(sorted(collection_slug(fm, p) for p, fm in find_collection_pages()))
            raise SystemExit(f"no collection page with slug {only!r} (have: {known})")
    for path, fm in pages:
        generate_collection(path, fm)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Generate OG share images for posts (without an image.feature) and collection pages")
    ap.add_argument("slug", nargs="?", help="post filename or slug, e.g. the-risk-and-opportunity-of-ai-for-faith")
    ap.add_argument("--all", action="store_true", help="regenerate every post card and every collection card")
    ap.add_argument("--collections", nargs="?", const="*", metavar="SLUG",
                    help="regenerate collection cards; pass a slug (e.g. faith-and-ai) for just one")
    args = ap.parse_args()

    if args.collections:
        run_collections(None if args.collections == "*" else args.collections)
    elif args.all:
        for path in sorted(glob.glob(os.path.join(POSTS_DIR, "*.md"))):
            generate(path)
        run_collections()
    elif args.slug:
        matches = [p for p in glob.glob(os.path.join(POSTS_DIR, "*.md")) if slug_for(p) == args.slug]
        if not matches:
            raise SystemExit(f"no post found with slug {args.slug!r}")
        generate(matches[0])
    else:
        ap.error("pass a slug, --all, or --collections")
