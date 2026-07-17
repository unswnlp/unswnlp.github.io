# Photo Galleries

The homepage has two sliding photo galleries: "Group at Conferences" and
"Group Outings", backed by `content/pictures/conferences/` and
`content/pictures/outings/` respectively.

## Adding a photo

1. Drop the image file directly into `content/pictures/conferences/` or
   `content/pictures/outings/`.
2. Add an entry for it in that folder's `_index.md`, under `resources:`:

   ```yaml
   resources:
     - src: "your-image-file.jpg"     # must match the filename exactly
       params:
         date: 2026-05-01             # controls sort order (most recent first)
         description: "Short caption shown on the slide."
   ```

That's it — no other page needs editing. The gallery automatically shows the
most recent photo first and cycles through all of them.
