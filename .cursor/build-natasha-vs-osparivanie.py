#!/usr/bin/env python3
"""Сборка HTML для vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026. MCP-only: без script/canvas."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HANDOFF = ROOT / "nero-network-handoff.md"
OUT = ROOT / "page-content-natasha-vs-osparivanie.html"
SLUG = "vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026"
PAGE_CLASS = f"{SLUG}-page"

TITLE = "Обзор ВС 2026: оспаривание сделок с жильём в банкротстве | Legis24"
DESCRIPTION = (
    "Обзор практики ВС РФ от 01.07.2026: оспаривание сделок с жильём при банкротстве по ст. 61.2 — "
    "дарение, заниженная цена, мнимость. Риски покупателя и защита сделки в арбитраже."
)
H1 = "Обзор ВС 2026: оспаривание сделок с жильём в банкротстве — дарение, цена, мнимость"

H2_IDS = {
    "Обзор ВС РФ от 01.07.2026: что изменилось в оспаривании сделок с жильём": "vs-zhiloe-obzor",
    "Ст. 61.2 Закона о банкротстве: подозрительные сделки с недвижимостью": "vs-zhiloe-612",
    "Дарение квартиры при банкротстве: когда ФУ оспорит договор дарения": "vs-zhiloe-darenie",
    "Заниженная цена и неравноценность: почему отклонение >20% уже недостаточно": "vs-zhiloe-cena",
    "Мнимая сделка продажи квартиры: признаки и доказательства в арбитраже": "vs-zhiloe-mnimaya",
    "Банкротство после продажи квартиры: риски для покупателя": "vs-zhiloe-riski",
    "Добросовестный покупатель: как защитить сделку в арбитражном суде": "vs-zhiloe-dobrosovest",
    "Сроки оспаривания сделок при банкротстве": "vs-zhiloe-sroki",
    "Практика арбитражных судов 2026: кто оспорит, а кто отстоит сделку": "vs-zhiloe-praktika",
    "Частые вопросы об оспаривании сделок с жильём в банкротстве": "vs-zhiloe-faq",
    "Консультация по оспариванию или защите сделки с жильём в арбитраже": "vs-zhiloe-konsult",
}

TOC_LABELS = [
    ("vs-zhiloe-obzor", "Обзор ВС 01.07.2026"),
    ("l24-boris-vs-osparivanie-sdelok-zhiloe", "Два контура"),
    ("vs-zhiloe-612", "ст. 61.2"),
    ("vs-zhiloe-darenie", "Дарение"),
    ("vs-zhiloe-cena", "Цена >20%"),
    ("vs-zhiloe-mnimaya", "Мнимость"),
    ("vs-zhiloe-riski", "Риски покупателя"),
    ("vs-zhiloe-dobrosovest", "Добросовестность"),
    ("vs-zhiloe-sroki", "Сроки"),
    ("vs-zhiloe-praktika", "Практика 2026"),
    ("vs-zhiloe-faq", "FAQ"),
    ("vs-zhiloe-konsult", "Консультация"),
]


def extract_section_html(handoff: str, marker: str, next_marker: str) -> str:
    start = handoff.find(marker)
    if start < 0:
        raise ValueError(f"Section not found: {marker}")
    end = handoff.find(next_marker, start + len(marker))
    block = handoff[start:end] if end >= 0 else handoff[start:]
    m = re.search(r"```html\n(.*?)```", block, re.DOTALL)
    if not m:
        raise ValueError(f"No html block in {marker}")
    return m.group(1).strip()


def extract_artur_body(handoff: str) -> str:
    m = re.search(
        r"=== АРТУР \(CTA И РЕКЛАМА\) ===.*?### Полный текст\n\n(.*?)(?:\n\n### Рекламные вставки|\n\n## Передача пайплайну)",
        handoff,
        re.DOTALL,
    )
    if not m:
        raise ValueError("Artur body not found")
    body = m.group(1).strip()
    body = re.sub(r"^# .+\n\n", "", body, count=1)
    return body


def strip_scripts_canvas(html: str) -> str:
    html = re.sub(r"<script\b[^>]*>[\s\S]*?</script>", "", html, flags=re.I)
    html = re.sub(r"<canvas\b[^>]*>[\s\S]*?</canvas>", "", html, flags=re.I)
    html = re.sub(r"<canvas\b[^>]*/>", "", html, flags=re.I)
    return html


def md_inline(s: str) -> str:
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        s,
    )
    s = re.sub(
        r'<a href="(https?://[^"]+)"(?![^>]*target=)',
        r'<a href="\1" target="_blank" rel="noopener noreferrer"',
        s,
    )
    return s


def parse_table(lines: list[str]) -> str:
    rows = []
    for line in lines:
        if not line.strip().startswith("|"):
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.match(r"^[-:]+$", c) for c in cells):
            continue
        rows.append(cells)
    if not rows:
        return ""
    html = ['<div class="l24-tbl-wrap"><table class="l24-tbl">', "<thead><tr>"]
    for c in rows[0]:
        html.append(f"<th>{md_inline(c)}</th>")
    html.append("</tr></thead><tbody>")
    for row in rows[1:]:
        html.append("<tr>")
        for c in row:
            html.append(f"<td>{md_inline(c)}</td>")
        html.append("</tr>")
    html.append("</tbody></table></div>")
    return "".join(html)


def parse_block(lines: list[str], start: int) -> tuple[str, int]:
    out: list[str] = []
    i = start
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("## "):
            break

        if stripped.startswith("<aside"):
            block = [line]
            i += 1
            while i < len(lines):
                block.append(lines[i])
                if "</aside>" in lines[i]:
                    i += 1
                    break
                i += 1
            out.append("\n".join(block))
            continue

        if stripped.startswith("|"):
            tbl_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl_lines.append(lines[i])
                i += 1
            out.append(parse_table(tbl_lines))
            continue

        if stripped.startswith("### "):
            out.append(f"<h3>{md_inline(stripped[4:].strip())}</h3>")
            i += 1
            continue

        if re.match(r"^\d+\.\s", stripped):
            out.append("<ol>")
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i].strip()):
                item = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                out.append(f"<li>{md_inline(item)}</li>")
                i += 1
            out.append("</ol>")
            continue

        if stripped.startswith("- "):
            out.append("<ul>")
            while i < len(lines) and lines[i].strip().startswith("- "):
                item = lines[i].strip()[2:]
                out.append(f"<li>{md_inline(item)}</li>")
                i += 1
            out.append("</ul>")
            continue

        if not stripped:
            i += 1
            continue

        para = [stripped]
        i += 1
        while i < len(lines):
            s = lines[i].strip()
            if not s or s.startswith("#") or s.startswith("|") or s.startswith("- ") or re.match(r"^\d+\.\s", s) or s.startswith("<aside"):
                break
            para.append(s)
            i += 1
        out.append(f"<p>{md_inline(' '.join(para))}</p>")

    return "\n".join(out), i


def parse_faq_section(lines: list[str], start: int) -> tuple[str, int]:
    items: list[tuple[str, str]] = []
    i = start
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith("## "):
            break
        if stripped.startswith("### "):
            q = stripped[4:].strip()
            i += 1
            ans_lines = []
            while i < len(lines):
                s = lines[i].strip()
                if s.startswith("### ") or s.startswith("## "):
                    break
                if s:
                    ans_lines.append(s)
                i += 1
            items.append((q, " ".join(ans_lines)))
            continue
        i += 1

    faq_html = []
    for q, a in items:
        faq_html.append(
            f"""  <div class="l24-faq__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 class="l24-faq__q" itemprop="name">{md_inline(q)}</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p class="l24-faq__a" itemprop="text">{md_inline(a)}</p>
    </div>
  </div>"""
        )
    section = f"""<section id="vs-zhiloe-faq" class="ym-section l24-faq" itemscope itemtype="https://schema.org/FAQPage" aria-label="Частые вопросы">
  <h2 id="vs-zhiloe-faq-h">Частые вопросы об оспаривании сделок с жильём в банкротстве</h2>
{chr(10).join(faq_html)}
</section>"""
    return section, i


def md_to_sections(md: str, boris_html: str) -> str:
    lines = md.split("\n")
    sections: list[str] = []
    i = 0
    boris_inserted = False
  # skip intro paragraph
    while i < len(lines) and not lines[i].strip().startswith("## "):
        if lines[i].strip():
            i += 1
        else:
            i += 1

    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped.startswith("## "):
            i += 1
            continue
        title = stripped[3:].strip()
        hid = H2_IDS.get(title, re.sub(r"[^a-z0-9-]+", "-", title.lower())[:40])

        if hid == "vs-zhiloe-faq":
            faq_section, i = parse_faq_section(lines, i + 1)
            sections.append(faq_section)
            continue

        i += 1
        content, i = parse_block(lines, i)
        section = f'<section class="ym-section" id="{hid}" aria-labelledby="{hid}-h">\n<h2 id="{hid}-h">{md_inline(title)}</h2>\n{content}\n</section>'
        sections.append(section)

        if hid == "vs-zhiloe-obzor" and not boris_inserted:
            sections.append(boris_html)
            boris_inserted = True

    if not boris_inserted:
        raise ValueError("Boris block was not inserted after first H2")

    return "\n\n".join(sections)


def parse_intro(md: str) -> str:
    lines = md.split("\n")
    intro = ""
    for line in lines:
        if line.strip().startswith("## "):
            break
        if line.strip() and not line.strip().startswith("#"):
            intro = line.strip()
            break
    return intro


def build_intro(lead: str) -> str:
    return f"""
<section class="l24-intro-arb ym-section" aria-label="Введение">
  <div class="l24-intro-arb__grid">
    <div class="l24-intro-arb__text">
      <p>{md_inline(lead)}</p>
      <div class="l24-intro-arb__brief">Материал разбирает обзор ВС 01.07.2026 по оспариванию сделок с жильём: <strong>20 позиций</strong> после «эффекта Долиной», <strong>ст. 61.2</strong> Закона о банкротстве, дела Чигарчаковой и Рыбалко — когда ФУ оспорит продажу или дарение квартиры, а добросовестный покупатель отстоит сделку в арбитраже.</div>
    </div>
    <aside class="l24-intro-arb__decor" aria-label="Ключевые маркеры обзора ВС">
      <ul class="l24-intro-arb__chips">
        <li class="l24-intro-arb__chip l24-intro-arb__chip--accent">обзор ВС 01.07.2026</li>
        <li class="l24-intro-arb__chip l24-intro-arb__chip--navy">ст. 61.2</li>
        <li class="l24-intro-arb__chip l24-intro-arb__chip--blue">20 позиций</li>
        <li class="l24-intro-arb__chip">дарение</li>
        <li class="l24-intro-arb__chip l24-intro-arb__chip--warn">&gt;20% цена</li>
        <li class="l24-intro-arb__chip l24-intro-arb__chip--ok">добросовестный покупатель</li>
        <li class="l24-intro-arb__chip">эффект Долиной</li>
        <li class="l24-intro-arb__chip l24-intro-arb__chip--navy">307-ЭС25-13338</li>
      </ul>
      <svg class="l24-intro-arb__route-svg" viewBox="0 0 360 88" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Маршрут: обзор ВС 01.07.2026 → ст. 61.2 → 20 позиций по жилью">
        <rect x="4" y="20" width="88" height="48" rx="8" fill="#eff6ff" stroke="#1e3a8a" stroke-width="1.2"/>
        <text x="48" y="42" text-anchor="middle" fill="#1e3a8a" font-size="6.5" font-weight="800">ОБЗОР ВС</text>
        <text x="48" y="56" text-anchor="middle" fill="#0369a1" font-size="5.5">01.07.2026</text>
        <line x1="94" y1="44" x2="118" y2="44" stroke="#0369a1" stroke-width="1.5" marker-end="url(#intrZh-arr)"/>
        <rect x="122" y="20" width="88" height="48" rx="8" fill="#f0f9ff" stroke="#0369a1" stroke-width="1.2"/>
        <text x="166" y="42" text-anchor="middle" fill="#0369a1" font-size="6.5" font-weight="800">ст. 61.2</text>
        <text x="166" y="56" text-anchor="middle" fill="#64748b" font-size="5.5">подозр. сделки</text>
        <line x1="212" y1="44" x2="236" y2="44" stroke="#1e3a8a" stroke-width="1.5" marker-end="url(#intrZh-arr)"/>
        <rect x="240" y="14" width="112" height="60" rx="8" fill="#1e3a8a" stroke="#0369a1" stroke-width="1.2"/>
        <text x="296" y="36" text-anchor="middle" fill="#e0f2fe" font-size="6.5" font-weight="800">20 ПОЗИЦИЙ</text>
        <text x="296" y="50" text-anchor="middle" fill="#93c5fd" font-size="5.5">жильё · дарение</text>
        <text x="296" y="62" text-anchor="middle" fill="#93c5fd" font-size="5.5">цена · мнимость</text>
        <defs>
          <marker id="intrZh-arr" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7Z" fill="#0369a1"/>
          </marker>
        </defs>
        <text x="180" y="12" text-anchor="middle" fill="#64748b" font-size="5.5" font-weight="600">оспаривание сделок с жильём · банкротство · арбитраж</text>
      </svg>
    </aside>
  </div>
</section>
"""


def build_toc() -> str:
    lis = "\n".join(f'    <li><a href="#{a}">{t}</a></li>' for a, t in TOC_LABELS)
    return f"""
<nav class="ym-toc ym-section" aria-label="Содержание статьи">
  <p class="ym-toc__title">Содержание</p>
  <ul class="ym-toc__list">
{lis}
  </ul>
</nav>
"""


def plain_text(s: str) -> str:
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def build_json_ld_hidden(faq_items: list[tuple[str, str]]) -> str:
    faq_entities = [
        {
            "@type": "Question",
            "name": plain_text(q),
            "acceptedAnswer": {"@type": "Answer", "text": plain_text(a)},
        }
        for q, a in faq_items
    ]
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": H1,
                "description": DESCRIPTION,
                "datePublished": "2026-07-01",
                "dateModified": "2026-07-02",
                "author": {"@type": "Organization", "name": "Legis24"},
                "publisher": {"@type": "Organization", "name": "Legis24"},
                "inLanguage": "ru-RU",
                "about": [
                    "оспаривание сделок при банкротстве",
                    "ст 61.2 закона о банкротстве",
                    "оспаривание сделок с жильем",
                    "обзор верховного суда 2026 банкротство",
                    "добросовестный покупатель банкротство",
                ],
            },
            {"@type": "FAQPage", "mainEntity": faq_entities},
        ],
    }
    return (
        '<pre class="l24-jsonld-vs-zhiloe" aria-hidden="true" hidden>'
        + json.dumps(graph, ensure_ascii=False)
        + "</pre>"
    )


def extract_faq_items(md: str) -> list[tuple[str, str]]:
    m = re.search(
        r"## Частые вопросы об оспаривании сделок с жильём в банкротстве\n(.*?)(?:\n## |\Z)",
        md,
        re.DOTALL,
    )
    if not m:
        return []
    block = m.group(1)
    items = []
    for chunk in re.split(r"\n### ", block):
        chunk = chunk.strip()
        if not chunk:
            continue
        lines = chunk.split("\n", 1)
        q = lines[0].strip()
        a = lines[1].strip() if len(lines) > 1 else ""
        if q and a:
            items.append((q, a))
    return items


def page_css() -> str:
    p = PAGE_CLASS
    return f"""
.breadcrumbs, .breadcrumb, .rank-math-breadcrumb, .yoast-breadcrumb,
.entry-header, .page-title-section {{ display: none !important; }}
#primary, .site-main, .site-content, #content, .content-area {{
  padding-top: 0 !important; margin-top: 0 !important;
}}
#sidebar, .sidebar, #secondary, .et_pb_column_1_4 {{ display: none !important; }}
.{p} .entry-content {{
  max-width: none !important; width: 100% !important; padding: 0 !important;
}}
.{p} .l24-longread-wrap {{
  max-width: 820px; margin: 0 auto; padding: 48px 24px 80px;
  font-size: 1.05rem; line-height: 1.65; color: #1a202c;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.{p} .ym-section h2 {{
  margin-top: 0; color: #1e3a8a; font-size: 1.45rem; font-weight: 800;
}}
.{p} .ym-section + .ym-section h2,
.{p} .l24-boris-vs-osparivanie-sdelok-zhiloe + .ym-section h2 {{
  margin-top: 2.5em;
}}
.{p} .ym-section:first-child h2 {{ margin-top: 0; }}
.{p} h3 {{ margin-top: 1.5em; color: #0369a1; font-size: 1.15rem; font-weight: 700; }}
.{p} a {{ color: #1e3a8a; }}
.{p} p {{ margin: 0 0 1.1em; }}
.{p} ol, .{p} ul {{ margin: 1em 0; padding-left: 1.4em; }}
.{p} li {{ margin-bottom: 0.45em; }}
.l24-tbl-wrap {{ overflow-x: auto; margin: 1.25em 0; }}
.l24-tbl {{ width: 100%; border-collapse: collapse; font-size: 0.95rem; }}
.l24-tbl th {{ background: #eff6ff; color: #1e3a8a; font-weight: 700; padding: 10px 12px; border: 1px solid #bfdbfe; text-align: left; }}
.l24-tbl td {{ padding: 9px 12px; border: 1px solid #e2e8f0; vertical-align: top; }}
.l24-tbl tr:nth-child(even) td {{ background: #f8fafc; }}
.l24-intro-arb {{ max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px; font-family: system-ui, sans-serif; }}
.l24-intro-arb__grid {{ display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr); gap: 28px; align-items: start; }}
.l24-intro-arb__text {{ border-left: 4px solid #1e3a8a; padding: 4px 0 4px 22px; text-align: left; }}
.l24-intro-arb__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.l24-intro-arb__brief {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; line-height: 1.55; color: #334155; }}
.l24-intro-arb__decor {{ background: linear-gradient(160deg, #eff6ff 0%, #fff 100%); border: 1px solid #bfdbfe; border-radius: 12px; padding: 18px; }}
.l24-intro-arb__chips {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none; }}
.l24-intro-arb__chip {{ font-size: 0.72rem; font-weight: 700; padding: 6px 10px; border-radius: 999px; background: #fff; border: 1px solid #cbd5e1; color: #475569; }}
.l24-intro-arb__chip--accent {{ border-color: #1e3a8a; color: #1e3a8a; background: #eff6ff; }}
.l24-intro-arb__chip--navy {{ border-color: #0f2744; color: #0f2744; background: #f1f5f9; }}
.l24-intro-arb__chip--blue {{ border-color: #0369a1; color: #0369a1; background: #f0f9ff; }}
.l24-intro-arb__chip--ok {{ border-color: #059669; color: #047857; background: #ecfdf5; }}
.l24-intro-arb__chip--warn {{ border-color: #dc2626; color: #991b1b; background: #fef2f2; }}
.l24-intro-arb__route-svg {{ display: block; width: 100%; height: auto; }}
.ym-toc {{ max-width: 820px; margin: 24px auto 0; padding: 0 24px 32px; text-align: center; font-family: system-ui, sans-serif; }}
.ym-toc__title {{ font-size: 0.8rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: #64748b; margin: 0 0 12px; }}
.ym-toc__list {{ list-style: none; padding: 0; margin: 0; display: flex; flex-wrap: wrap; justify-content: center; gap: 8px 10px; }}
.ym-toc__list a {{ display: inline-block; padding: 8px 12px; border-radius: 8px; background: #eff6ff; color: #1e3a8a; text-decoration: none; font-size: 0.88rem; font-weight: 600; border: 1px solid #bfdbfe; }}
.ym-toc__list a:hover {{ background: #dbeafe; }}
.ym-section {{ display: block; }}
.ym-cta {{ margin: 28px 0; padding: 22px 24px; border-radius: 10px; background: linear-gradient(135deg, #f8fafc 0%, #eff6ff 100%); border: 1px solid #bfdbfe; border-left: 4px solid #1e3a8a; }}
.ym-cta--legis24.ym-cta--bottom {{ border-left-color: #0369a1; background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border-color: #7dd3fc; }}
.ym-cta__text {{ margin: 0 0 14px; line-height: 1.55; color: #334155; font-size: 0.98rem; }}
.ym-cta__actions {{ margin: 0; }}
.ym-cta__btn {{ display: inline-block; background: #a31830; color: #fff !important; padding: 12px 22px; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 0.93rem; }}
.ym-cta__btn:hover {{ background: #8b1528; }}
.ym-cta--legis24.ym-cta--bottom .ym-cta__btn {{ background: #1e3a8a; }}
.ym-cta--legis24.ym-cta--bottom .ym-cta__btn:hover {{ background: #0f2744; }}
.l24-faq {{ margin-top: 2.5em; padding: 28px 24px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; }}
.l24-faq > h2 {{ margin-top: 0 !important; }}
.l24-faq__item {{ margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0; }}
.l24-faq__item:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
.l24-faq__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #1e3a8a; font-weight: 700; }}
.l24-faq__a {{ margin: 0; color: #334155; font-size: 0.97rem; line-height: 1.6; }}
.l24-jsonld-vs-zhiloe {{ display: none !important; }}
@media (max-width: 900px) {{ .l24-intro-arb__grid {{ grid-template-columns: 1fr; }} }}
"""


def main():
    handoff = HANDOFF.read_text(encoding="utf-8")
    hero = strip_scripts_canvas(
        extract_section_html(handoff, "=== АЛИНА (HERO) ===", "=== БОРИС")
    )
    boris = strip_scripts_canvas(
        extract_section_html(handoff, "=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===", "## Передача Наташе")
    )
    artur_md = extract_artur_body(handoff)
    intro_lead = parse_intro(artur_md)
    faq_items = extract_faq_items(artur_md)
    sections_html = md_to_sections(artur_md, boris)
    json_ld = build_json_ld_hidden(faq_items)

    html = f"""<!-- wp:html -->
<style>
{page_css()}
</style>
<main id="primary" class="site-main {PAGE_CLASS}" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">
<meta itemprop="headline" content="{H1}">
<meta itemprop="description" content="{DESCRIPTION}">
<meta itemprop="inLanguage" content="ru-RU">

{hero}

{build_intro(intro_lead)}

{build_toc()}

<div class="l24-longread-wrap" itemprop="articleBody">

{sections_html}

</div>

{json_ld}
</main>
<!-- /wp:html -->
"""

    html = strip_scripts_canvas(html)
    OUT.write_text(html, encoding="utf-8")
    char_count = len(html)

    natasha_block = f"""=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО
SLUG: {SLUG}
Размер HTML: {char_count} символов
main#primary: да
script: нет
canvas: нет
JSON-LD Article: да (скрытый `<pre class="l24-jsonld-vs-zhiloe" hidden>` + microdata на `<main>`)
ВНИМАНИЕ: MCP-only Legis24 — без `<script>` и `<canvas>`; hero Алины и блок Бориса — static SVG + inline CSS. При публикации обернуть в <!-- wp:html -->

{html}

## Передача Юре
SLUG: {SLUG}
Title: {TITLE}
Description: {DESCRIPTION}
Контент MCP-only: hero static SVG, блок Бориса static SVG, JSON-LD Article в hidden pre. Обязательно обернуть в <!-- wp:html --> при публикации.
Размер HTML: {char_count} символов
main#primary: да
script: нет
"""

    if "=== НАТАША (HTML СТРАНИЦЫ) ===" in handoff:
        handoff = handoff.split("=== НАТАША (HTML СТРАНИЦЫ) ===")[0].rstrip() + "\n\n" + natasha_block
    else:
        handoff = handoff.rstrip() + "\n\n" + natasha_block
    HANDOFF.write_text(handoff, encoding="utf-8")

    assert 'id="primary"' in html
    assert "l24-boris-vs-osparivanie-sdelok-zhiloe" in html
    assert "l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026" in html
    assert "ym-section" in html
    assert "<script" not in html.lower()
    assert "<canvas" not in html.lower()

    print(f"Wrote {OUT}")
    print(f"Chars: {char_count}")
    print(f"main#primary: {'id=\"primary\"' in html}")
    print(f"script: {'<script' in html.lower()}")


if __name__ == "__main__":
    main()
