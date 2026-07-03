#!/usr/bin/env python3
"""Build full Legis24 HTML page for SIP Fanta vs Rospatent article."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

SLUG = "sip-fanta-rospatent-obshcheizvestnyy-tovarnyy-znak-2026"
PAGE_CLASS = f"{SLUG}-page"
ARTICLE = Path("/workspace/.cursor/zhenya-fanta-article-body.md")
OUT = Path(f"/workspace/.cursor/page-content-natasha-{SLUG}.html")

TITLE = "Coca-Cola vs Роспатент: иск о признании Fanta общеизвестным товарным знаком"
DESCRIPTION = (
    "Отказ Роспатента в марте 2026 и заседание СИП 20.07.2026: как Coca-Cola оспаривает "
    "решение по Fanta и Sprite, что даёт статус общеизвестного товарного знака и как "
    "доказать известность бренда."
)
H1 = "Coca-Cola vs Роспатент: иск о признании Fanta общеизвестным товарным знаком в России"
SUB = (
    "Отказ ведомства в марте 2026 и заседание СИП 20.07.2026 — как оспорить отказ "
    "и доказать известность бренда"
)
CTA = "Консультация по защите товарного знака"


def md_to_html(md: str) -> tuple[str, list[tuple[str, str]]]:
    """Convert markdown body to HTML sections; return (html, toc_items)."""
    lines = md.strip().split("\n")
    parts: list[str] = []
    toc: list[tuple[str, str]] = []
    in_table = False
    table_rows: list[str] = []
    buf: list[str] = []
    section_open = False
    sec_id = 0

    def flush_para() -> None:
        nonlocal buf
        if buf:
            text = " ".join(buf).strip()
            if text:
                parts.append(f"<p>{inline(text)}</p>")
            buf = []

    def inline(s: str) -> str:
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        return s

    def close_table() -> None:
        nonlocal in_table, table_rows
        if in_table and table_rows:
            parts.append("<table><tbody>" + "".join(table_rows) + "</tbody></table>")
            table_rows = []
            in_table = False

    for line in lines:
        if line.startswith("---"):
            continue
        if line.startswith("|") and "|" in line[1:]:
            flush_para()
            if re.match(r"^\|[-| ]+\|$", line):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if not in_table:
                in_table = True
            tag = "th" if not table_rows else "td"
            table_rows.append(
                "<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells) + "</tr>"
            )
            continue
        close_table()

        if line.startswith("### "):
            flush_para()
            parts.append(f"<h3>{inline(line[4:])}</h3>")
            continue
        if line.startswith("## "):
            flush_para()
            if section_open:
                parts.append("</section>")
            sec_id += 1
            title = line[3:].strip()
            if title.upper() == "FAQ":
                anchor = "faq"
            elif title.startswith("Источники"):
                anchor = "istochniki"
            else:
                anchor = f"s{sec_id}"
            toc.append((anchor, title))
            parts.append(f'<section class="ym-section" id="{anchor}">')
            parts.append(f"<h2>{inline(title)}</h2>")
            section_open = True
            continue

        if line.startswith("**Кратко:**"):
            flush_para()
            parts.append(f'<p class="l24-brief">{inline(line)}</p>')
            continue

        if line.strip() == "":
            flush_para()
            continue

        if line.startswith("- "):
            flush_para()
            items = [line[2:]]
            while lines and lines[0].startswith("- "):
                items.append(lines.pop(0)[2:])
            parts.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>")
            continue

        if re.match(r"^\d+\.\s", line):
            flush_para()
            items = [re.sub(r"^\d+\.\s*", "", line)]
            while lines and re.match(r"^\d+\.\s", lines[0]):
                items.append(re.sub(r"^\d+\.\s*", "", lines.pop(0)))
            parts.append("<ol>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ol>")
            continue

        buf.append(line)

    flush_para()
    close_table()
    if section_open:
        parts.append("</section>")

    # FAQ styling wrapper
    body = "\n".join(parts)
    body = body.replace(
        '<section class="ym-section" id="faq">',
        '<section class="ym-section l24-faq" id="faq">',
    )
    body = re.sub(
        r"(<h3>(.+?)</h3>)\s*<p>",
        r'<div class="l24-faq__item"><p class="l24-faq__q">\2</p><p class="l24-faq__a">',
        body,
    )
    # close faq items before next h3 or end
    body = body.replace("</p>\n<h3>", '</p></div>\n<h3>')
    if "l24-faq" in body and not body.rstrip().endswith("</div>"):
        body = body.rstrip() + "</div>"

    return body, toc


def hero_svg() -> str:
    return """<svg viewBox="0 0 520 440" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:520px" role="img" aria-label="Coca-Cola vs Роспатент: спор об общеизвестном товарном знаке Fanta — СИП, заседание 20.07.2026">
  <defs>
    <linearGradient id="hf-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fff7ed"/><stop offset="50%" stop-color="#fff"/><stop offset="100%" stop-color="#eff6ff"/>
    </linearGradient>
    <linearGradient id="hf-fanta" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fb923c"/><stop offset="100%" stop-color="#ea580c"/>
    </linearGradient>
    <linearGradient id="hf-sip" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/><stop offset="100%" stop-color="#5b21b6"/>
    </linearGradient>
    <linearGradient id="hf-rosp" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2563eb"/><stop offset="100%" stop-color="#1e3a5f"/>
    </linearGradient>
    <filter id="hf-sh"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#1e3a5f" flood-opacity="0.12"/></filter>
  </defs>
  <rect x="10" y="12" width="500" height="416" rx="16" fill="url(#hf-bg)" stroke="#fed7aa" stroke-width="1.2"/>
  <g filter="url(#hf-sh)" transform="translate(148,14)">
    <rect x="0" y="32" width="224" height="48" rx="4" fill="url(#hf-sip)"/>
    <polygon points="112,2 224,32 0,32" fill="#6d28d9"/>
    <text x="112" y="48" text-anchor="middle" fill="#ede9fe" font-size="6.5" font-weight="800">СУД ПО ИНТЕЛЛЕКТУАЛЬНЫМ ПРАВАМ</text>
    <text x="112" y="62" text-anchor="middle" fill="#c4b5fd" font-size="5.5">заседание 20.07.2026</text>
    <text x="112" y="74" text-anchor="middle" fill="#ddd6fe" font-size="5">Fanta + Sprite · общеизвестный ТЗ</text>
  </g>
  <g filter="url(#hf-sh)" transform="translate(24,88)">
    <rect width="120" height="70" rx="8" fill="#fff" stroke="#ea580c" stroke-width="1.4"/>
    <text x="60" y="16" text-anchor="middle" fill="#c2410c" font-size="5.5" font-weight="800">COCA-COLA</text>
    <circle cx="60" cy="42" r="22" fill="url(#hf-fanta)" opacity="0.9"/>
    <text x="60" y="46" text-anchor="middle" fill="#fff" font-size="11" font-weight="900">F</text>
    <text x="60" y="64" text-anchor="middle" fill="#ea580c" font-size="5" font-weight="700">с 1966 · СССР</text>
  </g>
  <g filter="url(#hf-sh)" transform="translate(376,88)">
    <rect width="120" height="70" rx="8" fill="#fff" stroke="#1e3a5f" stroke-width="1.4"/>
    <text x="60" y="16" text-anchor="middle" fill="#1e3a5f" font-size="5.5" font-weight="800">РОСПАТЕНТ</text>
    <rect x="20" y="28" width="80" height="32" rx="4" fill="#eff6ff" stroke="#93c5fd"/>
    <text x="60" y="42" text-anchor="middle" fill="#dc2626" font-size="7" font-weight="900">ОТКАЗ</text>
    <text x="60" y="54" text-anchor="middle" fill="#64748b" font-size="4.5">март 2026</text>
    <text x="60" y="64" text-anchor="middle" fill="#94a3b8" font-size="4.5">продажи ↓ · узкий сегмент</text>
  </g>
  <path d="M144 123 Q260 100 376 123" fill="none" stroke="#7c3aed" stroke-width="2" marker-end="url(#hf-arr)"/>
  <text x="260" y="108" text-anchor="middle" fill="#5b21b6" font-size="5.5" font-weight="700">иск · оспаривание отказа</text>
  <g filter="url(#hf-sh)" transform="translate(168,148)">
    <rect width="184" height="56" rx="8" fill="#fff" stroke="#7c3aed" stroke-width="1.2"/>
    <text x="92" y="18" text-anchor="middle" fill="#5b21b6" font-size="6" font-weight="800">ст. 1508 ГК РФ</text>
    <text x="92" y="32" text-anchor="middle" fill="#334155" font-size="5">общеизвестный товарный знак</text>
    <text x="92" y="46" text-anchor="middle" fill="#059669" font-size="5" font-weight="600">бессрочно · без продления</text>
  </g>
  <g filter="url(#hf-sh)" transform="translate(40,220)">
    <rect width="100" height="48" rx="6" fill="#ecfdf5" stroke="#059669"/>
    <text x="50" y="18" text-anchor="middle" fill="#047857" font-size="5" font-weight="700">СИП-506/2025</text>
    <text x="50" y="30" text-anchor="middle" fill="#334155" font-size="4.5">Савушкин</text>
    <text x="50" y="42" text-anchor="middle" fill="#059669" font-size="4.5">прецедент ✓</text>
  </g>
  <g filter="url(#hf-sh)" transform="translate(380,220)">
    <rect width="100" height="48" rx="6" fill="#ecfdf5" stroke="#059669"/>
    <text x="50" y="18" text-anchor="middle" fill="#047857" font-size="5" font-weight="700">СИП-1243/2024</text>
    <text x="50" y="30" text-anchor="middle" fill="#334155" font-size="4.5">соцопрос</text>
    <text x="50" y="42" text-anchor="middle" fill="#059669" font-size="4.5">известность ✓</text>
  </g>
  <g filter="url(#hf-sh)" transform="translate(148,280)">
    <rect width="224" height="64" rx="8" fill="#fff" stroke="#ea580c" stroke-width="1.2"/>
    <text x="112" y="18" text-anchor="middle" fill="#c2410c" font-size="5.5" font-weight="800">FANTA + SPRITE</text>
    <rect x="24" y="28" width="72" height="28" rx="6" fill="url(#hf-fanta)"/>
    <text x="60" y="46" text-anchor="middle" fill="#fff" font-size="8" font-weight="900">Fanta</text>
    <rect x="128" y="28" width="72" height="28" rx="6" fill="#22c55e"/>
    <text x="164" y="46" text-anchor="middle" fill="#fff" font-size="7" font-weight="900">Sprite</text>
    <text x="112" y="62" text-anchor="middle" fill="#64748b" font-size="4.5">параллельные заявки · апрель 2025</text>
  </g>
  <text x="260" y="368" text-anchor="middle" fill="#64748b" font-size="5">дата общеизвестности: 01.01.2020</text>
  <text x="260" y="382" text-anchor="middle" fill="#94a3b8" font-size="4.5">защита товарного знака · IP · Legis24</text>
</svg>"""


def boris_block() -> str:
    return f"""<section class="ym-section l24-boris-{SLUG}" id="l24-boris-{SLUG}" aria-label="Схема: путь к статусу общеизвестного товарного знака">
<style>
.l24-boris-{SLUG} {{ max-width: 1200px; margin: 2.5em auto; padding: 0 24px; font-family: system-ui, sans-serif; }}
.l24-boris-{SLUG}__grid {{ display: grid; grid-template-columns: 1fr 1.2fr; gap: 24px; align-items: center; }}
.l24-boris-{SLUG}__card {{ background: #faf5ff; border: 1px solid #ddd6fe; border-radius: 12px; padding: 20px; }}
.l24-boris-{SLUG}__card h3 {{ margin: 0 0 12px; color: #5b21b6; font-size: 1.1rem; }}
.l24-boris-{SLUG}__steps {{ list-style: none; padding: 0; margin: 0; }}
.l24-boris-{SLUG}__steps li {{ padding: 10px 12px; margin-bottom: 8px; background: #fff; border-radius: 8px; border-left: 3px solid #7c3aed; font-size: 0.92rem; color: #334155; }}
@media (max-width: 800px) {{ .l24-boris-{SLUG}__grid {{ grid-template-columns: 1fr; }} }}
</style>
<div class="l24-boris-{SLUG}__grid">
  <div class="l24-boris-{SLUG}__card">
    <h3>Маршрут правообладателя при отказе Роспатента</h3>
    <ol class="l24-boris-{SLUG}__steps">
      <li><strong>Заявка</strong> о признании общеизвестным (ст. 1508 ГК РФ)</li>
      <li><strong>Отказ</strong> ведомства → пакет доказательств</li>
      <li><strong>Иск в СИП</strong> об оспаривании отказа</li>
      <li><strong>Соцопрос + продажи + реклама</strong> на дату 01.01.2020</li>
      <li><strong>Внесение</strong> в перечень общеизвестных ТЗ</li>
    </ol>
  </div>
  <svg viewBox="0 0 480 280" xmlns="http://www.w3.org/2000/svg" width="100%" role="img" aria-label="Схема признания общеизвестного товарного знака: заявка, отказ Роспатента, СИП, доказательства, реестр">
    <rect width="480" height="280" rx="12" fill="#faf5ff" stroke="#ddd6fe"/>
    <rect x="20" y="100" width="80" height="44" rx="6" fill="#fff" stroke="#7c3aed"/><text x="60" y="126" text-anchor="middle" fill="#5b21b6" font-size="6" font-weight="700">Заявка</text>
    <path d="M100 122 H140" stroke="#7c3aed" stroke-width="2"/><polygon points="140,122 132,118 132,126" fill="#7c3aed"/>
    <rect x="140" y="100" width="80" height="44" rx="6" fill="#fef2f2" stroke="#dc2626"/><text x="180" y="120" text-anchor="middle" fill="#dc2626" font-size="5.5" font-weight="700">Отказ</text><text x="180" y="132" text-anchor="middle" fill="#64748b" font-size="4.5">март 2026</text>
    <path d="M220 122 H260" stroke="#7c3aed" stroke-width="2"/><polygon points="260,122 252,118 252,126" fill="#7c3aed"/>
    <rect x="260" y="88" width="90" height="68" rx="6" fill="#ede9fe" stroke="#6d28d9"/><text x="305" y="114" text-anchor="middle" fill="#5b21b6" font-size="5.5" font-weight="800">СИП</text><text x="305" y="128" text-anchor="middle" fill="#7c3aed" font-size="4.5">20.07.2026</text><text x="305" y="142" text-anchor="middle" fill="#64748b" font-size="4">Fanta · Sprite</text>
    <path d="M350 122 H390" stroke="#7c3aed" stroke-width="2"/><polygon points="390,122 382,118 382,126" fill="#7c3aed"/>
    <rect x="390" y="100" width="70" height="44" rx="6" fill="#ecfdf5" stroke="#059669"/><text x="425" y="126" text-anchor="middle" fill="#047857" font-size="5.5" font-weight="700">Реестр</text>
    <text x="240" y="200" text-anchor="middle" fill="#334155" font-size="6" font-weight="600">Доказательства: соцопрос · продажи · реклама · СМИ</text>
    <rect x="60" y="220" width="360" height="40" rx="6" fill="#fff" stroke="#c4b5fd"/><text x="240" y="244" text-anchor="middle" fill="#5b21b6" font-size="5.5">ст. 1508 ГК РФ — бессрочная охрана общеизвестного знака</text>
  </svg>
</div>
</section>"""


def cta_block(text: str) -> str:
    return f"""<div class="ym-cta">
  <p class="ym-cta__text">{html.escape(text)}</p>
  <p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">{html.escape(CTA)}</a></p>
</div>"""


def build() -> str:
    md = ARTICLE.read_text(encoding="utf-8")
    body_html, toc = md_to_html(md)

    # Insert Boris after 2nd section
    sections = body_html.split('<section class="ym-section"')
    if len(sections) > 3:
        body_html = (
            sections[0]
            + '<section class="ym-section"'
            + sections[1]
            + '<section class="ym-section"'
            + sections[2]
            + boris_block()
            + '<section class="ym-section"'
            + '<section class="ym-section"'.join(sections[3:])
        )

    # Insert CTA after intro (before first H2 content area) and mid-article
    body_html = body_html.replace(
        "</section>",
        cta_block(
            "Спор Coca-Cola с Роспатентом показывает: даже легендарный бренд не получает статус "
            "общеизвестного знака автоматически. Нужна стратегия доказывания и готовность к суду в СИП."
        )
        + "\n</section>",
        1,
    )

    toc_html = "".join(
        f'<li><a href="#{a}">{html.escape(t)}</a></li>' for a, t in toc if t.upper() != "ИСТОЧНИКИ"
    )

    hero_id = f"l24-hero-{SLUG}"
    page = f"""<!-- wp:html -->
<style>
.breadcrumbs, .breadcrumb, .rank-math-breadcrumb, .yoast-breadcrumb,
.entry-header, .page-title-section {{ display: none !important; }}
#primary, .site-main, .site-content, #content, .content-area {{
  padding-top: 0 !important; margin-top: 0 !important;
}}
#sidebar, .sidebar, #secondary {{ display: none !important; }}
.{PAGE_CLASS} .entry-content {{ max-width: none !important; width: 100% !important; padding: 0 !important; }}
.{PAGE_CLASS} .l24-longread-wrap {{
  max-width: 820px; margin: 0 auto; padding: 48px 24px 80px;
  font-size: 1.05rem; line-height: 1.65; color: #1a202c;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.{PAGE_CLASS} .ym-section h2 {{ margin-top: 0; color: #5b21b6; font-size: 1.45rem; font-weight: 800; }}
.{PAGE_CLASS} .ym-section + .ym-section h2 {{ margin-top: 2.5em; }}
.{PAGE_CLASS} h3 {{ margin-top: 1.5em; color: #7c3aed; font-size: 1.15rem; font-weight: 700; }}
.{PAGE_CLASS} a {{ color: #7c3aed; }}
.{PAGE_CLASS} p {{ margin: 0 0 1.1em; }}
.{PAGE_CLASS} table {{ width: 100%; border-collapse: collapse; margin: 1em 0; font-size: 0.95rem; }}
.{PAGE_CLASS} th, .{PAGE_CLASS} td {{ border: 1px solid #e2e8f0; padding: 10px 12px; text-align: left; }}
.{PAGE_CLASS} th {{ background: #faf5ff; color: #5b21b6; }}
.l24-intro-ip {{ max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px; font-family: system-ui, sans-serif; }}
.l24-intro-ip__grid {{ display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr); gap: 28px; }}
.l24-intro-ip__text {{ border-left: 4px solid #7c3aed; padding: 4px 0 4px 22px; text-align: left; }}
.l24-intro-ip__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.l24-intro-ip__decor {{ background: linear-gradient(160deg, #faf5ff 0%, #fff 100%); border: 1px solid #ddd6fe; border-radius: 12px; padding: 18px; }}
.l24-intro-ip__chips {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none; }}
.l24-intro-ip__chip {{ font-size: 0.72rem; font-weight: 700; padding: 6px 10px; border-radius: 999px; background: #fff; border: 1px solid #cbd5e1; color: #475569; }}
.l24-intro-ip__chip--ip {{ border-color: #7c3aed; color: #5b21b6; background: #faf5ff; }}
.l24-intro-ip__chip--sip {{ border-color: #ea580c; color: #c2410c; background: #fff7ed; }}
.ym-toc {{ max-width: 820px; margin: 24px auto 0; padding: 0 24px 32px; text-align: center; }}
.ym-toc__title {{ font-size: 0.8rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: #64748b; margin: 0 0 12px; }}
.ym-toc__list {{ list-style: none; padding: 0; margin: 0; display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; }}
.ym-toc__list a {{ display: inline-block; padding: 8px 12px; border-radius: 8px; background: #faf5ff; color: #5b21b6; text-decoration: none; font-size: 0.88rem; font-weight: 600; border: 1px solid #ddd6fe; }}
.ym-cta {{ margin: 28px 0; padding: 22px 24px; border-radius: 10px; background: linear-gradient(135deg, #faf5ff 0%, #fff7ed 100%); border: 1px solid #ddd6fe; border-left: 4px solid #7c3aed; }}
.ym-cta__btn {{ display: inline-block; background: #5b21b6; color: #fff !important; padding: 12px 22px; border-radius: 8px; font-weight: 700; text-decoration: none; }}
.l24-faq {{ margin-top: 2.5em; padding: 28px 24px; background: #faf5ff; border: 1px solid #ddd6fe; border-radius: 12px; }}
.l24-faq__q {{ margin: 0 0 8px; font-weight: 700; color: #5b21b6; }}
.l24-faq__a {{ margin: 0; color: #334155; }}
.l24-brief {{ background: #faf5ff; border-left: 4px solid #7c3aed; padding: 16px 18px; border-radius: 0 8px 8px 0; }}
.{hero_id} {{
  min-height: 88vh; display: flex; align-items: center; padding: 112px 24px 72px;
  background: linear-gradient(152deg, #fff 0%, #faf5ff 42%, #fff7ed 100%);
  font-family: system-ui, sans-serif; overflow: hidden;
}}
.{hero_id}__inner {{ max-width: 1200px; margin: 0 auto; width: 100%; display: grid; grid-template-columns: 1.04fr 0.96fr; gap: 44px; align-items: center; }}
.{hero_id}__badge {{ display: inline-flex; padding: 8px 14px; border-radius: 999px; background: #fff; border: 1px solid #ddd6fe; font-size: 0.78rem; font-weight: 600; color: #5b21b6; margin-bottom: 18px; }}
.{hero_id}__h1 {{ margin: 0 0 18px; font-size: clamp(1.32rem, 2.85vw, 2.08rem); line-height: 1.22; font-weight: 800; color: #0f172a; }}
.{hero_id}__sub {{ margin: 0 0 26px; color: #475569; font-size: 1.05rem; line-height: 1.58; }}
.{hero_id}__facts {{ display: flex; flex-wrap: wrap; gap: 10px; margin: 0 0 26px; padding: 0; list-style: none; }}
.{hero_id}__fact {{ font-size: 0.76rem; font-weight: 700; padding: 7px 12px; border-radius: 8px; background: #fff; border: 1px solid #e2e8f0; }}
.{hero_id}__cta {{ display: inline-block; background: #5b21b6; color: #fff !important; padding: 14px 28px; border-radius: 8px; font-weight: 700; text-decoration: none; }}
@media (max-width: 900px) {{ .{hero_id}__inner, .l24-intro-ip__grid {{ grid-template-columns: 1fr; }} }}
</style>
<main id="primary" class="site-main {PAGE_CLASS}" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">
<meta itemprop="headline" content="{html.escape(H1)}">
<meta itemprop="description" content="{html.escape(DESCRIPTION)}">

<section id="{hero_id}" class="{hero_id}" aria-label="{html.escape(H1)}">
  <div class="{hero_id}__inner">
    <div>
      <div class="{hero_id}__badge">IP · СИП · Fanta vs Роспатент · 20.07.2026</div>
      <h1 class="{hero_id}__h1">{html.escape(H1)}</h1>
      <p class="{hero_id}__sub">{html.escape(SUB)}</p>
      <ul class="{hero_id}__facts">
        <li class="{hero_id}__fact">отказ март 2026</li>
        <li class="{hero_id}__fact">ст. 1508 ГК РФ</li>
        <li class="{hero_id}__fact">Fanta с 1966</li>
        <li class="{hero_id}__fact">Sprite параллельно</li>
      </ul>
      <a class="{hero_id}__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">{html.escape(CTA)}</a>
    </div>
    <div aria-hidden="true">{hero_svg()}</div>
  </div>
</section>

<div class="l24-intro-ip">
  <div class="l24-intro-ip__grid">
    <div class="l24-intro-ip__text">
      <p>The Coca-Cola Company оспаривает в Суде по интеллектуальным правам отказ Роспатента признать <strong>Fanta</strong> и <strong>Sprite</strong> общеизвестными товарными знаками в России. Заседание назначено на <strong>20 июля 2026 года</strong>.</p>
      <p>Отказ ведомства в марте 2026 года опирается на снижение продаж и узкую ассоциацию брендов с лимонадами. Для правообладателей это прецедент: даже многолетняя регистрация не гарантирует статус общеизвестного знака без доказательств.</p>
    </div>
    <div class="l24-intro-ip__decor">
      <ul class="l24-intro-ip__chips">
        <li class="l24-intro-ip__chip l24-intro-ip__chip--ip">IP · товарный знак</li>
        <li class="l24-intro-ip__chip l24-intro-ip__chip--sip">СИП 20.07.2026</li>
        <li class="l24-intro-ip__chip">ст. 1508 ГК РФ</li>
        <li class="l24-intro-ip__chip">Fanta · Sprite</li>
        <li class="l24-intro-ip__chip">отказ Роспатента</li>
      </ul>
      <p style="margin:0;font-size:0.9rem;color:#475569;line-height:1.5">Общеизвестный товарный знак: бессрочная охрана, без продления, сохраняется при временном неиспользовании.</p>
    </div>
  </div>
</div>

<nav class="ym-toc" aria-label="Оглавление">
  <p class="ym-toc__title">Содержание</p>
  <ul class="ym-toc__list">{toc_html}</ul>
</nav>

<div class="l24-longread-wrap">
{body_html}
{cta_block("Нужна помощь с заявкой на общеизвестный товарный знак или оспариванием отказа Роспатента в СИП? Подготовим доказательственную базу и стратегию защиты бренда.")}
</div>

<script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": {json.dumps(H1, ensure_ascii=False)},
  "description": {json.dumps(DESCRIPTION, ensure_ascii=False)},
  "datePublished": "2026-07-03",
  "inLanguage": "ru-RU",
  "author": {{"@type": "Organization", "name": "Legis24"}}
}}</script>
</main>
<!-- /wp:html -->
"""
    return page


def main() -> None:
    html_out = build()
    OUT.write_text(html_out, encoding="utf-8")
    print(json.dumps({"path": str(OUT), "bytes": len(html_out), "slug": SLUG}, ensure_ascii=False))


if __name__ == "__main__":
    main()
