#!/usr/bin/env python3
"""Сборка page-content-natasha-B2.html — иск о защите ИС, план ответа."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HANDOFF = ROOT / "nero-network-handoff.md"
ALINA = ROOT / "nero-network-fragments/alina.md"
BORIS = ROOT / "nero-network-fragments/boris.md"
OUT = ROOT / "page-content-natasha-B2.html"
SLUG = "isk-o-zashchite-is-protiv-vas-plan-otveta"
PAGE_CLASS = f"{SLUG}-page"

TITLE = "Иск о защите ИС против вас: пошаговый план ответа — сроки, возражение, компенсация"
DESCRIPTION = (
    "Получили иск о защите интеллектуальной собственности или претензию по товарному знаку "
    "и авторским правам? Пошаговый план ответчика: сроки, возражение на иск, досудебный ответ, "
    "оспаривание компенсации. Консультация Legis24."
)

H2_IDS = {
    "Что означает иск о защите интеллектуальной собственности для ответчика": "ip-isk-smysl",
    "Пошаговый план: первые 7–14 дней после получения иска": "ip-isk-plan7",
    "Досудебный этап: ответ на претензию до суда": "ip-isk-dosud",
    "Ответ на иск и возражение на исковое заявление": "ip-isk-otvet",
    "Защита при иске о нарушении товарного знака": "ip-isk-tz",
    "Защита при иске о нарушении исключительных и авторских прав": "ip-isk-avtor",
    "Компенсация и взыскание: как снизить сумму требований": "ip-isk-comp",
    "Судебная защита и итог: решение суда и риски": "ip-isk-sud",
    "Дерево решений ответчика (2026)": "ip-isk-derevo",
    "Когда нужен юрист по интеллектуальной собственности": "ip-isk-yurist",
    "FAQ": "b2-faq",
}

TOC_LABELS = {
    "ip-isk-smysl": "Смысл иска для ответчика",
    "ip-isk-plan7": "План 7–14 дней",
    "ip-isk-dosud": "Претензия до суда",
    "ip-isk-otvet": "Отзыв и возражение",
    "l24-anchor-ip-decision-tree-2026": "Дерево решений 2026",
    "ip-isk-tz": "Товарный знак",
    "ip-isk-avtor": "Авторские права",
    "ip-isk-comp": "Компенсация",
    "ip-isk-sud": "Итог в суде",
    "ip-isk-yurist": "Когда нужен юрист",
    "b2-faq": "FAQ",
}

FAQ_ITEMS = [
    (
        "Что делать в первый день после получения иска?",
        "Зафиксировать дату, найти дело на kad.arbitr.ru, не уничтожать спорные материалы, проверить претензию (п. 5.1 ст. 1252).",
    ),
    (
        "Обязателен ли ответ на иск?",
        "Формально — отзыв в арбитраже (ст. 131 АПК); пропуск ведёт к риску решения без учёта ваших доводов и к расходам.",
    ),
    (
        "Можно ли снизить компенсацию ниже 10 000 ₽?",
        "В исключительных случаях — да, по линии КС № 28-П и разумности (Пленум № 10); для добросовестных «не знавших» — отдельный коридор 10 000–500 000 ₽ (п. 7 ст. 1252.1).",
    ),
    (
        "Нужна ли претензия перед иском о компенсации?",
        "Между ЮЛ/ИП в арбитраже — да, 30 дней (п. 5.1 ст. 1252), если истец требует убытки/компенсацию. На прекращение нарушения претензия не всегда нужна.",
    ),
    (
        "Чем отличается возражение от отзыва?",
        "В арбитраже используется термин отзыв на исковое заявление; в СОЮ — возражения (ст. 131 ГПК). Суть одна: ответ на иск по существу.",
    ),
    (
        "Работает ли защита «товар куплен у поставщика»?",
        "Для добросовестного оборота — да, в связке с доказательствами закупки и п. 7 ст. 1252.1; при контрафакте прекращение и изъятие всё равно возможны.",
    ),
    (
        "Куда обжаловать решение по ИС?",
        "В апелляцию (срок уточняйте в решении), касация по спецкатегории — СИП.",
    ),
]


def extract_artur_body(handoff: str) -> str:
    start = handoff.find("=== АРТУР (CTA И РЕКЛАМА) ===")
    if start < 0:
        raise ValueError("Artur block not found")
    end = handoff.find("=== АЛИНА (HERO) ===", start)
    block = handoff[start:end]
    m = re.search(r"### Полный текст\n", block)
    if not m:
        raise ValueError("Artur ### Полный текст not found")
    body = block[m.end() :]
    for stop in ("### Рекламные вставки", "## GEO-чеклист", "## Передача пайплайну"):
        if stop in body:
            body = body.split(stop)[0]
    body = body.strip()
    body = re.sub(r"^# .+\n\n", "", body, count=1)
    return body


def slugify_title(title: str) -> str:
    return H2_IDS.get(title.strip(), re.sub(r"[^a-z0-9]+", "-", title.lower())[:40].strip("-"))


def md_inline(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
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
        rows.append(cells)
    if len(rows) < 2:
        return ""
    html = ["<table>", "<thead><tr>"]
    for c in rows[0]:
        html.append(f"<th>{md_inline(c)}</th>")
    html.append("</tr></thead><tbody>")
    for row in rows[2:]:
        html.append("<tr>")
        for c in row:
            html.append(f"<td>{md_inline(c)}</td>")
        html.append("</tr>")
    html.append("</tbody></table>")
    return "".join(html)


def md_to_html(md: str) -> str:
    lines = md.split("\n")
    out: list[str] = []
    i = 0
    skip_intro = True

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if skip_intro and stripped.startswith("## "):
            skip_intro = False
        elif skip_intro:
            i += 1
            continue

        if stripped == "<!-- BORIS_ANCHOR -->":
            out.append(stripped)
            i += 1
            continue

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

        if stripped.startswith("<") and stripped.endswith(">"):
            out.append(line)
            i += 1
            continue

        if stripped.startswith("```"):
            block = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1
            out.append(
                '<pre class="l24-code-tree" aria-label="Схема решений">'
                + "\n".join(block)
                + "</pre>"
            )
            continue

        if stripped.startswith("## "):
            title = stripped[3:].strip()
            hid = slugify_title(title)
            if hid == "b2-faq":
                out.append(build_faq_section())
                while i < len(lines):
                    s = lines[i].strip()
                    if s.startswith("<aside"):
                        break
                    if s.startswith("## ") and "FAQ" not in s:
                        break
                    i += 1
                continue
            out.append(f'<h2 id="{hid}">{md_inline(title)}</h2>')
            i += 1
            continue

        if stripped.startswith("### "):
            out.append(f"<h3>{md_inline(stripped[4:].strip())}</h3>")
            i += 1
            continue

        if stripped.startswith("|"):
            tbl_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl_lines.append(lines[i])
                i += 1
            out.append(parse_table(tbl_lines))
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

        if stripped == "---":
            i += 1
            continue

        if not stripped:
            i += 1
            continue

        if stripped.startswith("["):
            out.append(f"<p>{md_inline(stripped)}</p>")
            i += 1
            continue

        out.append(f"<p>{md_inline(stripped)}</p>")
        i += 1

    return "\n\n".join(out)


def build_faq_section() -> str:
    items = []
    for q, a in FAQ_ITEMS:
        items.append(
            f"""  <div class="l24-faq-b2__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 class="l24-faq-b2__q" itemprop="name">{md_inline(q)}</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p class="l24-faq-b2__a" itemprop="text">{md_inline(a)}</p>
    </div>
  </div>"""
        )
    return (
        f'<section id="b2-faq" class="l24-faq-b2 ym-section" itemscope itemtype="https://schema.org/FAQPage" aria-label="Частые вопросы">\n'
        f"  <h2>Частые вопросы (FAQ)</h2>\n"
        + "\n".join(items)
        + "\n</section>"
    )


def build_jsonld_pre() -> str:
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": TITLE,
                "description": DESCRIPTION,
                "author": {"@type": "Organization", "name": "Legis24"},
                "publisher": {"@type": "Organization", "name": "Legis24"},
                "dateModified": "2026-05-28",
                "inLanguage": "ru-RU",
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a},
                    }
                    for q, a in FAQ_ITEMS
                ],
            },
        ],
    }
    payload = json.dumps(graph, ensure_ascii=False, separators=(",", ":"))
    return f'<pre class="l24-jsonld-b2" aria-hidden="true" hidden>{payload}</pre>'


def extract_boris_html() -> str:
    text = BORIS.read_text(encoding="utf-8")
    m = re.search(r"```html\n(.*?)```", text, re.DOTALL)
    if not m:
        raise ValueError("Boris html block not found")
    return m.group(1).strip()


def extract_hero_html() -> str:
    text = ALINA.read_text(encoding="utf-8")
    m = re.search(
        r'(<section id="l24-hero-ip-isk-otvet".*?</section>)',
        text,
        re.DOTALL,
    )
    if not m:
        raise ValueError("Hero section not found in alina.md")
    return m.group(1).strip()


def insert_boris(html: str, boris_html: str) -> str:
    anchor = "<!-- BORIS_ANCHOR -->"
    if anchor not in html:
        raise ValueError("BORIS_ANCHOR not found in longread")
    return html.replace(anchor, boris_html, 1)


PAGE_CSS = f"""
.breadcrumbs, .breadcrumb, .woocommerce-breadcrumb, .rank-math-breadcrumb, .yoast-breadcrumb,
.entry-header, .page-title-section,
.entry-title, h1.entry-title, .et_pb_title_container,
#main-content > .container > .et_pb_row:first-child h1 {{ display: none !important; visibility: hidden !important; height: 0 !important; overflow: hidden !important; margin: 0 !important; padding: 0 !important; }}
#primary, .site-main, .site-content, #content, .content-area {{
  padding-top: 0 !important; margin-top: 0 !important;
}}
#sidebar, .sidebar, #secondary, .et_pb_column_1_4 {{ display: none !important; }}
.{PAGE_CLASS} .entry-content {{
  max-width: none !important; width: 100% !important; padding: 0 !important;
}}
.{PAGE_CLASS} .l24-longread-wrap {{
  max-width: 820px; margin: 0 auto; padding: 48px 24px 80px;
  font-size: 1.05rem; line-height: 1.65; color: #1a202c;
}}
.{PAGE_CLASS} h2 {{
  margin-top: 2.5em; color: #1a365d; font-size: 1.45rem;
}}
.{PAGE_CLASS} h3 {{
  margin-top: 1.5em; color: #2c5282; font-size: 1.15rem;
}}
.{PAGE_CLASS} table {{
  width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.95rem;
}}
.{PAGE_CLASS} th, .{PAGE_CLASS} td {{
  border: 1px solid #e2e8f0; padding: 10px 12px; text-align: left;
}}
.{PAGE_CLASS} th {{ background: #edf2f7; }}
.{PAGE_CLASS} a {{ color: #1e40af; }}
.{PAGE_CLASS} code {{
  font-size: 0.9em; background: #f1f5f9; padding: 2px 6px; border-radius: 4px;
}}
.{PAGE_CLASS} .l24-code-tree {{
  margin: 1.5em 0; padding: 16px 18px; background: #f8fafc; border: 1px solid #e2e8f0;
  border-radius: 8px; font-size: 0.82rem; line-height: 1.45; overflow-x: auto; white-space: pre-wrap;
}}
.l24-intro-ip-isk {{
  max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.l24-intro-ip-isk__grid {{
  display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
  gap: 28px; align-items: start;
}}
.l24-intro-ip-isk__text {{
  border-left: 4px solid #0f766e; padding: 4px 0 4px 22px; text-align: left;
}}
.l24-intro-ip-isk__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.l24-intro-ip-isk__text p:last-child {{ margin-bottom: 0; }}
.l24-intro-ip-isk__brief {{
  background: #f0fdfa; border: 1px solid #99f6e4; border-radius: 10px;
  padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; line-height: 1.55;
}}
.l24-intro-ip-isk__decor {{
  background: linear-gradient(160deg, #faf9f7 0%, #fff 100%);
  border: 1px solid #e7e5e4; border-radius: 12px; padding: 18px;
}}
.l24-intro-ip-isk__chips {{
  display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none;
}}
.l24-intro-ip-isk__chip {{
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.03em;
  padding: 6px 10px; border-radius: 999px; background: #fff;
  border: 1px solid #cbd5e1; color: #475569;
}}
.l24-intro-ip-isk__chip--accent {{ border-color: #0f766e; color: #0f766e; }}
.l24-intro-ip-isk__chip--warn {{ border-color: #7c3aed; color: #6d28d9; }}
.l24-intro-ip-isk__route-svg {{ display: block; width: 100%; height: auto; }}
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
  background: #f1f5f9; color: #1e40af; text-decoration: none; font-size: 0.88rem; font-weight: 600;
}}
.ym-toc__list a:hover {{ background: #e2e8f0; }}
.ym-cta {{
  margin: 28px 0; padding: 22px 24px; border-radius: 10px;
  background: linear-gradient(135deg, #f8fafc 0%, #edf2f7 100%);
  border: 1px solid #cbd5e1; border-left: 4px solid #a31830;
}}
.ym-cta--legis24 {{ border-left-color: #1e3a8a; background: linear-gradient(135deg, #eff6ff 0%, #f8fafc 100%); }}
.ym-cta__text {{ margin: 0 0 14px; line-height: 1.55; color: #334155; }}
.ym-cta__actions {{ margin: 0; }}
.ym-cta__btn {{
  display: inline-block; background: #a31830; color: #fff !important;
  padding: 12px 22px; border-radius: 8px; font-weight: 700; text-decoration: none;
}}
.ym-cta__btn:hover {{ background: #8b1528; }}
.l24-faq-b2 {{
  margin-top: 2.5em; padding: 28px 24px; background: #f8fafc;
  border: 1px solid #e2e8f0; border-radius: 12px;
}}
.l24-faq-b2 > h2 {{ margin-top: 0 !important; }}
.l24-faq-b2__item {{ margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0; }}
.l24-faq-b2__item:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
.l24-faq-b2__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #1a365d; }}
.l24-faq-b2__a {{ margin: 0; color: #334155; }}
.ym-section {{ display: block; }}
@media (max-width: 900px) {{
  .l24-intro-ip-isk__grid {{ grid-template-columns: 1fr; }}
}}
"""

INTRO_HTML = """
<section class="l24-intro-ip-isk ym-section" aria-label="Введение">
  <div class="l24-intro-ip-isk__grid">
    <div class="l24-intro-ip-isk__text">
      <p>Письмо из суда, определение о принятии иска или уведомление с <strong>kad.arbitr.ru</strong> — для ИП, магазина, маркетплейса или онлайн-проекта это старт процесса, где на кону деньги, репутация и оборот. С 4 января 2026 года реформа по ФЗ <strong>№ 214-ФЗ</strong> усилила риски по компенсации, но дала ответчику рычаги: <strong>ст. 1252.1</strong>, смена способа расчёта, потолок для добросовестных, позиции <strong>КС № 57-П</strong>.</p>
      <p>Ниже — практический план для <strong>ответчика</strong>: от первых суток после вручения иска до <strong>возражения на исковое заявление</strong>, защиты по товарному знаку и авторским правам, оспаривания компенсации и итогов судебной стадии.</p>
      <div class="l24-intro-ip-isk__brief">
        <strong>Кратко:</strong> проверьте претензию и 30 дней (п. 5.1 ст. 1252), не уничтожайте доказательства, подготовьте отзыв по <strong>ст. 131 АПК</strong> по каждому доводу; на досудебке — <a href="https://advokat-vsem.online/otvet-na-pretensiyu-po-intellektualnoj-sobstvennosti/" target="_blank" rel="noopener noreferrer">ответ на претензию по ИС</a>.
      </div>
    </div>
    <aside class="l24-intro-ip-isk__decor" aria-label="Маршрут ответчика">
      <ul class="l24-intro-ip-isk__chips">
        <li class="l24-intro-ip-isk__chip l24-intro-ip-isk__chip--accent">214-ФЗ</li>
        <li class="l24-intro-ip-isk__chip">ст. 131 АПК</li>
        <li class="l24-intro-ip-isk__chip l24-intro-ip-isk__chip--warn">1252.1</li>
        <li class="l24-intro-ip-isk__chip">57-П</li>
        <li class="l24-intro-ip-isk__chip">ТЗ · ©</li>
        <li class="l24-intro-ip-isk__chip">kad.arbitr.ru</li>
      </ul>
      <svg class="l24-intro-ip-isk__route-svg" viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Схема: иск, претензия, отзыв, компенсация">
        <rect x="8" y="8" width="304" height="184" rx="10" fill="#fff" stroke="#d6d3d1"/>
        <text x="24" y="32" fill="#57534e" font-size="10" font-weight="700">ОТВЕТЧИК · 2026</text>
        <circle cx="56" cy="96" r="20" fill="#dc2626"/><text x="56" y="101" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">иск</text>
        <circle cx="160" cy="96" r="20" fill="#0f766e"/><text x="160" y="101" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">30д</text>
        <circle cx="264" cy="96" r="20" fill="#7c3aed"/><text x="264" y="101" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">131</text>
        <line x1="76" y1="96" x2="140" y2="96" stroke="#94a3b8" stroke-width="2"/>
        <line x1="180" y1="96" x2="244" y2="96" stroke="#94a3b8" stroke-width="2"/>
        <text x="56" y="130" text-anchor="middle" fill="#78716c" font-size="8">вручение</text>
        <text x="160" y="130" text-anchor="middle" fill="#78716c" font-size="8">претензия</text>
        <text x="264" y="130" text-anchor="middle" fill="#78716c" font-size="8">отзыв</text>
        <rect x="24" y="148" width="272" height="36" rx="6" fill="#f0fdfa" stroke="#99f6e4"/>
        <text x="160" y="170" text-anchor="middle" fill="#0f766e" font-size="10" font-weight="700">1252.1 · 57-П · 1486</text>
      </svg>
    </aside>
  </div>
</section>
"""

TOC_HTML = (
    """
<nav class="ym-toc ym-section" aria-label="Содержание статьи">
  <p class="ym-toc__title">По статье</p>
  <ul class="ym-toc__list">
"""
    + "\n".join(f'    <li><a href="#{hid}">{label}</a></li>' for hid, label in TOC_LABELS.items())
    + """
  </ul>
</nav>
"""
)


def main():
    handoff = HANDOFF.read_text(encoding="utf-8")
    artur_md = extract_artur_body(handoff)
    body = md_to_html(artur_md)
    body = insert_boris(body, extract_boris_html())
    hero = extract_hero_html()
    jsonld_pre = build_jsonld_pre()

    html = f"""<!-- wp:html -->
<style>
{PAGE_CSS}
</style>
<main id="primary" class="site-main {PAGE_CLASS}" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">

{hero}

{INTRO_HTML}

{TOC_HTML}

<section class="ym-section">
<div class="l24-longread-wrap" itemprop="articleBody">

{body}

<p><em>Материал носит информационный характер и не заменяет юридическую консультацию. Нормы ГК РФ ч. 4, АПК РФ, ФЗ № 214-ФЗ уточняйте по официальным текстам и с учётом вашей ситуации.</em></p>

</div>
</section>

{jsonld_pre}

</main>
<!-- /wp:html -->
"""

    assert "<script" not in html.lower()
    assert "<canvas" not in html.lower()
    assert 'id="primary"' in html
    assert "<!-- BORIS_ANCHOR -->" not in html

    OUT.write_text(html, encoding="utf-8")
    size_bytes = OUT.stat().st_size

    natasha_block = f"""
=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО

**Файл:** `{OUT.relative_to(ROOT.parent)}`  
**SLUG:** `{SLUG}`  
**Title:** {TITLE}  
**Description:** {DESCRIPTION}  
**Размер:** {size_bytes} байт  

ВНИМАНИЕ: без `<script>` и `<canvas>` — hero и Борис static SVG + inline CSS. FAQ — microdata FAQPage + скрытый `<pre>` JSON-LD в теле страницы.

```html
{html}
```

## Передача Юре

**slug:** `{SLUG}`  
**Title:** {TITLE}  
**Description:** {DESCRIPTION}  
**page_id:** `PLACEHOLDER` (после wordpress_create_page)  

**Публикация:** blob flow, `<!-- wp:html -->`; MCP publish удаляет `<script>` — в blob их нет.  

**Проверить live:** `main#primary`, класс `{PAGE_CLASS}`, hero `#l24-hero-ip-isk-otvet`, Boris `#l24-boris-ip-plan-b2`, FAQ `#b2-faq`, breadcrumbs скрыты, padding-top сброшен, CTA `https://advokat-vsem.ru/` с `target="_blank" rel="noopener noreferrer"`.  

**JSON-LD:** дублируется в скрытом `<pre class="l24-jsonld-b2">` внутри страницы; при необходимости Rank Math — тот же `@graph` из файла.
"""

    if "=== НАТАША (HTML СТРАНИЦЫ) ===" in handoff:
        handoff = handoff.split("=== НАТАША (HTML СТРАНИЦЫ) ===")[0].rstrip() + "\n" + natasha_block
    else:
        handoff = handoff.rstrip() + "\n" + natasha_block
    HANDOFF.write_text(handoff, encoding="utf-8")

    print(f"Wrote {OUT}")
    print(f"Size: {size_bytes} bytes ({size_bytes / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
