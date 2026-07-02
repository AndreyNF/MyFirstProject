#!/usr/bin/env python3
"""Сборка HTML для vs-prodazha-kvartiry-moshenniki-st-159-zashchita-2026. MCP-only: без script/canvas."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HANDOFF = ROOT / "nero-network-handoff.md"
OUT = ROOT / "page-content-natasha-vs-prodazha-kvartiry.html"
SLUG = "vs-prodazha-kvartiry-moshenniki-st-159-zashchita-2026"
PAGE_CLASS = f"{SLUG}-page"

TITLE = "ВС 2026: продажа квартиры под влиянием мошенников и ст. 159 УК | Legis24"
DESCRIPTION = (
    "Обзор ВС РФ от 01.07.2026: когда продажа квартиры после обмана ведёт к делу по ст. 159 УК (ч. 3–4), "
    "риски покупателя и защита на проверке и в суде. Консультация адвоката по мошенничеству."
)
H1 = (
    "ВС разъяснил продажу квартиры под влиянием мошенников: "
    "уголовные риски по ст. 159 и защита на проверке и в суде"
)

H2_IDS = {
    "Обзор ВС РФ от 01.07.2026: продажа квартиры после обмана и уголовная ответственность": "vs-ug-obzor",
    "Ст. 159 УК РФ: когда продажа квартиры квалифицируется как мошенничество": "vs-ug-st159",
    "Мошенничество с недвижимостью: схемы обмана при продаже квартиры": "vs-ug-shemy",
    "Продажа квартиры под влиянием мошенников: граница заблуждения и уголовного дела": "vs-ug-granica",
    "Ст. 178–179 ГК РФ и ст. 159 УК: гражданское оспаривание и уголовная защита": "vs-ug-gk-uk",
    "Риски для покупателя квартиры: «знал или должен был знать»": "vs-ug-riski-pokupatel",
    "Защита продавца и покупателя на доследственной проверке и в суде": "vs-ug-zashchita",
    "Наказание по ст. 159 УК и сроки давности": "vs-ug-nakazanie",
    "Частые вопросы о мошенничестве при продаже квартиры": "vs-ug-faq",
}

BORIS_AFTER_H2 = "vs-ug-gk-uk"

TOC_LABELS = [
    ("vs-ug-obzor", "Обзор ВС 01.07.2026"),
    ("vs-ug-st159", "ст. 159 УК"),
    ("vs-ug-shemy", "Схемы обмана"),
    ("vs-ug-granica", "Заблуждение vs обман"),
    ("vs-ug-gk-uk", "ст. 178–179 ГК ↔ ст. 159"),
    ("l24-boris-vs-prodazha-kvartiry-evidence", "Два контура"),
    ("vs-ug-riski-pokupatel", "Риски покупателя"),
    ("vs-ug-zashchita", "Защита на проверке"),
    ("vs-ug-nakazanie", "Наказание"),
    ("vs-ug-faq", "FAQ"),
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
        r"=== АРТУР \(CTA И РЕКЛАМА\) ===.*?### Полный текст\n+(.*?)(?:\n\n### Рекламные вставки для Наташи|\n\n## Передача пайплайну)",
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
            if (
                not s
                or s.startswith("#")
                or s.startswith("|")
                or s.startswith("- ")
                or re.match(r"^\d+\.\s", s)
                or s.startswith("<aside")
            ):
                break
            para.append(s)
            i += 1
        out.append(f"<p>{md_inline(' '.join(para))}</p>")

    return "\n".join(out), i


def parse_faq_section(lines: list[str], start: int) -> tuple[str, int]:
    items: list[tuple[str, str]] = []
    bottom_cta = ""
    i = start
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith("## "):
            break
        if stripped.startswith("<aside"):
            block = [line for line in lines[i:] if True]
            block_lines = []
            while i < len(lines):
                block_lines.append(lines[i])
                if "</aside>" in lines[i]:
                    i += 1
                    break
                i += 1
            bottom_cta = "\n".join(block_lines)
            break
        if stripped.startswith("### "):
            q = stripped[4:].strip()
            i += 1
            ans_lines = []
            while i < len(lines):
                s = lines[i].strip()
                if s.startswith("### ") or s.startswith("## ") or s.startswith("<aside"):
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
    section = f"""<section id="vs-ug-faq" class="ym-section l24-faq" itemscope itemtype="https://schema.org/FAQPage" aria-label="Частые вопросы">
  <h2 id="vs-ug-faq-h">Частые вопросы о мошенничестве при продаже квартиры</h2>
{chr(10).join(faq_html)}
{bottom_cta}
</section>"""
    return section, i


def md_to_sections(md: str, boris_html: str, intro_lead: str = "") -> str:
    lines = md.split("\n")
    sections: list[str] = []
    i = 0
    boris_inserted = False
    first_section = True

    while i < len(lines) and not lines[i].strip().startswith("## "):
        i += 1

    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped.startswith("## "):
            i += 1
            continue
        title = stripped[3:].strip()
        hid = H2_IDS.get(title, re.sub(r"[^a-z0-9-]+", "-", title.lower())[:40])

        if hid == "vs-ug-faq":
            faq_section, i = parse_faq_section(lines, i + 1)
            sections.append(faq_section)
            continue

        i += 1
        content, i = parse_block(lines, i)
        if first_section and intro_lead:
            lead_plain = plain_text(intro_lead)
            content = re.sub(
                rf"<p>{re.escape(md_inline(intro_lead))}</p>\s*",
                "",
                content,
                count=1,
            )
            if lead_plain and content.count(lead_plain):
                content = content.replace(f"<p>{md_inline(intro_lead)}</p>", "", 1)
            first_section = False
        section = (
            f'<section class="ym-section" id="{hid}" aria-labelledby="{hid}-h">\n'
            f'<h2 id="{hid}-h">{md_inline(title)}</h2>\n{content}\n</section>'
        )
        sections.append(section)
        first_section = False

        if hid == BORIS_AFTER_H2 and not boris_inserted:
            sections.append(boris_html)
            boris_inserted = True

    if not boris_inserted:
        raise ValueError(f"Boris block was not inserted after {BORIS_AFTER_H2}")

    return "\n\n".join(sections)


def parse_intro(md: str) -> str:
    lines = md.split("\n")
    for i, line in enumerate(lines):
        if line.strip().startswith("## "):
            j = i + 1
            while j < len(lines):
                s = lines[j].strip()
                if s.startswith("### ") or s.startswith("## "):
                    break
                if s and not s.startswith("|"):
                    return s
                j += 1
            break
    return ""


def build_intro(lead: str) -> str:
    return f"""
<section class="l24-intro-ug ym-section" aria-label="Введение">
  <div class="l24-intro-ug__grid">
    <div class="l24-intro-ug__text">
      <p>{md_inline(lead)}</p>
      <div class="l24-intro-ug__brief">Материал разбирает обзор ВС РФ от 01.07.2026 по сделкам с жильём под влиянием мошенников: <strong>20 позиций</strong> практики, параллель гражданского оспаривания по <strong>ст. 179 ГК</strong> и уголовного дела по <strong>ч. 3–4 ст. 159 УК</strong>, дело Долиной и защита продавца-потерпевшего и добросовестного покупателя на доследственной проверке и в суде.</div>
    </div>
    <aside class="l24-intro-ug__decor" aria-label="Ключевые маркеры обзора ВС">
      <ul class="l24-intro-ug__chips">
        <li class="l24-intro-ug__chip l24-intro-ug__chip--accent">обзор ВС 01.07.2026</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--red">ч. 3–4 ст. 159 УК</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--navy">ст. 178–179 ГК</li>
        <li class="l24-intro-ug__chip">обман третьих лиц</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--warn">дело Долиной</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--blue">20 позиций</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--ok">добросовестный покупатель</li>
        <li class="l24-intro-ug__chip">защита на проверке</li>
      </ul>
      <svg class="l24-intro-ug__route-svg" viewBox="0 0 380 88" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Маршрут: обман мошенников → продажа квартиры → ст. 159 УК и ст. 179 ГК">
        <defs>
          <marker id="intrUg-arr" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7Z" fill="#a31830"/>
          </marker>
        </defs>
        <rect x="4" y="20" width="88" height="48" rx="8" fill="#fff7f7" stroke="#fecaca" stroke-width="1.2"/>
        <text x="48" y="42" text-anchor="middle" fill="#a31830" font-size="6.5" font-weight="800">ОБМАН</text>
        <text x="48" y="56" text-anchor="middle" fill="#64748b" font-size="5.5">телефон · ЦБ · ФСБ</text>
        <line x1="94" y1="44" x2="118" y2="44" stroke="#a31830" stroke-width="1.5" marker-end="url(#intrUg-arr)"/>
        <rect x="122" y="20" width="88" height="48" rx="8" fill="#f5f3ff" stroke="#4338ca" stroke-width="1.2"/>
        <text x="166" y="42" text-anchor="middle" fill="#4338ca" font-size="6.5" font-weight="800">СДЕЛКА</text>
        <text x="166" y="56" text-anchor="middle" fill="#64748b" font-size="5.5">продажа квартиры</text>
        <line x1="212" y1="44" x2="236" y2="44" stroke="#1a365d" stroke-width="1.5" marker-end="url(#intrUg-arr)"/>
        <rect x="240" y="14" width="132" height="60" rx="8" fill="#1a365d" stroke="#a31830" stroke-width="1.2"/>
        <text x="306" y="36" text-anchor="middle" fill="#fecaca" font-size="6.5" font-weight="800">ст. 159 УК · ст. 179 ГК</text>
        <text x="306" y="50" text-anchor="middle" fill="#93c5fd" font-size="5.5">два параллельных контура</text>
        <text x="306" y="62" text-anchor="middle" fill="#93c5fd" font-size="5.5">защита на проверке</text>
        <text x="190" y="12" text-anchor="middle" fill="#64748b" font-size="5.5" font-weight="600">мошенничество с недвижимостью · ВС 2026</text>
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
                    "ст 159 ук рф",
                    "мошенничество с недвижимостью",
                    "продажа квартиры под влиянием мошенников",
                    "обзор верховного суда 2026 мошенничество",
                    "защита по уголовному делу мошенничество",
                ],
            },
            {"@type": "FAQPage", "mainEntity": faq_entities},
        ],
    }
    return (
        '<pre class="l24-jsonld-vs-ug" aria-hidden="true" hidden>'
        + json.dumps(graph, ensure_ascii=False)
        + "</pre>"
    )


def extract_faq_items(md: str) -> list[tuple[str, str]]:
    m = re.search(
        r"## Частые вопросы о мошенничестве при продаже квартиры\n(.*?)(?:\n<aside|\Z)",
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
  margin-top: 0; color: #1a365d; font-size: 1.45rem; font-weight: 800;
}}
.{p} .ym-section + .ym-section h2,
.{p} .l24-boris-vs-prodazha-kvartiry + .ym-section h2 {{
  margin-top: 2.5em;
}}
.{p} .ym-section:first-child h2 {{ margin-top: 0; }}
.{p} h3 {{ margin-top: 1.5em; color: #a31830; font-size: 1.15rem; font-weight: 700; }}
.{p} a {{ color: #4338ca; }}
.{p} p {{ margin: 0 0 1.1em; }}
.{p} ol, .{p} ul {{ margin: 1em 0; padding-left: 1.4em; }}
.{p} li {{ margin-bottom: 0.45em; }}
.l24-tbl-wrap {{ overflow-x: auto; margin: 1.25em 0; }}
.l24-tbl {{ width: 100%; border-collapse: collapse; font-size: 0.95rem; }}
.l24-tbl th {{ background: #fff7f7; color: #a31830; font-weight: 700; padding: 10px 12px; border: 1px solid #fecaca; text-align: left; }}
.l24-tbl td {{ padding: 9px 12px; border: 1px solid #e2e8f0; vertical-align: top; }}
.l24-tbl tr:nth-child(even) td {{ background: #f8fafc; }}
.l24-intro-ug {{ max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px; font-family: system-ui, sans-serif; }}
.l24-intro-ug__grid {{ display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr); gap: 28px; align-items: start; }}
.l24-intro-ug__text {{ border-left: 4px solid #a31830; padding: 4px 0 4px 22px; text-align: left; }}
.l24-intro-ug__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.l24-intro-ug__brief {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; line-height: 1.55; color: #334155; }}
.l24-intro-ug__decor {{ background: linear-gradient(160deg, #fff7f7 0%, #fff 100%); border: 1px solid #fecaca; border-radius: 12px; padding: 18px; }}
.l24-intro-ug__chips {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none; }}
.l24-intro-ug__chip {{ font-size: 0.72rem; font-weight: 700; padding: 6px 10px; border-radius: 999px; background: #fff; border: 1px solid #cbd5e1; color: #475569; }}
.l24-intro-ug__chip--accent {{ border-color: #a31830; color: #a31830; background: #fff7f7; }}
.l24-intro-ug__chip--red {{ border-color: #dc2626; color: #991b1b; background: #fef2f2; }}
.l24-intro-ug__chip--navy {{ border-color: #1a365d; color: #1a365d; background: #eff6ff; }}
.l24-intro-ug__chip--blue {{ border-color: #4338ca; color: #4338ca; background: #f5f3ff; }}
.l24-intro-ug__chip--ok {{ border-color: #059669; color: #047857; background: #ecfdf5; }}
.l24-intro-ug__chip--warn {{ border-color: #d97706; color: #92400e; background: #fffbeb; }}
.l24-intro-ug__route-svg {{ display: block; width: 100%; height: auto; }}
.ym-toc {{ max-width: 820px; margin: 24px auto 0; padding: 0 24px 32px; text-align: center; font-family: system-ui, sans-serif; }}
.ym-toc__title {{ font-size: 0.8rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: #64748b; margin: 0 0 12px; }}
.ym-toc__list {{ list-style: none; padding: 0; margin: 0; display: flex; flex-wrap: wrap; justify-content: center; gap: 8px 10px; }}
.ym-toc__list a {{ display: inline-block; padding: 8px 12px; border-radius: 8px; background: #fff7f7; color: #a31830; text-decoration: none; font-size: 0.88rem; font-weight: 600; border: 1px solid #fecaca; }}
.ym-toc__list a:hover {{ background: #fee2e2; }}
.ym-section {{ display: block; }}
.ym-cta {{ margin: 28px 0; padding: 22px 24px; border-radius: 10px; background: linear-gradient(135deg, #f8fafc 0%, #fff7f7 100%); border: 1px solid #fecaca; border-left: 4px solid #a31830; }}
.ym-cta--legis24.ym-cta--bottom {{ border-left-color: #4338ca; background: linear-gradient(135deg, #f5f3ff 0%, #eff6ff 100%); border-color: #c4b5fd; }}
.ym-cta--legis24.ym-cta--bottom h3 {{ margin: 0 0 12px; font-size: 1.1rem; color: #1a365d; }}
.ym-cta__text {{ margin: 0 0 14px; line-height: 1.55; color: #334155; font-size: 0.98rem; }}
.ym-cta__actions {{ margin: 0; }}
.ym-cta__btn {{ display: inline-block; background: #a31830; color: #fff !important; padding: 12px 22px; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 0.93rem; }}
.ym-cta__btn:hover {{ background: #8b1528; }}
.ym-cta--legis24.ym-cta--bottom .ym-cta__btn {{ background: #4338ca; }}
.ym-cta--legis24.ym-cta--bottom .ym-cta__btn:hover {{ background: #3730a3; }}
.l24-faq {{ margin-top: 2.5em; padding: 28px 24px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; }}
.l24-faq > h2 {{ margin-top: 0 !important; }}
.l24-faq__item {{ margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0; }}
.l24-faq__item:last-of-type {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
.l24-faq__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #a31830; font-weight: 700; }}
.l24-faq__a {{ margin: 0; color: #334155; font-size: 0.97rem; line-height: 1.6; }}
.l24-jsonld-vs-ug {{ display: none !important; }}
@media (max-width: 900px) {{ .l24-intro-ug__grid {{ grid-template-columns: 1fr; }} }}
"""


def main():
    handoff = HANDOFF.read_text(encoding="utf-8")
    hero = strip_scripts_canvas(
        extract_section_html(handoff, "=== АЛИНА (HERO) ===", "=== БОРИС")
    )
    boris = strip_scripts_canvas(
        extract_section_html(
            handoff, "=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===", "## Передача Наташе"
        )
    )
    artur_md = extract_artur_body(handoff)
    intro_lead = parse_intro(artur_md)
    faq_items = extract_faq_items(artur_md)
    sections_html = md_to_sections(artur_md, boris, intro_lead)
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
    byte_count = len(html.encode("utf-8"))

    natasha_block = f"""=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО
SLUG: {SLUG}
Размер HTML: {byte_count} байт
main#primary: да
script: нет
canvas: нет
JSON-LD Article + FAQPage: да (скрытый `<pre class="l24-jsonld-vs-ug" hidden>` + microdata на `<main>` и FAQ)
ВНИМАНИЕ: MCP-only Legis24 — без `<script>` и `<canvas>`; hero Алины и блок Бориса — static SVG + inline CSS. При публикации обернуть в <!-- wp:html -->

{html}

## Передача Юре
SLUG: {SLUG}
Title: {TITLE}
Description: {DESCRIPTION}
Контент MCP-only: hero static SVG, блок Бориса static SVG по якорю `l24-boris-vs-prodazha-kvartiry-evidence`, JSON-LD Article + FAQPage в hidden pre. Обязательно обернуть в <!-- wp:html --> при публикации.
Размер HTML: {byte_count} байт
main#primary: да
script: нет
canvas: нет
"""

    if "=== НАТАША (HTML СТРАНИЦЫ) ===" in handoff:
        handoff = handoff.split("=== НАТАША (HTML СТРАНИЦЫ) ===")[0].rstrip() + "\n\n" + natasha_block
    else:
        handoff = handoff.rstrip() + "\n\n" + natasha_block
    HANDOFF.write_text(handoff, encoding="utf-8")

    assert 'id="primary"' in html
    assert "l24-boris-vs-prodazha-kvartiry-evidence" in html
    assert "l24-hero-vs-prodazha-kvartiry-moshenniki-st-159" in html
    assert "ym-section" in html
    assert "<script" not in html.lower()
    assert "<canvas" not in html.lower()
    assert 'href="https://advokat-vsem.ru/"' in html

    print(f"Wrote {OUT}")
    print(f"Bytes: {byte_count}")
    print(f"SLUG: {SLUG}")


if __name__ == "__main__":
    main()
