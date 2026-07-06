# davidtorosyan.github.io

Personal portfolio site. Plain HTML + CSS — no build step, no dependencies.

## Running locally

Open `index.html` in a browser, or serve it:

```sh
python -m http.server 8000
```

## Adding a project

Copy an `<article class="card">` block in `index.html` and edit the
title, description, language, and links. Language dot colors are defined
in `assets/css/style.css` (`.dot-js`, `.dot-ts`, `.dot-py`, ...).

## Icons

This repo owns the icons for the site and all project sites. Each
project gets a glyph in `scripts/gen_icons.py` (run with `pip install
pillow`, then `python scripts/gen_icons.py`) plus a matching
hand-authored `favicon.svg`, published under `assets/icons/<project>/`:

- `favicon.svg` — modern browsers, and the portfolio card icon
- `favicon.ico` — 16/32/48 fallback
- `apple-touch-icon.png` — 180x180, full-bleed

Project sites reference these by absolute path (same domain), e.g.:

```html
<link rel="icon" href="/assets/icons/hood/favicon.ico" sizes="32x32">
<link rel="icon" type="image/svg+xml" href="/assets/icons/hood/favicon.svg">
<link rel="apple-touch-icon" href="/assets/icons/hood/apple-touch-icon.png">
```
