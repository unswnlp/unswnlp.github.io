# People

Core group members each get their own file in `content/people/`. Everyone else
(masters/honours students, taste-of-research, research assistants, alumni)
lives in two roster files instead of individual pages.

## Adding a core member (PI, postdoc, Ph.D., M.Phil.)

1. Add a photo to `content/people/pictures/`, named after the person, e.g.
   `phd-07-jane-doe.jpg`.
2. Create `content/people/<role-prefix>-<nn>-first-last.md` (prefix convention:
   `acad-` for the PI, `post-` for postdocs, `phd-` for Ph.D. students,
   `mphil-` for M.Phil. students). The number keeps files sorted; use the next
   free one for that prefix.
3. Fill in the front matter:

   ```yaml
   ---
   title:       "Jane Doe"
   weight:      7                      # controls ordering within the role
   role:        "Ph.D. Students"       # must be one of the roles below
   photo:       "people/pictures/phd-07-jane-doe.jpg"
   comment:     "Co-advise w/ <a href='...' class='join-link'>Some Prof</a>"  # optional, HTML allowed
   research:    "Short research blurb" # optional, shown under the name
   website:     "https://jane.github.io"     # optional
   email:       "j.doe@unsw.edu.au"           # optional
   google_scholar: "https://scholar.google.com/citations?user=..."  # optional
   twitter:     "https://twitter.com/janedoe" # optional
   ---
   ```

   `role` must exactly match one of: `Principal Investigator`, `Postdocs`,
   `Ph.D. Students`, `M.Phil. Students`, `Visiting Researchers` — anything
   else silently won't show up on the People page.

No other page needs editing — the People page (`layouts/people/list.html`)
automatically groups and lists every page with a matching `role`.

## Adding a non-core member (masters, honours, ToR, RA)

These live as simple list entries, not separate pages, in
`content/people/rest.md`:

```yaml
groups:
  - name: "Honours Students"
    members:
      - name: "New Student (Primary: Supervisor Name)"  # supervisor optional
```

Add a new `members` entry under the matching `- name:` group (or add a new
group if needed). No `note:` field is used here (see alumni below).

## Moving someone to alumni

**Members with a profile file** (`content/people/phd-*.md`, `mphil-*.md`, ...):
do not delete the file. Add two lines to its front matter:

```yaml
status: past                 # current is the default; past hides them from People
pastNote: "co-supervised with X; Now: Research Scientist @ Company"   # optional
```

They disappear from the People page and appear on Past Members under the group
matching their `role` (e.g. `M.Phil. Students` goes under "M.Phil Students").
The photo and links stay in the file, so moving them back is one line.

**Members without a profile file** (listed in `content/people/rest.md`): move
their entry into `content/people/alumni.md`, under the matching group:

```yaml
groups:
  - name: "Ph.D. Students"
    members:
      - name: "Jane Doe"
        note: "co-supervised with X; Now: Research Scientist @ Company"  # optional
```

`note:` / `pastNote:` is optional and shows as a small tooltip next to the name.
