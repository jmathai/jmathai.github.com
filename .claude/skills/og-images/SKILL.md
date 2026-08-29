---
name: og-images
description: Generate/refresh a post's 1200x630 social share (OG) image at images/og/<slug>.png. Use whenever a post is created without an image.feature, or whenever a post's title changes.
---

# Post OG images

Every post needs a social share image. `_layouts/nocturne.html`'s `og_image` capture
picks one of two sources, in order:

1. **`page.image.feature`**, if the post's frontmatter sets one — the real photo is
   used as-is, no generation.
2. **`images/og/<slug>.png`** otherwise — a generated card with the site's own look
   (warm paper background, Newsreader type, amber accent), carrying the post's eyebrow
   category and title. `<slug>` is Jekyll's `page.slug` (the filename minus the date
   and extension), so no frontmatter change is needed to wire a generated card in.

Generated cards are committed to the repo, the same way the sojourn-pages `topics/*/og.png`
cards are — GitHub Pages' build has no room for a Python step, so this runs locally and
the PNG ships as a normal asset.

## When to run it

- **New post, no `image.feature`.** Generate its card before publishing.
- **Title changes** on a post that has a generated card (i.e. no `image.feature`).
  Regenerate — the image is derived from the title and will go stale otherwise.
- **`image.feature` is added or removed** on a post. Re-run so the right source (photo
  vs. generated card) is reflected; removing a stale `images/og/<slug>.png` isn't
  required (unused generated files are harmless) but regenerating after removing
  `image.feature` is, since the template will start pointing at that file.

## Environment setup (first use)

```bash
cd .claude/skills/og-images
python3 -m venv .venv
.venv/bin/pip install Pillow PyYAML
```

The **Newsreader** font (Regular/Medium/SemiBold, matching `--font-heading` in
`assets/css/nocturne.css`) is vendored in `fonts/` and checked in — never fetched at
generation time.

## Usage

```bash
# one post, by slug (filename minus the date prefix and .md)
.claude/skills/og-images/.venv/bin/python .claude/skills/og-images/generate_og.py <slug>

# every post missing image.feature — safe to run any time, always overwrites
.claude/skills/og-images/.venv/bin/python .claude/skills/og-images/generate_og.py --all
```

Posts with `image.feature` set are always skipped/reported, never touched.

## Design

Read straight from `assets/css/nocturne.css`'s custom properties, not reinvented:
`--color-bg` background with the same two corner accent glows as the site body,
`--color-accent`/`--color-accent-700` for the eyebrow rule and label (mirrors
`.eyebrow-row`/`.eyebrow`), `--color-text` for the title in Newsreader Medium
(mirrors `.hero h1`'s weight), `--color-neutral-600` for the muted footer line. The
eyebrow category mapping (`generosity` → Generosity, `openphoto-trovebox` → Startup
Journey, `faith-and-ai` → Faith and AI, else capitalized, else "Writing") is kept in
sync **by hand** with the equivalent Liquid logic in `_layouts/post.html` — if that
mapping changes, update `EYEBROW` in `generate_og.py` to match.
