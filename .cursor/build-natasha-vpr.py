#!/usr/bin/env python3
"""Сборка page-content-natasha-vpr.html — СИП ВПР / Просвещение. MCP-only: JSON-LD script only."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HANDOFF = ROOT / "nero-network-handoff.md"
ALINA = ROOT / "nero-network-fragments/alina.md"
BORIS = ROOT / "nero-network-fragments/boris.md"
OUT = ROOT / "page-content-natasha-vpr.html"
SLUG = "sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie"
PAGE_CLASS = f"{SLUG}-page"

TITLE = "СИП 2026: аннулировали ТЗ «ВПР» «Просвещение» — злоупотребление правом | Legis24"
DESCRIPTION = (
    "СИП 2026 прекратил охрану ТЗ «ВПР» «Просвещение»: злоупотребление правом на госаббревиатуру. "
    "Оспаривание, ответ на претензию и иск — ст. 10, 1483 ГК РФ."
)
H1 = "СИП 2026: Президиум аннулировал товарный знак «ВПР» издательства «Просвещение»"

H2_IDS = {
    "СИП 2026: полное прекращение охраны товарного знака «ВПР»": "vpr-prekrashchenie",
    "Злоупотребление правом при регистрации товарного знака (ст. 10 ГК РФ)": "vpr-zloupotreblenie",
    "Государственная аббревиатура и неохраняемые элементы (ст. 1483 ГК РФ)": "vpr-1483",
    "Оспаривание товарного знака: возражение в Роспатенте и иск в СИП": "vpr-osparivanie",
    "Претензия правообладателя: что делать, если требуют убрать аббревиатуру": "vpr-pretenziya",
    "Защита от иска о нарушении товарного знака": "vpr-zashchita",
    "Кому актуален кейс: издатели, EdTech, репетиторы и любой бизнес с «похожей» аббревиатурой": "vpr-auditoriya",
    "Практика 2026: дело СИП-844/2025 vs другие IP-материалы Legis24": "vpr-praktika",
    "Получите консультацию по оспариванию товарного знака и ответу на иск": "vpr-konsultaciya",
    "Часто задаваемые вопросы": "faq",
}

TOC_LABELS = {
    "vpr-prekrashchenie": "Прекращение охраны",
    "vpr-zloupotreblenie": "Злоупотребление · ст. 10",
    "vpr-1483": "ст. 1483 ГК",
    "vpr-osparivanie": "Оспаривание в СИП",
    "boris-vpr-process": "Маршрут дела",
    "vpr-pretenziya": "Претензия",
    "vpr-zashchita": "Защита от иска",
    "vpr-auditoriya": "Кому актуален",
    "vpr-praktika": "Практика 2026",
    "vpr-konsultaciya": "Консультация",
    "faq": "FAQ",
}

FAQ_ITEMS = [
    (
        "Можно ли аннулировать товарный знак только из-за того, что это госаббревиатура?",
        "Сама по себе аббревиатура не автоматически лишает знака охраны. Нужно доказать описательность (ст. 1483), введение в заблуждение или злоупотребление правом при регистрации (ст. 10, подп. 6 п. 2 ст. 1512). Кейс «ВПР» объединил все три линии.",
    ),
    (
        "Чем полное прекращение охраны отличается от исключения слова из знака?",
        "При исключении элемента знак остаётся в реестре; правообладатель сохраняет охрану родовых позиций и комбинированного обозначения. При полном прекращении свидетельство прекращает действие — монополия исчезает целиком. ФИОКО добился именно полного варианта.",
    ),
    (
        "Сколько длится оспаривание товарного знака в СИП?",
        "Дело СИП-844/2025: возражение в Роспатент подано 17.12.2024, итог кассации — 01.06.2026. Ориентир — 12–18 месяцев при обжаловании в Президиум. Сроки зависят от сложности и необходимости экспертиз.",
    ),
    (
        "Обязательно ли отвечать на претензию правообладателя товарного знака?",
        "Юридически срок ответа на досудебную претензию может не быть жёстким, но молчание ухудшает переговорную позицию. Ответ фиксирует аргументы до суда и подтверждает добросовестность.",
    ),
    (
        "Можно ли подать встречный иск об аннулировании, если на вас уже подали иск о нарушении?",
        "Да. Защита от иска часто включает встречное требование о признании регистрации недействительной (ст. 1512–1513 ГК РФ). Суды рассматривают взаимосвязь споров.",
    ),
    (
        "Взыскивали ли с «Просвещения» компенсацию за нарушение по делу ВПР?",
        "Нет. Взыскано 100 000 ₽ госпошлины. Ст. 1515 ГК РФ в этом деле не применялась — спор об оспаривании регистрации, не о контрафакте.",
    ),
    (
        "Что делать, если Роспатент частично удовлетворил возражение, но монополия осталась?",
        "Оспорить решение в суде по интеллектуальной собственности и требовать полного прекращения охраны. Кейс «ВПР» — прямое подтверждение: частичного исключения недостаточно, если родовые позиции МКТУ сохраняют давление на рынок.",
    ),
]


CTA_AFTER_LEAD = """<aside class="ym-cta ym-cta--primary" role="complementary">
  <p class="ym-cta__text">Получили претензию за использование аббревиатуры или похожего обозначения? Дело «ВПР» показало: монополия на госаббревиатуру снимается — но только при правильной стратегии оспаривания в Роспатенте и СИП.</p>
  <p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по оспариванию товарного знака</a></p>
</aside>"""

CTA_AFTER_OSPARIVANIE = """<aside class="ym-cta ym-cta--primary" role="complementary">
  <p class="ym-cta__text">Роспатент частично удовлетворил возражение, но монополия осталась — как в деле «ВПР». Для полного снятия охраны нужны ст. 10 и ст. 1483 ГК РФ, иск в СИП и при необходимости кассация в Президиум.</p>
  <p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Помощь с возражением в Роспатенте и иском в СИП</a></p>
</aside>"""

CTA_AFTER_ZASHCHITA = """<aside class="ym-cta ym-cta--primary" role="complementary">
  <p class="ym-cta__text">На вас уже подали иск о нарушении товарного знака? Встречное требование об аннулировании регистрации и защита от компенсации по ст. 1515 ГК РФ — рабочая линия после дела СИП-844/2025.</p>
  <p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Помощь с ответом на иск по интеллектуальной собственности</a></p>
</aside>"""

CTA_BOTTOM = """<aside class="ym-cta ym-cta--legis24 ym-cta--bottom" role="complementary">
  <h3>Оспаривание товарного знака и защита от иска по ИС</h3>
  <p class="ym-cta__text"><strong>Legis24</strong> — материалы и консультации по оспариванию регистрации в Роспатенте, иску в СИП, ответу на претензию правообладателя и защите от взыскания компенсации по ст. 1515 ГК РФ.</p>
  <p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по оспариванию товарного знака</a></p>
</aside>"""


def strip_faq_from_md(md: str) -> str:
    return re.sub(
        r"## Часто задаваемые вопросы.*?(?=## Получите консультацию)",
        "",
        md,
        count=1,
        flags=re.DOTALL,
    )


def extract_zhenya_body(handoff: str) -> str:
    marker = f"SLUG: {SLUG}"
    idx = handoff.rfind(marker)
    chunk = handoff[:idx] if idx >= 0 else handoff
    start = chunk.rfind("=== ЖЕНЯ (ЛОНГРИД) ===")
    if start < 0:
        raise ValueError("Zhenya block not found")
    block = handoff[start:]
    m = re.search(r"### Полный текст\n", block)
    if not m:
        raise ValueError("Zhenya ### Полный текст not found")
    body = block[m.end() :]
    body = body.split("### GEO-чеклист")[0].strip()
    return body


def inject_ctas(md: str) -> str:
    md = re.sub(
        r"\*\*Ключевой вывод:\*\*.*?\n\n",
        r"\g<0>" + CTA_AFTER_LEAD + "\n\n",
        md,
        count=1,
        flags=re.DOTALL,
    )
    md = re.sub(
        r"(## Претензия правообладателя)",
        CTA_AFTER_OSPARIVANIE + "\n\n\\1",
        md,
        count=1,
    )
    md = re.sub(
        r"(## Кому актуален кейс)",
        CTA_AFTER_ZASHCHITA + "\n\n\\1",
        md,
        count=1,
    )
    md = re.sub(
        r"<p><a href=\"https://advokat-vsem\.ru/\">.*?</p>\s*<p>Также доступна.*?</p>\s*",
        CTA_BOTTOM + "\n\n",
        md,
        flags=re.DOTALL,
    )
    return md


def extract_artur_body(handoff: str) -> str:
    marker = f"SLUG: {SLUG}"
    idx = handoff.rfind(marker)
    if idx < 0:
        raise ValueError(f"Slug {SLUG} not found in handoff")
    chunk = handoff[:idx]
    start = chunk.rfind("=== АРТУР (CTA И РЕКЛАМА) ===")
    if start >= 0:
        end = handoff.find("=== АЛИНА (HERO) ===", start)
        if end < 0:
            end = handoff.find("=== ЖЕНЯ", start)
        block = handoff[start:end]
        m = re.search(r"### Полный текст\n", block)
        if m and SLUG in block:
            body = block[m.end() :]
            body = body.split("### Рекламные вставки")[0].strip()
            body = re.sub(
                r"^1 июня 2026 года.*?\n\n\*\*Ключевой вывод:\*\*.*?\n\n",
                "",
                body,
                count=1,
                flags=re.DOTALL,
            )
            return body
    body = extract_zhenya_body(handoff)
    body = re.sub(
        r"^1 июня 2026 года.*?\n\n\*\*Ключевой вывод:\*\*.*?\n\n",
        "",
        body,
        count=1,
        flags=re.DOTALL,
    )
    body = strip_faq_from_md(body)
    return inject_ctas(body)


def md_inline(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
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

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

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

        if stripped.startswith("<p>") or stripped.startswith("<p "):
            out.append(line)
            i += 1
            continue

        if stripped.startswith("## Часто задаваемые вопросы"):
            break

        if stripped.startswith("## "):
            title = stripped[3:].strip()
            hid = H2_IDS.get(title, re.sub(r"[^a-z0-9]+", "-", title.lower())[:40].strip("-"))
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

        if stripped.startswith("*Материал подготовлен"):
            out.append(f"<p><em>{md_inline(stripped[1:-1])}</em></p>")
            i += 1
            continue

        if not stripped:
            i += 1
            continue

        out.append(f"<p>{md_inline(stripped)}</p>")
        i += 1

    return "\n\n".join(out)


SLUG_LINKS = {
    "sip-prekrashchenie-tz-neispolzovanie": "https://advokat-vsem.online/sip-prekrashchenie-tz-neispolzovanie/",
    "sip-565-zloupotreblenie-pravom-tovarnyj-znak-byvshij-uchastnik": "https://advokat-vsem.online/sip-565-zloupotreblenie-pravom-tovarnyj-znak-byvshij-uchastnik/",
    "poizon-tovarnyj-znak": "https://advokat-vsem.online/poizon-tovarnyj-znak/",
    "sip-sinergetik-766-mln": "https://advokat-vsem.online/sip-sinergetik-766-mln/",
}


def link_internal_slugs(html: str) -> str:
    for slug, url in SLUG_LINKS.items():
        html = re.sub(
            rf'(?<![/"\'>])\b{re.escape(slug)}\b(?![^<]*>)',
            f'<a href="{url}" target="_blank" rel="noopener noreferrer">{slug}</a>',
            html,
        )
    return html


def insert_boris(html: str, boris_html: str) -> str:
    marker = "Роспатент частично удовлетворил возражение, но монополия осталась"
    pos = html.find(marker)
    if pos < 0:
        raise ValueError("Boris insert anchor not found")
    pos = html.rfind("</table>", 0, pos)
    if pos < 0:
        raise ValueError("Strategy table not found before Boris anchor")
    insert_at = pos + len("</table>")
    return html[:insert_at] + "\n\n" + boris_html + "\n\n" + html[insert_at:]


def extract_boris_html() -> str:
    text = BORIS.read_text(encoding="utf-8")
    m = re.search(r"```html\n(.*?)```", text, re.DOTALL)
    if not m:
        text = HANDOFF.read_text(encoding="utf-8")
        start = text.rfind("=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===")
        m = re.search(r"```html\n(.*?)```", text[start:], re.DOTALL)
    if not m:
        raise ValueError("Boris html block not found")
    return m.group(1).strip()


def extract_hero_html() -> str:
    text = ALINA.read_text(encoding="utf-8")
    m = re.search(
        r'(<section id="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie".*?</section>)',
        text,
        re.DOTALL,
    )
    if not m:
        raise ValueError("Hero section not found in alina.md")
    return m.group(1).strip()


def build_faq_html() -> str:
    items = []
    for q, a in FAQ_ITEMS:
        items.append(
            f"""<div class="l24-faq__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
<h3 class="l24-faq__q" itemprop="name">{md_inline(q)}</h3>
<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
<p class="l24-faq__a" itemprop="text">{md_inline(a)}</p>
</div>
</div>"""
        )
    return f"""<section id="faq" class="l24-faq" itemscope itemtype="https://schema.org/FAQPage" aria-label="Частые вопросы">
<h2>Частые вопросы (FAQ)</h2>
{chr(10).join(items)}
</section>"""


def build_json_ld_script() -> str:
    faq_entities = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for q, a in FAQ_ITEMS
    ]
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": H1,
                "description": DESCRIPTION,
                "author": {"@type": "Organization", "name": "Legis24"},
                "publisher": {"@type": "Organization", "name": "Legis24"},
                "inLanguage": "ru-RU",
                "mainEntityOfPage": f"https://advokat-vsem.online/{SLUG}/",
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_entities,
            },
        ],
    }
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(graph, ensure_ascii=False, indent=2)
        + "\n</script>"
    )


PAGE_CSS = f"""
.breadcrumbs, .breadcrumb, .woocommerce-breadcrumb, .rank-math-breadcrumb, .yoast-breadcrumb,
.entry-header, .page-title-section,
.entry-title, .main_title, h1.entry-title {{ display: none !important; }}
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
.{PAGE_CLASS} ol, .{PAGE_CLASS} ul {{ margin: 1em 0; padding-left: 1.4em; }}
.{PAGE_CLASS} li {{ margin-bottom: 0.45em; }}
.l24-intro-vpr {{
  max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.l24-intro-vpr__grid {{
  display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
  gap: 28px; align-items: start;
}}
.l24-intro-vpr__text {{
  border-left: 4px solid #4338ca; padding: 4px 0 4px 22px; text-align: left;
}}
.l24-intro-vpr__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.l24-intro-vpr__text p:last-child {{ margin-bottom: 0; }}
.l24-intro-vpr__brief {{
  background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px;
  padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; line-height: 1.55;
}}
.l24-intro-vpr__decor {{
  background: linear-gradient(160deg, #f0fdf4 0%, #fff 100%);
  border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px;
}}
.l24-intro-vpr__chips {{
  display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none;
}}
.l24-intro-vpr__chip {{
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.03em;
  padding: 6px 10px; border-radius: 999px; background: #fff;
  border: 1px solid #cbd5e1; color: #475569;
}}
.l24-intro-vpr__chip--accent {{ border-color: #4338ca; color: #4338ca; }}
.l24-intro-vpr__chip--warn {{ border-color: #dc2626; color: #991b1b; }}
.l24-intro-vpr__chip--edu {{ border-color: #059669; color: #047857; }}
.l24-intro-vpr__route-svg {{ display: block; width: 100%; height: auto; }}
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
.ym-cta--legis24 {{ border-left-color: #4338ca; background: linear-gradient(135deg, #f5f3ff 0%, #f8fafc 100%); }}
.ym-cta__text {{ margin: 0 0 14px; line-height: 1.55; color: #334155; }}
.ym-cta__actions {{ margin: 0; }}
.ym-cta__btn {{
  display: inline-block; background: #a31830; color: #fff !important;
  padding: 12px 22px; border-radius: 8px; font-weight: 700; text-decoration: none;
}}
.ym-cta__btn:hover {{ background: #8b1528; }}
.l24-faq {{
  max-width: 820px; margin: 0 auto 48px; padding: 28px 24px; background: #f8fafc;
  border: 1px solid #e2e8f0; border-radius: 12px;
}}
.l24-faq > h2 {{ margin-top: 0 !important; }}
.l24-faq__item {{ margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0; }}
.l24-faq__item:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
.l24-faq__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #1a365d; }}
.l24-faq__a {{ margin: 0; color: #334155; }}
@media (max-width: 900px) {{
  .l24-intro-vpr__grid {{ grid-template-columns: 1fr; }}
}}
"""

INTRO_HTML = """
<section class="l24-intro-vpr" aria-label="Введение">
  <div class="l24-intro-vpr__grid">
    <div class="l24-intro-vpr__text">
      <p>1 июня 2026 года Президиум Суда по интеллектуальной собственности <strong>полностью аннулировал</strong> товарный знак «ВПР» (свидетельство № 652761) издательства «Просвещение». Это не спор о компенсации — это <strong>прекращение правовой охраны</strong> за злоупотребление правом и попытку монополизировать аббревиатуру госпроекта.</p>
      <p>Для издателей, EdTech и любого бизнеса с <strong>претензией по товарному знаку</strong> дело № СИП-844/2025 — практический ориентир: как оспорить регистрацию, ответить правообладателю и снять монополию с общеизвестной аббревиатуры.</p>
      <div class="l24-intro-vpr__brief"><strong>Ключевой вывод:</strong> регистрация в Роспатенте не означает неоспоримость. Если правообладатель лицензирует описательное обозначение, а не бренд, СИП вправе признать охрану недействительной полностью — даже после частичного решения Палаты по патентным спорам.</div>
    </div>
    <aside class="l24-intro-vpr__decor" aria-label="Контекст дела СИП-844/2025">
      <ul class="l24-intro-vpr__chips">
        <li class="l24-intro-vpr__chip l24-intro-vpr__chip--accent">СИП-844/2025</li>
        <li class="l24-intro-vpr__chip l24-intro-vpr__chip--warn">ст. 10 + 1483 ГК</li>
        <li class="l24-intro-vpr__chip">свид. № 652761</li>
        <li class="l24-intro-vpr__chip l24-intro-vpr__chip--edu">ФИОКО vs Роспатент</li>
        <li class="l24-intro-vpr__chip">01.06.2026</li>
        <li class="l24-intro-vpr__chip">полное аннулирование</li>
        <li class="l24-intro-vpr__chip l24-intro-vpr__chip--warn">без ст. 1515</li>
        <li class="l24-intro-vpr__chip">100 000 ₽ госпошлины</li>
      </ul>
      <svg class="l24-intro-vpr__route-svg" viewBox="0 0 380 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Маршрут оспаривания ТЗ ВПР: возражение ФИОКО, частичный Роспатент, отказ СИП, полное аннулирование Президиумом">
        <defs>
          <marker id="intro-vpr-arr" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7Z" fill="#4338ca"/></marker>
        </defs>
        <rect x="4" y="38" width="68" height="44" rx="6" fill="#fffbeb" stroke="#fcd34d" stroke-width="1.2"/>
        <text x="38" y="56" text-anchor="middle" fill="#92400e" font-size="7" font-weight="700">Роспатент</text>
        <text x="38" y="70" text-anchor="middle" fill="#64748b" font-size="6">частично</text>
        <line x1="76" y1="60" x2="90" y2="60" stroke="#4338ca" stroke-width="1.5" marker-end="url(#intro-vpr-arr)"/>
        <rect x="94" y="38" width="68" height="44" rx="6" fill="#fef2f2" stroke="#fecaca" stroke-width="1.2"/>
        <text x="128" y="56" text-anchor="middle" fill="#991b1b" font-size="7" font-weight="700">СИП</text>
        <text x="128" y="70" text-anchor="middle" fill="#64748b" font-size="6">отказ</text>
        <line x1="166" y1="60" x2="180" y2="60" stroke="#4338ca" stroke-width="1.5" marker-end="url(#intro-vpr-arr)"/>
        <rect x="184" y="38" width="68" height="44" rx="6" fill="#f5f3ff" stroke="#c4b5fd" stroke-width="1.2"/>
        <text x="218" y="56" text-anchor="middle" fill="#4338ca" font-size="7" font-weight="700">Кассация</text>
        <text x="218" y="70" text-anchor="middle" fill="#64748b" font-size="6">С01-405</text>
        <line x1="256" y1="60" x2="270" y2="60" stroke="#4338ca" stroke-width="1.5" marker-end="url(#intro-vpr-arr)"/>
        <rect x="274" y="38" width="100" height="44" rx="6" fill="#ecfdf5" stroke="#6ee7b7" stroke-width="1.2"/>
        <text x="324" y="56" text-anchor="middle" fill="#047857" font-size="7" font-weight="700">Президиум</text>
        <text x="324" y="70" text-anchor="middle" fill="#64748b" font-size="6">полное ✓</text>
      </svg>
    </aside>
  </div>
</section>
"""

TOC_HTML = (
    """
<nav class="ym-toc" aria-label="Содержание">
  <p class="ym-toc__title">Содержание</p>
  <ul class="ym-toc__list">
"""
    + "\n".join(
        f'    <li><a href="#{hid}">{TOC_LABELS[hid]}</a></li>' for hid in TOC_LABELS
    )
    + """
  </ul>
</nav>
"""
)


def main():
    handoff = HANDOFF.read_text(encoding="utf-8")
    artur_md = extract_artur_body(handoff)
    body = md_to_html(artur_md)
    body = link_internal_slugs(body)
    body = insert_boris(body, extract_boris_html())
    hero = extract_hero_html()
    faq = build_faq_html()
    json_ld = build_json_ld_script()

    html = f"""<!-- wp:html -->
<style>
{PAGE_CSS}
</style>
<main id="primary" class="site-main {PAGE_CLASS}" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">
<meta itemprop="headline" content="{H1}">
<meta itemprop="description" content="{DESCRIPTION}">
<meta itemprop="inLanguage" content="ru-RU">

{hero}

{INTRO_HTML}

{TOC_HTML}

<div class="l24-longread-wrap">

{CTA_AFTER_LEAD}

{body}

</div>

{faq}

{json_ld}
</main>
<!-- /wp:html -->
"""

    OUT.write_text(html, encoding="utf-8")
    byte_size = OUT.stat().st_size

    natasha_block = f"""=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО

**Файл:** `{OUT.relative_to(ROOT.parent)}`
**SLUG:** `{SLUG}`
**Title:** {TITLE}
**Description:** {DESCRIPTION}
**Размер файла:** {byte_size} байт
**Класс main:** `site-main {PAGE_CLASS}`

ВНИМАНИЕ: MCP-only — без `<canvas>` и произвольных `<script>`; единственный script — `application/ld+json` (Article + FAQPage). Hero Алины и блок Бориса — static SVG + inline CSS.

**Структура:** hero → intro grid + ym-toc → контент Артура (4 CTA) → `#boris-vpr-process` после таблицы стратегий в H2 оспаривания → FAQ → JSON-LD.

## Передача Юре

**slug:** `{SLUG}`
**title:** {TITLE}
**excerpt (Description):** {DESCRIPTION}
**page_id:** `PLACEHOLDER` (после `wordpress_create_page`)
**Публикация:** blob flow; обернуть в `<!-- wp:html -->`; не добавлять `<script>` кроме JSON-LD.
**Проверить:** `main#primary`, класс `{PAGE_CLASS}`, hero `#l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie`, Boris `#boris-vpr-process`, FAQ `#faq`, breadcrumbs скрыты, padding-top сброшен.
**CTA:** https://advokat-vsem.ru/ (4 блока ym-cta)
"""

    # Дописать блок только в конец handoff (не трогать чужие НАТАША-блоки выше)
    marker = f"SLUG: {SLUG}"
    if marker in handoff:
        tail_start = handoff.rfind(marker)
        tail = handoff[tail_start:]
        if "=== НАТАША (HTML СТРАНИЦЫ) ===" in tail:
            handoff = handoff[:tail_start] + re.sub(
                r"=== НАТАША \(HTML СТРАНИЦЫ\) ===.*",
                natasha_block.strip(),
                tail,
                flags=re.DOTALL,
            )
        else:
            handoff = handoff.rstrip() + "\n\n" + natasha_block
    else:
        handoff = handoff.rstrip() + "\n\n" + natasha_block
    HANDOFF.write_text(handoff, encoding="utf-8")

    print(f"Wrote {OUT}")
    print(f"Bytes: {byte_size}")
    print(f"main class: site-main {PAGE_CLASS}")


if __name__ == "__main__":
    main()
