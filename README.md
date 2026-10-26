# davidtorosyan.github.io

Personal portfolio site. Plain HTML + CSS — no build step, no dependencies.

## Running locally

Open `index.html` in a browser, or serve it:

```sh
python -m http.server 8000
```

## Adding a project

Projects are grouped into `<section class="projects">` blocks in
`index.html` (web apps, libraries & tools, just for fun, userscripts, open
source); add `grid` to a section's class for two-column small cards. Copy an
`<article class="card">` block into the right section and edit the title,
description, language, and links. Language dot colors are defined in
`assets/css/style.css` (`.dot-js`, `.dot-ts`, `.dot-py`, ...).
[PROJECTS.md](PROJECTS.md) records which repos are listed and why.

## Cache busting

Local asset URLs in `index.html` carry `?v=<build>`, and the footer shows
`build <build>`. Before pushing a change, run:

```sh
python scripts/bump_build.py
```

New CSS and icons then load immediately, and the footer tells you which
build you're seeing. The HTML itself is cached by GitHub Pages for up to 10
minutes. If the footer still shows the old build, hard-refresh or add any
query string to the URL (e.g. `/?1`).

## Icons

This repo owns the icons for the site and all project sites. Each
project's glyph is a list of shapes in `PROJECTS` in
`scripts/gen_icons.py` (run with `pip install pillow`, then
`python scripts/gen_icons.py`), which writes all of these under
`assets/icons/<project>/`:

- `favicon.svg` — modern browsers, and the portfolio card icon
- `favicon.ico` — 16/32/48 fallback
- `apple-touch-icon.png` — 180x180, full-bleed

Project sites reference these by absolute path (same domain), e.g.:

```html
<link rel="icon" href="/assets/icons/hood/favicon.ico" sizes="32x32">
<link rel="icon" type="image/svg+xml" href="/assets/icons/hood/favicon.svg">
<link rel="apple-touch-icon" href="/assets/icons/hood/apple-touch-icon.png">
```
