# Spark machines user guide (`/spark-docs/`)

The user guide for the group's GPU machines: spark-1 (two GB10 nodes) and spark-2 (one GB10
node, `unswnlp-spark2`). Both are set up the same way, so the guide is written for both, with
spark-1's differences called out. It's a "docsite" like
TriageSim's: see [docs/adding-a-docsite.md](adding-a-docsite.md) for how docsites work. This
file covers what's specific to this one.

- **Not linked from anywhere** on the site. Accounts are invitation-only, so new users get
  the link with their account.
- **Source**: `sources/spark-docs/` in this repo (MkDocs Material). It's docs only, so unlike
  TriageSim it lives here rather than in its own repo; Hugo ignores the folder. The prose is
  Markdown under its `docs/`. Never hand-edit `content/spark-docs/`: the port script
  regenerates it.
- **Config**: `scripts/port-spark-docs.py` (`DOCSITE_KEY = "spark-docs"` and its `PAGES`
  list) and `data/docsites/spark-docs.yaml` (sidebar). Update both if a page is added,
  renamed or removed in `sources/spark-docs/mkdocs.yml`'s `nav:`.
- **Public**: the site is public, so the guide never gives the machines' IP addresses. Users
  get them with their account.

## Updating the guide

```bash
pip install mkdocs-material beautifulsoup4      # once
(cd sources/spark-docs && mkdocs build)
python3 scripts/port-spark-docs.py
hugo server                                     # check /spark-docs/...
```

Then commit `content/spark-docs/` here as normal.
