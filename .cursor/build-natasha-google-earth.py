#!/usr/bin/env python3
"""Assemble Natasha HTML for vs-google-earth-dokazatelstva-moshennichestvo-zashchita-2026."""
import json
import re
from pathlib import Path

SLUG = "vs-google-earth-dokazatelstva-moshennichestvo-zashchita-2026"
PAGE_CLASS = f"{SLUG}-page"
ROOT = Path("/workspace/.cursor")
HANDOFF = ROOT / "nero-network-handoff.md"
OUT = ROOT / "page-content-natasha-google-earth.html"

TITLE = "ВС 2026: Google Earth не доказывает мошенничество — защита по ст. 159"
DESCRIPTION = (
    "Верховный суд отменил приговор за мошенничество с земельным участком: снимки Google Earth Pro "
    "нельзя считать единственным доказательством. Линия защиты, кассация и оспаривание цифровых улик."
)
H1 = "ВС 2026: Google Earth не доказывает мошенничество — отмена приговора и защита по ст. 159"

H2_IDS = {
    "Позиция Верховного суда 2026: дело Аверченкова и отмена приговора за мошенничество": "vs-ge-poziciya",
    "Состав мошенничества по ст. 159 УК РФ при сделке с земельным участком": "vs-ge-st159",
    "Google Earth Pro и цифровые доказательства: почему одного снимка недостаточно": "vs-ge-gis",
    "Допустимость и оценка доказательств по уголовному делу (ст. 74, 88 УПК РФ)": "vs-ge-upk",
    "Выписки ЕГРН, показания свидетелей и заключения специалистов": "vs-ge-egrn",
    "Гражданский спор о недвижимости или уголовное дело о мошенничестве": "vs-ge-grazhd",
    "Защита от обвинения в мошенничестве на стадии проверки, следствия и суда": "vs-ge-zashchita",
    "Кассационная жалоба по делу о мошенничестве после позиции ВС": "vs-ge-kassaciya",
    "Практика судов: аэрофото, GIS и карты как доказательства — краткий обзор": "vs-ge-praktika",
    "Консультация по уголовным рискам и защите в уголовном деле": "vs-ge-konsultaciya",
}

TOC_LABELS = {
    "vs-ge-poziciya": "Позиция ВС 2026",
    "vs-ge-st159": "Ст. 159 УК",
    "vs-ge-gis": "Google Earth Pro",
    "vs-ge-upk": "ст. 74, 88 УПК",
    "vs-ge-egrn": "ЕГРН и свидетели",
    "l24-boris-google-earth-evidence": "Схема улик",
    "vs-ge-grazhd": "Гражданский спор",
    "vs-ge-zashchita": "Защита",
    "vs-ge-kassaciya": "Кассация",
    "vs-ge-praktika": "Практика судов",
    "vs-ge-konsultaciya": "Консультация",
    "l24-faq-google-earth": "FAQ",
}

FAQ_ITEMS = [
    (
        "Можно ли осудить за мошенничество только на основании снимков Google Earth Pro?",
        "По позиции ВС в деле Аверченкова (2026) — нет, если снимки опровергаются показаниями свидетелей и выписками ЕГРН, а суд не мотивировал, почему принял одни улики и отверг другие (ст. 88 УПК РФ).",
    ),
    (
        "Являются ли скриншоты Google Earth и Google Maps допустимыми доказательствами по уголовному делу?",
        "Могут быть допустимыми при введении через протокол осмотра по правилам УПК (ст. 74, 166, 180). Вопрос достоверности и достаточности решается на стадии оценки (ст. 88).",
    ),
    (
        "Что изменил Верховный суд в деле Аверченкова о мошенничестве с земельным участком?",
        "Отменены приговор и определения нижестоящих инстанций; дело направлено на новое апелляционное рассмотрение из‑за неполной оценки противоречивых доказательств.",
    ),
    (
        "Как оспорить цифровые доказательства при обвинении по ст. 159 УК РФ?",
        "Ходатайства о проверке протокола осмотра, экспертиза методики фиксации, выписки ЕГРН, сопоставительный тест с соседними участками, показания свидетелей и контрагентов.",
    ),
    (
        "В чём разница между гражданским спором о продаже участка и уголовным делом о мошенничестве?",
        "В уголовном деле должны быть доказаны корыстный умысел и обман до получения права на чужое имущество; гражданский спор касается качества сделки, границ и недействительности без автоматической ст. 159.",
    ),
    (
        "Какие доказательства должны дополнять аэрофото по требованию ВС?",
        "Показания свидетелей, выписки ЕГРН (включая соседние объекты), заключения специалистов о методике съёмки, акты осмотра места.",
    ),
    (
        "Как подать кассационную жалобу по делу о мошенничестве после отмены приговора?",
        "Жалоба в ВС подаётся при исчерпании обычных инстанций; в делах по аналогии с 24-УД26-1-К4 аргумент — нарушение ст. 88 УПК при неоценённых свидетелях и ЕГРН. Конкретные сроки и процессуальный статус дела уточняются по материалам.",
    ),
    (
        "Нужен ли адвокат при проверке по ст. 159 из‑за ложных сведений в Росреестр?",
        "Да, с первого допроса: протоколы осмотра карт и показания фиксируются на ранней стадии, ошибки потом исправлять сложнее.",
    ),
    (
        "Можно ли использовать выписку ЕГРН для опровержения обвинения в мошенничестве?",
        "Да, в том числе выписки о постройках на соседних участках для дискредитации GIS как единственного источника.",
    ),
    (
        "Что такое комплексная оценка доказательств по ст. 88 УПК РФ в делах о мошенничестве?",
        "Суд обязан всесторонне исследовать все улики, не придавать заранее установленной силы ни одной из них и мотивировать в приговоре, почему при противоречиях принял одни доказательства и отверг другие.",
    ),
]


def extract_section_html(handoff: str, section_marker: str, next_marker: str | None = None) -> str:
    start = handoff.find(section_marker)
    if start < 0:
        raise ValueError(f"Section not found: {section_marker}")
    if next_marker:
        end = handoff.find(next_marker, start + len(section_marker))
        block = handoff[start:end] if end >= 0 else handoff[start:]
    else:
        block = handoff[start:]
    m = re.search(r"```html\n(.*?)```", block, re.DOTALL)
    if not m:
        raise ValueError(f"No html block in {section_marker}")
    return m.group(1).strip()


def extract_artur_md(handoff: str) -> str:
    m = re.search(
        r"=== АРТУР \(CTA И РЕКЛАМА\) ===.*?### Полный текст\n\n(.*?)(?:\n\n### Рекламные вставки|\n\n## Передача пайплайну)",
        handoff,
        re.DOTALL,
    )
    if not m:
        raise ValueError("Artur section not found")
    body = m.group(1).strip()
    body = re.split(r"\n## Частые вопросы\n", body)[0].strip()
    return body


def strip_scripts_canvas(html: str) -> str:
    html = re.sub(r"<script\b[^>]*>[\s\S]*?</script>", "", html, flags=re.I)
    html = re.sub(r"<canvas\b[^>]*>[\s\S]*?</canvas>", "", html, flags=re.I)
    html = re.sub(r"<canvas\b[^>]*/>", "", html, flags=re.I)
    return html


def slugify_heading(title: str) -> str:
    return H2_IDS.get(title.strip(), re.sub(r"[^a-z0-9а-яё]+", "-", title.lower())[:48].strip("-"))


def inline_md(text: str) -> str:
    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        text,
    )
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(
        r'<a href="(https?://[^"]+)"(?![^>]*target=)',
        r'<a href="\1" target="_blank" rel="noopener noreferrer"',
        text,
    )
    return text


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
    html = ["<table>", "<thead><tr>"]
    for c in rows[0]:
        html.append(f"<th>{inline_md(c)}</th>")
    html.append("</tr></thead><tbody>")
    for row in rows[1:]:
        html.append("<tr>")
        for c in row:
            html.append(f"<td>{inline_md(c)}</td>")
        html.append("</tr>")
    html.append("</tbody></table>")
    return "".join(html)


def md_to_html(md: str, boris_html: str) -> str:
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

        if stripped == "BORIS_PLACEHOLDER":
            out.append(boris_html)
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

        if stripped.startswith("|"):
            tbl_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl_lines.append(lines[i])
                i += 1
            out.append(parse_table(tbl_lines))
            continue

        if stripped.startswith("## "):
            title = stripped[3:].strip()
            hid = slugify_heading(title)
            out.append(f'<h2 id="{hid}">{inline_md(title)}</h2>')
            i += 1
            if hid == "vs-ge-egrn":
                while i < len(lines) and not lines[i].strip():
                    i += 1
                if i < len(lines) and lines[i].strip() and not lines[i].startswith("#"):
                    out.append(f"<p>{inline_md(lines[i].strip())}</p>")
                    i += 1
                out.append(boris_html)
            continue

        if stripped.startswith("### "):
            out.append(f"<h3>{inline_md(stripped[4:].strip())}</h3>")
            i += 1
            continue

        if stripped == "---":
            i += 1
            continue

        if re.match(r"^\d+\.\s", stripped):
            out.append("<ol>")
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i].strip()):
                item = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                out.append(f"<li>{inline_md(item)}</li>")
                i += 1
            out.append("</ol>")
            continue

        if stripped.startswith("- "):
            out.append("<ul>")
            while i < len(lines) and lines[i].strip().startswith("- "):
                item = lines[i].strip()[2:]
                out.append(f"<li>{inline_md(item)}</li>")
                i += 1
            out.append("</ul>")
            continue

        if stripped:
            para = [stripped]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith("#") and lines[i].strip() != "---" and not lines[i].strip().startswith("|") and not lines[i].strip().startswith("- ") and not re.match(r"^\d+\.\s", lines[i].strip()) and not lines[i].strip().startswith("<aside"):
                para.append(lines[i].strip())
                i += 1
            out.append(f"<p>{inline_md(' '.join(para))}</p>")
            continue

        i += 1

    return "\n".join(out)


def build_intro(p1: str, p2: str) -> str:
    return f"""
<section class="l24-intro-ug" aria-label="Кратко о теме">
  <div class="l24-intro-ug__grid">
    <div class="l24-intro-ug__text">
      <p>{inline_md(p1)}</p>
      <p>{inline_md(p2)}</p>
      <div class="l24-intro-ug__brief"><strong>Источник:</strong> РАПСИ 04–06.06.2026 · дело № 24-УД26-1-К4 · Сергей Аверченков · Республика Адыгея</div>
    </div>
    <div class="l24-intro-ug__decor">
      <ul class="l24-intro-ug__chips">
        <li class="l24-intro-ug__chip l24-intro-ug__chip--accent">ст. 159 УК</li>
        <li class="l24-intro-ug__chip">ст. 88 УПК</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--warn">Google Earth Pro</li>
        <li class="l24-intro-ug__chip">выписка ЕГРН</li>
      </ul>
      <p style="margin:0;font-size:.9rem;color:#475569">ВС 04.06.2026: GIS-снимок не заменяет комплексную оценку улик при мошенничестве с земельным участком.</p>
    </div>
  </div>
</section>
"""


def build_toc() -> str:
    lis = "\n".join(f'    <li><a href="#{a}">{t}</a></li>' for a, t in TOC_LABELS.items())
    return f"""
<nav class="ym-toc" aria-label="Содержание статьи">
  <p class="ym-toc__title">По статье</p>
  <ul class="ym-toc__list">
{lis}
  </ul>
</nav>
"""


def build_faq_section() -> str:
    items = []
    for q, a in FAQ_ITEMS:
        items.append(
            f"""<div class="l24-faq__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
<h3 class="l24-faq__q" itemprop="name">{q}</h3>
<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
<p class="l24-faq__a" itemprop="text">{inline_md(a)}</p>
</div>
</div>"""
        )
    return f"""
<section id="l24-faq-google-earth" class="l24-faq" itemscope itemtype="https://schema.org/FAQPage" aria-label="Частые вопросы">
<h2>Частые вопросы (FAQ)</h2>
{"".join(items)}
</section>
"""


def build_jsonld() -> str:
    main_entity = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", inline_md(a))},
        }
        for q, a in FAQ_ITEMS
    ]
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": main_entity}
    return f'<pre class="l24-jsonld-vs" aria-hidden="true" hidden>{json.dumps(data, ensure_ascii=False)}</pre>'


def page_css() -> str:
    p = PAGE_CLASS
    return f"""
.breadcrumbs,.breadcrumb,.woocommerce-breadcrumb,.rank-math-breadcrumb,.yoast-breadcrumb,
.entry-header,.page-title-section,.entry-title,.main_title,h1.entry-title{{display:none!important}}
#primary,.site-main,.site-content,#content,.content-area{{padding-top:0!important;margin-top:0!important}}
#sidebar,.sidebar,#secondary{{display:none!important}}
.{p} .entry-content{{max-width:none!important;width:100%!important;padding:0!important}}
.{p} .l24-longread-wrap{{max-width:820px;margin:0 auto;padding:48px 24px 80px;font-size:1.05rem;line-height:1.65;color:#1a202c}}
.{p} h2{{margin-top:2.5em;color:#1a365d;font-size:1.45rem}}
.{p} h3{{margin-top:1.5em;color:#2c5282;font-size:1.15rem}}
.{p} a{{color:#1e40af}}
.{p} table{{width:100%;border-collapse:collapse;margin:1.25em 0;font-size:.95rem}}
.{p} th,.{p} td{{border:1px solid #e2e8f0;padding:10px 12px;text-align:left;vertical-align:top}}
.{p} th{{background:#f1f5f9;color:#1a365d;font-weight:700}}
.l24-intro-ug{{max-width:1200px;margin:0 auto;padding:40px 24px 8px;font-family:system-ui,sans-serif}}
.l24-intro-ug__grid{{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(260px,.9fr);gap:28px}}
.l24-intro-ug__text{{border-left:4px solid #0f2744;padding:4px 0 4px 22px}}
.l24-intro-ug__text p{{margin:0 0 14px;font-size:1.02rem;line-height:1.6;color:#334155}}
.l24-intro-ug__brief{{background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:16px 18px;margin-top:16px;font-size:.95rem}}
.l24-intro-ug__decor{{background:linear-gradient(160deg,#f1f5f9 0%,#fff 100%);border:1px solid #e2e8f0;border-radius:12px;padding:18px}}
.l24-intro-ug__chips{{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 14px;padding:0;list-style:none}}
.l24-intro-ug__chip{{font-size:.72rem;font-weight:700;padding:6px 10px;border-radius:999px;background:#fff;border:1px solid #cbd5e1;color:#475569}}
.l24-intro-ug__chip--accent{{border-color:#1e40af;color:#1e40af}}
.l24-intro-ug__chip--warn{{border-color:#a31830;color:#a31830}}
.ym-toc{{max-width:820px;margin:24px auto 0;padding:0 24px 32px;text-align:center;font-family:system-ui,sans-serif}}
.ym-toc__title{{font-size:.8rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#64748b;margin:0 0 12px}}
.ym-toc__list{{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;justify-content:center;gap:8px}}
.ym-toc__list a{{display:inline-block;padding:8px 12px;border-radius:8px;background:#f1f5f9;color:#1e40af;text-decoration:none;font-size:.88rem;font-weight:600}}
.ym-cta{{margin:28px 0;padding:22px 24px;border-radius:10px;background:linear-gradient(135deg,#f8fafc,#edf2f7);border:1px solid #cbd5e1;border-left:4px solid #a31830}}
.ym-cta--legis24{{border-left-color:#1e3a8a;background:linear-gradient(135deg,#eff6ff,#f8fafc)}}
.ym-cta__text{{margin:0 0 14px;line-height:1.55;color:#334155}}
.ym-cta__btn{{display:inline-block;background:#a31830;color:#fff!important;padding:12px 22px;border-radius:8px;font-weight:700;text-decoration:none}}
.l24-faq{{margin-top:2.5em;padding:28px 24px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;max-width:820px;margin-left:auto;margin-right:auto}}
.l24-faq h2{{margin-top:0!important}}
.l24-faq__item{{margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #e2e8f0}}
.l24-faq__q{{margin:0 0 8px;font-size:1.05rem;color:#1a365d;font-weight:600}}
.l24-faq__a{{margin:0;color:#334155}}
@media(max-width:900px){{.l24-intro-ug__grid{{grid-template-columns:1fr}}}}
"""


def parse_intro_paragraphs(md: str) -> tuple[str, str]:
    lines = md.split("\n")
    paras = []
    for line in lines:
        if line.strip().startswith("## "):
            break
        if line.strip():
            paras.append(line.strip())
    if len(paras) < 2:
        raise ValueError("Expected at least 2 intro paragraphs")
    return paras[0], paras[1]


def main():
    handoff = HANDOFF.read_text(encoding="utf-8")
    hero = strip_scripts_canvas(
        extract_section_html(handoff, "=== АЛИНА (HERO) ===", "=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===")
    )
    boris = strip_scripts_canvas(
        extract_section_html(handoff, "=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===")
    )
    artur_md = extract_artur_md(handoff)
    p1, p2 = parse_intro_paragraphs(artur_md)
    content = md_to_html(artur_md, boris)

    html = f"""<!-- wp:html -->
<style>
{page_css()}
</style>
<main id="primary" class="site-main {PAGE_CLASS}" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">
<meta itemprop="headline" content="{H1}">
<meta itemprop="description" content="{DESCRIPTION}">
<meta itemprop="inLanguage" content="ru-RU">

{hero}

{build_intro(p1, p2)}

{build_toc()}

<div class="l24-longread-wrap" itemprop="articleBody">

{content}

</div>

{build_faq_section()}

{build_jsonld()}
</main>
<!-- /wp:html -->
"""
    html = strip_scripts_canvas(html)
    OUT.write_text(html, encoding="utf-8")
    char_count = len(html)

    natasha_block = f"""=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО

**Файл:** `.cursor/page-content-natasha-google-earth.html`
**SLUG:** `{SLUG}`
**Размер HTML:** {char_count} символов

ВНИМАНИЕ: без `<script>` и `<canvas>` — hero Алины и блок Бориса static SVG + inline CSS (Legis24 MCP-only). FAQ — microdata FAQPage + скрытый `<pre class="l24-jsonld-vs">` JSON-LD.

## Передача Юре

**Title:** {TITLE}
**Description:** {DESCRIPTION}
**slug:** `{SLUG}`
**page_id:** `PLACEHOLDER` (заполнить после wordpress_create_page)

**Публикация:** обернуть в `<!-- wp:html -->`; CTA `https://advokat-vsem.ru/` с `target="_blank" rel="noopener noreferrer"`.
**Проверить:** `main#primary`, класс `{PAGE_CLASS}`, hero `#l24-hero-{SLUG}`, Boris `#l24-boris-google-earth-evidence`, FAQ `#l24-faq-google-earth`, breadcrumbs скрыты, padding-top сброшен.
"""

    if "=== НАТАША (HTML СТРАНИЦЫ) ===" in handoff:
        handoff = handoff.split("=== НАТАША (HTML СТРАНИЦЫ) ===")[0].rstrip() + "\n\n" + natasha_block
    else:
        handoff = handoff.rstrip() + "\n\n" + natasha_block
    HANDOFF.write_text(handoff, encoding="utf-8")

    assert "<script" not in html.lower()
    assert "<canvas" not in html.lower()
    assert 'id="primary"' in html
    assert "l24-boris-google-earth-evidence" in html

    print(f"Wrote {OUT}")
    print(f"Chars: {char_count}")


if __name__ == "__main__":
    main()
