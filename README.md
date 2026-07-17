# UNSW NLP Website

This is the [Hugo](https://gohugo.io) site for the UNSW NLP research group,
built on a fork of [Pascal Michaillat's academic website
template](https://github.com/pmichaillat/hugo-website) (MIT licensed, see
[LICENSE.md](LICENSE.md)). It's hosted on [GitHub
Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)
at https://unswnlp.github.io/.

## Installation

### On your local machine

- Install [Hugo](https://gohugo.io/installation/). On a Mac:
  `brew install hugo` (or `brew upgrade hugo` if already installed). This
  site requires the **extended** Hugo build (`hugo version` should say
  `extended`).
- Clone this repository:

  ```bash
  git clone https://github.com/unswnlp/unswnlp.github.io.git
  cd unswnlp.github.io
  ```

### On GitHub

- GitHub Actions and GitHub Pages must be enabled once, in the repo's
  **Settings > Pages**, with the publishing source set to "GitHub Actions".
- The workflow that builds and deploys the site on every push to `main` is
  defined in `.github/workflows/hugo.yml`. If it starts failing (e.g. after a
  Hugo version bump), compare it against the [official starter
  workflow](https://github.com/actions/starter-workflows/blob/main/pages/hugo.yml)
  — just make sure `push: branches` stays `["main"]`.

## Local development

From the repository root:

```bash
hugo server
```

This builds the site and serves it at http://localhost:1313, rebuilding
automatically as you edit files. Use this to preview changes before pushing.

## Deployment

Deployment is automatic: commit your changes and push to `main`. The GitHub
Actions workflow then builds the site with Hugo and publishes it to GitHub
Pages — there's no manual build or deploy step.

```bash
git add <files>
git commit -m "..."
git push origin main
```

## Adding content

Every page on the site is generated from Markdown files with YAML front
matter under `content/`. Each content type has its own guide with the exact
fields to fill in and where new files go:

| Page | Guide |
|---|---|
| People (PI, postdocs, students, alumni) | [docs/people.md](docs/people.md) |
| Publications (accepted papers & preprints) | [docs/publications.md](docs/publications.md) |
| Grants | [docs/grants.md](docs/grants.md) |
| Courses | [docs/courses.md](docs/courses.md) |
| Shared tasks, tutorials & workshops | [docs/shared-tasks-tutorials-workshops.md](docs/shared-tasks-tutorials-workshops.md) |
| News | [docs/news.md](docs/news.md) |
| Photo galleries | [docs/pictures.md](docs/pictures.md) |
| Location | [docs/location.md](docs/location.md) |

In general: copy the front matter pattern from an existing file of the same
type, fill in the new values, and run `hugo server` locally to check it
renders before pushing.

## License

This repository is licensed under the [MIT License](LICENSE.md).
