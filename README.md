# caldera-web

Source and published output for **[caldera.beer](https://caldera.beer)** — Caldera, Calcutta's Finest Craft.
Operated by Karnani FnB Specialities LLP.

Hosted on Netlify (project `caldera-beer`). A push to `main` deploys the site.

- Live: <https://caldera.beer>
- Netlify project: `caldera-beer` &middot; publish directory `public`, no build command

## Layout

| Path | What it is |
|---|---|
| `public/` | **The deployed site.** Netlify publishes this directory verbatim — no build step. |
| `src/` | The Python generators that produced `public/`, plus the CSS/JS sources they inline. |
| `src/data/outlets_public.json` | The outlet list rendered into `public/find.html`. Public-safe fields only. |
| `netlify.toml` | Publish directory and cache/security headers. |

## Deploying

Push to `main`. Netlify builds nothing and serves `public/`.

To change the site, edit under `src/`, regenerate (below), and commit the resulting `public/`.
For a one-line content fix, editing `public/` directly is fine — just mirror it into `src/` so the
next regeneration doesn't silently revert it.

## Regenerating

```bash
cd src
export CALDERA_SITE=../_work/site     # scratch tree, git-ignored
python3 build_all.py
```

**Always use `build_all.py`.** `build_white.py` regenerates every page at import time, so
running the stage scripts in separate processes lets the last one to import it clobber pages an
earlier stage had already specialised. `build_all.py` runs them in one process, where the import
is cached and each stage's output survives.

`outlets_prep.py` turns the internal ERP extract into `data/outlets_public.json`. It needs the source
workbook, which is **not in this repo** — see Data below.

Canonical host is set by `SITE_URL` at the top of `src/build_white.py`.

## Data

`src/data/outlets_public.json` holds only what the website shows: outlet name, area, venue type,
and whether the outlet serves Caldera on tap, by the pint, or both.

The ERP extract it derives from must **never** be committed. It carries per-outlet sales volumes,
excise licence numbers and last-sale dates — commercially sensitive, and this repository is public.
`.gitignore` blocks `*.xlsx` and `outlets_review.json` as a backstop, but the rule is the point,
not the backstop.

Outlets are included only once they have a usable area and a recognisable trading name. Licence-register
names, licensee personal names and bare street addresses are held back for review rather than published.

## Conventions

- Every page is self-contained HTML with relative asset paths, so the tree can be served from any root.
- `404.html` is the exception: it uses root-absolute paths so it renders correctly at any depth.
- Fonts: Poppins (headings and UI), Rock Salt (cursive accents), Oswald (legacy).
- Brand yellow `#F2C719`; gold `#A9790A` for accent text on white.
- Checked at 11 widths from 344px (Galaxy Z Fold) to 1920px, with no horizontal overflow.
