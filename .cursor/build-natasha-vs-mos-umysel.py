#!/usr/bin/env python3
"""Assemble Natasha HTML for vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026."""
import json
import re
from pathlib import Path

SLUG = "vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026"
PAGE_CLASS = f"{SLUG}-page"
ROOT = Path("/workspace/.cursor")
HANDOFF = ROOT / "nero-network-handoff.md"
OUT = ROOT / "page-vs-moshennichestvo-municipalnyj-kontrakt.html"

TITLE = "ВС 2026: отмена приговора директору МУП за мошенничество по ч. 3 ст. 159"
DESCRIPTION = (
    "Верховный суд отменил приговор директору МУП по ч. 3 ст. 159 УК РФ: работы по муниципальному "
    "контракту приняты, умысел и корыстная цель не доказаны (дело № 85-УД26-2-К1). Граница "
    "гражданского спора и уголовного преследования — защита руководителя на кассации."
)
H1 = (
    "ВС отменил приговор директору МУП за мошенничество по ч. 3 ст. 159: "
    "работы по контракту выполнены, умысел не доказан (дело № 85-УД26-2-К1)"
)

H2_IDS = {
    "Позиция Верховного суда 2026: отмена приговора по делу № 85-УД26-2-К1": "vs-mos-poziciya",
    "Ч. 3 ст. 159 УК РФ: состав мошенничества в крупном размере": "vs-mos-st159",
    "Гражданский спор или уголовное дело: когда переплата по контракту не равна мошенничеству": "vs-mos-grazhd",
    "Умысел до получения денег: Пленум ВС № 48 и доказывание корыстной цели": "vs-mos-umysel",
    "Уголовная ответственность директора МУП и ООО при госконтракте": "vs-mos-direktor",
    "Кассационная защита: линия аргументов при обвинении в мошенничестве по контракту": "vs-mos-kassaciya",
    "Когда нужен адвокат по уголовным делам о мошенничестве": "vs-mos-advokat",
    "Отличие от дела о завышении цен на госконтрактах (параллель с ч. 4 ст. 159)": "vs-mos-tomashev",
    "Итог": "vs-mos-itog",
}

TOC_LABELS = [
    ("vs-mos-poziciya", "Позиция ВС 2026"),
    ("vs-mos-st159", "ч. 3 ст. 159 УК"),
    ("vs-mos-grazhd", "Гражданский спор"),
    ("l24-boris-vs-moshennichestvo-umysel", "Схема границы"),
    ("vs-mos-umysel", "Умысел и Пленум № 48"),
    ("vs-mos-direktor", "Ответственность директора"),
    ("vs-mos-kassaciya", "Кассация"),
    ("vs-mos-advokat", "Адвокат"),
    ("vs-mos-tomashev", "Параллель с ч. 4"),
    ("l24-faq-mos-umysel", "FAQ"),
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


def extract_artur_parts(handoff: str) -> tuple[str, list[tuple[str, str]], str]:
    m = re.search(
        r"=== АРТУР \(CTA И РЕКЛАМА\) ===.*?### Полный текст\n\n(.*?)(?:\n\n### Рекламные вставки|\n\n## Передача пайплайну)",
        handoff,
        re.DOTALL,
    )
    if not m:
        raise ValueError("Artur section not found")
    full = m.group(1).strip()
    parts = re.split(r"\n## Частые вопросы \(FAQ\)\n", full, maxsplit=1)
    body = parts[0].strip()
    faq_items: list[tuple[str, str]] = []
    itog_md = ""
    if len(parts) > 1:
        tail_parts = re.split(r"\n## Итог\n", parts[1], maxsplit=1)
        faq_block = tail_parts[0].strip()
        faq_block = re.sub(r"^###\s+", "", faq_block)
        chunks = re.split(r"\n###\s+", faq_block)
        for chunk in chunks:
            chunk = chunk.strip()
            if not chunk:
                continue
            lines = chunk.split("\n", 1)
            q = lines[0].strip()
            a = lines[1].strip() if len(lines) > 1 else ""
            if q and a:
                faq_items.append((q, a))
        if len(tail_parts) > 1:
            itog_md = "## Итог\n" + tail_parts[1].strip()
    return body, faq_items, itog_md


def strip_scripts_canvas(html: str) -> str:
    html = re.sub(r"<script\b[^>]*>[\s\S]*?</script>", "", html, flags=re.I)
    html = re.sub(r"<canvas\b[^>]*>[\s\S]*?</canvas>", "", html, flags=re.I)
    html = re.sub(r"<canvas\b[^>]*/>", "", html, flags=re.I)
    return html


def slugify_heading(title: str) -> str:
    return H2_IDS.get(title.strip(), re.sub(r"[^a-z0-9а-яё-]+", "-", title.lower())[:48].strip("-"))


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
    boris_inserted = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if skip_intro and stripped.startswith("## "):
            skip_intro = False
        elif skip_intro:
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

        if stripped.startswith("> "):
            bq_lines = []
            while i < len(lines) and lines[i].strip().startswith("> "):
                bq_lines.append(lines[i].strip()[2:])
                i += 1
            out.append(f"<blockquote><p>{inline_md(' '.join(bq_lines))}</p></blockquote>")
            continue

        if stripped.startswith("## "):
            title = stripped[3:].strip()
            hid = slugify_heading(title)
            if hid == "vs-mos-umysel" and not boris_inserted:
                out.append(boris_html)
                boris_inserted = True
            out.append(f'<h2 id="{hid}">{inline_md(title)}</h2>')
            i += 1
            continue

        if stripped.startswith("### "):
            out.append(f"<h3>{inline_md(stripped[4:].strip())}</h3>")
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
            while i < len(lines) and lines[i].strip() and not lines[i].startswith("#") and not lines[i].strip().startswith("|") and not lines[i].strip().startswith("- ") and not re.match(r"^\d+\.\s", lines[i].strip()) and not lines[i].strip().startswith("<aside") and not lines[i].strip().startswith("> "):
                para.append(lines[i].strip())
                i += 1
            out.append(f"<p>{inline_md(' '.join(para))}</p>")
            continue

        i += 1

    if boris_html and not boris_inserted:
        raise ValueError("Boris block was not inserted before H2-4")

    return "\n".join(out)


def parse_intro_paragraphs(md: str) -> tuple[str, str, str]:
    lines = md.split("\n")
    paras = []
    for line in lines:
        if line.strip().startswith("## "):
            break
        if line.strip():
            paras.append(line.strip())
    if len(paras) < 2:
        raise ValueError("Expected at least 2 intro paragraphs")
    p1 = paras[0]
    p2 = paras[1]
    if len(paras) > 2:
        brief = paras[2]
    else:
        brief = (
            "Материал разбирает дело Столярова (МУП МРЭП, 612 144 ₽), ч. 3 ст. 159 УК, "
            "границу гражданского спора и уголовного преследования, Пленум ВС № 48 "
            "и линию кассационной защиты для директоров МУП и подрядчиков по 44-ФЗ."
        )
    return p1, p2, brief


def build_intro(p1: str, p2: str, brief: str) -> str:
    return f"""
<section class="l24-intro-ug" aria-label="Кратко о теме">
  <div class="l24-intro-ug__grid">
    <div class="l24-intro-ug__text">
      <p>{inline_md(p1)}</p>
      <p>{inline_md(p2)}</p>
      <div class="l24-intro-ug__brief">{inline_md(brief)}</div>
    </div>
    <div class="l24-intro-ug__decor">
      <ul class="l24-intro-ug__chips">
        <li class="l24-intro-ug__chip l24-intro-ug__chip--accent">ч. 3 ст. 159 УК</li>
        <li class="l24-intro-ug__chip">№ 85-УД26-2-К1</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--blue">612 144 ₽</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--ok">Пленум № 48</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--blue">44-ФЗ · п. 9 ст. 93</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--accent">МУП МРЭП</li>
        <li class="l24-intro-ug__chip">Калужская обл.</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--warn">умысел не доказан</li>
      </ul>
      <svg class="l24-intro-ug__route-svg" viewBox="0 0 390 100" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Маршрут дела Столярова: контракт 612 144 ₽ → приговор → ВС отменил приговор 14.05.2026">
        <defs>
          <marker id="intr159-arr" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7Z" fill="#4338ca"/>
          </marker>
          <marker id="intr159-grn" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7Z" fill="#059669"/>
          </marker>
        </defs>
        <rect x="4" y="32" width="72" height="44" rx="6" fill="#f5f3ff" stroke="#4338ca" stroke-width="1.2"/>
        <text x="40" y="50" text-anchor="middle" fill="#4338ca" font-size="5.5" font-weight="700">Контракт</text>
        <text x="40" y="62" text-anchor="middle" fill="#64748b" font-size="5">612 144 ₽</text>
        <text x="40" y="72" text-anchor="middle" fill="#64748b" font-size="5">работы приняты</text>
        <line x1="78" y1="54" x2="92" y2="54" stroke="#a31830" stroke-width="1.5" marker-end="url(#intr159-arr)"/>
        <rect x="96" y="32" width="72" height="44" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
        <text x="132" y="50" text-anchor="middle" fill="#991b1b" font-size="5.5" font-weight="700">Приговор</text>
        <text x="132" y="62" text-anchor="middle" fill="#b91c1c" font-size="5">ч. 3 ст. 159</text>
        <text x="132" y="72" text-anchor="middle" fill="#b91c1c" font-size="5">штраф 200 тыс.</text>
        <line x1="170" y1="54" x2="184" y2="54" stroke="#4338ca" stroke-width="1.5" marker-end="url(#intr159-arr)"/>
        <rect x="188" y="32" width="72" height="44" rx="6" fill="#fff" stroke="#cbd5e1" stroke-width="1.2"/>
        <text x="224" y="50" text-anchor="middle" fill="#334155" font-size="5.5" font-weight="700">Кассация</text>
        <text x="224" y="62" text-anchor="middle" fill="#64748b" font-size="5">отказы</text>
        <text x="224" y="72" text-anchor="middle" fill="#64748b" font-size="5">нижест. судов</text>
        <line x1="262" y1="54" x2="276" y2="54" stroke="#059669" stroke-width="1.5" marker-end="url(#intr159-grn)"/>
        <rect x="280" y="20" width="104" height="68" rx="7" fill="#0f172a" stroke="#a31830" stroke-width="1.2"/>
        <text x="332" y="42" text-anchor="middle" fill="#e2e8f0" font-size="6" font-weight="700">ВС РФ</text>
        <text x="332" y="54" text-anchor="middle" fill="#93c5fd" font-size="5.5">14.05.2026</text>
        <text x="332" y="66" text-anchor="middle" fill="#6ee7b7" font-size="5.5">приговор отменён</text>
        <text x="332" y="78" text-anchor="middle" fill="#fcd34d" font-size="5">умысел не доказан</text>
        <text x="195" y="16" text-anchor="middle" fill="#64748b" font-size="6" font-weight="600">№ 85-УД26-2-К1 · Столяров · МУП МРЭП</text>
        <text x="195" y="94" text-anchor="middle" fill="#94a3b8" font-size="5.5">муниципальный контракт · переправа · 44-ФЗ</text>
      </svg>
    </div>
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


def build_faq_section(faq_items: list[tuple[str, str]]) -> str:
    items = []
    for q, a in faq_items:
        items.append(
            f"""<div class="l24-faq__item">
<h3 class="l24-faq__q">{inline_md(q)}</h3>
<p class="l24-faq__a">{inline_md(a)}</p>
</div>"""
        )
    return f"""
<section id="l24-faq-mos-umysel" class="l24-faq" aria-label="Частые вопросы">
<h2>Частые вопросы (FAQ)</h2>
{"".join(items)}
</section>
"""


def build_jsonld(faq_items: list[tuple[str, str]]) -> str:
    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": H1,
        "description": DESCRIPTION,
        "inLanguage": "ru-RU",
        "datePublished": "2026-07-01",
        "dateModified": "2026-07-01",
        "author": {"@type": "Organization", "name": "Legis24"},
        "publisher": {"@type": "Organization", "name": "Legis24"},
        "about": [
            "мошенничество ст 159",
            "ч 3 ст 159 ук рф мошенничество",
            "уголовная ответственность директора",
            "мошенничество при исполнении контракта",
            "умысел при мошенничестве",
            "защита по уголовному делу",
            "адвокат по уголовным делам",
            "дело № 85-УД26-2-К1",
        ],
    }
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", inline_md(a))},
            }
            for q, a in faq_items
        ],
    }
    return (
        f'<script type="application/ld+json">{json.dumps(article, ensure_ascii=False)}</script>\n'
        f'<script type="application/ld+json">{json.dumps(faq, ensure_ascii=False)}</script>'
    )


def page_css() -> str:
    p = PAGE_CLASS
    return f"""
.breadcrumbs,.breadcrumb,.woocommerce-breadcrumb,.rank-math-breadcrumb,.yoast-breadcrumb,
.entry-header,.page-title-section,.entry-title,.main_title,h1.entry-title{{display:none!important}}
#primary,.site-main,.site-content,#content,.content-area{{padding-top:0!important;margin-top:0!important}}
#sidebar,.sidebar,#secondary,.et_pb_column_1_4{{display:none!important}}
.{p} .entry-content{{max-width:none!important;width:100%!important;padding:0!important}}
.{p} .l24-longread-wrap{{max-width:820px;margin:0 auto;padding:48px 24px 80px;font-size:1.05rem;line-height:1.65;color:#1a202c;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
.{p} h2{{margin-top:2.5em;color:#1a365d;font-size:1.45rem;font-weight:800}}
.{p} h3{{margin-top:1.5em;color:#2c5282;font-size:1.15rem;font-weight:700}}
.{p} a{{color:#a31830}}
.{p} table{{width:100%;border-collapse:collapse;margin:1.25em 0;font-size:.95rem}}
.{p} th,.{p} td{{border:1px solid #e2e8f0;padding:10px 12px;text-align:left;vertical-align:top}}
.{p} th{{background:#fff7f7;color:#a31830;font-weight:700}}
.{p} blockquote{{margin:1.5em 0;padding:16px 22px;border-left:4px solid #a31830;background:#fff7f7;color:#334155;font-style:italic;border-radius:0 6px 6px 0;font-size:.98rem;line-height:1.6}}
.{p} p{{margin:0 0 1.1em}}
.{p} ol,.{p} ul{{margin:1em 0;padding-left:1.4em}}
.{p} li{{margin-bottom:.45em}}
.l24-intro-ug{{max-width:1200px;margin:0 auto;padding:40px 24px 8px;font-family:system-ui,sans-serif}}
.l24-intro-ug__grid{{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(260px,.9fr);gap:28px;align-items:start}}
.l24-intro-ug__text{{border-left:4px solid #a31830;padding:4px 0 4px 22px}}
.l24-intro-ug__text p{{margin:0 0 14px;font-size:1.02rem;line-height:1.6;color:#334155}}
.l24-intro-ug__brief{{background:#fff7f7;border:1px solid #fecaca;border-radius:10px;padding:16px 18px;margin-top:16px;font-size:.95rem;line-height:1.55;color:#334155}}
.l24-intro-ug__decor{{background:linear-gradient(160deg,#fff7f7 0%,#fff 100%);border:1px solid #fecaca;border-radius:12px;padding:18px}}
.l24-intro-ug__chips{{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 14px;padding:0;list-style:none}}
.l24-intro-ug__chip{{font-size:.72rem;font-weight:700;padding:6px 10px;border-radius:999px;background:#fff;border:1px solid #cbd5e1;color:#475569}}
.l24-intro-ug__chip--accent{{border-color:#a31830;color:#a31830;background:#fff7f7}}
.l24-intro-ug__chip--ok{{border-color:#059669;color:#047857;background:#ecfdf5}}
.l24-intro-ug__chip--warn{{border-color:#dc2626;color:#991b1b;background:#fef2f2}}
.l24-intro-ug__chip--blue{{border-color:#4338ca;color:#4338ca;background:#f5f3ff}}
.l24-intro-ug__route-svg{{display:block;width:100%;height:auto}}
.ym-toc{{max-width:820px;margin:24px auto 0;padding:0 24px 32px;text-align:center;font-family:system-ui,sans-serif}}
.ym-toc__title{{font-size:.8rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#64748b;margin:0 0 12px}}
.ym-toc__list{{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;justify-content:center;gap:8px 10px}}
.ym-toc__list a{{display:inline-block;padding:8px 12px;border-radius:8px;background:#fff7f7;color:#a31830;text-decoration:none;font-size:.88rem;font-weight:600;border:1px solid #fecaca}}
.ym-toc__list a:hover{{background:#fef2f2}}
.ym-cta{{margin:28px 0;padding:22px 24px;border-radius:10px;background:linear-gradient(135deg,#f8fafc 0%,#fff7f7 100%);border:1px solid #fecaca;border-left:4px solid #a31830}}
.ym-cta--legis24.ym-cta--bottom{{border-left-color:#4338ca;background:linear-gradient(135deg,#f5f3ff 0%,#ede9fe 100%);border-color:#c4b5fd}}
.ym-cta__text{{margin:0 0 14px;line-height:1.55;color:#334155;font-size:.98rem}}
.ym-cta__actions{{margin:0}}
.ym-cta__btn{{display:inline-block;background:#a31830;color:#fff!important;padding:12px 22px;border-radius:8px;font-weight:700;text-decoration:none;font-size:.93rem}}
.ym-cta__btn:hover{{background:#8b1528}}
.ym-cta--legis24.ym-cta--bottom .ym-cta__btn{{background:#4338ca}}
.ym-cta--legis24.ym-cta--bottom .ym-cta__btn:hover{{background:#312e81}}
.l24-faq{{margin:2.5em auto 0;max-width:820px;padding:28px 24px 48px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px}}
.l24-faq h2{{margin-top:0!important;color:#1a365d}}
.l24-faq__item{{margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #e2e8f0}}
.l24-faq__item:last-child{{margin-bottom:0;padding-bottom:0;border-bottom:none}}
.l24-faq__q{{margin:0 0 8px;font-size:1.05rem;color:#1a365d;font-weight:700}}
.l24-faq__a{{margin:0;color:#334155;font-size:.97rem;line-height:1.6}}
@media(max-width:900px){{.l24-intro-ug__grid{{grid-template-columns:1fr}}}}
"""


def main():
    handoff = HANDOFF.read_text(encoding="utf-8")
    alina_path = ROOT / "nero-network-fragments" / "alina.md"
    boris_path = ROOT / "nero-network-fragments" / "boris.md"
    hero = strip_scripts_canvas(
        extract_section_html(alina_path.read_text(encoding="utf-8"), "=== АЛИНА (HERO) ===")
    )
    boris = strip_scripts_canvas(
        extract_section_html(boris_path.read_text(encoding="utf-8"), "=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===")
    )
    artur_md, faq_items, itog_md = extract_artur_parts(handoff)
    p1, p2, brief = parse_intro_paragraphs(artur_md)
    content = md_to_html(artur_md, boris)
    if itog_md:
        content += "\n\n" + md_to_html(itog_md, "")

    html = f"""<!-- wp:html -->
<style>
{page_css()}
</style>
<main id="primary" class="site-main {PAGE_CLASS}" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">
<meta itemprop="headline" content="{H1}">
<meta itemprop="description" content="{DESCRIPTION}">
<meta itemprop="inLanguage" content="ru-RU">

{hero}

{build_intro(p1, p2, brief)}

{build_toc()}

<div class="l24-longread-wrap" itemprop="articleBody">

{content}

</div>

{build_faq_section(faq_items)}

{build_jsonld(faq_items)}
</main>
<!-- /wp:html -->
"""
    html = strip_scripts_canvas(html)
    # Re-inject JSON-LD scripts after strip
    jsonld = build_jsonld(faq_items)
    html = html.replace("</main>", f"\n{jsonld}\n</main>")

    OUT.write_text(html, encoding="utf-8")
    char_count = len(html)

    natasha_block = f"""=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО
SLUG: {SLUG}
ВНИМАНИЕ: MCP-only — без `<canvas>` и `<script>` кроме JSON-LD Article + FAQPage. При публикации обернуть в <!-- wp:html -->

{html}

## Передача Юре
SLUG: {SLUG}
Контент MCP-only: hero static SVG, блок Бориса static SVG, JSON-LD Article. Обязательно обернуть в <!-- wp:html --> при публикации.
Размер HTML: {char_count} символов
main#primary: да
"""

    if "=== НАТАША (HTML СТРАНИЦЫ) ===" in handoff:
        handoff = handoff.split("=== НАТАША (HTML СТРАНИЦЫ) ===")[0].rstrip() + "\n\n" + natasha_block
    else:
        handoff = handoff.rstrip() + "\n\n" + natasha_block
    HANDOFF.write_text(handoff, encoding="utf-8")

    assert 'id="primary"' in html
    assert "l24-boris-vs-moshennichestvo-umysel" in html
    assert 'type="application/ld+json"' in html
    assert "<canvas" not in html.lower()
    script_count = len(re.findall(r"<script", html, re.I))
    assert script_count == 2, f"Expected 2 JSON-LD scripts, got {script_count}"

    print(f"Wrote {OUT}")
    print(f"Chars: {char_count}")
    print(f"main#primary: {'id=\"primary\"' in html}")


if __name__ == "__main__":
    main()
