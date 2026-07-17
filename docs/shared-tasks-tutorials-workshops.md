# Shared Tasks, Tutorials & Workshops

These live together in `content/activities/shared-tasks-tutorials-workshops/`
and show up under Activities, grouped by type.

## Adding an entry

Create a new file, e.g.
`content/activities/shared-tasks-tutorials-workshops/03-aditya-newthing.md`.
The schema is the same as a publication entry (see `docs/publications.md`),
plus one required field:

```yaml
---
title: 'Title of the Shared Task / Tutorial / Workshop Proceedings'
activityType: shared-task    # one of: shared-task | tutorial | workshop
date: 2026-01-08
authors:
    - Aditya Joshi
    - Other Organiser

underlineAuthors:
    - "Aditya Joshi"

arxivID: "2601.01234"        # optional
links:
    paper: "https://arxiv.org/pdf/2601.01234"

venue: "Some Conference 2026"

bibtex: |
    @misc{...}
---
```

`activityType` controls which section it appears under on the Activities
page (Tutorials, Workshops, or Shared Tasks) — it must be exactly
`shared-task`, `tutorial`, or `workshop`.
