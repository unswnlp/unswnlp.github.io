# Brand files

`static/brand/` holds the UNSW-NLP lockup (logo, bar, "UNSW-NLP"), built from the
original logo and the Clancy Bold font rather than from a screenshot.

| File | Use |
|---|---|
| `unsw-nlp-logo.svg` | Website, documents; black text, transparent background |
| `unsw-nlp-logo-white.svg` | Dark backgrounds (slides, posters); white text |
| `unsw-nlp-logo.png` | Where SVG is not accepted (Word, some slide tools); 2851x840, transparent |
| `unsw-nlp-logo-white.png` | Same, white text |

The text is converted to outlines, so the files look the same without the font
installed. Published at https://unswnlp.github.io/brand/unsw-nlp-logo.svg etc.

The home page header uses `unsw-nlp-logo.svg`. The navbar keeps a separate
small version (mark + live text) because at 28px the lockup's text is too small.
