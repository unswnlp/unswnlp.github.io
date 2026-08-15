# TriageSim documentation (`/triagesim/`)

The TriageSim package docs (from the TRIBOT/NHMRC grant, see
[docs/grants.md](grants.md)) live as **native Hugo pages** under
`content/triagesim/`, styled entirely by this site's own layout and CSS
(`layouts/triagesim/*.html`, `assets/css/triagesim.css`) — not by MkDocs
Material. They render inside the normal site header/footer/nav, with a docs
sidebar of their own for in-docs navigation.

## Where the content actually comes from

The prose and the auto-generated API reference (from the `triagesim` Python
package's docstrings, via `mkdocstrings`) are authored in a separate sibling
repo, `triagesim-website` (a standalone MkDocs Material site). We don't hand
port that content by hand, and we don't publish its build as-is either —
instead, `scripts/port-triagesim-docs.py` takes MkDocs's *rendered* HTML
output for each page (so code highlighting, admonitions, tabs, mermaid
diagrams, and the mkdocstrings symbol docs are already correct) and extracts
just the `<article>` body, rewriting internal links to point at
`/triagesim/...` on this site. That HTML is dropped into
`content/triagesim/**/*.md` as the page body, with our own layout wrapped
around it.

This means: **edit prose/API docstrings in `triagesim-website`, never edit
the extracted HTML in `content/triagesim/` by hand** — it gets overwritten
every time the port script runs.

## Updating the docs

1. Make your changes in the other repo (`triagesim-website`) — Markdown
   under `docs/`, or docstrings in the `triagesim` package itself.
2. Rebuild that site and re-run the port script from here:

   ```bash
   cd ../triagesim-website
   .venv/bin/mkdocs build

   cd ../unswnlp.github.io      # this repo
   python3 scripts/port-triagesim-docs.py
   ```

3. Preview with `hugo server` and check the changed page(s) under
   `/triagesim/...`, then commit `content/triagesim/` (and any layout/CSS
   changes) here like normal.

## Adding or removing a doc page

`scripts/port-triagesim-docs.py` has a hardcoded `PAGES` list mapping each
MkDocs page path to its target file under `content/triagesim/`.
`layouts/partials/triagesim-nav.html` has a matching hardcoded nav (also used
to compute prev/next links). If a page is added, renamed, or removed in
`triagesim-website/mkdocs.yml`'s `nav:`, update **both** lists to match, then
re-run the port script.

## Design notes

- `assets/css/triagesim.css` is scoped entirely under a `.tsdoc` class so it
  can't leak into the rest of the site. It reuses the UNSW NLP palette/fonts
  from `assets/css/main.css` (same navy/purple, same Clancy/Roboto/Roboto
  Mono) rather than anything from Material.
- Mermaid diagrams are rendered client-side by a self-hosted
  `static/js/mermaid.min.js`, only loaded on pages that actually contain a
  `.mermaid` block (checked via `findRE` in
  `layouts/partials/triagesim-body.html`).
- Tabbed content (`=== "Tab"` blocks in the source Markdown) uses MkDocs's
  original pure-CSS radio-input pattern — no JS needed, just restyled in
  `triagesim.css`.
- `triagesim-website/mkdocs.yml` and `docs/stylesheets/extra.css` in that
  repo are still themed to match this site (in case anyone runs
  `mkdocs serve` there directly to preview), but **those files no longer
  affect what's actually deployed** at unswnlp.github.io/triagesim/ — only
  the rendered `<article>` content the port script extracts does.
