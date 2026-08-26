# CLAUDE.md

Personal site for Jaisen Mathai (jaisenmathai.com) — writing on faith, generosity, and building software.

## Stack

- **Jekyll 4.3.4** static site, Ruby + Bundler (`Gemfile`/`Gemfile.lock`). No `.ruby-version` pinned; local Ruby is 2.6.10 via system/rbenv.
- Markdown via **kramdown**. Highlighting via pygments.
- Base theme is a heavily modified fork of "So Simple Theme" (see `README.md` for the original theme's docs — mostly superseded). The active design is the custom **"Nocturne"** theme layered on top (see `README-nocturne.md` for how it was installed/mapped).
- No Node/npm/Grunt installed locally. `Gruntfile.js` + `package.json` declare a legacy asset pipeline (`recess`/LESS, `uglify`, `imagemin`, `svgmin`) that isn't currently runnable as-is — see Image optimization below for the workaround used instead.

## Build & preview

```bash
bundle install
bundle exec jekyll serve   # local preview at http://localhost:4000
bundle exec jekyll build   # outputs to _site/ (gitignored)
```

`_site/` is a build artifact — don't hand-edit it.

## Deployment

GitHub Pages, **legacy build type**, source = `master` branch, root path. Pushing to `master` triggers GitHub's own Jekyll build and deploy automatically — there is no CI/deploy step in this repo to run. Custom domain via `CNAME` (`jaisenmathai.com`), HTTPS enforced.

`.travis.yml` (Jekyll build + html-proofer) is a leftover from an old Travis CI setup and is not currently wired to anything — treat as historical, not active CI.

Because GitHub Pages' legacy builder uses its own supported Jekyll/plugin versions, a local `bundle exec jekyll build` succeeding doesn't guarantee the Pages build will match exactly — keep plugin usage to what's already in the Gemfile.

## Structure

```
_posts/            blog posts, filename YYYY-MM-DD-slug.md
_layouts/
  nocturne.html     base layout: head, nav, footer
  home.html         homepage (hero + focus + work timeline)
  post.html         article reading view (current, active layout for posts)
  archive.html      writing list / collection pages (Articles, Generosity, Startup Journey)
  page.html         legacy So Simple Theme page layout
_includes/          mostly legacy So Simple Theme partials, largely unreferenced by Nocturne layouts
_data/projects.yml  "Selected work" timeline shown on the homepage
assets/css/nocturne.css   the entire active design, single stylesheet
assets/js/                nocturne-peek.js (Luke 12 bottom-sheet), legacy So Simple JS
images/            all site images
images/photos/     post-specific screenshots/photos (see naming convention below)
```

## Writing a new post

Frontmatter conventions (see any recent file in `_posts/` for a live example):

```yaml
---
layout: post
title: "Title Here"
description: "One-sentence description/meta description."
category: some-category   # optional — omit entirely for no category; layout falls back to "Writing" eyebrow. Special-cased values: generosity -> "Generosity", openphoto-trovebox -> "Startup Journey"
logo:  skip
tags: [tag1,tag2]          # array, comma-separated, no spaces
image:
  feature: some-image.jpg  # optional; shown as the post's feature image if present
comments: false
share: true
---
```

`post.html` unconditionally renders `<p class="disclaimer">This post was not written with or by AI.</p>` on every post — a deliberate site-wide claim, not a bug. Be aware of it if a post's subject matter concerns AI.

### Images in post body

Convention: `images/photos/YYYY-MM-DD-descriptive-slug.ext`, referenced as `src="/images/photos/YYYY-MM-DD-descriptive-slug.ext"`.

Single image with caption:

```html
<figure>
	<img src="/images/photos/2026-08-25-example.png" alt="Descriptive alt text">
	<figcaption>Caption text.</figcaption>
</figure>
```

Multiple images in a row (horizontal row on desktop, stacked on mobile, breaks out to ~1040px wide regardless of the narrower article column):

```html
<figure class="shots">
	<div class="shots-row">          <!-- 3 images: use "shots-row" alone -->
	<!-- <div class="shots-row shots-row--4">   4 images: add the --4 modifier -->
		<figure>
			<img src="/images/photos/....png" alt="...">
			<figcaption>...</figcaption>
		</figure>
		<!-- repeat per image, each with its own figcaption -->
	</div>
</figure>
```

`shots-row` defaults to a 3-column grid; add `shots-row--4` for a 4-column desktop layout. Both collapse to a single column at ≤640px (defined in `assets/css/nocturne.css`).

## Image optimization

Recompress losslessly (no quality change, no resizing) before committing new or updated images.

Requires `oxipng` and `jpeg-turbo` (installed via Homebrew: `brew install oxipng jpeg-turbo`).

```bash
cd images

# PNGs
find . -type f -iname "*.png" -print0 | xargs -0 oxipng -o max --strip safe -a -q

# JPEGs
JPEGTRAN="$(brew --prefix jpeg-turbo)/bin/jpegtran"
find . -type f \( -iname "*.jpg" -o -iname "*.jpeg" \) -print0 | while IFS= read -r -d '' f; do
  "$JPEGTRAN" -copy none -optimize -progressive -outfile "$f.opt" "$f" && mv "$f.opt" "$f"
done
```

This mirrors the lossless intent of the `imagemin`/`svgmin` tasks already declared in `Gruntfile.js`, without requiring the Node/Grunt toolchain to be installed locally.
