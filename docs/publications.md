# Publications

Publications live in two folders:

- `content/publications/accepted/` — published or accepted papers.
- `content/publications/preprints/` — preprints / arXiv-only work.

## Adding a paper

Create a new file, e.g. `content/publications/accepted/22-firstauthor-shortname-venue.md`
(numbered prefix keeps files ordered; the rest of the filename is free-form).

```yaml
---
title: 'Full Paper Title'
date: 2026-06-01
preprint: false            # true only for files under preprints/
authors:
    - "First Author"
    - "Second Author"

underlineAuthors:           # names from this list are bolded/underlined
    - "First Author"        # (use for current group members)

arxivID: "2606.01234"       # optional
links:
    paper: "https://aclanthology.org/..."   # or an arXiv PDF link
    code: "https://github.com/..."          # optional
    dataset: "https://huggingface.co/..."   # optional
    project: "https://..."                  # optional

venue: "Findings of ACL 2026"   # omit for preprints — a preprint auto-labels as "Preprint"
featured: true                  # optional — shows this paper in the homepage "Selected Publications"
grant: 2025dtb                  # optional — links this paper to a grant, see docs/grants.md
torwork: true                   # optional — shows under People > Student Work > Taste of Research
honorswork: true                # optional — shows under Student Work > Honours Projects
masterswork: true               # optional — shows under Student Work > COMP9991

bibtex: |
    @inproceedings{...}
---
```

Notes:

- `underlineAuthors` should list current group members only (matches the
  convention used across the whole site).
- Only set one of `torwork` / `honorswork` / `masterswork` if the paper came
  out of that kind of student project.
- To link a paper to a grant, set `grant:` to the grant's filename (without
  `.md`) from `content/activities/grants/` — see `docs/grants.md`. The paper
  will then automatically appear as a card under that grant's banner.
