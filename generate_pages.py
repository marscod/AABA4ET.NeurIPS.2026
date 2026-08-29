#!/usr/bin/env python3
"""Generate multi-page AABA4ET site with shared chrome."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FONTS = """  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet" />"""


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
      <nav class="site-nav" id="site-nav">
        {a("index.html", "Home", "home")}
        {a("call-for-papers.html", "CFP", "cfp")}
        {a("speakers.html", "Speakers", "speakers")}
        {a("panel.html", "Panel", "panel")}
        {a("schedule.html", "Schedule", "schedule")}
        {a("organizers.html", "Organizers", "organizers")}
        {a("accepted-papers.html", "Papers", "accepted")}
        <a href="https://sites.google.com/view/aaba4et/past-workshop" target="_blank" rel="noopener">Past</a>
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
        <a href="{prefix}panel.html">Panel</a>
        <a href="{prefix}schedule.html">Schedule</a>
        <a href="{prefix}organizers.html">Organizers</a>
        <a href="{prefix}accepted-papers.html">Accepted Papers</a>
        <a href="https://sites.google.com/view/aaba4et/past-workshop" target="_blank" rel="noopener">Past Workshop</a>
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
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
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
      <p class="lede">We invite submissions on benchmarking, evaluating, and deploying Agentic AI systems for complex enterprise operations. This is the 2nd edition, following AAAI 2026 in Singapore.</p>
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
      <p class="lede">Talk titles will be announced soon.</p>

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
          <p class="role">AI and Engineering Executive @ Netflix</p>
{social_icons("https://www.karyafar.com/", "https://www.linkedin.com/in/karyafar", "https://scholar.google.com/citations?user=whu7X_kAAAAJ&hl=en")}
        </div>
      </article>

      <article class="person-full speaker">
        <img class="person-photo" src="images/panelists/mehdi-bahrami.jpg" alt="Mehdi Bahrami" width="160" height="160" loading="lazy" />
        <div class="person-copy">
          {person_name("Mehdi Bahrami")}
          <p class="role">Fujitsu Research of America</p>
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
        <img class="person-photo" src="images/organizers/drouin.png" alt="Alexandre Drouin" width="160" height="160" loading="lazy" />
        <div class="person-copy">
          {person_name("Alexandre Drouin", "https://www.alexdrouin.com/")}
          <p class="role">Head of Frontier AI Research, ServiceNow · Adjunct Professor, Laval University &amp; Mila</p>
          <p>Leads Frontier AI Research at ServiceNow Research. Work focuses on ML for decision-making in complex environments—causal inference, probabilistic forecasting, and LLM-based agents—plus benchmarks for browser automation, data analytics, forecasting, security, and robustness. Program Committee for NeurIPS 2026 Evaluations and Datasets track.</p>
          <p class="expertise"><strong>Expertise:</strong> Agentic systems, benchmarking, decision-making under uncertainty.</p>
{social_icons("https://www.alexdrouin.com/", "https://linkedin.com/in/drouinalexandre", "https://scholar.google.com/citations?user=LR6aJcEAAAAJ&hl=en")}
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

(ROOT / "panel.html").write_text(page(
    "Panel — AABA4ET NeurIPS 2026", "panel", panel_body,
    hero_title="Panel",
    hero_lede="Industry and research perspectives on agentic AI for enterprise",
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

print("Generated pages OK")
