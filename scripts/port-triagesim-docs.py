#!/usr/bin/env python3
"""Port the TriageSim docs into native Hugo content under content/triagesim/.

Source of truth for prose/API content is the sibling `triagesim-website` repo
(a separate MkDocs Material + mkdocstrings site). We don't publish that build
directly — instead this script takes its *rendered* HTML (so code highlighting,
admonitions, tabs, mermaid blocks, and the mkdocstrings API reference are all
already correct) and extracts just the article body, with internal links
rewritten to point at /triagesim/... on this site. The result is styled by our
own layouts/triagesim/*.html + assets/css/triagesim.css, not MkDocs Material's
CSS, so it looks native to unswnlp.github.io. See docs/triagesim.md.

Usage:
    cd ../triagesim-website && .venv/bin/mkdocs build
    cd ../unswnlp.github.io   # this repo
    python3 scripts/port-triagesim-docs.py
"""
import re
import os
from urllib.parse import urljoin, urlsplit
from bs4 import BeautifulSoup

SITE = "../triagesim-website/site"
OUT = "content/triagesim"
BASE = "https://unswnlp.github.io/triagesim/"

# (mkdocs page url path, target hugo content relpath under content/triagesim/)
# Keep this in sync with triagesim-website/mkdocs.yml's nav, and with
# layouts/partials/triagesim-nav.html on the Hugo side.
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


def target_for(mkdocs_url):
    """Map an mkdocs page path (relative to site root) to its Hugo /triagesim/ URL."""
    for src, _ in PAGES:
        if src == mkdocs_url:
            return "/triagesim/" + src if src else "/triagesim/"
    return None


def rewrite_hrefs(soup, current_mkdocs_url):
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
            if path.startswith("/triagesim/"):
                a["href"] = path
            continue
        # relative link -> resolve against current page, then map to hugo path
        resolved = urljoin(current_abs, href)
        path = urlsplit(resolved).path
        if path.startswith("/triagesim/"):
            rel = path[len("/triagesim/"):]
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
    title = re.sub(r"\s*-\s*TriageSim\s*$", "", title).strip()
    if not title:
        title = "TriageSim"
    rewrite_hrefs(article, mkdocs_url)
    inner_html = article.decode_contents().strip()
    return title, inner_html


def main():
    for mkdocs_url, rel in PAGES:
        title, body = extract(mkdocs_url)
        target_path = os.path.join(OUT, rel)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        fm_title = title.replace('"', '\\"')
        front_matter = f'---\ntitle: "{fm_title}"\n---\n\n'
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(front_matter)
            f.write(body)
            f.write("\n")
        print("wrote", target_path)


if __name__ == "__main__":
    main()
