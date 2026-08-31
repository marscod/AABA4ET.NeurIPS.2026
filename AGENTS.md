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

Person cards: use `person_name()`, `social_icons()`, and `steering_card()`. Photos are optional; without a file, a placeholder is used.

If dates, submission links, or the workshop description change, update them in every body string that mentions them **and** in `write_discovery_files()` / JSON-LD so pages stay consistent.

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
