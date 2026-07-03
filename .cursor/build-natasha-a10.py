#!/usr/bin/env python3
"""Сборка page-content-natasha-A10.html (UG A10 — защита на стадии проверки)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HANDOFF = ROOT / "nero-network-handoff.md"
ALINA = ROOT / "nero-network-fragments/alina.md"
BORIS = ROOT / "nero-network-fragments/boris.md"
OUT = ROOT / "page-content-natasha-A10.html"
SLUG = "zashchita-po-ugolovnomu-delu-stadiya-proverki"
PAGE_CLASS = f"{SLUG}-page"

TITLE = "Защита по уголовному делу на стадии проверки и в суде: права и тактика | Legis24"
DESCRIPTION = (
    "Права подозреваемого и обвиняемого на проверке сообщения о преступлении, "
    "при допросе и следственных действиях; роль адвоката, ходатайства и защита в суде. "
    "Консультация по уголовному делу и рискам."
)

H2_IDS = {
    "Зачем подключать защиту сразу: стадии от проверки до суда": "ug-stadii",
    "Права подозреваемого и обвиняемого: что разъясняют по УПК": "ug-prava",
    "Адвокат и защитник: участие, полномочия, назначение": "ug-advokat",
    "Следственные действия: допрос, задержание, обыск — тактика защиты": "ug-sledstvie",
    "Предъявление обвинения и ознакомление с материалами дела": "ug-obvinenie",
    "Меры пресечения: избрание, срок, обжалование": "ug-mery",
    "Ходатайства защиты на следствии и перед судом": "ug-hodataystva",
    "Защита в суде: судебное разбирательство и позиция по делу": "ug-sud",
    "Два трека защиты и чеклист первых 72 часов": "ug-treki",
    "Типовые ошибки подозреваемого и когда нужна консультация": "ug-oshibki",
    "Судебная практика: что учитывать в 2024–2026": "ug-praktika",
    "FAQ": "ug-faq",
}

TOC_LABELS = {
    "ug-stadii": "Стадии: проверка → суд",
    "ug-prava": "Права по УПК",
    "ug-advokat": "Адвокат и защитник",
    "ug-sledstvie": "Допрос и обыск",
    "ug-obvinenie": "Обвинение и ст. 217",
    "ug-mery": "Меры пресечения",
    "ug-hodataystva": "Ходатайства",
    "ug-sud": "Защита в суде",
    "ug-treki": "Два трека · 72 часа",
    "ug-oshibki": "Типовые ошибки",
    "ug-praktika": "Практика 2024–2026",
    "ug-faq": "FAQ",
}


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
    body = body.split("## GEO-чеклист")[0].strip()
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

        if stripped.startswith("<") and stripped.endswith(">"):
            out.append(line)
            i += 1
            continue

        if stripped.startswith("## "):
            title = stripped[3:].strip()
            hid = slugify_title(title)
            if hid == "ug-faq":
                out.append(
                    f'<section id="{hid}" class="l24-faq-ug ym-section" aria-label="Частые вопросы">'
                )
                out.append("<h2>Частые вопросы (FAQ)</h2>")
            else:
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

        if re.match(r"^\*\*\d+\.\s", stripped):
            q = re.sub(r"^\*\*|\*\*$", "", stripped).strip()
            out.append(f'<div class="l24-faq-ug__item"><h3 class="l24-faq-ug__q">{md_inline(q)}</h3>')
            i += 1
            ans_parts = []
            while i < len(lines):
                s = lines[i].strip()
                if not s:
                    if ans_parts:
                        break
                    i += 1
                    continue
                if re.match(r"^\*\*\d+\.\s", s) or s.startswith("##"):
                    break
                ans_parts.append(s)
                i += 1
            out.append(f'<p class="l24-faq-ug__a">{md_inline(" ".join(ans_parts))}</p></div>')
            continue

        if not stripped:
            i += 1
            continue

        out.append(f"<p>{md_inline(stripped)}</p>")
        i += 1

    html = "\n\n".join(out)
    if '<section id="ug-faq"' in html and not html.rstrip().endswith("</section>"):
        html = html.rstrip() + "\n</section>"
    return html


def extract_boris_html() -> str:
    text = BORIS.read_text(encoding="utf-8")
    m = re.search(r"```html\n(.*?)```", text, re.DOTALL)
    if not m:
        raise ValueError("Boris html block not found")
    return m.group(1).strip()


def extract_hero_html() -> str:
    text = ALINA.read_text(encoding="utf-8")
    m = re.search(
        r'(<section id="l24-hero-ug-defense".*?</section>)',
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
    return html.replace(anchor, boris_html)


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
.l24-intro-ug {{
  max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.l24-intro-ug__grid {{
  display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
  gap: 28px; align-items: start;
}}
.l24-intro-ug__text {{
  border-left: 4px solid #7f1d1d; padding: 4px 0 4px 22px; text-align: left;
}}
.l24-intro-ug__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.l24-intro-ug__text p:last-child {{ margin-bottom: 0; }}
.l24-intro-ug__brief {{
  background: #fafaf9; border: 1px solid #e7e5e4; border-radius: 10px;
  padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; line-height: 1.55;
}}
.l24-intro-ug__decor {{
  background: linear-gradient(160deg, #f5f4f1 0%, #fff 100%);
  border: 1px solid #e7e5e4; border-radius: 12px; padding: 18px;
}}
.l24-intro-ug__chips {{
  display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none;
}}
.l24-intro-ug__chip {{
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.03em;
  padding: 6px 10px; border-radius: 999px; background: #fff;
  border: 1px solid #cbd5e1; color: #475569;
}}
.l24-intro-ug__chip--accent {{ border-color: #1e3a5f; color: #1e3a5f; }}
.l24-intro-ug__chip--warn {{ border-color: #a31830; color: #a31830; }}
.l24-intro-ug__chip--navy {{ border-color: #57534e; color: #44403c; }}
.l24-intro-ug__route-svg {{ display: block; width: 100%; height: auto; }}
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
.l24-faq-ug {{
  margin-top: 2.5em; padding: 28px 24px; background: #f8fafc;
  border: 1px solid #e2e8f0; border-radius: 12px;
}}
.l24-faq-ug > h2 {{ margin-top: 0 !important; }}
.l24-faq-ug__item {{ margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0; }}
.l24-faq-ug__item:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
.l24-faq-ug__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #1a365d; }}
.l24-faq-ug__a {{ margin: 0; color: #334155; }}
.ym-section {{ display: block; }}
@media (max-width: 900px) {{
  .l24-intro-ug__grid {{ grid-template-columns: 1fr; }}
}}
"""

INTRO_HTML = """
<section class="l24-intro-ug ym-section" aria-label="Введение">
  <div class="l24-intro-ug__grid">
    <div class="l24-intro-ug__text">
      <p>Вызов в отдел, обыск, постановление о возбуждении — для гражданина и предпринимателя это не «теория стадий», а угроза свободе и бизнесу. <strong>Защита по уголовному делу</strong> начинается в первые часы контакта с органом, а не в зале суда.</p>
      <p>Ниже — операционная карта стороны защиты: статус (проверка, подозреваемый, обвиняемый), права по <strong>ч. 1.1 ст. 144</strong> и ст. 46–53 УПК, допрос, ходатайства и линия до <strong>ст. 217</strong> и суда. Без энциклопедии УК — только процесс и тактика.</p>
      <div class="l24-intro-ug__brief">
        <strong>Кратко:</strong> на проверке уже действуют адвокат и отказ от объяснений; сроки по ст. 144 — <strong>3 / 10 / 30 суток</strong>; задержание — до <strong>48 ч</strong> (по ряду статей — 72); следствие — <strong>2 месяца</strong> с продлениями.
      </div>
    </div>
    <aside class="l24-intro-ug__decor" aria-label="Стадии и нормы УПК">
      <ul class="l24-intro-ug__chips">
        <li class="l24-intro-ug__chip l24-intro-ug__chip--navy">ч. 1.1 ст. 144</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--accent">ст. 46–53</li>
        <li class="l24-intro-ug__chip">ст. 216–217</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--warn">3 / 10 / 30</li>
        <li class="l24-intro-ug__chip">гл. 16 жалобы</li>
        <li class="l24-intro-ug__chip">72 часа</li>
      </ul>
      <svg class="l24-intro-ug__route-svg" viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Проверка, следствие, суд: линия защиты подозреваемого">
        <rect x="8" y="8" width="304" height="184" rx="10" fill="#fff" stroke="#d6d3d1"/>
        <text x="24" y="32" fill="#57534e" font-size="10" font-weight="700">СТАДИИ ЗАЩИТЫ</text>
        <circle cx="56" cy="96" r="20" fill="#57534e"/><text x="56" y="101" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">144</text>
        <text x="56" y="130" text-anchor="middle" fill="#44403c" font-size="8">проверка</text>
        <circle cx="160" cy="96" r="20" fill="#1e3a5f"/><text x="160" y="101" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">216</text>
        <text x="160" y="130" text-anchor="middle" fill="#1e3a5f" font-size="8">следствие</text>
        <circle cx="264" cy="96" r="20" fill="#7f1d1d"/><text x="264" y="101" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">51</text>
        <text x="264" y="130" text-anchor="middle" fill="#7f1d1d" font-size="8">суд</text>
        <line x1="76" y1="96" x2="140" y2="96" stroke="#94a3b8" stroke-width="2"/>
        <line x1="180" y1="96" x2="244" y2="96" stroke="#94a3b8" stroke-width="2"/>
        <rect x="24" y="148" width="272" height="36" rx="6" fill="#fafaf9" stroke="#e7e5e4"/>
        <text x="160" y="170" text-anchor="middle" fill="#1c1917" font-size="10" font-weight="700">адвокат · молчание · ст. 217</text>
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
        r"^<p>Вызов в отдел.*?</p>\n\n<p>Ниже — операционная.*?</p>\n\n",
        "",
        body,
        count=1,
        flags=re.DOTALL,
    )

    body = insert_boris(body, extract_boris_html())
    hero = extract_hero_html()

    html = f"""<!-- wp:html -->
<style>
{PAGE_CSS}
</style>
<main id="primary" class="site-main {PAGE_CLASS}" role="main" tabindex="-1">

{hero}

{INTRO_HTML}

{TOC_HTML}

<section class="ym-section">
<div class="l24-longread-wrap">

{body}

</div>
</section>

</main>
<!-- /wp:html -->
"""

    OUT.write_text(html, encoding="utf-8")
    size_kb = len(html.encode("utf-8")) / 1024

    natasha_block = f"""
=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО

**Файл:** `{OUT.relative_to(ROOT.parent)}`
**SLUG:** `{SLUG}`
**Title:** {TITLE}
**Description:** {DESCRIPTION}

ВНИМАНИЕ: без `<script>` и `<canvas>` — hero и Борис static SVG + inline CSS (MCP publish удаляет scripts).

```html
{html}
```

## Передача Юре

**slug:** `{SLUG}`
**page_id:** `PLACEHOLDER` (после wordpress_create_page)
**Публикация:** blob flow, `<!-- wp:html -->`; проверить `main#primary`, класс `{PAGE_CLASS}`, hero `#l24-hero-ug-defense`, Boris `#l24-boris-ug-defense-stages`.
"""

    if "=== НАТАША (HTML СТРАНИЦЫ) ===" in handoff:
        handoff = handoff.split("=== НАТАША (HTML СТРАНИЦЫ) ===")[0].rstrip() + "\n" + natasha_block
    else:
        handoff = handoff.rstrip() + "\n" + natasha_block
    HANDOFF.write_text(handoff, encoding="utf-8")

    print(f"Wrote {OUT}")
    print(f"Size: {size_kb:.1f} KB")
    print(f'main#primary: {"id=\"primary\"" in html}')


if __name__ == "__main__":
    main()
