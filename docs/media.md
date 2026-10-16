# In the Media

The "In the Media" section on the home page is built from `data/media.yaml`.

## Adding coverage

Add an entry at the top of `data/media.yaml` (newest first):

```yaml
- outlet: ABC News
  title: "Headline exactly as the outlet published it"
  date: 2026-09-29
  url: https://www.abc.net.au/news/...
```

The home page shows the six most recent entries; older ones sit behind an
"All coverage" button.

## What to include

Only established outlets: national broadcasters and newspapers (ABC, SBS,
The Sydney Morning Herald, The Guardian, news.com.au, ...), The Conversation,
and the UNSW Newsroom. Skip aggregators, syndicated reposts, press-release
mirrors and small blogs, even when they cover the same story.

When a story is picked up widely, list the original and the one or two most
prominent outlets rather than every repost.
