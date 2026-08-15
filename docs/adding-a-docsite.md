# Adding a "docsite" (ported project docs)

A "docsite" is a project's own documentation (prose + optionally an
auto-generated API reference), authored in that project's own repo and
docs tool, ported into this site as native Hugo pages so it looks and
navigates like part of unswnlp.github.io — not like an embedded third-party
tool. TriageSim's docs (`/triagesim/`, from the sibling `triagesim-website`
MkDocs Material repo) are the first one and the template for any future one.

**Only reachable from wherever you choose to link it** — there's no global
"Docs" nav item. TriageSim's is linked only from its publication entry (a
`docs:` link under that page's `links:` in
`content/publications/preprints/07-dipankar-triagesim-preprint.md` — see
`docs/publications.md`). Follow that pattern: link a new docsite from the
publication or grant it actually belongs to, not from the main nav.

## How the pieces fit together

- **Content**: `content/<slug>/**/*.md` — plain Hugo pages, but their body is
  raw HTML lifted from a build of the source project's own docs (see below),
  not hand-written Markdown.
- **Front matter**: every ported page has `type: "docsite"` and
  `docSite: "<slug>"`. `type` is what makes Hugo use the shared
  `layouts/docsite/{single,list}.html` templates regardless of what the
  content section is actually called; `docSite` is what tells those
  templates which sidebar/nav data to use.
- **Nav data**: `data/docsites/<slug>.yaml` — a `groups:` list of
  `{title, pages: [{url, title}]}`, read by `layouts/partials/docsite-nav.html`.
  This is the only thing that changes per project structurally (besides the
  content itself) — no new Go templates needed.
- **Theme**: `assets/css/docsite.css`, scoped entirely under `.docsite` /
  `.docsite-*` classes, shared by every docsite. It reuses this site's own
  palette/fonts (`assets/css/main.css`'s navy/purple, Clancy/Roboto/Roboto
  Mono) and styles every element type MkDocs Material commonly produces:
  code blocks (with a copy button), tables, admonitions, pure-CSS tabs,
  mermaid containers, landing-page cards/buttons, and mkdocstrings'
  class/function/method symbol badges.
- **Port script**: `scripts/port-docsite.py` — the template script. It reads
  a *built* MkDocs Material site (`mkdocs build` output), extracts each
  page's rendered `<article>` body (so highlighting/admonitions/tabs/mermaid/
  mkdocstrings output are already correct — Hugo/goldmark can't parse
  MkDocs's pymdownx Markdown extensions, so we never touch the raw source
  Markdown), rewrites internal links to root-relative `/<slug>/...` paths,
  and writes the result into `content/<slug>/` with the `type`/`docSite`
  front matter already set.

## Porting a new project's docs

1. **Get the source docs built.** The project needs its own MkDocs Material
   site (or similar) somewhere buildable — doesn't have to be a sibling repo,
   just somewhere you can point the port script at its build output.
2. **Copy `scripts/port-docsite.py`** (or edit it in place if you're not
   keeping TriageSim's port around) and fill in its `CONFIG` block: the
   built site's path, the target `content/<slug>/` dir, the docsite's
   canonical URL, a `DOCSITE_KEY`, and a `PAGES` list mapping each source
   page path to its target Hugo file — mirror the source project's own nav
   structure here.
3. **Add `data/docsites/<slug>.yaml`** with a `groups:` list matching the
   `PAGES` you just listed — this drives the sidebar and prev/next links.
   Copy `data/docsites/triagesim.yaml`'s shape.
4. **Run the port**: build the source site, then run your script from this
   repo's root. Check `hugo server` locally — routes should resolve at
   `/<slug>/...`, with the sidebar, code copy buttons, and (if used) mermaid
   diagrams all working.
5. **Link it in** from wherever makes sense — typically a `docs:` link on
   the relevant publication or grant (see `docs/publications.md` /
   `docs/grants.md`), not the main nav.
6. **Re-run the port** whenever the source docs change — it fully
   regenerates `content/<slug>/`, so never hand-edit those files directly.

## Design notes that carry over to any docsite

- Mermaid diagrams render via a self-hosted `static/js/mermaid.min.js`
  (shared across all docsites), only loaded on pages whose extracted content
  actually contains a `.mermaid` block (checked via `findRE` in
  `layouts/partials/docsite-body.html`) — no per-project asset needed.
- Tabbed content (MkDocs's `=== "Tab"` blocks) uses its original pure-CSS
  radio-input pattern; `docsite.css` just restyles it, no JS required.
- The sidebar is a single `<details>` element: forced permanently open (via
  `display: block !important` on non-summary children) above 780px width so
  it reads as a plain sidebar, and a real collapsible native `<details>`
  menu below that — never a flattened wall of links on narrow viewports.

See `docs/triagesim.md` for the TriageSim-specific specifics (its own
`CONFIG`/data file values, its source repo, how to refresh it).
