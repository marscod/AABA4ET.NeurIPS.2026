#!/usr/bin/env python3
"""Generate multi-page AABA4ET site with shared chrome."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAST = ROOT / "past"
PAST.mkdir(exist_ok=True)

FONTS = """  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet" />"""


def nav(active: str, prefix: str = "") -> str:
    def a(href, label, key):
        cur = ' aria-current="page"' if active == key else ""
        return f'<a href="{prefix}{href}"{cur}>{label}</a>'

    past_cur = ' aria-current="page"' if active.startswith("past") else ""
    past_open = " open" if active.startswith("past") else ""
    return f"""  <header class="site-header">
    <div class="wrap site-header__inner">
      <a class="site-logo" href="{prefix}index.html">AABA4ET<span>NeurIPS 2026</span></a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
      <nav class="site-nav" id="site-nav">
        {a("index.html", "Home", "home")}
        {a("call-for-papers.html", "Call for Papers", "cfp")}
        {a("speakers.html", "Speakers", "speakers")}
        {a("schedule.html", "Schedule", "schedule")}
        {a("organizers.html", "Organizers", "organizers")}
        {a("accepted-papers.html", "Accepted Papers", "accepted")}
        <div class="nav-dropdown{past_open}">
          <button type="button"{past_cur}>Past Workshop</button>
          <div class="nav-dropdown__menu">
            <a href="{prefix}past-workshop.html"{' aria-current="page"' if active == "past" else ""}>Overview</a>
            <a href="{prefix}past/aaai-2026-overview.html"{' aria-current="page"' if active == "past-overview" else ""}>AAAI 2026 · Overview</a>
            <a href="{prefix}past/aaai-2026-cfp.html"{' aria-current="page"' if active == "past-cfp" else ""}>AAAI 2026 · Call for Papers</a>
            <a href="{prefix}past/aaai-2026-speakers.html"{' aria-current="page"' if active == "past-speakers" else ""}>AAAI 2026 · Speakers</a>
            <a href="{prefix}past/aaai-2026-schedule.html"{' aria-current="page"' if active == "past-schedule" else ""}>AAAI 2026 · Schedule</a>
            <a href="{prefix}past/aaai-2026-organizers.html"{' aria-current="page"' if active == "past-organizers" else ""}>AAAI 2026 · Organizers</a>
            <a href="{prefix}past/aaai-2026-accepted.html"{' aria-current="page"' if active == "past-accepted" else ""}>AAAI 2026 · Accepted Papers</a>
          </div>
        </div>
      </nav>
    </div>
  </header>"""


def footer(prefix: str = "") -> str:
    return f"""  <footer class="site-footer">
    <div class="wrap">
      <div class="site-footer__nav">
        <a href="{prefix}index.html">Home</a>
        <a href="{prefix}call-for-papers.html">CFP</a>
        <a href="{prefix}speakers.html">Speakers</a>
        <a href="{prefix}schedule.html">Schedule</a>
        <a href="{prefix}organizers.html">Organizers</a>
        <a href="{prefix}accepted-papers.html">Accepted Papers</a>
        <a href="{prefix}past-workshop.html">Past Workshop</a>
      </div>
      <p>2nd Workshop on Agentic AI Benchmarks and Applications for Enterprise Tasks · NeurIPS 2026 · Sydney</p>
    </div>
  </footer>
  <script src="{prefix}script.js"></script>"""


def page(title, active, body, *, prefix="", body_class="", hero_title="", hero_lede="", archive=False):
    css = f'{prefix}style.css'
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
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
{FONTS}
  <link rel="stylesheet" href="{css}" />
</head>
<body class="{body_class}">
{nav(active, prefix)}
{archive_html}
{hero}
{body}
{footer(prefix)}
</body>
</html>
"""


# —— Home ——
home_body = """  <header class="hero">
    <div class="hero__media" aria-hidden="true"></div>
    <div class="hero__veil" aria-hidden="true"></div>
    <div class="wrap hero__inner">
      <p class="brand"><span>NeurIPS 2026 Workshop</span>AABA4ET</p>
      <h1>Where Agentic AI meets the real world of work</h1>
      <p class="hero__lede">
        Benchmarking, evaluating, and deploying intelligent agents for complex enterprise operations at scale.
      </p>
      <div class="hero__meta">
        <span><strong>Sydney, Australia</strong></span>
        <span>December 11 or 12, 2026</span>
        <span>2nd edition · after AAAI 2026</span>
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
        <a class="btn btn-solid" href="call-for-papers.html">Read the CFP</a>
      </div>
    </div>
  </section>
"""

# —— CFP ——
cfp_body = """  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Overview</p>
      <h2>Submit original work on Agentic AI for enterprise</h2>
      <p class="lede">We invite submissions on benchmarking, evaluating, and deploying Agentic AI systems for complex enterprise operations. This is the 2nd edition, following AAAI 2026 in Singapore.</p>
    </div>
  </section>
  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Guidelines</p>
      <h2>How to submit</h2>
      <ul class="guidelines">
        <li><strong>Format:</strong> Official NeurIPS 2026 LaTeX style (<code>neurips_2026.sty</code>).</li>
        <li><strong>Page limit:</strong> Up to 4 pages including figures and tables. References and optional appendices are unlimited.</li>
        <li><strong>Anonymity:</strong> Double-blind. Omit names, affiliations, and identifying information. Do not use <code>preprint</code> or <code>final</code> style options.</li>
        <li><strong>File:</strong> One anonymized PDF (main + references + optional appendix).</li>
        <li><strong>Dual submission:</strong> Work under review or destined for other venues is welcome.</li>
        <li><strong>Presentation:</strong> At least one author must present in person (poster or oral).</li>
        <li><strong>Archival:</strong> Non-archived; may appear on venues such as arXiv.</li>
      </ul>
      <div class="cta-row" style="margin-top:1.75rem">
        <a class="btn btn-solid" href="https://openreview.net/group?id=NeurIPS.cc/2026/Workshop/AABA4ET" target="_blank" rel="noopener">Submit on OpenReview</a>
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
speakers_body = """  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Invited talks</p>
      <h2>Confirmed speakers</h2>
      <p class="lede">Talk titles will be announced soon.</p>
      <div class="person-grid">
        <article class="person">
          <h3>Diyi Yang</h3>
          <p class="role">Associate Professor, Stanford University</p>
          <p class="title-talk">Title: TBD</p>
        </article>
        <article class="person">
          <h3>Yu Su</h3>
          <p class="role">Associate Professor, Ohio State University</p>
          <p class="title-talk">Title: TBD</p>
        </article>
        <article class="person">
          <h3>Wei-Peng Chen</h3>
          <p class="role">Research Director, Fujitsu Research of America, Inc.</p>
          <p class="title-talk">Title: TBD</p>
        </article>
      </div>
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
organizers_body = """  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Team</p>
      <h2>Organizers</h2>
      <div class="person-full">
        <h3>Graham Neubig</h3>
        <p class="role">Associate Professor, Language Technologies Institute, Carnegie Mellon University</p>
        <p>A prominent figure in machine learning and NLP, with extensive work on large language models, question answering, code generation, and evaluation. Academic leadership includes organizing workshops such as the ACL 2017 workshop on neural machine translation.</p>
        <p class="expertise"><strong>Expertise:</strong> LLMs, QA, code generation, multilingual processing, evaluation/interpretability; workshop organization.</p>
      </div>
      <div class="person-full">
        <h3>Yonatan Bisk</h3>
        <p class="role">Assistant Professor, Language Technologies Institute, Carnegie Mellon University</p>
        <p>Research focuses on Natural Language Processing with an emphasis on grounding and embodiment. Extensive program committee experience for major conferences (NeurIPS 2023, ICLR 2024).</p>
        <p class="expertise"><strong>Expertise:</strong> NLP, grounding, embodiment; conference reviewing.</p>
      </div>
      <div class="person-full">
        <h3>Hideo Saito</h3>
        <p class="role">Professor, Department of Information and Computer Science, Keio University</p>
        <p>Specializes in computer vision, pattern recognition, computational photography, and XR applications. Program Chair for ACCV 2014, General Chair for ISMAR 2015, ISMAR 2023 Best Journal Paper Award; organized workshops at ISMAR, WACV, and ACM Multimedia.</p>
        <p class="expertise"><strong>Expertise:</strong> Computer vision, vision-based sensing/recognition, human behavior sensing and applications.</p>
      </div>
      <div class="person-full">
        <h3>Alexandre Drouin</h3>
        <p class="role">Head of Frontier AI Research, ServiceNow · Adjunct Professor, Laval University &amp; Mila</p>
        <p>Leads Frontier AI Research at ServiceNow Research. Work focuses on ML for decision-making in complex environments—causal inference, probabilistic forecasting, and LLM-based agents—plus benchmarks for browser automation, data analytics, forecasting, security, and robustness. Program Committee for NeurIPS 2026 Evaluations and Datasets track.</p>
        <p class="expertise"><strong>Expertise:</strong> Agentic systems, benchmarking, decision-making under uncertainty.</p>
      </div>
      <div class="person-full">
        <h3>Atsunori Moteki</h3>
        <p class="role">Senior Research Manager, Artificial Intelligence Laboratory, Fujitsu Limited</p>
        <p>Research interests include Agentic AI, computer vision, and HCI (including XR) in manufacturing and retail. His team recently proposed a benchmark for AI agents that support on-site field work.</p>
        <p class="expertise"><strong>Expertise:</strong> Agentic AI, computer vision, human–computer interaction.</p>
      </div>
    </div>
  </section>
  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Committees</p>
      <h2>Steering &amp; program</h2>
      <p class="muted" style="margin-bottom:1rem">Steering Committee: Organizing Committee + additional members (to be listed).</p>
      <p class="muted">Program Committee: Organizing Committee + Steering Committee + reviewers (to be listed).</p>
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

# —— Past hub ——
past_hub = """  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Archive</p>
      <h2>1st edition · AAAI 2026</h2>
      <p class="lede">Held January 26, 2026 at Singapore EXPO (W8). Explore the archived pages below.</p>
      <div class="link-list">
        <div class="link-card"><strong>Overview</strong><a href="past/aaai-2026-overview.html">Workshop goals and themes →</a></div>
        <div class="link-card"><strong>Call for Papers</strong><a href="past/aaai-2026-cfp.html">Submission rules and dates →</a></div>
        <div class="link-card"><strong>Speakers</strong><a href="past/aaai-2026-speakers.html">Invited talks →</a></div>
        <div class="link-card"><strong>Schedule</strong><a href="past/aaai-2026-schedule.html">Program notes →</a></div>
        <div class="link-card"><strong>Organizers</strong><a href="past/aaai-2026-organizers.html">Organizing, steering, and PC →</a></div>
        <div class="link-card"><strong>Accepted Papers</strong><a href="past/aaai-2026-accepted.html">25 accepted papers →</a></div>
      </div>
    </div>
  </section>
"""

past_overview = """  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">W8 · January 26, 2026 · Singapore EXPO</p>
      <h2>Agentic AI Benchmarks and Applications for Enterprise Tasks</h2>
      <p class="lede">Foster discussions and collaborations to build robust, efficient, and trustworthy Agentic AI for complex enterprise operations—bridging research and practical deployment.</p>
      <div class="update" style="margin:1.5rem 0;border-radius:6px;">
        <div class="wrap" style="width:auto;padding:0 1rem;">
          <span class="update__label">Updates</span>
          <p>Invited talk slides available on Speakers (Mar 5, 2026). Poster allocation on Accepted Papers (Jan 16). Final schedule uploaded (Jan 5).</p>
        </div>
      </div>
      <ul class="guidelines">
        <li><strong>Benchmarking and Evaluation</strong> — datasets, metrics, realistic enterprise environments.</li>
        <li><strong>Enterprise Applications</strong> — on-site operations, planning, observation, reflection, system management.</li>
        <li><strong>Human–Agent Interaction</strong> — assistants that augment business operations.</li>
        <li><strong>Multimodal Reasoning</strong> — visual, textual, and auditory enterprise data.</li>
        <li><strong>Planning &amp; Orchestration</strong> — multi-agent and tool strategies for multi-step goals.</li>
      </ul>
    </div>
  </section>
"""

past_cfp = """  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Archived CFP</p>
      <h2>Submission details</h2>
      <p class="lede">Original, unpublished work. Single-blind peer review. AAAI-26 formatting guidelines. Non-archived (e.g. arXiv OK). Contact: aaai26ws.aaba4et@gmail.com</p>
      <ul class="guidelines">
        <li><strong>Full research papers:</strong> up to 8 pages (excluding references/supplement).</li>
        <li><strong>Short/poster papers:</strong> up to 4 pages (excluding references/supplement).</li>
        <li>In-person presentation required for accepted papers.</li>
        <li>Elaborations of AAAI-26 track submissions were allowed.</li>
      </ul>
      <div class="deadline-list">
        <div class="deadline-item"><strong>Oct 29, 2025 (AoE)</strong><span class="muted"><span class="strike">Oct 22</span>Submission deadline</span></div>
        <div class="deadline-item"><strong>Nov 13, 2025</strong><span class="muted"><span class="strike">Nov 5</span>Notification</span></div>
        <div class="deadline-item"><strong>Jan 26, 2026</strong><span class="muted">Workshop</span></div>
      </div>
      <p style="margin-top:1.25rem"><a href="https://openreview.net/group?id=AAAI.org/2026/Workshop/AABA4ET" target="_blank" rel="noopener">OpenReview (AAAI 2026)</a></p>
    </div>
  </section>
"""

past_speakers = """  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Invited talks</p>
      <h2>AAAI 2026 speakers</h2>
      <div class="person-full">
        <h3>Hirotaka Osawa</h3>
        <p class="role">Associate Professor, Keio University</p>
        <p><strong>How to Design Benchmarks for Augmented Society: Based on 20 Years of Trends in Human-Agent Interaction Research</strong></p>
        <p>Traces two decades of HAI research and explores benchmarks that evaluate not only algorithms and devices, but also how agents and interpersonal relationships shape human society.</p>
      </div>
      <div class="person-full">
        <h3>Alexandre Drouin</h3>
        <p class="role">Head of Frontier AI Research, ServiceNow</p>
        <p><strong>Agentic Full-Stack Benchmarking for Knowledge Work</strong></p>
        <p>Empirical look at benchmarking long-running knowledge-work agents across browser use, multimodal understanding, analytics, deep research, and safety/security.</p>
      </div>
      <div class="person-full">
        <h3>Asim Munawar</h3>
        <p class="role">Project Lead, IBM Watson Research Center</p>
        <p><strong>Small Language Models for Enterprise Agentic Workflows</strong></p>
        <p>Equipping small models with function calling, reasoning, and planning for trustworthy enterprise automation—drawing on IT Bench, BFCL v4, and related benchmarks.</p>
      </div>
    </div>
  </section>
"""

past_schedule = """  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Program notes</p>
      <h2>AAAI 2026 schedule</h2>
      <p class="lede">All accepted papers were presented as on-site posters. A co-author (or substitute) had to register and attend; otherwise the paper was withdrawn.</p>
      <ul class="guidelines">
        <li>Poster venue shared across workshops; sessions featured up to ~10 posters each.</li>
        <li>Poster size: A0 portrait; format free. See <a href="https://aaai.org/conference/aaai/aaai-26/poster-guidelines/" target="_blank" rel="noopener">AAAI poster guidelines</a>.</li>
        <li>Authors also uploaded poster PDFs (and optional materials) to Underline for workshop registrants.</li>
        <li>Detailed timing and poster installation windows were published in the Jan 23 schedule update on the original site.</li>
      </ul>
      <p class="muted" style="margin-top:1.25rem">For the full timed agenda, see the archived Google Sites schedule page.</p>
    </div>
  </section>
"""

past_organizers = """  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">AAAI 2026</p>
      <h2>Organizers</h2>
      <div class="person-grid">
        <article class="person"><h3>Graham Neubig</h3><p class="role">Associate Professor, CMU</p></article>
        <article class="person"><h3>Yonatan Bisk</h3><p class="role">Assistant Professor, CMU</p></article>
        <article class="person"><h3>Hideo Saito</h3><p class="role">Professor, Keio University</p></article>
        <article class="person"><h3>Atsunori Moteki</h3><p class="role">Principal Researcher, Fujitsu</p></article>
      </div>
    </div>
  </section>
  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Steering Committee</p>
      <h2>Additional members</h2>
      <ul class="pc-list">
        <li>Pascal Singer — GK Software SE</li>
        <li>Jacqueline Tews — GK Software SE</li>
        <li>Alexandre Drouin — ServiceNow Research</li>
        <li>Kanji Uchino — Fujitsu Research of America</li>
        <li>Akiyoshi Uchida — Fujitsu Ltd.</li>
        <li>Hiromichi Kobashi — Fujitsu Ltd.</li>
        <li>Jun Takahashi — Fujitsu Ltd.</li>
        <li>Natsuki Miyahara — Fujitsu Ltd.</li>
        <li>Ryutaro Okada — Fujitsu Ltd.</li>
        <li>Moyuru Yamada — Fujitsu Ltd.</li>
      </ul>
    </div>
  </section>
  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Program Committee</p>
      <h2>Reviewers</h2>
      <ul class="pc-list">
        <li>Priyam Basu, Grammarly</li>
        <li>Shoichi Masui, Agent Research Collective</li>
        <li>Taiki Sekii, CyberAgent, Inc.</li>
        <li>Ryo Hachiuma, NVIDIA</li>
        <li>Tianyi Yao, Microsoft</li>
        <li>Rafael Pardinas, ServiceNow</li>
        <li>Ehsan Kamalloo, ServiceNow</li>
        <li>Khyati Mahajan, ServiceNow</li>
        <li>Nicolas Gontier, ServiceNow</li>
        <li>Sebastien Paquet, ServiceNow</li>
        <li>Massimo Caccia, ServiceNow</li>
        <li>Léo Boisvert, ServiceNow</li>
        <li>Hadi Nekoei Qachkanloo, Mila</li>
        <li>Megh Vipul Thakkar, Université de Montréal</li>
        <li>Dheeraj Vattikonda, McGill University</li>
        <li>Kiran Purohit, Fujitsu Research of India</li>
        <li>Wei-Peng Chen, Fujitsu Research of America</li>
        <li>Shailaja Keyur Sampat, Fujitsu Research of America</li>
        <li>So Hasegawa, Fujitsu Research of America</li>
        <li>Mehdi Bahrami, Fujitsu Research of America</li>
        <li>Fan Yang, Fujitsu Research of America</li>
        <li>Lei Liu, Fujitsu Research of America</li>
        <li>Fangjun Wang, Fujitsu R&amp;D Center</li>
      </ul>
    </div>
  </section>
"""

PAPERS = [
    ("AAAI26_W8_1", "ViG-LLM: Enhancing Visual Grounding Capabilities in Closed-Box LLMs for Document Information Extraction without OCR Dependencies", "Sudhanshu Bhoi"),
    ("AAAI26_W8_2", "CausalFusion: Integrating LLMs and Graph Falsification for Causal Discovery", "Alessandro Casadei, Sreyoshi Bhaduri, Pavan Nithin Mullapudi, Rohit Malshe"),
    ("AAAI26_W8_3", "Small Language Models for Efficient Agentic Tool Calling: Outperforming Large Models with Targeted Fine-tuning", "Owais Kazi, Shreyas Subramanian, Polaris Singh Jhandi, Neel Sendas"),
    ("AAAI26_W8_4", "CAD Inspection Assistant: Tool-Augmented Agentic CAD Inspection Solution", "Fangjun Wang, Xidan Zhang, Jianing Wei, Nan Zhang, Yunqing Liu, Zhiming Tan"),
    ("AAAI26_W8_5", "ECHO: EvidenCe-prior Hallucination Observation", "Ziqiang Shi, Liu Liu, Zihao Guo, Fei Li, Rujie Liu, Shanshan Yu, Satoshi Munakata, Koichi Shirahata"),
    ("AAAI26_W8_6", "BAID: A Benchmark for Bias Assessment of AI Detectors", "Priyam Basu, Yunfeng Zhang, Vipul Raheja"),
    ("AAAI26_W8_7", "MeetBench-XL: Calibrated Multi-Dimensional Evaluation and Learned Dual-Policy Agents for Real-Time Meetings", "Yuelin Hu, Jun Xu, Bingcong Lu, Zhengxue Cheng, Hongwei Hu, Ronghua Wu, Li Song"),
    ("AAAI26_W8_8", "Overcoming the ‘Impracticality’ of RAG: Proposing a Real-World Benchmark and Multi-Dimensional Diagnostic Framework", "Kenichirou Narita, Siqi Peng, Taku Fukui, Moyuru Yamada, Satoshi Munakata, Satoru Takahashi"),
    ("AAAI26_W8_9", "Reason-Plan-ReAct: A Reasoner-Planner Supervising a ReAct Executor for Complex Enterprise Tasks", "Gianni Molinari, Fabio Ciravegna"),
    ("AAAI26_W8_10", "Agentic Observability: Automated Alert Triage for Adobe E-Commerce", "Aprameya Bharadwaj, Kyle Tu"),
    ("AAAI26_W8_11", "Beyond Curated Benchmarking: Automated Evaluation of LLM Agents for Safe and Reliable IT Infrastructure Management", "Gayathri Saranathan, Aalap Tripathy, Tarun Kumar, Scott Hinchley, Martin Foltin, Christopher L Holmes, David Brookshire, Donald M Bahls, Cong Xu, Robert W. Wisniewski, Larry Kaplan, Suparna Bhattacharya"),
    ("AAAI26_W8_12", "Multi-Agent AI Trainer: Adaptive Skill Evaluation via Persona-Driven Examiners and Multi-Criteria Judging", "Daniil Sukhorukov, Kirill Dzhunkovsky, Aleksandr Tsymbalov, Roman Kharkovskoy, Mikhail Mozikov, Ivan Nasonov, Nikita Glazkov, Vlad Kuznetsov, Maxim Dubovitsky, Ilya Makarov"),
    ("AAAI26_W8_13", "Agentic Code Generation for Heuristic Rules in Equipment Monitoring", "Fabio Lorenzi, Abigail Langbridge, Fearghal O'Donncha, James T Rayfield, Bradley Eck, Sal Rosato"),
    ("AAAI26_W8_14", "POLARIS: Typed Planning and Governed Execution for Agentic AI in Back-Office Automation", "Zahra Moslemi, Keerthi Koneru, Sheethal Kumar, Yen-Ting Lee, Ramesh Radhakrishnan"),
    ("AAAI26_W8_15", "Multi-Agent Coordination for Dynamic Supply Chain Resilience: A Benchmark and Evaluation", "Bayron Jossue Serrano Mena"),
    ("AAAI26_W8_16", "Beyond Accuracy: A Multi-Dimensional Framework for Evaluating Enterprise Agentic AI Systems", "Sushant Mehta"),
    ("AAAI26_W8_17", "Polaris: Multi Agentic System for Conversational Enterprise Analytics", "Varuni H K, Soham Sarkar, Jay Kumar, Goutham Krishnan, Tanvi Johari, Santosh Hegde, Avinash Bharadwaj"),
    ("AAAI26_W8_18", "Verification-Guided Context Optimization for Tool Calling via Hierarchical LLMs-as-editors", "Henger Li, Shuangjie You, Flavio Di Palo, Yiyue Qian, Ayush Jain"),
    ("AAAI26_W8_19", "The Forecast Critic: Leveraging Large Language Models for Poor Forecast Identification", "Luke Bhan, Hanyu Zhang, Andrew Gordon Wilson, Michael W. Mahoney, Chuck Arvin"),
    ("AAAI26_W8_20", "MFCL Vision: Benchmarking Tool Use in Multimodal Large Language Models for Visual Reasoning Tasks", "Huanzhi Mao, Jad Bendarkawi, Evan Maxwell Turner, Ritesh Sunil Chavan"),
    ("AAAI26_W8_21", "VLM-guided Object-level Segmentation from Dynamic Scene", "Feiran Yang"),
    ("AAAI26_W8_22", "Auditing Generative AI Benchmarks with a Multi-Agent Compliance System", "Ananya Joshi, Michael Rudow"),
    ("AAAI26_W8_23", "Enterprise Deep Research: Steerable Multi-Agent Deep Research for Enterprise Analytics", "Akshara Prabhakar, Roshan Ram, Zixiang Chen, Silvio Savarese, Frank Wang, Caiming Xiong, Huan Wang, Weiran Yao"),
    ("AAAI26_W8_24", "Visualizing and Benchmarking LLM Factual Hallucination Tendencies via Internal State Analysis and Clustering", "Nathan Mao, Varun Kaushik, Shreya Shivkumar, Parham Sharafoleslami, Kevin Zhu, Sunishchal Dev"),
    ("AAAI26_W8_25", "Realistic Synthetic Household Data Generation at Scale", "Siddharth Singh, Ifrah Idrees, Abraham Dauhajre"),
]

papers_html = "\n".join(
    f"""        <article>
          <p class="pid">{pid}</p>
          <h3>{title}</h3>
          <p class="muted">{authors}</p>
        </article>"""
    for pid, title, authors in PAPERS
)

past_accepted = f"""  <section class="page-section">
    <div class="wrap">
      <p class="eyebrow">Poster allocation</p>
      <h2>Accepted papers</h2>
      <p class="lede">Camera-ready upload to Underline was optional for archival reasons. Authors could share via arXiv; organizers can add links on request.</p>
      <div class="paper-list">
{papers_html}
      </div>
    </div>
  </section>
"""

# Write files
(ROOT / "index.html").write_text(page(
    "AABA4ET — NeurIPS 2026 Workshop", "home", home_body, body_class="home"
))

(ROOT / "call-for-papers.html").write_text(page(
    "Call for Papers — AABA4ET NeurIPS 2026", "cfp", cfp_body,
    hero_title="Call for Papers",
    hero_lede="4 pages · NeurIPS 2026 style · double-blind · non-archival",
))

(ROOT / "speakers.html").write_text(page(
    "Speakers — AABA4ET NeurIPS 2026", "speakers", speakers_body,
    hero_title="Speakers",
    hero_lede="Invited talks at NeurIPS 2026 in Sydney",
))

(ROOT / "schedule.html").write_text(page(
    "Schedule — AABA4ET NeurIPS 2026", "schedule", schedule_body,
    hero_title="Schedule",
    hero_lede="December 11 or 12, 2026 · Sydney, Australia",
))

(ROOT / "organizers.html").write_text(page(
    "Organizers — AABA4ET NeurIPS 2026", "organizers", organizers_body,
    hero_title="Organizers",
    hero_lede="CMU · Keio · ServiceNow · Fujitsu",
))

(ROOT / "accepted-papers.html").write_text(page(
    "Accepted Papers — AABA4ET NeurIPS 2026", "accepted", accepted_body,
    hero_title="Accepted Papers",
    hero_lede="Coming after September 29, 2026 notifications",
))

(ROOT / "past-workshop.html").write_text(page(
    "Past Workshop — AABA4ET", "past", past_hub,
    body_class="past",
    hero_title="Past Workshop",
    hero_lede="1st edition at AAAI 2026 · Singapore",
    archive=True,
))

for name, active, body, title, lede in [
    ("aaai-2026-overview.html", "past-overview", past_overview, "Overview", "W8 · AAAI 2026 · Singapore"),
    ("aaai-2026-cfp.html", "past-cfp", past_cfp, "Call for Papers", "Archived submission guidelines"),
    ("aaai-2026-speakers.html", "past-speakers", past_speakers, "Speakers", "Invited talks from AAAI 2026"),
    ("aaai-2026-schedule.html", "past-schedule", past_schedule, "Schedule", "Poster sessions and program notes"),
    ("aaai-2026-organizers.html", "past-organizers", past_organizers, "Organizers", "Organizing, steering, and program committees"),
    ("aaai-2026-accepted.html", "past-accepted", past_accepted, "Accepted Papers", "25 papers from AAAI 2026"),
]:
    (PAST / name).write_text(page(
        f"AAAI 2026 {title} — AABA4ET", active, body,
        prefix="../", body_class="past-sub",
        hero_title=title, hero_lede=lede, archive=True,
    ))

print("Generated pages OK")
