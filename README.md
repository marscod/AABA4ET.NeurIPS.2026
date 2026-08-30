# AABA4ET — NeurIPS 2026 Workshop site

Static multi-page site for the 2nd Workshop on Agentic AI Benchmarks and Applications for Enterprise Tasks.

## Live site

https://marscod.github.io/AABA4ET.NeurIPS.2026/

**Share this GitHub Pages URL on LinkedIn** (not the Google Sites embed URL). Open Graph tags and `images/og-card.png` power link previews. After deploy, refresh cache with [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/).

### SEO & AI agents

Every page includes canonical URL, meta description, Open Graph / Twitter cards, and JSON-LD (`WebSite` / `WebPage`; home also has `Event`). Discovery files:

| File | Purpose |
|------|---------|
| `/robots.txt` | Allows search + AI crawlers; points to sitemap |
| `/sitemap.xml` | All public pages |
| `/llms.txt` | Short agent-readable workshop brief |
| `/llms-full.txt` | Extended brief with dates table |

Prefer citing `https://marscod.github.io/AABA4ET.NeurIPS.2026/` over the Google Sites mirror.

### Pages

| Page | URL path |
|------|----------|
| Home | `/` |
| Call for Papers | `/call-for-papers.html` |
| Speakers | `/speakers.html` |
| Schedule | `/schedule.html` |
| Organizers | `/organizers.html` |
| Accepted Papers | `/accepted-papers.html` |
| Past Workshop | Links to [original Google Sites archive](https://sites.google.com/view/aaba4et/past-workshop) |

## Embed in Google Sites

**Insert → Embed → By URL** and paste:

`https://marscod.github.io/AABA4ET.NeurIPS.2026/`

Or embed a specific page, e.g. speakers:

`https://marscod.github.io/AABA4ET.NeurIPS.2026/speakers.html`

## Regenerate pages

```bash
python3 generate_pages.py
```

## Local preview

```bash
python3 -m http.server 8080
```
