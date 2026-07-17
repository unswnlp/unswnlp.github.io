# Courses

Courses live in `content/activities/courses/` and show up under Activities >
Teaching.

## Adding a course

Create one file per course, e.g. `content/activities/courses/comp1234.md` —
this is a **one file per course, many terms** model: don't create a new file
each term, just append to `terms:` on the existing course file.

```yaml
---
title:       "Course Full Name"
course:      true
courseCode:  "COMP1234"
terms:
  - term: "T1 2026"
    convenor: Aditya Joshi        # single name — use for courses with a convenor
    # lecturer: Aditya Joshi      # use instead of convenor where that's the site's term
    team:                          # optional — teaching team for that term, one or more names
      - Some Group Member
lastTaught: 2026-05-15
---
```

To add a new term to an existing course, append another entry to the `terms:`
list (most recent first is conventional but not required — the page doesn't
re-sort them). Update `lastTaught` to the end date of the most recent term.
