# Brand files

The UNSW-NLP mark is the official UNSW logo on a cloud of bubbles: one bubble
per group member, coloured by region (teal top-left, yellow top-right, purple
bottom-left, coral bottom-right) and blending where bubbles overlap.

## Current logo

```bash
python3 scripts/build-logo.py --people 150 --seed 60 --logo-width 50 --opacity 50 --all
```

`--all` rebuilds everything the site uses from the mark: the lockup, navbar
mark, favicons, legacy `logo.png` / `prof-pic.png` and the link-preview image.

## Trying variations

```bash
python3 -m http.server --directory scripts 8765
```

Open http://localhost:8765/logo-studio.html, adjust the sliders (bubbles,
layout, logo size, opacity) and copy the command it shows. The studio and the
script use the same drawing rules, so the files match the preview exactly.

## Files in `static/brand/`

| File | Use |
|---|---|
| `unsw-nlp-mark.svg` / `.png` | The square mark on its own |
| `unsw-nlp-logo.svg` / `.png` | Mark, bar and "UNSW-NLP"; black text, transparent background |
| `unsw-nlp-logo-white.svg` / `.png` | Same with white text, for dark backgrounds |

The official UNSW logo files used as the source go in `scripts/brand-src/`
(`unsw-sydney-portrait.png`, from UNSW's internal logo pack). That folder is
git-ignored, so copy the files there before rebuilding on a new machine.
