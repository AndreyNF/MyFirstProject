#!/usr/bin/env python3
"""Сборка page-content-natasha-A5.html для MCP publish (ARB A5)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HANDOFF = ROOT / "nero-network-handoff.md"
ALINA = ROOT / "nero-network-fragments/alina.md"
BORIS = ROOT / "nero-network-fragments/boris.md"
OUT = ROOT / "page-content-natasha-A5.html"
SLUG = "arbitrazhnyj-spor-s-kreditorom-sroki-strategiya"
PAGE_CLASS = f"{SLUG}-page"

H2_IDS = {
    "Три трека защиты: выберите сценарий до первого заседания": "arb-tri-treka",
    "Когда возникает арбитражный спор с кредитором": "arb-kogda",
    "Подсудность: в какой арбитражный суд идти и как оспорить": "arb-podsudnost",
    "Сроки: исковая давность, процессуальные сроки и реестр": "arb-sroki",
    "Первая стратегия ответа: отзыв, возражения, встречный иск": "arb-strategiya",
    "Доказательства и представитель в арбитраже": "arb-dokazatelstva",
    "Чеклист первых 14 дней после получения иска": "arb-cheklist",
    "Банкротство и кредитор: что меняется для ответчика": "arb-bankrotstvo",
    "Типовые ошибки ответчика и когда нужен адвокат": "arb-oshibki",
    "FAQ": "arb-faq",
}

TOC_LABELS = {
    "arb-tri-treka": "Три трека A/B/C",
    "arb-kogda": "Когда возникает спор",
    "arb-podsudnost": "Подсудность",
    "arb-sroki": "Сроки и давность",
    "arb-strategiya": "Отзыв и возражения",
    "arb-dokazatelstva": "Доказательства",
    "arb-cheklist": "Чеклист 14 дней",
    "arb-bankrotstvo": "Банкротство",
    "arb-oshibki": "Ошибки ответчика",
    "arb-faq": "FAQ",
}


def extract_block(path: Path, marker: str) -> str:
    text = path.read_text(encoding="utf-8")
    idx = text.find(marker)
    if idx < 0:
        raise ValueError(f"Marker {marker!r} not found in {path}")
    chunk = text[idx:]
    if marker.startswith("==="):
        chunk = chunk.split("\n", 1)[1]
    return chunk.strip()


def extract_artur_body(handoff: str) -> str:
    start = handoff.find("=== АРТУР (CTA И РЕКЛАМА) ===")
    end = handoff.find("=== АЛИНА (HERO) ===", start)
    block = handoff[start:end]
    m = re.search(r"### Полный текст\n", block)
    if not m:
        raise ValueError("Artur ### Полный текст not found")
    body = block[m.end() :]
    body = body.split("### GEO-чеклист")[0].strip()
    # drop leading H1 duplicate (hero has H1)
    body = re.sub(r"^# .+\n\n", "", body, count=1)
    return body


def slugify_title(title: str) -> str:
    return H2_IDS.get(title.strip(), re.sub(r"[^a-z0-9]+", "-", title.lower())[:40].strip("-"))


def md_inline(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(
        r"`([^`]+)`",
        r"<code>\1</code>",
        s,
    )
    s = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        s,
    )
    s = re.sub(
        r"<a href=\"(https?://[^\"]+)\"(?![^>]*target=)",
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

        if stripped.startswith("<aside") or stripped.startswith("</aside>"):
            block = [line]
            i += 1
            while i < len(lines) and "</aside>" not in lines[i - 1] if i > 0 else True:
                if i < len(lines):
                    block.append(lines[i])
                    if "</aside>" in lines[i]:
                        i += 1
                        break
                    i += 1
            out.append("\n".join(block))
            continue

        if stripped.startswith("<a ") or stripped.startswith("<p>"):
            out.append(md_inline(line))
            i += 1
            continue

        if stripped.startswith("## "):
            title = stripped[3:].strip()
            hid = slugify_title(title)
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

        if stripped.startswith("**") and stripped.endswith("**") and "?" in stripped:
            # FAQ question line
            q = stripped.strip("*")
            out.append(f'<div class="l24-faq-arb__item"><h3 class="l24-faq-arb__q">{md_inline(q)}</h3>')
            i += 1
            ans_parts = []
            while i < len(lines) and lines[i].strip() and not (
                lines[i].strip().startswith("**")
                and "?" in lines[i]
            ) and not lines[i].strip().startswith("##"):
                ans_parts.append(lines[i].strip())
                i += 1
            out.append(f'<p class="l24-faq-arb__a">{md_inline(" ".join(ans_parts))}</p></div>')
            continue

        if not stripped:
            i += 1
            continue

        out.append(f"<p>{md_inline(stripped)}</p>")
        i += 1

    return "\n\n".join(out)


def insert_boris(html: str, boris_html: str) -> str:
    anchor = "<!-- BORIS_ANCHOR -->"
    if anchor in html:
        return html.replace(anchor, boris_html)
    marker = '<h2 id="arb-tri-treka">'
    pos = html.find(marker)
    if pos < 0:
        raise ValueError("H2 три трека not found")
    # after first CTA following tri-treka section
    cta_end = html.find("</aside>", pos)
    if cta_end < 0:
        raise ValueError("CTA after tri-treka not found")
    insert_at = cta_end + len("</aside>")
    return html[:insert_at] + "\n\n" + boris_html + "\n\n" + html[insert_at:]


def extract_boris_html() -> str:
    text = BORIS.read_text(encoding="utf-8")
    m = re.search(r"```html\n(.*?)```", text, re.DOTALL)
    if not m:
        raise ValueError("Boris html block not found")
    return m.group(1).strip()


def extract_hero_html() -> str:
    text = ALINA.read_text(encoding="utf-8")
    m = re.search(
        r"(<section id=\"l24-hero-arb-kred\".*?</section>)",
        text,
        re.DOTALL,
    )
    if not m:
        raise ValueError("Hero section not found in alina.md")
    return m.group(1).strip()


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
.l24-intro-arb {{
  max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.l24-intro-arb__grid {{
  display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
  gap: 28px; align-items: start;
}}
.l24-intro-arb__text {{
  border-left: 4px solid #1e3a8a; padding: 4px 0 4px 22px; text-align: left;
}}
.l24-intro-arb__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.l24-intro-arb__text p:last-child {{ margin-bottom: 0; }}
.l24-intro-arb__brief {{
  background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px;
  padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; line-height: 1.55;
}}
.l24-intro-arb__decor {{
  background: linear-gradient(160deg, #f1f5f9 0%, #fff 100%);
  border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px;
}}
.l24-intro-arb__chips {{
  display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none;
}}
.l24-intro-arb__chip {{
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.03em;
  padding: 6px 10px; border-radius: 999px; background: #fff;
  border: 1px solid #cbd5e1; color: #475569;
}}
.l24-intro-arb__chip--accent {{ border-color: #1e40af; color: #1e40af; }}
.l24-intro-arb__chip--warn {{ border-color: #a31830; color: #a31830; }}
.l24-intro-arb__chip--navy {{ border-color: #0f2744; color: #0f2744; }}
.l24-intro-arb__route-svg {{ display: block; width: 100%; height: auto; }}
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
.l24-faq-arb {{
  margin-top: 2.5em; padding: 28px 24px; background: #f8fafc;
  border: 1px solid #e2e8f0; border-radius: 12px;
}}
.l24-faq-arb > h2 {{ margin-top: 0 !important; }}
.l24-faq-arb__item {{ margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0; }}
.l24-faq-arb__item:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
.l24-faq-arb__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #1a365d; }}
.l24-faq-arb__a {{ margin: 0; color: #334155; }}
.ym-section {{ display: block; }}
@media (max-width: 900px) {{
  .l24-intro-arb__grid {{ grid-template-columns: 1fr; }}
}}
"""

INTRO_HTML = """
<section class="l24-intro-arb ym-section" aria-label="Введение">
  <div class="l24-intro-arb__grid">
    <div class="l24-intro-arb__text">
      <p>Когда банк, поставщик, цессионарий или налоговый орган уже подал <strong>иск в арбитражный суд</strong> или заявление в деле о банкротстве, у ответчика нет роскоши «разобраться потом». <strong>Арбитражные споры</strong> с кредиторами — это процессуальные вилки: подсудность, срок исковой давности, отзыв, обеспечение иска, реестр требований.</p>
      <p>Материал собран с угла <strong>защиты ответчика и должника</strong>, а не инструкции «как взыскать долг». До первого заседания важно выбрать трек A, B или C и сверить срок отзыва с <strong>определением суда</strong>, а не с «15 днями из интернета».</p>
      <div class="l24-intro-arb__brief">
        <strong>Кратко:</strong> отзыв по ст. 131 АПК обязателен; исковая давность — только по заявлению (ст. 199 ГК); в банкротстве на обособленный спор — <strong>1 месяц</strong> на апелляцию (ст. 61 127-ФЗ).
      </div>
    </div>
    <aside class="l24-intro-arb__decor" aria-label="Нормы и треки">
      <ul class="l24-intro-arb__chips">
        <li class="l24-intro-arb__chip l24-intro-arb__chip--navy">АПК ст. 131</li>
        <li class="l24-intro-arb__chip l24-intro-arb__chip--accent">ст. 39 подсудность</li>
        <li class="l24-intro-arb__chip">127-ФЗ реестр</li>
        <li class="l24-intro-arb__chip l24-intro-arb__chip--warn">3 / 10 лет</li>
        <li class="l24-intro-arb__chip">ст. 93 обеспечение</li>
        <li class="l24-intro-arb__chip">трек A/B/C</li>
      </ul>
      <svg class="l24-intro-arb__route-svg" viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Иск кредитора: арбитраж, третейский суд или банкротство">
        <rect x="8" y="8" width="304" height="184" rx="10" fill="#fff" stroke="#cbd5e1"/>
        <text x="24" y="32" fill="#64748b" font-size="10" font-weight="700">ИСК КРЕДИТОРА → РАЗВИЛКА</text>
        <rect x="108" y="44" width="104" height="28" rx="6" fill="#1e3a8a"/>
        <text x="160" y="63" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">ответчик</text>
        <line x1="160" y1="72" x2="56" y2="108" stroke="#63b3ed" stroke-width="2"/>
        <line x1="160" y1="72" x2="160" y2="108" stroke="#5eead4" stroke-width="2"/>
        <line x1="160" y1="72" x2="264" y2="108" stroke="#f56565" stroke-width="2"/>
        <rect x="24" y="112" width="72" height="40" rx="6" fill="#eff6ff" stroke="#93c5fd"/>
        <text x="60" y="132" text-anchor="middle" fill="#1e40af" font-size="8" font-weight="700">АС</text>
        <text x="60" y="144" text-anchor="middle" fill="#64748b" font-size="7">трек A</text>
        <rect x="124" y="112" width="72" height="40" rx="6" fill="#f0fdfa" stroke="#99f6e4"/>
        <text x="160" y="132" text-anchor="middle" fill="#0f766e" font-size="8" font-weight="700">третейский</text>
        <rect x="224" y="112" width="72" height="40" rx="6" fill="#fef2f2" stroke="#fca5a5"/>
        <text x="260" y="132" text-anchor="middle" fill="#b91c1c" font-size="8" font-weight="700">127-ФЗ</text>
        <text x="260" y="144" text-anchor="middle" fill="#64748b" font-size="7">трек B/C</text>
        <rect x="24" y="158" width="272" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
        <text x="160" y="176" text-anchor="middle" fill="#0f2744" font-size="9" font-weight="700">14 дней · срок из определения суда</text>
      </svg>
    </aside>
  </div>
</section>
"""

TOC_HTML = """
<nav class="ym-toc" aria-label="Содержание статьи">
  <p class="ym-toc__title">По статье</p>
  <ul class="ym-toc__list">
""" + "\n".join(
    f'    <li><a href="#{hid}">{TOC_LABELS[hid]}</a></li>' for hid in TOC_LABELS
) + """
  </ul>
</nav>
"""


def wrap_faq(html: str) -> str:
    m = re.search(r'(<h2 id="arb-faq">.*)', html, re.DOTALL)
    if not m:
        return html
    faq_part = m.group(1)
    before = html[: m.start()]
    faq_part = faq_part.replace('<h2 id="arb-faq">FAQ</h2>', '<section class="l24-faq-arb ym-section"><h2 id="arb-faq">Частые вопросы (FAQ)</h2>', 1)
    if not faq_part.rstrip().endswith("</section>"):
        faq_part = faq_part.rstrip() + "\n</section>"
    return before + faq_part


def main():
    handoff = HANDOFF.read_text(encoding="utf-8")
    artur_md = extract_artur_body(handoff)
    body = md_to_html(artur_md)
    # Лид уже во вступлении (l24-intro-arb)
    body = re.sub(
        r"^<p>Когда банк, поставщик.*?</p>\n\n",
        "",
        body,
        count=1,
        flags=re.DOTALL,
    )
    body = insert_boris(body, extract_boris_html())
    body = wrap_faq(body)

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
    has_main = 'id="primary"' in html
    print(f"Wrote {OUT}")
    print(f"Size: {size_kb:.1f} KB")
    print(f"main#primary: {has_main}")


if __name__ == "__main__":
    main()
