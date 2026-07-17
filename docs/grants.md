# Grants

Grants live in `content/activities/grants/` and show up in two places: a
compact card on the homepage "Funding" section, and an expandable banner on
the `/activities/grants/` page (grouped by year). Clicking "More information"
on a homepage card jumps straight to that grant's banner and opens it.

## Adding a grant

Create a new file, e.g. `content/activities/grants/2026somegrant.md`. **The
filename (without `.md`) is the grant's slug** — it's used both as the page
anchor (`/activities/grants/#2026somegrant`) and as the value publications use
to link themselves to this grant (see `docs/publications.md`), so pick
something short and stable and don't rename it later.

```yaml
---
title: 'Short Name'              # shown on the card and as the collapsed banner's subtitle
longName: 'Full official project title'   # optional — shown instead of title once expanded; falls back to title
activityType: grants
date: 2026-01-01                 # used for year grouping and sort order
pi: Aditya Joshi                 # required — the lead investigator
piRole: CI                       # optional label next to the PI, e.g. CI, PI, Lead CI
grantType: Government            # UNSW-Internal | Government | Industry | Academia-Industry Partnership | Other
venue: Funding Body / Scheme Name
link: "https://..."              # optional — external grant source (award page, PDF, etc.)

investigators:                   # optional — other group members on the grant (comma-separated line)
    - "Other Group Member"

partners:                        # optional — external partner orgs, sub-bulleted
    - "Plain Partner Name"                     # no link
    - name: "Linked Partner"
      link: "https://partner.com"              # opens in a new tab

deliverables:                    # optional — anything that isn't a paper (packages, presentations, demos)
    - "Plain text deliverable"
    - title: "Linked deliverable"
      link: "https://..."
    # or embed a link inline as raw HTML:
    - Presentation at <a href="https://example.com/">Some Summit 2026</a>

projectPage: "https://..."       # optional — external project/demo site
---
```

## Linking papers to a grant

Don't list papers manually. Instead, add `grant: <slug>` to the publication's
own front matter (in `content/publications/accepted/` or `.../preprints/`),
where `<slug>` is the grant's filename without `.md`:

```yaml
grant: 2026somegrant
```

The paper will then automatically show up as a card (title, venue, authors)
under that grant's "Papers" section — no need to touch the grant file itself.

## Field reference

| Field | Required | Notes |
|---|---|---|
| `title` | yes | Short project name |
| `longName` | no | Full project name, shown when expanded |
| `date` | yes | Drives year grouping on `/activities/grants/` |
| `pi` / `piRole` | `pi` yes | Lead investigator + optional role label |
| `grantType` | no | One of the five categories above |
| `venue` | yes | Funding body / scheme name |
| `link` | no | External source (award page, PDF) |
| `investigators` | no | List of names (group members) |
| `partners` | no | List of strings or `{name, link}` |
| `deliverables` | no | List of strings, `{title, link}`, or raw HTML strings |
| `projectPage` | no | External project/demo URL |
