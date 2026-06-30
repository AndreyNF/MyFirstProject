#!/usr/bin/env python3
"""Сборка page-content-natasha-A8.html (ARB A8 — иск в арбитраже при банкротстве). MCP-only: без script/canvas."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HANDOFF = ROOT / "nero-network-handoff.md"
ALINA = ROOT / "nero-network-fragments/alina.md"
BORIS = ROOT / "nero-network-fragments/boris.md"
OUT = ROOT / "page-content-natasha-A8.html"
SLUG = "isk-v-arbitrazhe-pri-bankrotstve-kogda-podavat"
PAGE_CLASS = f"{SLUG}-page"

TITLE = "Иск в арбитраже при банкротстве: сроки, подсудность, оспаривание требований"
DESCRIPTION = (
    "Когда подавать иск в арбитражный суд при банкротстве и какая подсудность дел о банкротстве. "
    "Сроки возражений на требования кредиторов и оспаривание включения в реестр. "
    "Поможем выстроить позицию в арбитражном споре — консультация."
)
H1 = "Иск в арбитраже при банкротстве: когда подавать и как оспорить требования"

H2_IDS = {
    "Когда в арбитраже при банкротстве нужен иск, а когда — заявление": "a8-kogda-isk",
    "Подсудность дел о банкротстве: в какой арбитражный суд подавать": "a8-podsudnost",
    "Сроки: подача иска, включение в реестр и возражения": "a8-sroki",
    "Как оспорить требования кредиторов: возражения и оспаривание включения в реестр": "a8-osparivanie",
    "Реестр требований кредиторов при банкротстве: что проверить до суда": "a8-reestr",
    "Оспаривание сделок при банкротстве: отдельный иск в арбитраже": "a8-sdelki",
    "Практика арбитражного суда: решения, определения, следующий шаг": "a8-praktika",
    "Консультация по арбитражному спору при банкротстве": "a8-konsultaciya",
    "Частые вопросы (FAQ)": "a8-faq",
}

TOC_LABELS = {
    "a8-kogda-isk": "Иск или заявление",
    "a8-podsudnost": "Подсудность",
    "a8-sroki": "Сроки и реестр",
    "a8-osparivanie": "Оспорить требования",
    "a8-reestr": "Проверка реестра",
    "a8-sdelki": "Оспаривание сделок",
    "a8-praktika": "Практика суда",
    "a8-konsultaciya": "Консультация",
    "l24-boris-arb-bankrotstvo-fork": "Три дороги · сроки",
    "a8-faq": "FAQ",
}

FAQ_ITEMS = [
    (
        "Можно ли подать отдельный иск о долге, если уже возбуждено банкротство?",
        "Как правило, нет смысла дублировать: требование предъявляется в деле о банкротстве. Отдельный иск возможен в исключительных ситуациях (иной ответчик, иное требование), но не вместо реестрового спора с тем же должником.",
    ),
    (
        "Сколько дней на возражение против требования кредитора при наблюдении?",
        "15 календарных дней после окончания 30-дневного срока предъявления требований (ст. 71 п. 3 127-ФЗ). Пропуск критичен при документарном порядке.",
    ),
    (
        "Чем возражение на требование отличается от оспаривания сделки?",
        "Возражение бьёт по долгу в реестре; оспаривание сделки — по активам и недействительности сделки. Цели, основания и сроки разные (см. таблицу в статье).",
    ),
    (
        "Можно ли исключить требование из реестра без отмены определения суда?",
        "Да, по п. 8 ст. 71 / 100 при новых обстоятельствах — в срок 3 месяцев с момента осведомлённости, с иными доказательствами, без повтора старых доводов.",
    ),
    (
        "Обязательно ли очное заседание, если поданы возражения?",
        "Нет. С 2024 года по умолчанию — документарное рассмотрение; заседание — при необходимости уточнения доказательств (Пленум № 40, проект по 107-ФЗ).",
    ),
    (
        "Какой суд рассматривает банкротство юрлица и гражданина?",
        "По месту нахождения юрлица или жительства гражданина (ст. 33 127-ФЗ), с учётом специальных правил закона.",
    ),
    (
        "Нужна ли электронная подача заявлений о включении и возражений?",
        "Да, это стандарт после изменений 2024–2025: электронная подача и публикации в ЕФРСБ — обязательный элемент процесса (Пленум № 40, ФЗ № 311-ФЗ).",
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
    body = body.split("### GEO-чеклист")[0].strip()
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
    skip_faq_section = False

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

        if stripped.startswith("<") and not stripped.startswith("##"):
            out.append(line)
            i += 1
            continue

        if stripped.startswith("## "):
            title = stripped[3:].strip()
            hid = slugify_title(title)
            if hid == "a8-faq":
                skip_faq_section = True
                break
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

        if stripped.startswith("*Материал носит"):
            break

        if not stripped:
            i += 1
            continue

        out.append(f"<p>{md_inline(stripped)}</p>")
        i += 1

    if skip_faq_section:
        pass
    return "\n\n".join(out)


def insert_boris(html: str, boris_html: str) -> str:
    marker = '<aside class="ym-cta ym-cta--primary"'
    pos = html.find(marker)
    if pos < 0:
        marker = '<h3>Заявление на банкротство в арбитражный суд и исковое заявление'
        pos = html.find(marker)
    if pos < 0:
        raise ValueError("Boris insert anchor not found")
    return html[:pos] + "\n\n" + boris_html + "\n\n" + html[pos:]


def extract_boris_html() -> str:
    text = BORIS.read_text(encoding="utf-8")
    m = re.search(r"```html\n(.*?)```", text, re.DOTALL)
    if not m:
        raise ValueError("Boris html block not found")
    return m.group(1).strip()


def extract_hero_html() -> str:
    text = ALINA.read_text(encoding="utf-8")
    m = re.search(
        r'(<section id="l24-hero-arb-bankr-isk".*?</section>)',
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
            f"""  <div class="l24-faq-a8__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 class="l24-faq-a8__q" itemprop="name">{md_inline(q)}</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p class="l24-faq-a8__a" itemprop="text">{md_inline(a)}</p>
    </div>
  </div>"""
        )
    return f"""<section id="a8-faq" class="l24-faq-a8 ym-section" itemscope itemtype="https://schema.org/FAQPage" aria-label="Частые вопросы">
  <h2>Частые вопросы (FAQ)</h2>
{chr(10).join(items)}
</section>

<p><em>Материал носит информационный характер и не заменяет юридическую консультацию по вашим документам. Нормы 127-ФЗ и АПК уточняйте на дату обращения.</em></p>"""


def build_json_ld_hidden() -> str:
    """Microdata on page; duplicate graph in hidden pre for Юра/Rank Math (no script tag)."""
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
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_entities,
            },
        ],
    }
    return (
        '<pre class="l24-jsonld-a8" aria-hidden="true" hidden>'
        + json.dumps(graph, ensure_ascii=False)
        + "</pre>"
    )


PAGE_CSS = f"""
.breadcrumbs, .breadcrumb, .woocommerce-breadcrumb, .rank-math-breadcrumb, .yoast-breadcrumb,
.entry-header, .page-title-section {{ display: none !important; }}
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
.l24-intro-a8 {{
  max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.l24-intro-a8__grid {{
  display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
  gap: 28px; align-items: start;
}}
.l24-intro-a8__text {{
  border-left: 4px solid #1e3a8a; padding: 4px 0 4px 22px; text-align: left;
}}
.l24-intro-a8__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.l24-intro-a8__text p:last-child {{ margin-bottom: 0; }}
.l24-intro-a8__brief {{
  background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px;
  padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; line-height: 1.55;
}}
.l24-intro-a8__decor {{
  background: linear-gradient(160deg, #f1f5f9 0%, #fff 100%);
  border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px;
}}
.l24-intro-a8__chips {{
  display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none;
}}
.l24-intro-a8__chip {{
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.03em;
  padding: 6px 10px; border-radius: 999px; background: #fff;
  border: 1px solid #cbd5e1; color: #475569;
}}
.l24-intro-a8__chip--accent {{ border-color: #1e40af; color: #1e40af; }}
.l24-intro-a8__chip--warn {{ border-color: #a31830; color: #a31830; }}
.l24-intro-a8__chip--navy {{ border-color: #0f2744; color: #0f2744; }}
.l24-intro-a8__route-svg {{ display: block; width: 100%; height: auto; }}
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
.l24-faq-a8 {{
  margin-top: 2.5em; padding: 28px 24px; background: #f8fafc;
  border: 1px solid #e2e8f0; border-radius: 12px;
}}
.l24-faq-a8 > h2 {{ margin-top: 0 !important; }}
.l24-faq-a8__item {{ margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0; }}
.l24-faq-a8__item:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
.l24-faq-a8__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #1a365d; }}
.l24-faq-a8__a {{ margin: 0; color: #334155; }}
.l24-jsonld-a8 {{ display: none !important; }}
.ym-section {{ display: block; }}
@media (prefers-reduced-motion: no-preference) {{
  .{PAGE_CLASS} .l24-longread-wrap > * {{
    animation: l24-a8-fade 0.5s ease both;
  }}
}}
@keyframes l24-a8-fade {{
  from {{ opacity: 0; transform: translateY(8px); }}
  to {{ opacity: 1; transform: none; }}
}}
@media (prefers-reduced-motion: reduce) {{
  .{PAGE_CLASS} .l24-longread-wrap > * {{ animation: none !important; }}
}}
@media (max-width: 900px) {{
  .l24-intro-a8__grid {{ grid-template-columns: 1fr; }}
}}
"""

INTRO_HTML = """
<section class="l24-intro-a8 ym-section" aria-label="Введение">
  <div class="l24-intro-a8__grid">
    <div class="l24-intro-a8__text">
      <p>В бытовой речи «<strong>иск в арбитраже при банкротстве</strong>» смешивают самостоятельный иск до возбуждения дела, заявление о банкротстве и обособленный спор о реестре. Для суда это разные инструменты — с разной <strong>подсудностью дел о банкротстве</strong> и календарём.</p>
      <p>Ниже — пошагово: когда подавать документы, как уложиться в <strong>срок возражений на требование кредитора</strong>, чем отличается <strong>оспаривание включения в реестр</strong> от оспаривания сделки и что изменилось после документарного порядка (107-ФЗ).</p>
      <div class="l24-intro-a8__brief">
        <strong>Кратко:</strong> возражение при наблюдении — <strong>15 календарных дней</strong> (ст. 71); исключение по новым фактам — <strong>3 месяца</strong> (п. 8 ст. 71 / 100); порог банкротства юрлица с 01.06.2024 — <strong>2 млн ₽</strong> (кроме заявления должника).
      </div>
    </div>
    <aside class="l24-intro-a8__decor" aria-label="Нормы и сроки банкротного арбитража">
      <ul class="l24-intro-a8__chips">
        <li class="l24-intro-a8__chip l24-intro-a8__chip--navy">ст. 33 127-ФЗ</li>
        <li class="l24-intro-a8__chip l24-intro-a8__chip--accent">ст. 71 / 100</li>
        <li class="l24-intro-a8__chip">107-ФЗ</li>
        <li class="l24-intro-a8__chip l24-intro-a8__chip--warn">15 дней</li>
        <li class="l24-intro-a8__chip">ЕФРСБ</li>
        <li class="l24-intro-a8__chip">Пленум № 40</li>
      </ul>
      <svg class="l24-intro-a8__route-svg" viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Три дороги: иск до банкротства, возражение 15 дней, исключение 3 месяца">
        <rect x="8" y="8" width="304" height="184" rx="10" fill="#fff" stroke="#cbd5e1"/>
        <text x="24" y="32" fill="#64748b" font-size="10" font-weight="700">РЕЕСТР → ВЫБОР ИНСТРУМЕНТА</text>
        <rect x="24" y="48" width="88" height="52" rx="8" fill="#f1f5f9" stroke="#94a3b8"/>
        <text x="68" y="72" text-anchor="middle" fill="#475569" font-size="8" font-weight="700">ИСК</text>
        <text x="68" y="86" text-anchor="middle" fill="#64748b" font-size="7">до дела</text>
        <rect x="116" y="48" width="88" height="52" rx="8" fill="#fef2f2" stroke="#a31830"/>
        <text x="160" y="72" text-anchor="middle" fill="#a31830" font-size="8" font-weight="800">15 ДН.</text>
        <text x="160" y="86" text-anchor="middle" fill="#991b1b" font-size="7">возражение</text>
        <rect x="208" y="48" width="88" height="52" rx="8" fill="#eff6ff" stroke="#1e3a8a"/>
        <text x="252" y="72" text-anchor="middle" fill="#1e3a8a" font-size="8" font-weight="700">3 МЕС.</text>
        <text x="252" y="86" text-anchor="middle" fill="#1e40af" font-size="7">исключение</text>
        <rect x="24" y="118" width="272" height="58" rx="8" fill="#f8fafc" stroke="#e2e8f0"/>
        <text x="160" y="142" text-anchor="middle" fill="#334155" font-size="9" font-weight="600">документарный порядок · ЕФРСБ · электронная подача</text>
        <text x="160" y="160" text-anchor="middle" fill="#64748b" font-size="8">обособленный спор в банкротном деле</text>
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
    body = insert_boris(body, extract_boris_html())
    body = body + "\n\n" + build_faq_html()
    hero = extract_hero_html()
    json_ld = build_json_ld_hidden()

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

<section class="ym-section">
<div class="l24-longread-wrap">

{body}

</div>
</section>

{json_ld}

</main>
<!-- /wp:html -->
"""

    OUT.write_text(html, encoding="utf-8")
    char_count = len(html)

    natasha_block = f"""=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО

**Файл:** `{OUT.relative_to(ROOT.parent)}`
**SLUG:** `{SLUG}`
**Title:** {TITLE}
**Description:** {DESCRIPTION}
**Размер HTML:** {char_count} символов
**Класс main:** `site-main {PAGE_CLASS}`

ВНИМАНИЕ: без `<script>` и `<canvas>` — hero и Борис static SVG + inline CSS (MCP publish удаляет scripts). JSON-LD: microdata Article на `<main>`, FAQPage на секции `#a8-faq`; дублирующий граф в `<pre class="l24-jsonld-a8" hidden>` без script.

```html
{html}
```

## Передача Юре

**slug:** `{SLUG}`
**title:** {TITLE}
**excerpt (Description):** {DESCRIPTION}
**page_id:** `PLACEHOLDER` (после `wordpress_create_page`)
**Публикация:** blob flow по `commands/nero-publish-mcp.md`; обернуть в `<!-- wp:html -->`; перед blob удалить любые случайные `<script>`.
**Проверить:** `main#primary`, класс `{PAGE_CLASS}`, hero `#l24-hero-arb-bankr-isk`, Boris `#l24-boris-arb-bankrotstvo-fork`, FAQ `#a8-faq`, breadcrumbs скрыты, padding-top сброшен.
**CTA:** https://advokat-vsem.ru/ (4 блока ym-cta в теле)
"""

    if "=== НАТАША (HTML СТРАНИЦЫ) ===" in handoff:
        handoff = handoff.split("=== НАТАША (HTML СТРАНИЦЫ) ===")[0].rstrip() + "\n" + natasha_block
    else:
        handoff = handoff.rstrip() + "\n" + natasha_block
    HANDOFF.write_text(handoff, encoding="utf-8")

    print(f"Wrote {OUT}")
    print(f"Chars: {char_count}")
    print(f"main class: site-main {PAGE_CLASS}")


if __name__ == "__main__":
    main()
