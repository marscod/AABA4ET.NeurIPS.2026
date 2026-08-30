#!/usr/bin/env python3
"""Generate multi-page AABA4ET site with shared chrome."""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE_URL = "https://marscod.github.io/AABA4ET.NeurIPS.2026"
SITE_NAME = "AABA4ET — NeurIPS 2026 Workshop"
OG_IMAGE = f"{SITE_URL}/images/og-card.png"
OPENREVIEW = "https://openreview.net/group?id=NeurIPS.cc/2026/Workshop/AABA4ET"
DEFAULT_DESCRIPTION = (
    "2nd Workshop on Agentic AI Benchmarks and Applications for Enterprise Tasks — "
    "NeurIPS 2026, Sydney. Where Agentic AI meets the real world of work."
)
KEYWORDS = (
    "AABA4ET, NeurIPS 2026, agentic AI, enterprise AI, AI benchmarks, "
    "multi-agent systems, workshop, Sydney"
)
FONTS = """  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet" />"""

PAGES = [
    ("", "Home", "Workshop overview, focus areas, and important dates."),
    ("call-for-papers.html", "Call for Papers", "Submission guidelines, deadlines, and review process."),
    ("speakers.html", "Speakers", "Invited speakers."),
    ("panel.html", "Panel", "Industry and research panel."),
    ("schedule.html", "Schedule", "Workshop day schedule."),
    ("organizers.html", "Organizers", "Organizers and steering committee."),
    ("accepted-papers.html", "Accepted Papers", "Accepted papers (after notifications)."),
    ("past.html", "Past Workshop", "AAAI 2026 first-edition archive."),
]

def nav(active: str, prefix: str = "") -> str:
    def a(href, label, key):
        cur = ' aria-current="page"' if active == key else ""
        return f'<a href="{prefix}{href}"{cur}>{label}</a>'

    return f"""  <header class="site-header">
    <div class="wrap site-header__inner">
      <a class="site-logo" href="{prefix}index.html">AABA4ET<span>NeurIPS 2026</span></a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
        <span class="nav-toggle__icon" aria-hidden="true"><i></i><i></i><i></i></span>
        Menu
      </button>
      <nav class="site-nav" id="site-nav" aria-label="Primary">
        {a("index.html", "Home", "home")}
        {a("call-for-papers.html", "CFP", "cfp")}
        {a("speakers.html", "Speakers", "speakers")}
        {a("panel.html", "Panel", "panel")}
        {a("schedule.html", "Schedule", "schedule")}
        {a("organizers.html", "Organizers", "organizers")}
        {a("accepted-papers.html", "Papers", "accepted")}
        {a("past.html", "Past", "past")}
      </nav>
    </div>
  </header>"""


def footer(prefix: str = "") -> str:
    return f"""  <footer class="site-footer">
    <div class="wrap">
      <div class="site-footer__nav" aria-label="Footer">
        <a href="{prefix}index.html">Home</a>
        <a href="{prefix}call-for-papers.html">CFP</a>
        <a href="{prefix}speakers.html">Speakers</a>
        <a href="{prefix}panel.html">Panel</a>
        <a href="{prefix}schedule.html">Schedule</a>
        <a href="{prefix}organizers.html">Organizers</a>
        <a href="{prefix}accepted-papers.html">Accepted Papers</a>
        <a href="{prefix}past.html">Past Workshop</a>
      </div>
      <p>2nd Workshop on Agentic AI Benchmarks and Applications for Enterprise Tasks · NeurIPS 2026 · Sydney</p>
    </div>
  </footer>
  <script src="{prefix}script.js"></script>"""


ICON_WEB = """<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>"""

ICON_LI = """<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>"""

ICON_GS = """<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 24a7 7 0 1 1 0-14 7 7 0 0 1 0 14zm0-24L0 9.5l4.838 3.94A8 8 0 0 1 12 9a8 8 0 0 1 7.162 4.44L24 9.5z"/></svg>"""


def social_icons(
    website: str | None = None,
    linkedin: str | None = None,
    scholar: str | None = None,
) -> str:
    parts = ['      <div class="social-icons">']
    if website:
        parts.append(
            f'        <a href="{website}" target="_blank" rel="noopener" aria-label="Website" title="Website">{ICON_WEB}</a>'
        )
    if linkedin:
        parts.append(
            f'        <a href="{linkedin}" target="_blank" rel="noopener" aria-label="LinkedIn" title="LinkedIn">{ICON_LI}</a>'
        )
    if scholar:
        parts.append(
            f'        <a href="{scholar}" target="_blank" rel="noopener" aria-label="Google Scholar" title="Google Scholar">{ICON_GS}</a>'
        )
    parts.append("      </div>")
    return "\n".join(parts) if (website or linkedin or scholar) else ""


def person_name(name: str, website: str | None = None) -> str:
    return f"<h3>{name}</h3>"


def steering_card(name: str, affiliation: str, photo: str | None = None, title: str = "") -> str:
    if photo:
        media = (
            f'<img class="steering-photo" src="{photo}" alt="{name}" '
            f'width="88" height="88" loading="lazy" />'
        )
    else:
        initials = "".join(p[0] for p in name.split() if p[:1].isalpha())[:2]
        media = (
            f'<span class="steering-photo steering-photo--placeholder" '
            f'aria-hidden="true">{initials}</span>'
        )
    title_html = f'<p class="role">{title}</p>' if title else ""
    return f"""      <article class="steering-card">
        {media}
        <h3>{name}</h3>
        {title_html}
        <p>{affiliation}</p>
      </article>"""


STEERING = [
    ("Graham Neubig", "Carnegie Mellon University", "images/organizers/neubig.jpg"),
    ("Yonatan Bisk", "Carnegie Mellon University", "images/organizers/bisk.jpg"),
    ("Rosa Vitiello", "Carnegie Mellon University", None),
    ("Atsunori Moteki", "Fujitsu Ltd.", "images/organizers/moteki.jpg"),
    ("Hiromichi Kobashi", "Fujitsu Ltd.", None),
    ("Akiyoshi Uchida", "Fujitsu Ltd.", None),
    ("Takuto Sato", "Fujitsu Ltd.", None),
    ("Jun Takahashi", "Fujitsu Ltd.", None),
    ("Natsuki Miyahara", "Fujitsu Ltd.", None),
    ("Ryutaro Okada", "Fujitsu Ltd.", None),
    ("Moyuru Yamada", "Fujitsu Ltd.", None),
    ("Mehdi Bahrami", "Fujitsu Research of America, Inc.", "images/panelists/mehdi-bahrami.jpg"),
    ("Kanji Uchino", "Fujitsu Research of America, Inc.", None),
    ("Lei Liu", "Fujitsu Research of America, Inc.", None, "Senior Research Manager"),
    ("Vardaan Pahuja", "Fujitsu Research of America, Inc.", None, "Principal Researcher"),
    ("Pascal Singer", "GK Software SE", None),
    ("Jacqueline Tews", "GK Software SE", None),
    ("Hideo Saito", "Keio University", "images/organizers/saito.jpg"),
    ("Alexandre Drouin", "ServiceNow", "images/organizers/drouin.png"),
]
STEERING_GRID = "\n".join(steering_card(*row) for row in STEERING)


def absolute_url(path: str = "") -> str:
    return f"{SITE_URL}/{path}" if path else f"{SITE_URL}/"


def json_ld(title: str, description: str, path: str = "", *, is_home: bool = False) -> str:
    """Structured data for search engines and AI agents."""
    url = absolute_url(path)
    website = {
        "@type": "WebSite",
        "@id": f"{SITE_URL}/#website",
        "name": SITE_NAME,
        "url": f"{SITE_URL}/",
        "description": DEFAULT_DESCRIPTION,
        "inLanguage": "en",
        "publisher": {"@type": "Organization", "name": "AABA4ET", "url": f"{SITE_URL}/"},
    }
    webpage = {
        "@type": "WebPage",
        "@id": f"{url}#webpage",
        "url": url,
        "name": title,
        "description": description,
        "isPartOf": {"@id": f"{SITE_URL}/#website"},
        "about": {"@id": f"{SITE_URL}/#event"},
        "primaryImageOfPage": {"@type": "ImageObject", "url": OG_IMAGE, "width": 1200, "height": 630},
        "inLanguage": "en",
    }
    graph: list[dict] = [website, webpage]
    if is_home:
        event = {
            "@type": "Event",
            "@id": f"{SITE_URL}/#event",
            "name": "2nd Workshop on Agentic AI Benchmarks and Applications for Enterprise Tasks (AABA4ET)",
            "alternateName": ["AABA4ET", "AABA4ET NeurIPS 2026"],
            "description": DEFAULT_DESCRIPTION,
            "url": f"{SITE_URL}/",
            "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
            "eventStatus": "https://schema.org/EventScheduled",
            "startDate": "2026-12-11",
            "endDate": "2026-12-12",
            "location": {
                "@type": "Place",
                "name": "NeurIPS 2026",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Sydney",
                    "addressCountry": "AU",
                },
            },
            "image": [OG_IMAGE],
            "organizer": {
                "@type": "Organization",
                "name": "AABA4ET Organizers",
                "url": f"{SITE_URL}/organizers.html",
            },
            "isAccessibleForFree": True,
            "inLanguage": "en",
            "keywords": KEYWORDS,
            "offers": {
                "@type": "Offer",
                "url": OPENREVIEW,
                "availability": "https://schema.org/InStock",
                "validThrough": "2026-08-31",
                "description": "Paper submissions via OpenReview through August 31, 2026 (AoE).",
            },
        }
        graph = [website, event, webpage]
    dumped = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)
    return f'  <script type="application/ld+json">\n{dumped}\n  </script>'


def page(
    title,
    active,
    body,
    *,
    prefix="",
    body_class="",
    hero_title="",
    hero_lede="",
    archive=False,
    description=None,
    path="",
):
    css = f"{prefix}style.css"
    desc = description or DEFAULT_DESCRIPTION
    url = absolute_url(path)
    is_home = active == "home" and not path
    archive_html = ""
    if archive:
        archive_html = f"""  <div class="archive-banner">
    <div class="wrap">Archived — 1st edition at AAAI 2026 (Singapore). For the current 2nd edition, see <a href="{prefix}index.html">Home</a>.</div>
  </div>"""
    hero = ""
    if hero_title:
        hero = f"""  <section class="page-hero">
    <div class="page-hero__media" aria-hidden="true"></div>
    <div class="wrap">
      <p class="eyebrow">AABA4ET</p>
      <h1>{hero_title}</h1>
      <p class="lede">{hero_lede}</p>
    </div>
  </section>"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="keywords" content="{KEYWORDS}" />
  <meta name="author" content="AABA4ET Organizers" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
  <meta name="googlebot" content="index, follow" />
  <meta name="theme-color" content="#0d7377" />
  <link rel="canonical" href="{url}" />
  <link rel="alternate" type="text/plain" title="LLM-friendly summary" href="{SITE_URL}/llms.txt" />
  <meta property="og:site_name" content="{SITE_NAME}" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="{OG_IMAGE}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="AABA4ET NeurIPS 2026 Workshop — Sydney" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <meta name="twitter:image" content="{OG_IMAGE}" />
  <meta name="twitter:image:alt" content="AABA4ET NeurIPS 2026 Workshop — Sydney" />
{FONTS}
  <link rel="stylesheet" href="{css}" />
{json_ld(title, desc, path, is_home=is_home)}
</head>
<body class="{body_class}">
  <a class="skip-link" href="#main">Skip to main content</a>
{nav(active, prefix)}
{archive_html}
<main id="main">
{hero}
{body}
</main>
{footer(prefix)}
</body>
</html>
"""


def write_discovery_files() -> None:
    """robots.txt, sitemap.xml, and llms.txt for crawlers and AI agents."""
    today = date.today().isoformat()
    robots = f"""# AABA4ET — NeurIPS 2026
User-agent: *
Allow: /

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: LinkedInBot
Allow: /

User-agent: Twitterbot
Allow: /

User-agent: Slackbot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Anthropic-AI
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Applebot-Extended
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    (ROOT / "robots.txt").write_text(robots)

    url_entries = []
    for path, _label, _blurb in PAGES:
        loc = absolute_url(path)
        priority = "1.0" if not path else ("0.9" if path == "call-for-papers.html" else "0.7")
        changefreq = "weekly" if path in ("", "call-for-papers.html", "accepted-papers.html") else "monthly"
        url_entries.append(
            f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>"""
        )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(url_entries)
        + "\n</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(sitemap)

    page_lines = "\n".join(
        f"- [{label}]({absolute_url(path)}): {blurb}" for path, label, blurb in PAGES
    )
    llms = f"""# AABA4ET — NeurIPS 2026 Workshop

> 2nd Workshop on Agentic AI Benchmarks and Applications for Enterprise Tasks
> NeurIPS 2026 · Sydney, Australia · December 11 or 12, 2026 (TBD)
> Tagline: Where Agentic AI meets the real world of work

This site is the canonical public homepage for the workshop.
Google Sites at https://sites.google.com/view/aaba4et embeds this GitHub Pages site; prefer this URL for citations and sharing.

## Key facts

- Full name: 2nd Workshop on Agentic AI Benchmarks and Applications for Enterprise Tasks (AABA4ET)
- Conference: NeurIPS 2026 (follows the AAAI 2026 first edition in Singapore)
- Location: Sydney, Australia
- Workshop day: December 11 or 12, 2026 (TBD)
- Format: In-person; non-archival; dual submission welcome; double-blind review
- Paper length: 4 pages, NeurIPS style
- Submission deadline: August 31, 2026 (Anywhere on Earth / AoE)
- Acceptance notification: September 29, 2026
- Submit: {OPENREVIEW}
- OpenReview group: NeurIPS.cc/2026/Workshop/AABA4ET

## Focus areas

- Benchmarking and evaluation for enterprise agent tasks
- Enterprise applications (planning, observation, reflection, system management)
- Safety, trustworthiness, failure recovery, and distribution shift
- Human–agent interaction in real workflows
- Multimodal reasoning (vision, text, audio)
- Multi-agent planning and orchestration

## Pages

{page_lines}

## Machine-readable

- Sitemap: {SITE_URL}/sitemap.xml
- Robots: {SITE_URL}/robots.txt
- Full agent brief: {SITE_URL}/llms-full.txt
- Open Graph image: {OG_IMAGE}
- Canonical site: {SITE_URL}/

## Citation hint

When referring to this workshop, use the canonical URL {SITE_URL}/ and the short name AABA4ET (NeurIPS 2026).
"""
    (ROOT / "llms.txt").write_text(llms)

    llms_full = llms + """
## About

The workshop fosters collaboration toward robust, efficient, and trustworthy Agentic AI for complex, dynamic enterprise operations. It connects cutting-edge agent research with practical evaluation and real-world deployment.

## Important dates (AoE)

| Date | Milestone |
|------|-----------|
| Aug 31, 2026 | Submission deadline |
| Sep 29, 2026 | Acceptance notification |
| Dec 11–12, 2026 | Workshop day (TBD) |

## Related

- Past workshop (AAAI 2026): https://sites.google.com/view/aaba4et/past-workshop
- NeurIPS paper template: https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip
"""
    (ROOT / "llms-full.txt").write_text(llms_full)


# —— Home ——
home_body = """  <header class="hero">
    <div class="hero__media" aria-hidden="true"></div>
    <div class="hero__veil" aria-hidden="true"></div>
    <div class="wrap hero__inner">
      <p class="brand"><span>NeurIPS 2026 Workshop · AABA4ET</span></p>
      <h1>2nd Workshop on Agentic AI Benchmarks and Applications for Enterprise Tasks</h1>
      <p class="hero__tagline">Where Agentic AI meets the real world of work</p>
      <p class="hero__lede">
        Benchmarking, evaluating, and deploying intelligent agents for complex enterprise operations at scale.
      </p>
      <div class="hero__meta">
        <span><strong>Sydney, Australia</strong></span>
        <span>December 11 or 12, 2026</span>
        <span>After AAAI 2026</span>
      </div>
      <div class="cta-row">
        <a class="btn btn-primary" href="https://openreview.net/group?id=NeurIPS.cc/2026/Workshop/AABA4ET" target="_blank" rel="noopener">Submit a paper</a>
        <a class="btn btn-ghost" href="call-for-papers.html">Call for papers</a>
      </div>
    </div>
  </header>

  <div class="update">
    <div class="wrap">
      <span class="update__label">Update</span>
      <p>Accepted for NeurIPS 2026 — submissions open through August 31, 2026 (AoE).</p>
    </div>
  </div>

  <section class="about">
    <div class="wrap">
      <p class="eyebrow">About the workshop</p>
      <h2>Bridge research and enterprise deployment</h2>
      <p class="lede">
        Foster collaboration toward robust, efficient, and trustworthy Agentic AI for complex, dynamic enterprise operations.
      </p>
      <p>
        The 2nd Workshop on Agentic AI Benchmarks and Applications for Enterprise Tasks continues the AAAI 2026 edition in Singapore. We connect cutting-edge agent research with the practical demands of evaluation and real-world deployment.
      </p>
    </div>
  </section>

  <section class="topics">
    <div class="wrap">
      <p class="eyebrow">Focus areas</p>
      <h2>What we want to discuss</h2>
      <p class="lede">Original work across benchmarking, applications, safety, and multi-agent systems in enterprise settings.</p>

      <div class="topic-grid">
        <article class="topic">
          <img src="images/icon-benchmark.svg" alt="" width="42" height="42" />
          <div>
            <h3>Benchmarking &amp; evaluation</h3>
            <p>Datasets, metrics, and realistic enterprise task environments for performance, safety, and reliability.</p>
          </div>
        </article>
        <article class="topic">
          <img src="images/icon-enterprise.svg" alt="" width="42" height="42" />
          <div>
            <h3>Enterprise applications</h3>
            <p>On-site understanding, planning, observation, reflection, and system management in business contexts.</p>
          </div>
        </article>
        <article class="topic">
          <img src="images/icon-safety.svg" alt="" width="42" height="42" />
          <div>
            <h3>Safety &amp; trustworthiness</h3>
            <p>Failure recovery, distribution shift, guardrails, and trust for long-running production agents.</p>
          </div>
        </article>
        <article class="topic">
          <img src="images/icon-human.svg" alt="" width="42" height="42" />
          <div>
            <h3>Human–agent interaction</h3>
            <p>Assistants that augment people inside real enterprise workflows.</p>
          </div>
        </article>
        <article class="topic">
          <img src="images/icon-multimodal.svg" alt="" width="42" height="42" />
          <div>
            <h3>Multimodal reasoning</h3>
            <p>Vision, text, and audio for robust decision-making in physical enterprise data.</p>
          </div>
        </article>
        <article class="topic">
          <img src="images/icon-orchestration.svg" alt="" width="42" height="42" />
          <div>
            <h3>Planning &amp; orchestration</h3>
            <p>Multi-agent and tool strategies for complex, multi-step enterprise goals.</p>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="dates">
    <div class="wrap">
      <p class="eyebrow" style="color:#7fd4d7">Important dates</p>
      <h2>Mark your calendar</h2>
      <p class="lede">All deadlines are Anywhere on Earth (AoE).</p>
      <div class="date-row">
        <div class="date-item">
          <strong>Aug 31, 2026</strong>
          <span>Submission deadline</span>
        </div>
        <div class="date-item">
          <strong>Sep 29, 2026</strong>
          <span>Acceptance notification</span>
        </div>
        <div class="date-item">
          <strong>Dec 11–12, 2026</strong>
          <span>Workshop day (TBD)</span>
        </div>
      </div>
    </div>
  </section>

  <section class="submit">
    <div class="wrap">
      <div class="submit-box">
        <div>
          <p class="eyebrow">Call for papers</p>
          <h2>4 pages · NeurIPS style · non-archival</h2>
          <p class="lede" style="margin-bottom:0">
            Double-blind review. Dual submission welcome. At least one author must present in person.
          </p>
        </div>
        <div class="cta-row">
          <a class="btn btn-solid" href="call-for-papers.html">Read the CFP</a>
          <a class="btn btn-ghost" style="border-color:var(--teal);color:var(--teal-deep);background:transparent" href="https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip" target="_blank" rel="noopener">Paper template</a>
        </div>
      </div>
    </div>
  </section>
"""

# —— CFP ——
cfp_body = """  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Overview</p>
      <h2>Submit original work on Agentic AI for enterprise</h2>
      <p class="lede">We invite submissions on benchmarking, evaluating, and deploying Agentic AI systems for complex enterprise operations. This is the 2nd edition, following <a href="past.html">AAAI 2026 in Singapore</a>.</p>
    </div>
  </section>
  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Guidelines</p>
      <h2>How to submit</h2>
      <ul class="guidelines">
        <li><strong>Format:</strong> Official NeurIPS 2026 LaTeX style (<code>neurips_2026.sty</code>). Download the <a href="https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip" target="_blank" rel="noopener">paper template ZIP</a>.</li>
        <li><strong>Page limit:</strong> Up to 4 pages including figures and tables. References and optional appendices are unlimited.</li>
        <li><strong>Anonymity:</strong> Double-blind. Omit names, affiliations, and identifying information. Do not use <code>preprint</code> or <code>final</code> style options.</li>
        <li><strong>File:</strong> One anonymized PDF (main + references + optional appendix).</li>
        <li><strong>Dual submission:</strong> Work under review or destined for other venues is welcome.</li>
        <li><strong>Presentation:</strong> At least one author must present in person (poster or oral).</li>
        <li><strong>Archival:</strong> Non-archived; may appear on venues such as arXiv.</li>
      </ul>
      <div class="cta-row" style="margin-top:1.75rem">
        <a class="btn btn-solid" href="https://openreview.net/group?id=NeurIPS.cc/2026/Workshop/AABA4ET" target="_blank" rel="noopener">Submit on OpenReview</a>
        <a class="btn btn-ghost" style="border-color:var(--teal);color:var(--teal-deep);background:transparent" href="https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip" target="_blank" rel="noopener">Download paper template</a>
      </div>
    </div>
  </section>
  <section class="page-section dates" style="padding: clamp(2.5rem, 6vw, 4rem) 0;">
    <div class="wrap">
      <p class="eyebrow" style="color:#7fd4d7">Important dates</p>
      <h2>Deadlines</h2>
      <div class="date-row">
        <div class="date-item">
          <strong>Aug 31, 2026</strong>
          <span><span class="strike">Aug 29</span>Submission deadline (AoE)</span>
        </div>
        <div class="date-item">
          <strong>Sep 29, 2026</strong>
          <span>Acceptance notification (AoE)</span>
        </div>
        <div class="date-item">
          <strong>Dec 11 or 12, 2026</strong>
          <span>Workshop date (TBD)</span>
        </div>
      </div>
    </div>
  </section>
"""

# —— Speakers ——
speakers_body = f"""  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Invited talks</p>
      <h2>Confirmed speakers</h2>

      <article class="person-full speaker">
        <img class="person-photo" src="images/speakers/diyi-yang.jpg" alt="Diyi Yang" width="160" height="160" loading="lazy" />
        <div class="person-copy">
          {person_name("Diyi Yang", "https://nlp.stanford.edu/~diyiy/")}
          <p class="role">Assistant Professor, Computer Science Department, Stanford University</p>
          <p class="title-talk">Title: TBD</p>
          <p>Diyi Yang is an assistant professor in the Computer Science Department at Stanford University, also affiliated with the Stanford NLP Group, Stanford HCI Group and Stanford Human Centered AI Institute. Her research focuses on human-centered natural language processing and human-AI interaction. She is a recipient of IEEE “AI 10 to Watch” (2020), Microsoft Research Faculty Fellowship (2021), NSF CAREER Award (2022), an ONR Young Investigator Award (2023), and a Sloan Research Fellowship (2024). Her work has received multiple paper awards or nominations at top NLP and HCI conferences.</p>
{social_icons("https://nlp.stanford.edu/~diyiy/", "https://www.linkedin.com/in/diyi-yang-10561924", "https://scholar.google.com/citations?user=j9jhYqQAAAAJ&hl=en")}
        </div>
      </article>

      <article class="person-full speaker">
        <img class="person-photo" src="images/speakers/yu-su.jpg" alt="Yu Su" width="160" height="160" loading="lazy" />
        <div class="person-copy">
          {person_name("Yu Su", "https://ysu1989.github.io/")}
          <p class="role">Associate Professor, Computer Science and Engineering, Ohio State University</p>
          <p class="title-talk">Title: TBD</p>
          <p>Yu Su is an Associate Professor in the Department of Computer Science and Engineering at the Ohio State University and a College of Engineering Innovation Scholar. Before coming to OSU, he was Senior Researcher at Microsoft Semantic Machines working on conversational AI. He received his PhD from University of California, Santa Barbara and his bachelor’s degree from Tsinghua University, both in Computer Science. His awards include the Outstanding Dissertation Award from UCSB and Best of IEEE ICDM 2019 Selection. His expertise includes natural language processing, artificial intelligence, conversational AI, and knowledge bases.</p>
{social_icons("https://ysu1989.github.io/", "https://www.linkedin.com/in/ysu1989", "https://scholar.google.com/citations?user=rIh5OqoAAAAJ&hl=en")}
        </div>
      </article>

      <article class="person-full speaker">
        <div class="person-photo person-photo--placeholder" aria-hidden="true"></div>
        <div class="person-copy">
          {person_name("Wei-Peng Chen")}
          <p class="role">Research Director, Fujitsu Research of America, Inc.</p>
          <p class="title-talk">Title: TBD</p>
{social_icons(linkedin="https://www.linkedin.com/in/wei-peng-chen-882819a", scholar="https://scholar.google.com/citations?user=YBjteIQAAAAJ&hl=en")}
        </div>
      </article>
    </div>
  </section>
"""

# —— Panel ——
panel_body = f"""  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Discussion</p>
      <h2>Panelists</h2>

      <article class="person-full speaker">
        <div class="person-photo person-photo--placeholder" aria-hidden="true"></div>
        <div class="person-copy">
          {person_name("Kamelia Aryafar")}
          <p class="role">AI and Engineering Executive, Netflix</p>
{social_icons("https://www.karyafar.com/", "https://www.linkedin.com/in/karyafar", "https://scholar.google.com/citations?user=whu7X_kAAAAJ&hl=en")}
        </div>
      </article>

      <article class="person-full speaker">
        <img class="person-photo" src="images/panelists/mehdi-bahrami.jpg" alt="Mehdi Bahrami" width="160" height="160" loading="lazy" />
        <div class="person-copy">
          {person_name("Mehdi Bahrami")}
          <p class="role">Senior Research Manager, Fujitsu Research of America</p>
          <p>Dr. Mehdi Bahrami is a Senior Research Manager at Fujitsu Research of America, where he leads research on Agentic AI, LLM-based agents, and AI for software engineering. His recent work includes Kozuchi Agent, an open-weight agent framework for autonomous software engineering and repair. His broader research interests include generative AI, LLMs, and applied machine learning.</p>
          <p>Dr. Bahrami has over 15 years of experience in software engineering and industrial AI research, with 30+ technical publications and 34+ granted U.S. patents. He is an ACM Distinguished Speaker and Senior Member of ACM and IEEE, and a recipient of the 2024 IEEE Outstanding Engineer Award for pioneering contributions to generative AI and API automation. His work has also been recognized with multiple industry awards and featured by leading technology media, including MIT Technology Review.</p>
{social_icons("https://cloudlab.ucmerced.edu/~mehdi-bahrami", "https://www.linkedin.com/in/mehdi-bahrami-cs", "https://scholar.google.com/citations?user=xAGN8vcAAAAJ&hl=en")}
        </div>
      </article>
    </div>
  </section>
"""

# —— Schedule ——
schedule_body = """  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Program</p>
      <h2>Workshop schedule</h2>
      <p class="lede">The detailed timetable will be posted once the NeurIPS 2026 workshop day is confirmed.</p>
      <div class="tbd-panel">
        <strong>TBD</strong>
        <p class="muted">Expected workshop date: December 11 or 12, 2026 · Sydney, Australia</p>
      </div>
    </div>
  </section>
"""

# —— Organizers ——
organizers_body = f"""  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Team</p>
      <h2>Organizers</h2>
      <article class="person-full">
        <img class="person-photo" src="images/organizers/neubig.jpg" alt="Graham Neubig" width="160" height="160" loading="lazy" />
        <div class="person-copy">
          {person_name("Graham Neubig", "https://www.phontron.com/")}
          <p class="role">Associate Professor, Language Technologies Institute, Carnegie Mellon University</p>
          <p>A prominent figure in machine learning and NLP, with extensive work on large language models, question answering, code generation, and evaluation. Academic leadership includes organizing workshops such as the ACL 2017 workshop on neural machine translation.</p>
          <p class="expertise"><strong>Expertise:</strong> LLMs, QA, code generation, multilingual processing, evaluation/interpretability; workshop organization.</p>
{social_icons("https://www.phontron.com/", "https://www.linkedin.com/in/graham-neubig-10b41616b", "https://scholar.google.com/citations?user=wlosgkoAAAAJ&hl=en")}
        </div>
      </article>
      <article class="person-full">
        <img class="person-photo" src="images/organizers/bisk.jpg" alt="Yonatan Bisk" width="160" height="160" loading="lazy" />
        <div class="person-copy">
          {person_name("Yonatan Bisk", "https://yonatanbisk.com/")}
          <p class="role">Assistant Professor, Language Technologies Institute, Carnegie Mellon University</p>
          <p>Research focuses on Natural Language Processing with an emphasis on grounding and embodiment. Extensive program committee experience for major conferences (NeurIPS 2023, ICLR 2024).</p>
          <p class="expertise"><strong>Expertise:</strong> NLP, grounding, embodiment; conference reviewing.</p>
{social_icons("https://yonatanbisk.com/", "https://www.linkedin.com/in/yonatanbisk", "https://scholar.google.com/citations?user=bWoGh8UAAAAJ&hl=en")}
        </div>
      </article>
      <article class="person-full">
        <img class="person-photo" src="images/organizers/saito.jpg" alt="Hideo Saito" width="160" height="160" loading="lazy" />
        <div class="person-copy">
          {person_name("Hideo Saito", "http://www.hvrl.ics.keio.ac.jp/professor-saito/")}
          <p class="role">Professor, Department of Information and Computer Science, Keio University</p>
          <p>Specializes in computer vision, pattern recognition, computational photography, and XR applications. Program Chair for ACCV 2014, General Chair for ISMAR 2015, ISMAR 2023 Best Journal Paper Award; organized workshops at ISMAR, WACV, and ACM Multimedia.</p>
          <p class="expertise"><strong>Expertise:</strong> Computer vision, vision-based sensing/recognition, human behavior sensing and applications.</p>
{social_icons("http://www.hvrl.ics.keio.ac.jp/professor-saito/", scholar="https://scholar.google.com/citations?user=JU9x-bcAAAAJ&hl=en")}
        </div>
      </article>
      <article class="person-full">
        <img class="person-photo" src="images/organizers/moteki.jpg" alt="Atsunori Moteki" width="160" height="160" loading="lazy" />
        <div class="person-copy">
          {person_name("Atsunori Moteki")}
          <p class="role">Senior Research Manager, Artificial Intelligence Laboratory, Fujitsu Limited</p>
          <p>Research interests include Agentic AI, computer vision, and HCI (including XR) in manufacturing and retail. His team recently proposed a benchmark for AI agents that support on-site field work.</p>
          <p class="expertise"><strong>Expertise:</strong> Agentic AI, computer vision, human–computer interaction.</p>
{social_icons(linkedin="https://www.linkedin.com/in/atsunori-moteki-a2a095119")}
        </div>
      </article>
      <article class="person-full">
        <img class="person-photo" src="images/organizers/drouin.png" alt="Alexandre Drouin" width="160" height="160" loading="lazy" />
        <div class="person-copy">
          {person_name("Alexandre Drouin", "https://www.alexdrouin.com/")}
          <p class="role">Head of Frontier AI Research, ServiceNow · Adjunct Professor, Laval University &amp; Mila</p>
          <p>Leads Frontier AI Research at ServiceNow Research. Work focuses on ML for decision-making in complex environments—causal inference, probabilistic forecasting, and LLM-based agents—plus benchmarks for browser automation, data analytics, forecasting, security, and robustness. Program Committee for NeurIPS 2026 Evaluations and Datasets track.</p>
          <p class="expertise"><strong>Expertise:</strong> Agentic systems, benchmarking, decision-making under uncertainty.</p>
{social_icons("https://www.alexdrouin.com/", "https://linkedin.com/in/drouinalexandre", "https://scholar.google.com/citations?user=LR6aJcEAAAAJ&hl=en")}
        </div>
      </article>
    </div>
  </section>
  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Committees</p>
      <h2>Steering Committee</h2>
      <div class="steering-grid">
{STEERING_GRID}
      </div>
    </div>
  </section>
  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Review</p>
      <h2>Technical Program Committee</h2>
      <div class="tbd-panel">
        <strong>TBD</strong>
      </div>
    </div>
  </section>
"""

# —— Accepted ——
accepted_body = """  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">NeurIPS 2026</p>
      <h2>Accepted papers</h2>
      <p class="lede">The list will be published after the notification date (September 29, 2026).</p>
      <div class="tbd-panel">
        <strong>TBD</strong>
        <p class="muted">Check back after acceptances are announced.</p>
      </div>
    </div>
  </section>
"""

# —— Past ——
PAST_BASE = "https://sites.google.com/view/aaba4et/past-workshop"
past_body = f"""  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">AAAI 2026 · Singapore</p>
      <h2>1st edition archive</h2>
      <p class="lede">W8: Agentic AI Benchmarks and Applications for Enterprise Tasks · January 26, 2026 · Singapore</p>
      <div class="link-list">
        <div class="link-card">
          <strong>Overview</strong>
          <a href="{PAST_BASE}/aaai-2026-1st-overview" target="_blank" rel="noopener">AAAI 2026 (1st) — Overview</a>
        </div>
        <div class="link-card">
          <strong>Call for Papers</strong>
          <a href="{PAST_BASE}/aaai-2026-1st-call-for-papers" target="_blank" rel="noopener">AAAI 2026 (1st) — Call for Papers</a>
        </div>
        <div class="link-card">
          <strong>Speakers</strong>
          <a href="{PAST_BASE}/aaai-2026-1st-speakers" target="_blank" rel="noopener">AAAI 2026 (1st) — Speakers</a>
        </div>
        <div class="link-card">
          <strong>Schedule</strong>
          <a href="{PAST_BASE}/aaai-2026-1st-schedule" target="_blank" rel="noopener">AAAI 2026 (1st) — Schedule</a>
        </div>
        <div class="link-card">
          <strong>Organizers</strong>
          <a href="{PAST_BASE}/aaai-2026-1st-organizers" target="_blank" rel="noopener">AAAI 2026 (1st) — Organizers</a>
        </div>
        <div class="link-card">
          <strong>Accepted Papers</strong>
          <a href="{PAST_BASE}/aaai-2026-1st-accepted-papers" target="_blank" rel="noopener">AAAI 2026 (1st) — Accepted Papers</a>
        </div>
      </div>
    </div>
  </section>
"""

# Write files
(ROOT / "index.html").write_text(page(
    "AABA4ET — NeurIPS 2026 Workshop", "home", home_body, body_class="home",
    description=DEFAULT_DESCRIPTION,
))

(ROOT / "call-for-papers.html").write_text(page(
    "Call for Papers — AABA4ET NeurIPS 2026", "cfp", cfp_body,
    hero_title="Call for Papers",
    hero_lede="4 pages · NeurIPS 2026 style · double-blind · non-archival",
    path="call-for-papers.html",
    description="Submit to AABA4ET at NeurIPS 2026: 4 pages, double-blind, non-archival. Deadline August 31, 2026 (AoE).",
))

(ROOT / "speakers.html").write_text(page(
    "Speakers — AABA4ET NeurIPS 2026", "speakers", speakers_body,
    hero_title="Speakers",
    hero_lede="Invited talks at NeurIPS 2026 in Sydney",
    path="speakers.html",
    description="Invited speakers for the AABA4ET NeurIPS 2026 workshop in Sydney.",
))

(ROOT / "panel.html").write_text(page(
    "Panel — AABA4ET NeurIPS 2026", "panel", panel_body,
    hero_title="Panel",
    hero_lede="Industry and research perspectives on agentic AI for enterprise",
    path="panel.html",
    description="Industry and research panel on agentic AI for enterprise at AABA4ET NeurIPS 2026.",
))

(ROOT / "schedule.html").write_text(page(
    "Schedule — AABA4ET NeurIPS 2026", "schedule", schedule_body,
    hero_title="Schedule",
    hero_lede="December 11 or 12, 2026 · Sydney, Australia",
    path="schedule.html",
    description="Workshop schedule for AABA4ET at NeurIPS 2026 — December 11 or 12, Sydney.",
))

(ROOT / "organizers.html").write_text(page(
    "Organizers — AABA4ET NeurIPS 2026", "organizers", organizers_body,
    hero_title="Organizers",
    hero_lede="CMU · Fujitsu · Keio · ServiceNow",
    path="organizers.html",
    description="Organizers and steering committee for AABA4ET NeurIPS 2026.",
))

(ROOT / "accepted-papers.html").write_text(page(
    "Accepted Papers — AABA4ET NeurIPS 2026", "accepted", accepted_body,
    hero_title="Accepted Papers",
    hero_lede="Coming after September 29, 2026 notifications",
    path="accepted-papers.html",
    description="Accepted papers for AABA4ET NeurIPS 2026 (list after September 29 notifications).",
))

(ROOT / "past.html").write_text(page(
    "Past Workshop — AABA4ET", "past", past_body,
    body_class="past",
    hero_title="Past Workshop",
    hero_lede="AAAI 2026 · 1st edition · Singapore",
    path="past.html",
    description="Archive of the 1st AABA4ET workshop at AAAI 2026 in Singapore.",
))

write_discovery_files()
print("Generated pages OK")
