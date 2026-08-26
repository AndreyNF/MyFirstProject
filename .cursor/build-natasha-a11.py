#!/usr/bin/env python3
"""Сборка page-content-natasha-A11.html (ARB A11 — АУ и оспаривание сделок). MCP-only: без script/canvas."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HANDOFF = ROOT / "nero-network-handoff.md"
ALINA = ROOT / "nero-network-fragments/alina.md"
BORIS = ROOT / "nero-network-fragments/boris.md"
OUT = ROOT / "page-content-natasha-A11.html"
SLUG = "arbitrazhnyj-upravlyayushchij-osparivanie-sdelok"
PAGE_CLASS = f"{SLUG}-page"

TITLE = "Арбитражный управляющий и оспаривание сделок: сроки и последствия для должника | Legis24"
DESCRIPTION = (
    "Когда арбитражный управляющий оспаривает сделки должника в банкротстве: сроки по ст. 61.1–61.5, "
    "подозрительные и с предпочтением сделки, заявление в арбитражный суд и последствия для должника. "
    "Консультация по защите."
)
H1 = "Арбитражный управляющий и оспаривание сделок: сроки и последствия для должника"

H2_IDS = {
    "Оспаривание сделок при банкротстве: кто и зачем": "a11-kto",
    "Роль арбитражного и финансового управляющего": "a11-au",
    "Какие сделки оспаривают: виды по закону о банкротстве": "a11-vidy",
    "Сроки оспаривания и исковая давность": "a11-sroki",
    "Процесс в арбитражном суде: заявление и защита должника": "a11-process",
    "Последствия для должника, если сделку признали недействительной": "a11-posledstviya",
    "Когда нужна консультация по арбитражному спору в банкротстве": "a11-konsultaciya",
    "Частые вопросы (FAQ)": "a11-faq",
}

TOC_LABELS = {
    "a11-kto": "Кто оспаривает",
    "a11-au": "Роль управляющего",
    "a11-vidy": "Виды сделок · 61.2–61.4",
    "a11-sroki": "Сроки и давность",
    "l24-boris-ospar-sroki-a11": "Два «часа» · сроки",
    "a11-process": "Заявление и отзыв",
    "a11-posledstviya": "Последствия",
    "a11-konsultaciya": "Консультация",
    "a11-faq": "FAQ",
}

FAQ_ITEMS = [
    (
        "Обязан ли арбитражный управляющий оспаривать каждую сомнительную сделку?",
        "Нет: оспаривание по ст. 61.1 — право, а не абсолютная обязанность. ВС указывал, что при отсутствии разумных судебных перспектив заявление подавать не обязаны; при явных основаниях и пропуске срока кредиторы вправе требовать убытков с управляющего (ст. 20.3 ЗоБ).",
    ),
    (
        "Чем look-back отличается от годичного срока на иск управляющего?",
        "Look-back — насколько далеко закон смотрит на сделки до принятия заявления о банкротстве (1 мес., 6 мес., 1 год, 3 года по основанию). Годичный срок — срок исковой давности на подачу заявления АУ по ст. 61.2 и 61.3 с момента, когда он узнал или должен был узнать об основаниях.",
    ),
    (
        "Чем подозрительная сделка (ст. 61.2) отличается от сделки с предпочтением (ст. 61.3)?",
        "61.2 — неравноценность или вред кредиторам (look-back 1 или 3 года); 61.3 — преимущество одному кредитору (1 месяц или 6 месяцев). После обзора ВС № 5/2026 (п. 10) нельзя «переодеть» предпочтение в подозрительную сделку ради иных сроков.",
    ),
    (
        "Может ли должник сам инициировать оспаривание сделки в свою пользу?",
        "В процедуре банкротства должник ограничен в распоряжении имуществом и, как правило, не инициирует конкурсное оспаривание «в свою пользу». Зато руководитель, учредитель или ИП обязаны активно участвовать в защите при оспаривании сделок против них.",
    ),
    (
        "Куда подаётся заявление об оспаривании сделки?",
        "В тот же арбитражный суд, что ведёт дело о банкротстве, через «Мой арбитр» — как обособлённый спор внутри банкротного производства, с требованиями к исковому заявлению по АПК РФ.",
    ),
    (
        "Можно ли заявить о пропуске исковой давности управляющим?",
        "Да: по ст. 199 ГК РФ сторона вправе заявить о пропуске годичного срока (п. 32 Пленума ВАС № 63) — это один из ключевых доводов в отзыве должника или контрагента.",
    ),
    (
        "Что такое реституция при признании сделки недействительной?",
        "По ст. 61.6 и 61.7 — возврат имущества в конкурсную массу и взаимное возвращение полученного. Для контрагента требование в реестре после возврата, как правило, субординированное и часто не погашается.",
    ),
]


def extract_artur_body(handoff: str) -> str:
    start = handoff.find("=== АРТУР (CTA И РЕКЛАМА) ===")
    if start < 0:
        raise ValueError("Artur block not found")
    end = handoff.find("=== АЛИНА (HERO) ===", start)
    if end < 0:
        end = len(handoff)
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

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

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

        if stripped.startswith("<") and not stripped.startswith("##"):
            out.append(line)
            i += 1
            continue

        if stripped.startswith("## "):
            title = stripped[3:].strip()
            hid = slugify_title(title)
            if hid == "a11-faq":
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

    return "\n\n".join(out)


def insert_boris(html: str, boris_html: str) -> str:
    anchor = "<!-- BORIS_ANCHOR -->"
    if anchor not in html:
        raise ValueError("BORIS_ANCHOR not found in longread")
    return html.replace(anchor, boris_html)


def extract_boris_html() -> str:
    text = BORIS.read_text(encoding="utf-8")
    m = re.search(r"```html\n(.*?)```", text, re.DOTALL)
    if not m:
        raise ValueError("Boris html block not found")
    return m.group(1).strip()


def extract_hero_html() -> str:
    text = ALINA.read_text(encoding="utf-8")
    m = re.search(
        r'(<section id="l24-hero-arb-au-deals".*?</section>)',
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
            f"""  <div class="l24-faq-a11__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 class="l24-faq-a11__q" itemprop="name">{md_inline(q)}</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p class="l24-faq-a11__a" itemprop="text">{md_inline(a)}</p>
    </div>
  </div>"""
        )
    return f"""<section id="a11-faq" class="l24-faq-a11 ym-section" itemscope itemtype="https://schema.org/FAQPage" aria-label="Частые вопросы">
  <h2>Частые вопросы (FAQ)</h2>
{chr(10).join(items)}
</section>

<p><em>Материал носит информационный характер и не заменяет юридическую консультацию. Сроки оспаривания и периоды подозрительности определяются по дате принятия заявления о банкротстве, виду процедуры и фактическим обстоятельствам конкретного дела.</em></p>"""


def build_json_ld_hidden() -> str:
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
            {"@type": "FAQPage", "mainEntity": faq_entities},
        ],
    }
    return (
        '<pre class="l24-jsonld-a11" aria-hidden="true" hidden>'
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
.l24-intro-a11 {{
  max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.l24-intro-a11__grid {{
  display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
  gap: 28px; align-items: start;
}}
.l24-intro-a11__text {{
  border-left: 4px solid #1e3a8a; padding: 4px 0 4px 22px; text-align: left;
}}
.l24-intro-a11__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.l24-intro-a11__text p:last-child {{ margin-bottom: 0; }}
.l24-intro-a11__brief {{
  background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px;
  padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; line-height: 1.55;
}}
.l24-intro-a11__decor {{
  background: linear-gradient(160deg, #f1f5f9 0%, #fff 100%);
  border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px;
}}
.l24-intro-a11__chips {{
  display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none;
}}
.l24-intro-a11__chip {{
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.03em;
  padding: 6px 10px; border-radius: 999px; background: #fff;
  border: 1px solid #cbd5e1; color: #475569;
}}
.l24-intro-a11__chip--accent {{ border-color: #1e40af; color: #1e40af; }}
.l24-intro-a11__chip--warn {{ border-color: #a31830; color: #a31830; }}
.l24-intro-a11__chip--navy {{ border-color: #0f2744; color: #0f2744; }}
.l24-intro-a11__route-svg {{ display: block; width: 100%; height: auto; }}
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
.l24-faq-a11 {{
  margin-top: 2.5em; padding: 28px 24px; background: #f8fafc;
  border: 1px solid #e2e8f0; border-radius: 12px;
}}
.l24-faq-a11 > h2 {{ margin-top: 0 !important; }}
.l24-faq-a11__item {{ margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0; }}
.l24-faq-a11__item:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
.l24-faq-a11__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #1a365d; }}
.l24-faq-a11__a {{ margin: 0; color: #334155; }}
.l24-jsonld-a11 {{ display: none !important; }}
.ym-section {{ display: block; }}
@media (prefers-reduced-motion: no-preference) {{
  .{PAGE_CLASS} .l24-longread-wrap > * {{
    animation: l24-a11-fade 0.5s ease both;
  }}
}}
@keyframes l24-a11-fade {{
  from {{ opacity: 0; transform: translateY(8px); }}
  to {{ opacity: 1; transform: none; }}
}}
@media (prefers-reduced-motion: reduce) {{
  .{PAGE_CLASS} .l24-longread-wrap > * {{ animation: none !important; }}
}}
@media (max-width: 900px) {{
  .l24-intro-a11__grid {{ grid-template-columns: 1fr; }}
}}
"""

INTRO_HTML = """
<section class="l24-intro-a11 ym-section" aria-label="Введение">
  <div class="l24-intro-a11__grid">
    <div class="l24-intro-a11__text">
      <p><strong>Оспаривание сделок при банкротстве</strong> — один из самых болезненных этапов для руководителя ООО и ИП: арбитражный управляющий должника вправе «откатить» сделки за годы до принятия заявления о банкротстве. В арбитражном суде это <strong>обособлённый спор</strong> внутри дела о несостоятельности, а не отдельный иск «с нуля».</p>
      <p>Ниже — кто инициирует оспаривание, роль арбитражного и финансового управляющего, чем отличается look-back от годичного срока на заявление, практика ВС 2024–2026 и защита в арбитраже.</p>
      <div class="l24-intro-a11__brief">
        <strong>Кратко:</strong> look-back по ст. 61.2–61.3 — от <strong>1 мес.</strong> до <strong>3 лет</strong> до принятия заявления о банкротстве; на иск АУ по 61.2/61.3 — как правило <strong>1 год</strong> с момента, когда управляющий должен был узнать об основании; отзыв и независимая оценка — первая линия защиты.
      </div>
    </div>
    <aside class="l24-intro-a11__decor" aria-label="Оспаривание сделок: нормы и сроки">
      <ul class="l24-intro-a11__chips">
        <li class="l24-intro-a11__chip l24-intro-a11__chip--navy">ст. 61.1–61.14</li>
        <li class="l24-intro-a11__chip l24-intro-a11__chip--accent">ст. 61.2 / 61.3</li>
        <li class="l24-intro-a11__chip">ст. 61.9</li>
        <li class="l24-intro-a11__chip l24-intro-a11__chip--warn">1 год · иск АУ</li>
        <li class="l24-intro-a11__chip">Пленум № 63</li>
        <li class="l24-intro-a11__chip">обзор ВС 5/2026</li>
      </ul>
      <svg class="l24-intro-a11__route-svg" viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Look-back и годичный срок на заявление арбитражного управляющего об оспаривании сделки">
        <rect x="8" y="8" width="304" height="184" rx="10" fill="#fff" stroke="#cbd5e1"/>
        <text x="24" y="32" fill="#64748b" font-size="10" font-weight="700">ДВА «ЧАСА» СРОКОВ</text>
        <rect x="24" y="48" width="120" height="52" rx="8" fill="#eff6ff" stroke="#1e3a8a"/>
        <text x="84" y="72" text-anchor="middle" fill="#1e3a8a" font-size="8" font-weight="700">LOOK-BACK</text>
        <text x="84" y="86" text-anchor="middle" fill="#64748b" font-size="7">1 мес. – 3 года</text>
        <rect x="176" y="48" width="120" height="52" rx="8" fill="#fef2f2" stroke="#a31830"/>
        <text x="236" y="72" text-anchor="middle" fill="#a31830" font-size="8" font-weight="800">1 ГОД</text>
        <text x="236" y="86" text-anchor="middle" fill="#991b1b" font-size="7">иск АУ · 61.2/61.3</text>
        <rect x="24" y="118" width="272" height="58" rx="8" fill="#f8fafc" stroke="#e2e8f0"/>
        <text x="160" y="142" text-anchor="middle" fill="#334155" font-size="9" font-weight="600">обособлённый спор · «Мой арбитр» · реституция</text>
        <text x="160" y="160" text-anchor="middle" fill="#64748b" font-size="8">отзыв: T₀ + дата знания АУ + квалификация 61.2/61.3</text>
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

    body = re.sub(
        r"^<p>Оспаривание сделок при банкротстве.*?</p>\n\n<p>Ниже — практический.*?</p>\n\n",
        "",
        body,
        count=1,
        flags=re.DOTALL,
    )

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
    byte_count = len(html.encode("utf-8"))

    natasha_block = f"""=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО

**Файл:** `{OUT.relative_to(ROOT.parent)}`
**SLUG:** `{SLUG}`
**Title:** {TITLE}
**Description:** {DESCRIPTION}
**Размер HTML:** {char_count} символов ({byte_count} байт UTF-8)
**Класс main:** `site-main {PAGE_CLASS}`

ВНИМАНИЕ: без `<script>` и `<canvas>` — hero и Борис static SVG + inline CSS (MCP publish удаляет scripts). JSON-LD: microdata Article на `<main>`, FAQPage на секции `#a11-faq`; дублирующий граф в `<pre class="l24-jsonld-a11" hidden>` без script.

## Передача Юре

**slug:** `{SLUG}`
**title:** {TITLE}
**excerpt (Description):** {DESCRIPTION}
**page_id:** `PLACEHOLDER` (после `wordpress_create_page`)
**Публикация:** MCP blob flow (`wordpress_content_blob_append` + `wordpress_update_page_from_blob` / create); обёртка `<!-- wp:html -->`; перед blob удалить любые случайные `<script>`.
**Проверить:** `main#primary`, класс `{PAGE_CLASS}`, hero `#l24-hero-arb-au-deals`, Boris `#l24-boris-ospar-sroki-a11`, FAQ `#a11-faq`, breadcrumbs скрыты, padding-top сброшен.
**CTA:** https://advokat-vsem.ru/ (3× ym-cta--primary + ym-cta--legis24)
"""

    if "=== НАТАША (HTML СТРАНИЦЫ) ===" in handoff:
        handoff = handoff.split("=== НАТАША (HTML СТРАНИЦЫ) ===")[0].rstrip() + "\n" + natasha_block
    else:
        handoff = handoff.rstrip() + "\n" + natasha_block
    HANDOFF.write_text(handoff, encoding="utf-8")

    print(f"Wrote {OUT}")
    print(f"Chars: {char_count}")
    print(f"Bytes UTF-8: {byte_count}")
    print(f"main class: site-main {PAGE_CLASS}")
    assert "<script" not in html.lower()
    assert "<canvas" not in html.lower()


if __name__ == "__main__":
    main()
