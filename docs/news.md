# News

News items live in `content/news/` and show up as the "Recent News" list on
the homepage (most recent 10).

## Adding a news item

Create a new file, e.g. `content/news/18-something-2026-05.md` (numbered
prefix keeps files ordered; the date suffix is just a naming convention, the
`date:` field is what actually controls ordering).

```yaml
---
date: 2026-05-01
---
Free-text Markdown body — this is what's shown, e.g.:
[Some Paper](https://arxiv.org/abs/...) — one-line description — accepted to
[Some Venue 2026](https://someconference.org).
```

The whole page body (below the front matter) is rendered as the news text, so
just write normal Markdown/links there. Only the 10 most recent items show on
the homepage; older ones stay reachable at their own URL but aren't linked
from anywhere by default.
