# Nocturne theme — install into jmathai.github.com

This folder is a drop-in Jekyll theme that renders the new warm/editorial design
at your existing permalinks, driven by your existing `_posts` and categories.
Nothing about your content or URLs changes.

## Copy these into the repo root

```
_layouts/nocturne.html      (new — base: head, nav, footer)
_layouts/home.html          (new — homepage hero + focus + work timeline)
_layouts/post.html          (OVERWRITES the old post layout — the article reading view)
_layouts/archive.html       (new — writing list + collection pages)
_data/projects.yml          (new — the "Selected work" timeline data; edit YAML, not markup)
assets/css/nocturne.css      (new — the whole design, one stylesheet)
assets/js/nocturne-peek.js   (new — the Luke 12 bottom-sheet)
index.html                  (OVERWRITES — now layout: home)
articles.html               (OVERWRITES — now layout: archive)
generosity.html             (OVERWRITES — now layout: archive)
openphoto-trovebox.md       (OVERWRITES — now layout: archive)
```

Your `_posts/*.md` need no change — they already say `layout: post` and the new
`post.html` picks up `title`, `date`, `category`, `image.feature`, and `author`.

## How it maps to your design

- **Permalinks unchanged.** `permalink:` in each page + your `_config.yml`
  (`/:categories/:title/`) are untouched, so every URL stays identical.
- **Article list** loops `site.posts`; **Generosity** loops `site.categories.generosity`;
  **Startup Journey** loops `site.tags.trovebox` — same sources your old pages used.
- **Work timeline** lives in `_data/projects.yml`. Add/edit an entry and the homepage updates.
- **Luke 12 peek** is the one interactive bit; `nocturne-peek.js` is ~30 lines of vanilla JS.

## Notes / things to check after you build (`bundle exec jekyll serve`)

1. **Images.** The homepage portrait uses `/assets/home/img/jaisen.jpg` (falls back to
   `/images/bio-photo-2.jpg`). Project icons and collaborator avatars come from
   `/assets/home/img/…`. If any are missing, drop them there or edit `_data/projects.yml`.
2. **Sojourn icon.** The newest work item uses a monogram tile in the app's brand color.
   Drop the real icon at `/assets/home/img/cd-icon-sojourn.png` and set `icon: cd-icon-sojourn.png`
   (remove `mono`/`mono_bg`) in `_data/projects.yml`.
3. **Post subheads.** In-post `**Bold lead-ins**` (e.g. "Donor Advised Funds") render as bold
   paragraphs. To make them large serif subheads like the prototype, change them to `## Donor Advised Funds`
   in the markdown.
4. **Other pages** (`about.md`, `theme-setup.md`, `404.md`, `download-elodie.md`) still use the
   old `page`/`default` layouts and old theme CSS — they were left untouched. Convert or remove
   as you like.
5. The old `_includes/head.html`, `navigation.html`, etc. are no longer referenced by these
   layouts and can be removed once you're happy.
