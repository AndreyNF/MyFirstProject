#!/usr/bin/env python3
"""Сборка HTML для rospatent-maugli-rot-front-annulirovanie-tovarnyj-znak-2026. MCP-only."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HANDOFF = ROOT / "nero-network-handoff.md"
OUT = ROOT / "page-content-natasha-maugli.html"
SLUG = "rospatent-maugli-rot-front-annulirovanie-tovarnyj-znak-2026"
PAGE_CLASS = f"{SLUG}-page"

TITLE = "Аннулирование товарного знака «Маугли»: возражение «Союзмультфильма» 2026"
DESCRIPTION = (
    "Роспатент аннулировал ТЗ «Маугли» у «Рот Фронта» по возражению «Союзмультфильма». "
    "Как оспорить регистрацию знака с персонажем мультфильма и ответить на иск по ИС."
)
H1 = (
    "Роспатент аннулировал товарный знак «Маугли» у «Рот Фронта»: "
    "возражение «Союзмультфильма» и защита бренда"
)

H2_IDS = {
    "Роспатент аннулировал товарный знак «Маугли»: суть решения и оспаривание регистрации": "s1-sut",
    "Дело «Маугли» и «Рот Фронт»: фабула, доводы сторон и позиция Роспатента": "s2-fabula",
    "Возражение против товарного знака в Роспатенте: сроки, основания и порядок": "s3-vozrazhenie",
    "Ст. 1483 и 1512 ГК РФ: основания недействительности охраны товарного знака": "s4-1483",
    "Товарный знак и персонаж мультфильма: пересечение авторских прав и бренда": "s5-personazh",
    "Нарушение товарного знака и компенсация: параллель с иском «Союзмультфильма» за Волка": "s6-kompensaciya",
    "Защита бренда и ответ на иск по интеллектуальной собственности": "s7-zashchita",
    "Обжалование решения Роспатента в СИП и как избежать спора при регистрации": "s8-sip",
}

TOC_LABELS = [
    ("s1-sut", "Суть решения"),
    ("boris-maugli-tz-flow", "Маршрут ППС → СИП"),
    ("s2-fabula", "Фабула дела"),
    ("s3-vozrazhenie", "Возражение в Роспатенте"),
    ("s4-1483", "ст. 1483 и 1512"),
    ("s5-personazh", "Персонаж и ТЗ"),
    ("s6-kompensaciya", "Компенсация"),
    ("s7-zashchita", "Защита бренда"),
    ("s8-sip", "СИП и регистрация"),
    ("faq", "FAQ"),
]


def extract_hero(handoff: str) -> str:
    start = handoff.index("=== АЛИНА (HERO) ===")
    end = handoff.index("=== БОРИС", start)
    block = handoff[start:end]
    idx = block.find("<section")
    if idx < 0:
        raise ValueError("Hero section not found")
    hero = block[idx:].strip()
    close = hero.rfind("</section>")
    if close < 0:
        raise ValueError("Hero closing tag not found")
    return hero[: close + len("</section>")]


def extract_boris(handoff: str) -> str:
    start = handoff.index("=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===")
    block = handoff[start:]
    m = re.search(r"```html\n(.*?)```", block, re.DOTALL)
    if not m:
        raise ValueError("Boris html block not found")
    return m.group(1).strip()


def extract_artur_body(handoff: str) -> str:
    m = re.search(
        r"=== АРТУР \(CTA И РЕКЛАМА\) ===[\s\S]*?### Полный текст\n+([\s\S]*?)\n+### Рекламные вставки",
        handoff,
    )
    if not m:
        raise ValueError("Artur body not found")
    return m.group(1).strip()


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
        r"\[([^\]]+)\]\((/[^)]+)\)",
        lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>',
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


def parse_block(lines: list[str], start: int, stop_at_faq: bool = False) -> tuple[str, int]:
    out: list[str] = []
    i = start
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("## "):
            break
        if stop_at_faq and stripped.startswith("### FAQ"):
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

        if stripped.startswith("> "):
            bq = []
            while i < len(lines) and lines[i].strip().startswith("> "):
                bq.append(lines[i].strip()[2:])
                i += 1
            out.append(f"<blockquote><p>{md_inline(' '.join(bq))}</p></blockquote>")
            continue

        if stripped == "---":
            i += 1
            continue

        if stripped.startswith("- [ ]"):
            out.append('<ul class="l24-checklist">')
            while i < len(lines) and lines[i].strip().startswith("- [ ]"):
                item = lines[i].strip()[5:].strip()
                out.append(f"<li>{md_inline(item)}</li>")
                i += 1
            out.append("</ul>")
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

        if stripped.startswith("**") and stripped.endswith("**") and "?" in stripped:
            # FAQ-style bold question inside section 8 — handled separately
            break

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
                or s.startswith("- [ ]")
                or s.startswith("> ")
                or s == "---"
                or re.match(r"^\d+\.\s", s)
                or s.startswith("<aside")
                or (s.startswith("**") and s.endswith("**") and "?" in s)
            ):
                break
            para.append(s)
            i += 1
        out.append(f"<p>{md_inline(' '.join(para))}</p>")

    return "\n".join(out), i


def extract_faq_from_s8(lines: list[str], start: int) -> tuple[list[tuple[str, str]], int]:
    items: list[tuple[str, str]] = []
    i = start
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith("## ") or stripped == "---":
            if stripped == "---":
                i += 1
            break
        if stripped.startswith("### FAQ"):
            i += 1
            continue
        if stripped.startswith("**") and stripped.endswith("**"):
            q = stripped.strip("*").strip()
            i += 1
            ans = []
            while i < len(lines):
                s = lines[i].strip()
                if s == "---":
                    break
                if s.startswith("**") and s.endswith("**") and "?" in s:
                    break
                if s.startswith("## "):
                    break
                if s:
                    ans.append(s)
                i += 1
            items.append((q, " ".join(ans)))
            continue
        i += 1
    return items, i


def parse_tail(lines: list[str], start: int) -> str:
    out = []
    i = start
    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped:
            i += 1
            continue
        if stripped.startswith("|"):
            tbl_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl_lines.append(lines[i])
                i += 1
            out.append(parse_table(tbl_lines))
            continue
        if stripped.startswith("<aside"):
            block = [lines[i]]
            i += 1
            while i < len(lines):
                block.append(lines[i])
                if "</aside>" in lines[i]:
                    i += 1
                    break
                i += 1
            out.append("\n".join(block))
            continue
        if stripped == "---":
            i += 1
            continue
        para = [stripped]
        i += 1
        while i < len(lines):
            s = lines[i].strip()
            if not s or s.startswith("|") or s.startswith("<aside") or s == "---":
                break
            para.append(s)
            i += 1
        out.append(f"<p>{md_inline(' '.join(para))}</p>")
    return "\n".join(out)


def build_faq_section(items: list[tuple[str, str]]) -> str:
    blocks = []
    for q, a in items:
        blocks.append(
            f"""  <div class="l24-faq__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 class="l24-faq__q" itemprop="name">{md_inline(q)}</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p class="l24-faq__a" itemprop="text">{md_inline(a)}</p>
    </div>
  </div>"""
        )
    return f"""<section id="faq" class="ym-section l24-faq" itemscope itemtype="https://schema.org/FAQPage" aria-label="Частые вопросы">
  <h2 id="faq-h">FAQ: возражение, аннулирование и лицензия «Союзмультфильма»</h2>
{chr(10).join(blocks)}
</section>"""


def md_to_sections(md: str, boris_html: str) -> tuple[str, list[tuple[str, str]], str]:
    lines = md.split("\n")
    sections: list[str] = []
    faq_items: list[tuple[str, str]] = []
    tail_html = ""
    boris_inserted = False
    i = 0

    while i < len(lines) and not lines[i].strip().startswith("## "):
        i += 1

    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped.startswith("## "):
            i += 1
            continue
        title = stripped[3:].strip()
        hid = H2_IDS.get(title)
        if not hid:
            i += 1
            continue
        i += 1

        if hid == "s8-sip":
            content, i = parse_block(lines, i, stop_at_faq=True)
            faq_items, i = extract_faq_from_s8(lines, i)
            section = (
                f'<section class="ym-section" id="{hid}" aria-labelledby="{hid}-h">\n'
                f'<h2 id="{hid}-h">{md_inline(title)}</h2>\n{content}\n</section>'
            )
            sections.append(section)
            tail_html = parse_tail(lines, i)
            break

        content, i = parse_block(lines, i)
        section = (
            f'<section class="ym-section" id="{hid}" aria-labelledby="{hid}-h">\n'
            f'<h2 id="{hid}-h">{md_inline(title)}</h2>\n{content}\n</section>'
        )
        sections.append(section)

        if hid == "s2-fabula" and not boris_inserted:
            sections.append(boris_html)
            boris_inserted = True

    if not boris_inserted:
        raise ValueError("Boris block was not inserted after section 2")

    return "\n\n".join(sections), faq_items, tail_html


def parse_intro_paragraphs(md: str) -> list[str]:
    paras = []
    for line in md.split("\n"):
        if line.strip().startswith("## "):
            break
        if line.strip() and not line.strip().startswith("#"):
            paras.append(line.strip())
    return paras[:3]


def build_intro(paras: list[str]) -> str:
    p_html = "\n".join(f"      <p>{md_inline(p)}</p>" for p in paras[:2])
    if len(paras) > 2:
        p_html += f"\n      <p>{md_inline(paras[2])}</p>"
    return f"""
<section class="l24-intro-ip" aria-label="Введение">
  <div class="l24-intro-ip__grid">
    <div class="l24-intro-ip__text">
{p_html}
    </div>
    <aside class="l24-intro-ip__decor" aria-label="Ключевые факты дела «Маугли»">
      <ul class="l24-intro-ip__chips">
        <li class="l24-intro-ip__chip l24-intro-ip__chip--ip">IP · Роспатент</li>
        <li class="l24-intro-ip__chip l24-intro-ip__chip--law">п. 9 ст. 1483</li>
        <li class="l24-intro-ip__chip">№ 162034</li>
        <li class="l24-intro-ip__chip">класс 30</li>
        <li class="l24-intro-ip__chip l24-intro-ip__chip--brand">Союзмультфильм</li>
        <li class="l24-intro-ip__chip l24-intro-ip__chip--candy">Рот Фронт</li>
        <li class="l24-intro-ip__chip l24-intro-ip__chip--ok">24.08.2026</li>
      </ul>
      <svg class="l24-intro-ip__route-svg" viewBox="0 0 360 88" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Маршрут: возражение Союзмультфильма → ППС → аннулирование ТЗ «МАУГЛИ ДРАЖЕ»">
        <rect x="4" y="20" width="100" height="48" rx="8" fill="#ecfdf5" stroke="#166534" stroke-width="1.2"/>
        <text x="54" y="42" text-anchor="middle" fill="#166534" font-size="6" font-weight="800">ВОЗРАЖЕНИЕ</text>
        <text x="54" y="56" text-anchor="middle" fill="#64748b" font-size="5.5">30.12.2025</text>
        <line x1="106" y1="44" x2="130" y2="44" stroke="#166534" stroke-width="1.5"/>
        <polygon points="130,44 124,41 124,47" fill="#166534"/>
        <rect x="134" y="20" width="92" height="48" rx="8" fill="#fffbeb" stroke="#ca8a04" stroke-width="1.2"/>
        <text x="180" y="42" text-anchor="middle" fill="#92400e" font-size="6" font-weight="800">ППС</text>
        <text x="180" y="56" text-anchor="middle" fill="#64748b" font-size="5.5">15.05.2026</text>
        <line x1="228" y1="44" x2="252" y2="44" stroke="#166534" stroke-width="1.5"/>
        <polygon points="252,44 246,41 246,47" fill="#166534"/>
        <rect x="256" y="14" width="100" height="60" rx="8" fill="#166534" stroke="#14532d" stroke-width="1.2"/>
        <text x="306" y="36" text-anchor="middle" fill="#ecfdf5" font-size="6" font-weight="800">АННУЛИРОВАНО</text>
        <text x="306" y="50" text-anchor="middle" fill="#bbf7d0" font-size="5.5">№ 162034</text>
        <text x="306" y="62" text-anchor="middle" fill="#bbf7d0" font-size="5.5">24.08.2026</text>
        <text x="180" y="12" text-anchor="middle" fill="#64748b" font-size="5.5" font-weight="600">ТЗ + авторское право на персонаж</text>
      </svg>
    </aside>
  </div>
</section>
"""


def build_toc() -> str:
    lis = "\n".join(f'    <li><a href="#{a}">{t}</a></li>' for a, t in TOC_LABELS)
    return f"""
<nav class="ym-toc" aria-label="Содержание статьи">
  <p class="ym-toc__title">Содержание</p>
  <ul class="ym-toc__list">
{lis}
  </ul>
</nav>
"""


def build_brief(md: str) -> str:
    return (
        '<p class="l24-brief"><strong>Кратко:</strong> 24 августа 2026 года Роспатент '
        '<strong>аннулировал</strong> комбинированный ТЗ <strong>«МАУГЛИ ДРАЖЕ»</strong> '
        '(свидетельство <strong>№ 162034</strong>, приоритет <strong>30.01.1996</strong>, класс <strong>30</strong>) '
        'по возражению <strong>«Союзмультфильма»</strong> — <strong>п. 9 ст. 1483 ГК РФ</strong>, '
        'персонаж без согласия. Ниже — фабула, процедура возражения, пересечение ТЗ и АП, '
        'параллель с иском за Волка на дыне и практические шаги защиты бренда.</p>'
    )


def plain_text(s: str) -> str:
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip()


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
                "datePublished": "2026-08-26",
                "dateModified": "2026-08-26",
                "author": {"@type": "Organization", "name": "Legis24"},
                "publisher": {"@type": "Organization", "name": "Legis24"},
                "inLanguage": "ru-RU",
            },
            {"@type": "FAQPage", "mainEntity": faq_entities},
        ],
    }
    return (
        '<pre class="l24-jsonld-maugli" aria-hidden="true" hidden>'
        + json.dumps(graph, ensure_ascii=False)
        + "</pre>"
    )


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
  margin-top: 0; color: #166534; font-size: 1.45rem; font-weight: 800;
}}
.{p} .ym-section + .ym-section h2,
.{p} #boris-maugli-tz-flow + .ym-section h2 {{
  margin-top: 2.5em;
}}
.{p} h3 {{ margin-top: 1.5em; color: #15803d; font-size: 1.15rem; font-weight: 700; }}
.{p} a {{ color: #166534; }}
.{p} p {{ margin: 0 0 1.1em; }}
.{p} ol, .{p} ul {{ margin: 1em 0; padding-left: 1.4em; }}
.{p} li {{ margin-bottom: 0.45em; }}
.{p} blockquote {{
  margin: 1.25em 0; padding: 14px 18px; border-left: 4px solid #86efac;
  background: #f0fdf4; color: #334155; border-radius: 0 8px 8px 0;
}}
.l24-tbl-wrap {{ overflow-x: auto; margin: 1.25em 0; }}
.l24-tbl {{ width: 100%; border-collapse: collapse; font-size: 0.95rem; }}
.l24-tbl th {{ background: #ecfdf5; color: #166534; font-weight: 700; padding: 10px 12px; border: 1px solid #bbf7d0; text-align: left; }}
.l24-tbl td {{ padding: 9px 12px; border: 1px solid #e2e8f0; vertical-align: top; }}
.l24-tbl tr:nth-child(even) td {{ background: #f8fafc; }}
.l24-checklist {{ list-style: none; padding-left: 0 !important; }}
.l24-checklist li {{
  position: relative; padding-left: 1.6em; margin-bottom: 0.55em;
}}
.l24-checklist li::before {{
  content: "☐"; position: absolute; left: 0; color: #166534; font-weight: 700;
}}
.l24-brief {{
  background: #f0fdf4; border-left: 4px solid #166534;
  padding: 16px 18px; border-radius: 0 8px 8px 0; margin-bottom: 1.5em;
}}
.l24-intro-ip {{
  max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.l24-intro-ip__grid {{
  display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
  gap: 28px; align-items: start;
}}
.l24-intro-ip__text {{
  border-left: 4px solid #166534; padding: 4px 0 4px 22px; text-align: left;
}}
.l24-intro-ip__text p {{
  margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155;
}}
.l24-intro-ip__decor {{
  background: linear-gradient(160deg, #ecfdf5 0%, #fff 100%);
  border: 1px solid #bbf7d0; border-radius: 12px; padding: 18px;
}}
.l24-intro-ip__chips {{
  display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none;
}}
.l24-intro-ip__chip {{
  font-size: 0.72rem; font-weight: 700; padding: 6px 10px; border-radius: 999px;
  background: #fff; border: 1px solid #cbd5e1; color: #475569;
}}
.l24-intro-ip__chip--ip {{ border-color: #166534; color: #166534; background: #f0fdf4; }}
.l24-intro-ip__chip--law {{ border-color: #7c3aed; color: #5b21b6; background: #faf5ff; }}
.l24-intro-ip__chip--brand {{ border-color: #fda4af; color: #be123c; background: #fff1f2; }}
.l24-intro-ip__chip--candy {{ border-color: #fcd34d; color: #92400e; background: #fffbeb; }}
.l24-intro-ip__chip--ok {{ border-color: #22c55e; color: #15803d; background: #ecfdf5; }}
.l24-intro-ip__route-svg {{ display: block; width: 100%; height: auto; }}
.ym-toc {{
  max-width: 820px; margin: 24px auto 0; padding: 0 24px 32px;
  text-align: center; font-family: system-ui, sans-serif;
}}
.ym-toc__title {{
  font-size: 0.8rem; font-weight: 700; letter-spacing: 0.06em;
  text-transform: uppercase; color: #64748b; margin: 0 0 12px;
}}
.ym-toc__list {{
  list-style: none; padding: 0; margin: 0;
  display: flex; flex-wrap: wrap; justify-content: center; gap: 8px 10px;
}}
.ym-toc__list a {{
  display: inline-block; padding: 8px 12px; border-radius: 8px;
  background: #f0fdf4; color: #166534; text-decoration: none;
  font-size: 0.88rem; font-weight: 600; border: 1px solid #bbf7d0;
}}
.ym-toc__list a:hover {{ background: #dcfce7; }}
.ym-cta {{
  margin: 28px 0; padding: 22px 24px; border-radius: 10px;
  background: linear-gradient(135deg, #f0fdf4 0%, #fffbeb 100%);
  border: 1px solid #bbf7d0; border-left: 4px solid #166534;
}}
.ym-cta--legis24.ym-cta--bottom {{
  border-left-color: #15803d;
  background: linear-gradient(135deg, #ecfdf5 0%, #f0fdf4 100%);
  border-color: #86efac;
}}
.ym-cta__text {{ margin: 0 0 14px; line-height: 1.55; color: #334155; font-size: 0.98rem; }}
.ym-cta__actions {{ margin: 0; }}
.ym-cta__btn {{
  display: inline-block; background: #166534; color: #fff !important;
  padding: 12px 22px; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 0.93rem;
}}
.ym-cta__btn:hover {{ background: #14532d; }}
.l24-faq {{
  margin-top: 2.5em; padding: 28px 24px; background: #f0fdf4;
  border: 1px solid #bbf7d0; border-radius: 12px;
}}
.l24-faq > h2 {{ margin-top: 0 !important; }}
.l24-faq__item {{ margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #bbf7d0; }}
.l24-faq__item:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
.l24-faq__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #166534; font-weight: 700; }}
.l24-faq__a {{ margin: 0; color: #334155; font-size: 0.97rem; line-height: 1.6; }}
.l24-jsonld-maugli {{ display: none !important; }}
#boris-maugli-tz-flow {{ max-width: 820px; margin: 2.5em auto; padding: 0 24px; }}
@media (max-width: 900px) {{ .l24-intro-ip__grid {{ grid-template-columns: 1fr; }} }}
"""


def patch_hero_cta(hero: str) -> str:
    return re.sub(
        r'(<a[^>]+href="https://advokat-vsem\.ru/")(?![^>]*target=)',
        r'\1 target="_blank" rel="noopener noreferrer"',
        hero,
    )


def main():
    handoff = HANDOFF.read_text(encoding="utf-8")
    hero = strip_scripts_canvas(patch_hero_cta(extract_hero(handoff)))
    boris = strip_scripts_canvas(extract_boris(handoff))
    artur_md = extract_artur_body(handoff)
    intro_paras = parse_intro_paragraphs(artur_md)
    sections_html, faq_items, tail_html = md_to_sections(artur_md, boris)
    faq_html = build_faq_section(faq_items)
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

{build_intro(intro_paras)}

{build_toc()}

<div class="l24-longread-wrap" itemprop="articleBody">

{build_brief(artur_md)}

{sections_html}

{faq_html}

<section class="ym-section" id="istochniki" aria-labelledby="istochniki-h">
<h2 id="istochniki-h">Источники и выводы</h2>
{tail_html}
</section>

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
FAQ: microdata FAQPage на секции #faq + hidden JSON-LD для Rank Math
ВНИМАНИЕ: MCP-only — без `<script>` и `<canvas>`; hero Алины и блок Бориса — static SVG + inline CSS. При публикации обернуть в <!-- wp:html -->

{html}

## Передача Юре
SLUG: {SLUG}
Title: {TITLE}
Description: {DESCRIPTION}
Контент MCP-only: hero static SVG, блок Бориса `#boris-maugli-tz-flow`, FAQ microdata. Обязательно обернуть в <!-- wp:html --> при публикации. Юра удаляет `<script>` перед blob — в HTML их нет.
Размер HTML: {char_count} символов
main#primary: да (`class="site-main {PAGE_CLASS}"`)
breadcrumbs: скрыты CSS
CTA: только https://advokat-vsem.ru/
"""

    if "=== НАТАША (HTML СТРАНИЦЫ) ===" in handoff:
        handoff = handoff.split("=== НАТАША (HTML СТРАНИЦЫ) ===")[0].rstrip() + "\n\n" + natasha_block
    else:
        handoff = handoff.rstrip() + "\n\n" + natasha_block
    HANDOFF.write_text(handoff, encoding="utf-8")

    assert 'id="primary"' in html
    assert "boris-maugli-tz-flow" in html
    assert "l24-hero-rospatent-maugli" in html
    assert "<script" not in html.lower()
    assert "<canvas" not in html.lower()

    print(f"Wrote {OUT}")
    print(f"Chars: {char_count}")
    print(f"SLUG: {SLUG}")


if __name__ == "__main__":
    main()
