# Agent instructions

Static workshop site. GitHub Pages serves this directory from `main`.

Repo: `marscod/AABA4ET.NeurIPS.2026`  
Live: https://marscod.github.io/AABA4ET.NeurIPS.2026/

## Source of truth

Edit **`generate_pages.py`**, then regenerate. Do not hand-edit generated HTML or discovery files; the next generate overwrites them.

| Edit | Generated (do not edit) |
|------|-------------------------|
| `generate_pages.py` | `index.html`, `call-for-papers.html`, `speakers.html`, `panel.html`, `schedule.html`, `organizers.html`, `accepted-papers.html`, `past.html` |
| `style.css`, `script.js` | `robots.txt`, `sitemap.xml`, `llms.txt`, `llms-full.txt` |
| `images/` | |

`README.md` is public. Keep it short. Put workflow here, not in the README.

## How to update content

All page copy, nav, SEO, and most people lists live in `generate_pages.py`.

1. Change the relevant section (see map below).
2. Add or replace photos under `images/speakers/`, `images/panelists/`, or `images/organizers/` when needed.
3. Run `python3 generate_pages.py` from this directory.
4. Preview locally, then open a PR.

### Where to edit

| Change | Location in `generate_pages.py` |
|--------|----------------------------------|
| Site URL, OpenReview, default description | Constants at top (`SITE_URL`, `OPENREVIEW`, …) |
| Nav / footer links | `PAGES`, `nav()`, `footer()` |
| Steering committee | `STEERING` list |
| Home, CFP, schedule, accepted papers, past | `home_body`, `cfp_body`, `schedule_body`, `accepted_body`, `past_body` |
| Speakers / panel / organizers bios | `speakers_body`, `panel_body`, `organizers_body` |
| New page | Add to `PAGES`, `nav()`, `footer()`, a `*_body`, and a `write_text` call at the bottom |
| Crawler / LLM briefs | `write_discovery_files()` (also rewritten on every generate) |

If dates, submission links, or the workshop description change, update them in every body string that mentions them **and** in `write_discovery_files()` / JSON-LD so pages stay consistent.

## People: speakers, panelists, organizers

Full bios use `person_name()` plus `social_icons()`. Steering committee uses `steering_card()` (name, affiliation, optional photo, optional title) and has **no** social links today.

Always add every public URL you have: personal website, LinkedIn, and Google Scholar. Omit only a link that does not exist. Never invent or guess a URL.

### Card layout

Speakers: `<article class="person-full speaker">`. Panelists use the same class. Organizers: `<article class="person-full">` (no `speaker`). Copy lives in `speakers_body`, `panel_body`, or `organizers_body`.

```html
<article class="person-full speaker">
  <img class="person-photo" src="images/speakers/slug.jpg" alt="Full Name" width="160" height="160" loading="lazy" />
  <div class="person-copy">
    {person_name("Full Name", "https://example.com/")}
    <p class="role">Title, Affiliation</p>
    <p class="title-talk">Title: TBD</p>
    <p>Short bio.</p>
{social_icons("https://example.com/", "https://www.linkedin.com/in/handle", "https://scholar.google.com/citations?user=USERID&hl=en")}
  </div>
</article>
```

- Photo: `images/speakers/`, `images/panelists/`, or `images/organizers/`. Lowercase kebab-case filenames. If there is no photo, use `<div class="person-photo person-photo--placeholder" aria-hidden="true"></div>` instead of `<img>`.
- `person_name(name, website=None)` renders the heading. Pass the website as the second argument when you have one (same URL as `social_icons` website).
- Role: one line, title then affiliation. Speakers also get `<p class="title-talk">Title: TBD</p>` until the talk title is known.
- Organizers may include `<p class="expertise"><strong>Expertise:</strong> …</p>` after the bio.
- Escape `&` as `&amp;` in HTML strings.

### Social icons

`social_icons(website=None, linkedin=None, scholar=None)` prints icons in that order: globe, LinkedIn, Scholar. Missing arguments are skipped; if all are missing, nothing is rendered.

| Link | Argument | URL shape |
|------|----------|-----------|
| Personal / lab site | `website` | `https://…` (homepage, lab page, or GitHub Pages). Trailing slash optional. |
| LinkedIn | `linkedin` | `https://www.linkedin.com/in/handle` — profile, not a company page or search URL. |
| Google Scholar | `scholar` | `https://scholar.google.com/citations?user=USERID&hl=en` — keep the `user=` id. |

When every URL is known, positional args match the signature:

```python
{social_icons("https://example.com/", "https://www.linkedin.com/in/handle", "https://scholar.google.com/citations?user=USERID&hl=en")}
```

When some are missing, use keywords so later args do not shift:

```python
{social_icons(linkedin="https://www.linkedin.com/in/handle", scholar="https://scholar.google.com/citations?user=USERID&hl=en")}
{social_icons("https://example.com/", scholar="https://scholar.google.com/citations?user=USERID&hl=en")}
```

Do not pass empty strings. Prefer `https://`. Do not add Twitter/X or other networks unless the helpers are extended. Leave `social_icons(...)` on its own line inside `person-copy`, after the bio.

## Regenerate

```bash
python3 generate_pages.py
```

Expect `Generated pages OK`. Commit both the script change and the regenerated files.

## Preview

```bash
python3 -m http.server 8080
```

Open http://127.0.0.1:8080/ and check every page you touched (nav, mobile menu, photos).

## Create a PR

Work in a branch. Do not commit directly to `main`.

```bash
git checkout main
git pull origin main
git checkout -b feat/short-description
python3 generate_pages.py
git add -A
git status
git diff --staged
git commit -m "$(cat <<'EOF'
feat: short description of the change.

EOF
)"
git push -u origin HEAD
gh pr create --title "feat: short description" --body "$(cat <<'EOF'
## Summary
- What changed and why

## Test plan
- [ ] Regenerated with `python3 generate_pages.py`
- [ ] Previewed affected pages locally
EOF
)"
```

Use conventional commits (`feat`, `fix`, `chore`, `docs`, `refactor`). Keep PRs small and focused. Do not force-push to `main`. Do not commit secrets or `.env` files.

After merge, GitHub Pages updates from `main`.
