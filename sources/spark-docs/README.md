# spark-docs

Source for the user guide to the Spark machines (spark-1 and spark-2), published at <https://unswnlp.github.io/spark-docs/>.

The prose is Markdown under `docs/`. This MkDocs Material site is not deployed itself: its
build is ported into the group website as a "docsite" (see `docs/adding-a-docsite.md` and
`docs/spark-docs.md` at the top of this repo).

```bash
pip install mkdocs-material
mkdocs serve                 # preview locally
mkdocs build                 # then, from the repo root: python3 scripts/port-spark-docs.py
```

The site is public. Never put the machines' IP addresses, account names other than the
maintainer's, or admin-only procedures in these pages.
