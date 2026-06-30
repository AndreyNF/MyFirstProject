#!/usr/bin/env python3
"""Assemble Natasha HTML for plenum-vs-19 UG article (MCP-only, no canvas/script)."""
import json
import re
from pathlib import Path

SLUG = "plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026"
HANDOFF = Path(".cursor/nero-network-handoff.md")
OUT = Path(".cursor/page-content-natasha-plenum19.html")

H1 = "Пленум ВС № 19 (2026): цифровой рубль как предмет кражи — когда обман это не мошенничество"
DESC = (
    "16.06.2026: Пленум ВС РФ № 19 разъяснил квалификацию хищений цифрового рубля и цифровых прав, "
    "отличие кражи от мошенничества и условия ст. 158.1 УК РФ. Защита при обвинении."
)
CANONICAL = "https://vsrf.ru/press_center/news/36011/"


def extract_block(text: str, start_marker: str, end_marker: str | None = None) -> str:
    i = text.find(start_marker)
    if i < 0:
        raise ValueError(f"Marker not found: {start_marker}")
    i = text.find("```html", i)
    if i < 0:
        raise ValueError(f"No html block after {start_marker}")
    i = text.find("\n", i) + 1
    j = text.find("```", i)
    block = text[i:j].strip()
    if end_marker:
        k = block.find(end_marker)
        if k >= 0:
            block = block[:k]
    return block


def extract_arthur_md(text: str) -> str:
    m = re.search(
        r"=== АРТУР \(CTA И РЕКЛАМА\) ===.*?### Полный текст\n\n(.*?)\n\n### Рекламные вставки",
        text,
        re.S,
    )
    if not m:
        raise ValueError("Arthur content not found")
    return m.group(1).strip()


def slugify(title: str) -> str:
    t = title.lower().replace("ё", "е")
    t = re.sub(r"[«»\"'():]", "", t)
    t = re.sub(r"[^a-z0-9а-я]+", "-", t)
    return t.strip("-")[:72]


def inline_md(s: str) -> str:
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        s,
    )
    return s


def _is_separator_row(cells: list[str]) -> bool:
    return all(re.match(r"^[-: ]+$", c) for c in cells if c)


def md_table(block: str) -> str:
    lines = [ln.strip() for ln in block.strip().splitlines() if ln.strip()]
    if len(lines) < 2:
        return f"<p>{inline_md(block)}</p>"
    rows = []
    for ln in lines:
        if re.match(r"^\|?[\s\-:|]+\|?$", ln) and "-" in ln:
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if _is_separator_row(cells):
            continue
        rows.append(cells)
    if not rows:
        return ""
    head, body = rows[0], rows[1:]
    out = ["<table><thead><tr>"]
    for c in head:
        out.append(f"<th scope=\"col\">{inline_md(c)}</th>")
    out.append("</tr></thead><tbody>")
    for row in body:
        out.append("<tr>")
        for c in row:
            out.append(f"<td>{inline_md(c)}</td>")
        out.append("</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def md_paragraph(p: str) -> str:
    p = p.strip()
    if not p:
        return ""
    if p.startswith("> "):
        q = inline_md(p[2:].strip())
        return f"<blockquote><p>{q}</p></blockquote>"
    if p.startswith("|"):
        return md_table(p)
    if p.startswith("- [ ]") or p.startswith("- [x]"):
        items = []
        for ln in p.splitlines():
            ln = ln.strip()
            m = re.match(r"^- \[[ x]\] (.+)$", ln)
            if m:
                items.append(f"<li>{inline_md(m.group(1))}</li>")
        return f'<ul class="l24-checklist">{"".join(items)}</ul>'
    if re.match(r"^- ", p):
        items = [f"<li>{inline_md(m.group(1))}</li>" for m in re.finditer(r"^- (.+)$", p, re.M)]
        return "<ul>" + "".join(items) + "</ul>"
    if re.match(r"^\d+\. ", p):
        items = [f"<li>{inline_md(m.group(1))}</li>" for m in re.finditer(r"^\d+\. (.+)$", p, re.M)]
        return "<ol>" + "".join(items) + "</ol>"
    return f"<p>{inline_md(p)}</p>"


def convert_md_to_html(md: str) -> tuple[str, list[tuple[str, str]]]:
    """Returns HTML and list of (id, title) for H2 sections."""
    md = re.sub(r"<aside[\s\S]*?</aside>", "", md)
    parts = re.split(r"\n(?=## )", md)
    html_parts = []
    toc = []
    for part in parts:
        part = part.strip()
        if not part.startswith("## "):
            if part:
                for para in re.split(r"\n\n+", part):
                    h = md_paragraph(para)
                    if h:
                        html_parts.append(h)
            continue
        lines = part.split("\n", 1)
        h2_title = lines[0][3:].strip()
        body = lines[1] if len(lines) > 1 else ""
        hid = slugify(h2_title)
        toc.append((hid, h2_title))
        html_parts.append(f'<h2 id="{hid}">{inline_md(h2_title)}</h2>')
        chunks = re.split(r"\n(?=### )", body)
        for chunk in chunks:
            chunk = chunk.strip()
            if not chunk:
                continue
            if chunk.startswith("### "):
                sub_lines = chunk.split("\n", 1)
                h3 = sub_lines[0][4:].strip()
                sub_body = sub_lines[1] if len(sub_lines) > 1 else ""
                html_parts.append(f"<h3>{inline_md(h3)}</h3>")
                for para in re.split(r"\n\n+", sub_body.strip()):
                    h = md_paragraph(para)
                    if h:
                        html_parts.append(h)
            else:
                for para in re.split(r"\n\n+", chunk):
                    h = md_paragraph(para)
                    if h:
                        html_parts.append(h)
    return "\n".join(html_parts), toc


def insert_boris(body_html: str, boris_html: str) -> str:
    marker = "<h3>Переквалификация со ст. 159 на ст. 158"
    idx = body_html.find(marker)
    if idx < 0:
        raise ValueError("Boris insertion point not found")
    return body_html[:idx] + "\n" + boris_html + "\n" + body_html[idx:]


def insert_ctas(body_html: str) -> str:
    cta1 = """<aside class="ym-cta ym-cta--primary" role="complementary">
  <p class="ym-cta__text">Следствие квалифицировало дело как мошенничество, а фактически было тайное списание? По Пленуму № 19 это может быть кража по ст. 158 — от квалификации зависят срок и мера пресечения.</p>
  <p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Помочь с переквалификацией кражи и мошенничества</a></p>
</aside>"""
    cta2 = """<aside class="ym-cta ym-cta--primary" role="complementary">
  <p class="ym-cta__text">Обвинение по ст. 158.1 требует проверки четырёх условий из п. 17.1 Пленума: административное дело само по себе не доказывает вину по УК.</p>
  <p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по защите при ст. 158.1</a></p>
</aside>"""
    cta3 = """<aside class="ym-cta ym-cta--primary" role="complementary">
  <p class="ym-cta__text">На стадии доследственной проверки и следствия важно выстроить линию защиты до первых показаний: квалификация по ст. 158 или 159, доказательства тайного списания, ходатайства о переквалификации.</p>
  <p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Помощь с защитой в уголовном деле о хищении</a></p>
</aside>"""
    cta_bottom = """<aside class="ym-cta ym-cta--legis24 ym-cta--bottom" role="complementary">
  <p class="ym-cta__text">Постановление Пленума ВС РФ № 19 от 16.06.2026 меняет расклад в делах о хищении цифровых рублей, списаниях с карт и повторном мелком хищении. От правильной квалификации — кража или мошенничество, ст. 158.1 или п. «г» ч. 3 ст. 158 — зависят сроки, мера пресечения и итог суда.</p>
  <p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по защите при квалификации хищения цифровых активов</a></p>
</aside>"""

    m1 = "<h2 id=\"ст-158-1-ук-рф"
    i1 = body_html.find(m1)
    if i1 < 0:
        m1 = "<h2 id="
        i1 = body_html.find("ст-158-1", body_html.find("мелкое хищение"))
    body_html = body_html[:i1] + "\n" + cta1 + "\n" + body_html[i1:]

    m2 = "<h2 id=\"квалификация-хищений"
    i2 = body_html.find(m2)
    body_html = body_html[:i2] + "\n" + cta2 + "\n" + body_html[i2:]

    m3 = "<h2 id=\"кому-актуально"
    i3 = body_html.find(m3)
    body_html = body_html[:i3] + "\n" + cta3 + "\n" + body_html[i3:]

    faq_marker = '<h2 id="частые-вопросы">'
    fi = body_html.find(faq_marker)
    if fi >= 0:
        rest = body_html[fi:]
        rest = re.sub(
            r"<h2 id=\"получите-консультацию[^\"]*\">.*",
            "",
            rest,
            flags=re.S,
        )
        body_html = body_html[:fi] + rest.rstrip() + "\n" + cta_bottom + "\n"

    body_html = re.sub(
        r"\[Консультация по уголовным рискам при хищении цифровых активов\]\(https://advokat-vsem\.ru/\)",
        '<p><a href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по уголовным рискам при хищении цифровых активов</a> — разбор ситуации по критериям Пленума № 19 до дачи показаний.</p>',
        body_html,
    )
    return body_html


def faq_section(body_html: str) -> str:
    faq_start = body_html.find('<h2 id="частые-вопросы">')
    if faq_start < 0:
        return body_html
    faq_end = body_html.find("<aside", faq_start)
    if faq_end < 0:
        faq_end = len(body_html)
    chunk = body_html[faq_start:faq_end]
    chunk = re.sub(r'<h2 id="частые-вопросы">.*?</h2>\s*', "", chunk, count=1)
    # FAQ in source: **Question?**\nAnswer paragraph
    items = re.findall(r"\*\*([^*]+\?)\*\*\s*\n(.+?)(?=\s*\*\*[^*]+\?\*\*|\Z)", chunk, re.S)
    if not items:
        items = re.findall(
            r"<p><strong>([^<]+\?)</strong>\s*(?:</p>\s*<p>)?(.+?)(?:</p>|(?=<p><strong>))",
            chunk,
            re.S,
        )
    if not items:
        items = re.findall(r"<p><strong>([^<]+\?)</strong></p>\s*<p>(.+?)</p>", chunk, re.S)
    faq_html = ['<section id="l24-faq-plenum19" class="l24-faq-ug" aria-label="Частые вопросы">', "<h2>Частые вопросы</h2>"]
    for q, a in items:
        faq_html.append('<div class="l24-faq-ug__item">')
        faq_html.append(f'<p class="l24-faq-ug__q">{inline_md(q.strip())}</p>')
        ans = a.strip()
        if ans.startswith("<p>"):
            faq_html.append(f'<div class="l24-faq-ug__a">{ans}</div>')
        else:
            faq_html.append(f'<p class="l24-faq-ug__a">{inline_md(ans)}</p>')
        faq_html.append("</div>")
    faq_html.append("</section>")
    return body_html[:faq_start] + "\n".join(faq_html) + body_html[faq_end:]


def strip_hero_inner_style(hero: str) -> str:
    hero = re.sub(r"<style>[\s\S]*?</style>\s*", "", hero, count=1)
    return hero.strip()


def hero_css() -> str:
    return """
.l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026 {
  position: relative; min-height: 88vh; min-height: 88dvh; box-sizing: border-box;
  display: flex; align-items: center; padding: 112px 24px 72px;
  background: linear-gradient(158deg, #fefefe 0%, #f0f9ff 42%, #ecfeff 100%);
  color: #0f172a; font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  overflow: hidden;
}
.l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026::before {
  content: ""; position: absolute; inset: 0;
  background: radial-gradient(ellipse 44% 36% at 88% 10%, rgba(3,105,161,.08) 0%, transparent 55%),
    radial-gradient(ellipse 38% 32% at 8% 88%, rgba(13,148,136,.07) 0%, transparent 52%);
  pointer-events: none;
}
.l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__inner {
  position: relative; z-index: 1; max-width: 1200px; margin: 0 auto; width: 100%;
  display: grid; grid-template-columns: 1.04fr 0.96fr; gap: 44px; align-items: center;
}
.l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__badge {
  display: inline-flex; align-items: center; gap: 10px; margin: 0 0 18px; padding: 8px 14px;
  border-radius: 999px; background: rgba(255,255,255,.96); border: 1px solid rgba(15,23,42,.1);
  font-size: .78rem; font-weight: 600; letter-spacing: .04em; text-transform: uppercase; color: #334155;
}
.l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__badge-mark {
  width: 8px; height: 8px; border-radius: 50%; background: #1e3a5f; flex-shrink: 0;
}
.l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__h1 {
  margin: 0 0 18px; font-size: clamp(1.38rem, 3vw, 2.1rem); line-height: 1.24;
  font-weight: 800; color: #0f172a; letter-spacing: -.02em;
}
.l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__h1-accent { color: #1e3a5f; }
.l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__sub {
  margin: 0 0 26px; max-width: 42em; font-size: clamp(.98rem, 1.48vw, 1.1rem);
  line-height: 1.58; color: #475569;
}
.l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__facts {
  display: flex; flex-wrap: wrap; gap: 10px; margin: 0; padding: 0; list-style: none;
}
.l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact {
  font-size: .76rem; font-weight: 700; padding: 7px 12px; border-radius: 8px;
  background: #fff; border: 1px solid #e2e8f0; color: #334155;
}
.l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact--vs { border-color: #93c5fd; color: #1e3a5f; background: #eff6ff; }
.l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact--theft { border-color: #5eead4; color: #0f766e; background: #f0fdfa; }
.l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact--fraud { border-color: #fecaca; color: #991b1b; background: #fef2f2; }
.l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact--ruble { border-color: #7dd3fc; color: #0369a1; background: #f0f9ff; }
.l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__visual { display: flex; justify-content: center; align-items: center; }
@media (max-width: 900px) {
  .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026 { min-height: auto; padding: 96px 20px 56px; }
  .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__inner { grid-template-columns: 1fr; gap: 30px; }
  .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__visual { order: -1; max-height: 320px; }
}
"""


def page_css() -> str:
    p = f".{SLUG}-page"
    return f"""
.breadcrumbs,.breadcrumb,.woocommerce-breadcrumb,.rank-math-breadcrumb,.yoast-breadcrumb,
.entry-header,.page-title-section,.entry-title,.main_title,h1.entry-title{{display:none!important}}
#primary,.site-main,.site-content,#content,.content-area{{padding-top:0!important;margin-top:0!important}}
#sidebar,.sidebar,#secondary,.et_pb_column_1_4{{display:none!important}}
{p} .entry-content{{max-width:none!important;width:100%!important;padding:0!important}}
{p} .l24-longread-wrap{{
  max-width:820px;margin:0 auto;padding:48px 24px 80px;font-size:1.05rem;line-height:1.65;color:#1a202c;
  font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
}}
{p} h2{{margin-top:2.5em;color:#1a365d;font-size:1.45rem;font-weight:800}}
{p} h3{{margin-top:1.5em;color:#1e3a5f;font-size:1.15rem;font-weight:700}}
{p} table{{width:100%;border-collapse:collapse;margin:1.5em 0;font-size:.95rem}}
{p} th,{p} td{{border:1px solid #e2e8f0;padding:10px 12px;text-align:left;vertical-align:top}}
{p} th{{background:#eff6ff;color:#1e3a5f}}
{p} a{{color:#0369a1}}
{p} blockquote{{
  margin:1.5em 0;padding:16px 22px;border-left:4px solid #0d9488;background:#f0fdfa;
  color:#334155;font-style:italic;border-radius:0 6px 6px 0;
}}
{p} ol,{p} ul{{margin:1em 0;padding-left:1.4em}}
{p} li{{margin-bottom:.45em}}
{p} .l24-checklist{{list-style:none;padding-left:0}}
{p} .l24-checklist li{{padding-left:1.6em;position:relative}}
{p} .l24-checklist li::before{{content:"☐";position:absolute;left:0;color:#0d9488}}
.l24-intro-ug{{max-width:1200px;margin:0 auto;padding:40px 24px 8px}}
.l24-intro-ug__grid{{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(260px,.9fr);gap:28px;align-items:start}}
.l24-intro-ug__text{{border-left:4px solid #1e3a5f;padding:4px 0 4px 22px}}
.l24-intro-ug__text p{{margin:0 0 14px;font-size:1.02rem;line-height:1.6;color:#334155}}
.l24-intro-ug__brief{{
  background:#f0f9ff;border:1px solid #bae6fd;border-radius:10px;padding:16px 18px;
  margin-top:16px;font-size:.95rem;line-height:1.55;color:#334155;
}}
.l24-intro-ug__decor{{
  background:linear-gradient(160deg,#f0f9ff 0%,#fff 100%);border:1px solid #e2e8f0;
  border-radius:12px;padding:18px;
}}
.l24-intro-ug__chips{{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 14px;padding:0;list-style:none}}
.l24-intro-ug__chip{{
  font-size:.72rem;font-weight:700;padding:6px 10px;border-radius:999px;background:#fff;
  border:1px solid #cbd5e1;color:#475569;
}}
.l24-intro-ug__chip--accent{{border-color:#0369a1;color:#0369a1;background:#f0f9ff}}
.l24-intro-ug__chip--theft{{border-color:#0d9488;color:#0f766e;background:#f0fdfa}}
.l24-intro-ug__chip--fraud{{border-color:#b91c1c;color:#991b1b;background:#fef2f2}}
.ym-toc{{max-width:820px;margin:24px auto 0;padding:0 24px 32px;text-align:center}}
.ym-toc__title{{
  font-size:.8rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
  color:#64748b;margin:0 0 12px;
}}
.ym-toc__list{{
  list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;justify-content:center;gap:8px 10px;
}}
.ym-toc__list a{{
  display:inline-block;padding:8px 12px;border-radius:8px;background:#f0f9ff;color:#0369a1;
  text-decoration:none;font-size:.88rem;font-weight:600;border:1px solid #bae6fd;
}}
.ym-cta{{
  margin:28px 0;padding:22px 24px;border-radius:10px;
  background:linear-gradient(135deg,#f8fafc 0%,#f0f9ff 100%);
  border:1px solid #cbd5e1;border-left:4px solid #0d9488;
}}
.ym-cta--primary{{border-left-color:#0d9488}}
.ym-cta--legis24.ym-cta--bottom{{
  border-left-color:#1e3a5f;background:linear-gradient(135deg,#eff6ff 0%,#f0f9ff 100%);border-color:#93c5fd;
}}
.ym-cta__text{{margin:0 0 14px;line-height:1.55;color:#334155}}
.ym-cta__actions{{margin:0}}
.ym-cta__btn{{
  display:inline-block;background:#0d9488;color:#fff!important;padding:12px 22px;border-radius:8px;
  font-weight:700;text-decoration:none;font-size:.93rem;
}}
.ym-cta__btn:hover{{background:#0f766e}}
.ym-cta--legis24.ym-cta--bottom .ym-cta__btn{{background:#1e3a5f}}
.ym-cta--legis24.ym-cta--bottom .ym-cta__btn:hover{{background:#0f2744}}
.l24-faq-ug{{margin-top:2.5em;padding:28px 24px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px}}
.l24-faq-ug h2{{margin-top:0!important}}
.l24-faq-ug__item{{margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #e2e8f0}}
.l24-faq-ug__item:last-child{{margin-bottom:0;padding-bottom:0;border-bottom:none}}
.l24-faq-ug__q{{margin:0 0 8px;font-size:1.05rem;color:#1a365d;font-weight:700}}
.l24-faq-ug__a{{margin:0;color:#334155;line-height:1.6}}
.l24-reveal{{
  opacity:0;transform:translateY(18px);
  animation:l24-p19-reveal .65s ease forwards;
  animation-delay:var(--reveal-delay,0ms);
}}
@keyframes l24-p19-reveal{{to{{opacity:1;transform:none}}}}
@media (prefers-reduced-motion:reduce){{.l24-reveal{{opacity:1;transform:none;animation:none}}}}
@media (max-width:900px){{.l24-intro-ug__grid{{grid-template-columns:1fr}}}}
"""


def boris_css_inline() -> str:
    """Boris block ships with its own style — keep as-is from handoff."""
    return ""


def build_toc(toc: list[tuple[str, str]]) -> str:
    items = []
    for hid, title in toc:
        if "частые вопросы" in hid or "получите консультацию" in hid:
            continue
        short = title if len(title) <= 48 else title[:45] + "…"
        items.append(f'<li><a href="#{hid}">{short}</a></li>')
    items.append('<li><a href="#l24-faq-plenum19">Частые вопросы</a></li>')
    return (
        '<nav class="ym-toc l24-reveal" aria-label="Содержание статьи" style="--reveal-delay:120ms">'
        '<p class="ym-toc__title">Содержание</p>'
        f'<ol class="ym-toc__list">{"".join(items)}</ol></nav>'
    )


def json_ld() -> str:
    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": H1,
        "description": DESC,
        "inLanguage": "ru-RU",
        "datePublished": "2026-06-16",
        "dateModified": "2026-06-30",
        "author": {"@type": "Organization", "name": "Legis24"},
        "publisher": {"@type": "Organization", "name": "Legis24"},
        "mainEntityOfPage": CANONICAL,
        "about": [
            "Пленум ВС № 19 2026",
            "цифровой рубль кража",
            "ст 158.1 ук рф",
            "отличие кражи от мошенничества",
            "защита по уголовным делам",
        ],
    }
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": "Что изменил постановление Пленума ВС № 19 от 16.06.2026?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Пленум внёс 15 изменений в разъяснения по краже, грабежу и разбою: закрепил цифровой рубль, цифровые права и цифровую валюту как предмет хищения, уточнил критерий «обман только для доступа», момент окончания кражи при списании безналичных ДС и чеклист проверок по ст. 158.1 УК РФ.",
                },
            },
            {
                "@type": "Question",
                "name": "Цифровой рубль — предмет кражи по УК РФ?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Да. Пленум прямо относит цифровые рубли к безналичным денежным средствам — объектам кражи по ст. 158 УК РФ.",
                },
            },
            {
                "@type": "Question",
                "name": "Чем отличается кража от мошенничества после Пленума № 19?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Если обман использован только для доступа, а имущество изъято тайно — это кража (ст. 158). Если потерпевший сам передал деньги — мошенничество (ст. 159).",
                },
            },
            {
                "@type": "Question",
                "name": "Когда применяется ст. 158.1 УК РФ?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "При хищении на сумму не более 2 500 руб. лицом, которое в течение года после исполнения наказания по ч. 2 ст. 7.27 КоАП было подвергнуто административному наказанию за мелкое хищение.",
                },
            },
            {
                "@type": "Question",
                "name": "Тайное списание с карты после обмана — кража или мошенничество?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "По п. 25.1 Пленума — кража по п. «г» ч. 3 ст. 158 УК РФ, даже если данные карты получены обманом.",
                },
            },
            {
                "@type": "Question",
                "name": "Чем Пленум № 19 отличается от Пленума № 48?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Пленум № 48 разъясняет мошенничество (ст. 159). Пленум № 19 — о краже, грабеже, разбое, границе ст. 158 и ст. 159, ст. 158.1.",
                },
            },
        ],
    }
    return (
        '<script type="application/ld+json">'
        + json.dumps(article, ensure_ascii=False)
        + "</script>\n"
        '<script type="application/ld+json">'
        + json.dumps(faq, ensure_ascii=False)
        + "</script>"
    )


def main():
    handoff = HANDOFF.read_text(encoding="utf-8")
    hero_raw = extract_block(handoff, "=== АЛИНА (HERO) ===")
    hero = strip_hero_inner_style(hero_raw)
    boris = extract_block(handoff, "=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===")
    # Boris includes <style> — keep it inside section
    arthur_md = extract_arthur_md(handoff)
    body_html, toc = convert_md_to_html(arthur_md)
    body_html = insert_boris(body_html, boris)
    body_html = insert_ctas(body_html)
    body_html = faq_section(body_html)
    toc_html = build_toc(toc)

    intro = """
<section class="l24-intro-ug l24-reveal" aria-label="Кратко о Пленуме ВС № 19" style="--reveal-delay:40ms">
<div class="l24-intro-ug__grid">
<div class="l24-intro-ug__text">
<p>16 июня 2026 года Пленум Верховного Суда РФ принял постановление № 19 — <strong>15 изменений</strong> в разъяснения по краже, грабежу и разбою. Три главные новеллы: цифровой рубль как предмет хищения, критерий «обман только для доступа → кража», чеклист по <strong>ст. 158.1 УК РФ</strong>.</p>
<p>Материал для обвиняемых, потерпевших и тех, кто работает с цифровыми платежами: как отличить кражу от мошенничества и какие шаги защиты возможны на каждой стадии уголовного дела.</p>
<div class="l24-intro-ug__brief"><strong>Источник:</strong> <a href="https://vsrf.ru/press_center/news/36011/" target="_blank" rel="noopener noreferrer">официальный инфоповод ВС от 16.06.2026</a> · публикация в «Российской газете» 23.06.2026.</div>
</div>
<div class="l24-intro-ug__decor">
<ul class="l24-intro-ug__chips">
<li class="l24-intro-ug__chip l24-intro-ug__chip--accent">Пленум № 19 · 16.06.2026</li>
<li class="l24-intro-ug__chip l24-intro-ug__chip--theft">ст. 158 · кража</li>
<li class="l24-intro-ug__chip l24-intro-ug__chip--fraud">ст. 159 · мошенничество</li>
<li class="l24-intro-ug__chip">цифровой рубль · ст. 158.1</li>
</ul>
<p style="margin:0;font-size:.9rem;color:#475569;line-height:1.5">Спрос Wordstat: «ст 158.1 ук» ~984; «отличие кражи от мошенничества» ~268; «защита по уголовным делам» ~3 606 показов/мес.</p>
</div>
</div>
</section>
"""

    page = f"""<!-- wp:html -->
<style>
{page_css()}
{hero_css()}
</style>

<main id="primary" class="site-main {SLUG}-page" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">
<meta itemprop="headline" content="{H1}">
<meta itemprop="description" content="{DESC}">
<meta itemprop="inLanguage" content="ru-RU">

{hero}

{intro}

{toc_html}

<div class="l24-longread-wrap l24-reveal" itemprop="articleBody" style="--reveal-delay:160ms">
{body_html}
<p><em>Материал носит информационно-аналитический характер и не является юридической консультацией. Для оценки конкретной ситуации обратитесь к специалисту по уголовному праву.</em></p>
</div>

{json_ld()}
</main>
<!-- /wp:html -->
"""

    OUT.write_text(page, encoding="utf-8")
    print(f"Wrote {OUT} ({len(page)} chars)")

    # Append handoff block
    handoff_block = f"""
=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО
SLUG: {SLUG}
ВНИМАНИЕ: MCP-only Legis24 — без `<canvas>` и `<script>` (кроме JSON-LD). При публикации обернуть в `<!-- wp:html -->`.

{page}

## Передача Юре
SLUG: {SLUG}
excerpt (Description): {DESC}
Режим: MCP-only — HTML без canvas/script-анимаций; JSON-LD Article + FAQPage в конце `<main>`.
Файл: `.cursor/page-content-natasha-plenum19.html`
"""
    if "=== НАТАША (HTML СТРАНИЦЫ) ===" not in handoff:
        HANDOFF.write_text(handoff.rstrip() + "\n" + handoff_block, encoding="utf-8")
        print("Appended handoff block")
    else:
        # replace existing block
        new_handoff = re.sub(
            r"=== НАТАША \(HTML СТРАНИЦЫ\) ===[\s\S]*",
            handoff_block.strip(),
            handoff,
        )
        HANDOFF.write_text(new_handoff, encoding="utf-8")
        print("Updated handoff block")


if __name__ == "__main__":
    main()
