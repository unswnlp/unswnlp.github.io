#!/usr/bin/env python3
"""Port a project's MkDocs Material docs into native Hugo content.

This is the reusable template for bringing a project's documentation onto
unswnlp.github.io as a "docsite" — its own content/<slug>/ tree, rendered by
the shared layouts/docsite/*.html + assets/css/docsite.css theme, not the
source project's own MkDocs/Material CSS. See docs/adding-a-docsite.md for
the full walkthrough; this docstring covers just the script.

How it works: rather than hand-porting Markdown (which would drop pymdownx
syntax our Hugo/goldmark doesn't understand — admonitions, tabs, mermaid
fences, mkdocstrings directives, ...) this script takes the *rendered* HTML
from an `mkdocs build` of the source repo and extracts just each page's
<article> body, with internal links rewritten to point at /<slug>/... on
this site. Code highlighting, admonitions, tabs, mermaid blocks, and any
mkdocstrings-generated API reference all arrive already correct.

To port a NEW project's docs:
  1. Copy this file (or just edit the CONFIG block below if you're
     replacing TriageSim's port).
  2. Fill in CONFIG: the built source site's path, this repo's output path,
     the site's base URL, and the PAGES list (mkdocs page path -> target
     Hugo file, matching that project's mkdocs.yml nav).
  3. Add a matching data/docsites/<slug>.yaml (same `groups` shape as
     data/docsites/triagesim.yaml) for the sidebar/prev-next nav.
  4. Run: mkdocs build (in the source repo), then this script (from this
     repo's root). It sets `type: docsite` + `docSite: <slug>` in each
     generated page's front matter automatically.

Usage (TriageSim, the current default CONFIG):
    cd ../triagesim-website && .venv/bin/mkdocs build
    cd ../unswnlp.github.io   # this repo
    python3 scripts/port-docsite.py
"""
import re
import os
from urllib.parse import urljoin, urlsplit
from bs4 import BeautifulSoup

# ─────────────────────────── CONFIG ───────────────────────────
# Everything in this block is project-specific — change it (or copy this
# whole file) to port a different project's docs.

DOCSITE_KEY = "triagesim"                 # matches data/docsites/<key>.yaml
SITE = "../triagesim-website/site"        # built `mkdocs build` output to read from
OUT = "content/triagesim"                 # Hugo content dir to write into
BASE = "https://unswnlp.github.io/triagesim/"  # this docsite's canonical URL
TITLE_SUFFIX_RE = r"\s*-\s*TriageSim\s*$"  # strips the site name mkdocs appends to <title>
DEFAULT_TITLE = "TriageSim"                # fallback if a page has no <title>

# (mkdocs page url path, target hugo content relpath under OUT/)
# Keep this in sync with the source repo's mkdocs.yml nav, and with
# data/docsites/<DOCSITE_KEY>.yaml on the Hugo side.
PAGES = [
    ("", "_index.md"),
    ("getting-started/installation/", "getting-started/installation.md"),
    ("getting-started/configuration/", "getting-started/configuration.md"),
    ("getting-started/quickstart/", "getting-started/quickstart.md"),
    ("guide/concepts/", "guide/concepts.md"),
    ("guide/personas/", "guide/personas.md"),
    ("guide/agents/", "guide/agents.md"),
    ("guide/runner/", "guide/runner.md"),
    ("guide/artifacts/", "guide/artifacts.md"),
    ("guide/metrics/", "guide/metrics.md"),
    ("guide/audio/", "guide/audio.md"),
    ("api/", "api/_index.md"),
    ("api/runner/", "api/runner.md"),
    ("api/agents/", "api/agents.md"),
    ("api/core/", "api/core.md"),
    ("api/personas/", "api/personas.md"),
    ("api/utils/", "api/utils.md"),
    ("api/audio/", "api/audio.md"),
    ("citation/", "citation.md"),
]
# ─────────────────────────────────────────────────────────────


def target_for(mkdocs_url):
    """Map an mkdocs page path (relative to site root) to its Hugo URL."""
    prefix = "/" + DOCSITE_KEY + "/"
    for src, _ in PAGES:
        if src == mkdocs_url:
            return prefix + src if src else prefix
    return None


def rewrite_hrefs(soup, current_mkdocs_url):
    prefix = "/" + DOCSITE_KEY + "/"
    current_abs = urljoin(BASE, current_mkdocs_url)
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("#") or href.startswith("mailto:"):
            continue
        if href.startswith("http://") or href.startswith("https://"):
            if not href.startswith(BASE):
                continue  # external, leave as-is
            # absolute link to this same docs site -> make root-relative
            path = urlsplit(href).path
            if path.startswith(prefix):
                a["href"] = path
            continue
        # relative link -> resolve against current page, then map to hugo path
        resolved = urljoin(current_abs, href)
        path = urlsplit(resolved).path
        if path.startswith(prefix):
            rel = path[len(prefix):]
            a["href"] = target_for(rel) or path
        else:
            a["href"] = path


def extract(mkdocs_url):
    if mkdocs_url == "":
        path = os.path.join(SITE, "index.html")
    else:
        path = os.path.join(SITE, mkdocs_url, "index.html")
    html = open(path, encoding="utf-8").read()
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article", class_="md-content__inner")
    title_tag = soup.find("title")
    title = title_tag.get_text().strip() if title_tag else mkdocs_url
    title = re.sub(TITLE_SUFFIX_RE, "", title).strip()
    if not title:
        title = DEFAULT_TITLE
    rewrite_hrefs(article, mkdocs_url)
    inner_html = article.decode_contents().strip()
    return title, inner_html


def main():
    for mkdocs_url, rel in PAGES:
        title, body = extract(mkdocs_url)
        target_path = os.path.join(OUT, rel)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        fm_title = title.replace('"', '\\"')
        front_matter = (
            "---\n"
            f'title: "{fm_title}"\n'
            'type: "docsite"\n'
            f'docSite: "{DOCSITE_KEY}"\n'
            "---\n\n"
        )
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(front_matter)
            f.write(body)
            f.write("\n")
        print("wrote", target_path)


if __name__ == "__main__":
    main()
