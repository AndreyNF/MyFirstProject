#!/usr/bin/env python3
"""Сборка page-content-natasha-A13.html (UG A13 — ст. 159/177 при долгах). MCP-only: без script/canvas."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HANDOFF = ROOT / "nero-network-handoff.md"
ALINA = ROOT / "nero-network-fragments/alina.md"
BORIS = ROOT / "nero-network-fragments/boris.md"
OUT = ROOT / "page-content-natasha-A13.html"
SLUG = "statya-159-177-uk-pri-dolgah-granica"
PAGE_CLASS = f"{SLUG}-page"

TITLE = "Ст. 159 и 177 УК при долгах: гражданская граница и защита | Legis24"
DESCRIPTION = (
    "Когда долг остаётся гражданским спором, а когда возможны ст. 159 УК (мошенничество) "
    "и ст. 177 УК (злостное уклонение от погашения). Граница ответственности, возбуждение дела, "
    "доследственная проверка и когда подключать адвоката."
)

H2_IDS = {
    "Простой долг и взыскание: что остаётся в гражданском поле": "a13-grazhdanka",
    "Статья 159 УК РФ: мошенничество при долгах и займах": "a13-159",
    "Статья 177 УК РФ: злостное уклонение от погашения задолженности": "a13-177",
    "Где проходит граница: гражданское взыскание или уголовное дело": "a13-granica",
    "Возбуждение дела, проверка следователя и доследственная проверка": "a13-vozbuzhdenie",
    "Защита на доследственной проверке и в суде: когда нужен адвокат": "a13-zashchita",
    "(Кратко) Налоговая задолженность: не путать со ст. 177": "a13-nalogi",
    "FAQ": "a13-faq",
}

TOC_LABELS = {
    "a13-grazhdanka": "Гражданское взыскание",
    "a13-159": "ст. 159 · мошенничество",
    "a13-177": "ст. 177 · уклонение",
    "a13-granica": "Граница ответственности",
    "boris-ug-matrix-a13": "Схема 159 / 177",
    "a13-vozbuzhdenie": "Проверка и возбуждение",
    "a13-zashchita": "Защита и адвокат",
    "a13-nalogi": "Налоги ≠ 177",
    "a13-faq": "FAQ",
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
    body = body.split("### Рекламные вставки для Наташи")[0].strip()
    body = body.split("## Передача пайплайну")[0].strip()
    body = re.sub(r"^# .+\n\n", "", body, count=1)
    cta_needle = (
        '<aside class="ym-cta ym-cta--primary" role="complementary">\n'
        "  <p class=\"ym-cta__text\">Просрочка по расписке"
    )
    if cta_needle in body:
        body = body.replace(cta_needle, "<!-- BORIS_ANCHOR -->\n\n" + cta_needle, 1)
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
            if hid == "a13-faq":
                out.append(
                    '<section id="a13-faq" class="l24-faq-a13 ym-section" '
                    'itemscope itemtype="https://schema.org/FAQPage" aria-label="Частые вопросы">'
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

        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            code = "\n".join(code_lines)
            cls = "l24-code-block" if not lang else f"l24-code-block l24-code-block--{lang}"
            out.append(f'<pre class="{cls}"><code>{code}</code></pre>')
            continue

        if stripped == "---":
            i += 1
            continue

        if stripped.startswith("**") and stripped.endswith("?**"):
            q = stripped.strip("*").strip()
            out.append(
                '<div class="l24-faq-a13__item" itemscope itemprop="mainEntity" '
                'itemtype="https://schema.org/Question">'
            )
            out.append(f'<h3 class="l24-faq-a13__q" itemprop="name">{md_inline(q)}</h3>')
            out.append(
                '<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">'
            )
            i += 1
            ans_parts = []
            while i < len(lines):
                s = lines[i].strip()
                if not s:
                    if ans_parts:
                        break
                    i += 1
                    continue
                if (s.startswith("**") and s.endswith("?**")) or s.startswith("##"):
                    break
                ans_parts.append(s)
                i += 1
            out.append(
                f'<p class="l24-faq-a13__a" itemprop="text">{md_inline(" ".join(ans_parts))}</p>'
            )
            out.append("</div></div>")
            continue

        if not stripped:
            i += 1
            continue

        out.append(f"<p>{md_inline(stripped)}</p>")
        i += 1

    html = "\n\n".join(out)
    if '<section id="a13-faq"' in html and not html.rstrip().endswith("</section>"):
        html = html.rstrip() + "\n</section>"
    return html


def extract_boris_html() -> str:
    text = BORIS.read_text(encoding="utf-8")
    m = re.search(r"```html\n(.*?)```", text, re.DOTALL)
    if not m:
        raise ValueError("Boris html block not found")
    block = m.group(1).strip()
    block = re.sub(r"<style>.*?</style>\s*", "", block, count=1, flags=re.DOTALL)
    return block


def extract_hero_html() -> str:
    text = ALINA.read_text(encoding="utf-8")
    m = re.search(r'(<section id="hero".*?</section>)', text, re.DOTALL)
    if not m:
        raise ValueError("Hero section not found in alina.md")
    block = m.group(1).strip()
    block = re.sub(r"<style>.*?</style>\s*", "", block, count=1, flags=re.DOTALL)
    return block


def extract_hero_css() -> str:
    text = ALINA.read_text(encoding="utf-8")
    m = re.search(r"<section id=\"hero\".*?<style>(.*?)</style>", text, re.DOTALL)
    return m.group(1).strip() if m else ""


def extract_boris_css() -> str:
    text = BORIS.read_text(encoding="utf-8")
    m = re.search(r"```html\n.*?<style>(.*?)</style>", text, re.DOTALL)
    return m.group(1).strip() if m else ""


def insert_boris(html: str, boris_html: str) -> str:
    anchor = "<!-- BORIS_ANCHOR -->"
    if anchor not in html:
        raise ValueError("BORIS_ANCHOR not found in longread")
    return html.replace(anchor, boris_html)


def build_json_ld() -> str:
    faq = [
        (
            "Можно ли сесть за долг по кредиту?",
            "Нет как общее правило. Просрочка по кредиту — гражданско-правовые меры. "
            "Уголовка — при ложных сведениях без намерения возвращать (ст. 159.1) или иных составах, "
            "не при обычной несостоятельности.",
        ),
        (
            "Считается ли невозврат долга мошенничеством?",
            "Нет, если при выдаче не было умысла не возвращать. Мошенничество при долгах — когда обман "
            "или злоупотребление доверием были до получения денег.",
        ),
        (
            "Чем ст. 159 отличается от ст. 177 при задолженности?",
            "159 — хищение до/в момент получения обманом; 177 — злостное неисполнение после судебного "
            "решения при возможности платить и крупной сумме (> 3,5 млн ₽ с 17.04.2024).",
        ),
        (
            "Как понять, что возбудят уголовное дело, а не ограничатся гражданским иском?",
            "Признаки: заявление о 159 с материалами об обмане; предупреждение ФССП о 177; сумма и "
            "поведение (сокрытие активов). Окончательно — решение следователя/дознавателя после проверки.",
        ),
        (
            "Нужен ли адвокат на доследственной проверке?",
            "Да, если тема — ст. 159, 177 или есть риск возбуждения. Ранняя защита дешевле, чем "
            "исправление ошибок после возбуждения дела.",
        ),
        (
            "Есть ли уголовная ответственность за долги?",
            "За сам факт долга — нет. За составы при обмане, злостном уклонении от судебного долга, "
            "налогах и т.д. — да, при доказанности элементов.",
        ),
        (
            "За какие долги уголовная ответственность?",
            "По ст. 177 — задолженность по вступившему судебному акту при злостном уклонении; "
            "по ст. 159 — хищение через обман при займах; налоги — отдельные статьи.",
        ),
    ]
    faq_entities = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for q, a in faq
    ]
    payload = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": (
                    "Статья 159 и 177 УК при долгах: где гражданская граница и когда нужен адвокат"
                ),
                "description": DESCRIPTION,
                "author": {"@type": "Organization", "name": "Legis24"},
                "publisher": {"@type": "Organization", "name": "Legis24"},
                "inLanguage": "ru-RU",
                "mainEntityOfPage": {
                    "@type": "WebPage",
                    "@id": f"https://advokat-vsem.online/{SLUG}/",
                },
            },
            {"@type": "FAQPage", "mainEntity": faq_entities},
        ],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


INTRO_HTML = """
<section class="ym-lead ym-section" aria-label="Введение">
  <div class="ym-lead__grid">
    <div class="ym-lead__text">
      <p>Просрочка по кредиту, расписке или договору займа сама по себе не означает уголовное дело. За невозврат денег в обычной ситуации кредитор идёт в суд, получает решение и взыскивает долг через приставов.</p>
      <p>Уголовная ответственность за долги наступает только при особых обстоятельствах: умысел не возвращать <strong>до</strong> получения денег (ст. 159 УК) или злостное уклонение от погашения после судебного решения при реальной возможности платить (ст. 177 УК).</p>
      <div class="ym-lead__brief">
        <strong>Кратко:</strong> ниже — граница гражданского и уголовного, пороги после <strong>ФЗ № 79‑ФЗ</strong> (с 17.04.2024), доследственная проверка и когда подключать адвоката. Не про «списание долгов» из рекламы.
      </div>
    </div>
    <aside class="ym-lead__decor" aria-label="Ключевые нормы">
      <ul class="ym-lead__chips">
        <li class="ym-lead__chip ym-lead__chip--navy">ст. 159 / 177</li>
        <li class="ym-lead__chip ym-lead__chip--accent">Пленум № 48</li>
        <li class="ym-lead__chip ym-lead__chip--warn">177 &gt; 3,5 млн ₽</li>
        <li class="ym-lead__chip">79‑ФЗ · 2024</li>
        <li class="ym-lead__chip">159.1 · кредит</li>
        <li class="ym-lead__chip">доследственная</li>
      </ul>
      <svg class="ym-lead__route-svg" viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Гражданское взыскание, статья 159 и 177 УК при долгах: граница ответственности">
        <rect x="8" y="8" width="304" height="184" rx="10" fill="#fff" stroke="#cbd5e1"/>
        <text x="24" y="32" fill="#475569" font-size="10" font-weight="700">ГРАНИЦА · A13</text>
        <rect x="24" y="48" width="80" height="56" rx="8" fill="#f1f5f9" stroke="#64748b"/>
        <text x="64" y="72" text-anchor="middle" fill="#475569" font-size="8" font-weight="800">ГПК</text>
        <text x="64" y="88" text-anchor="middle" fill="#64748b" font-size="7">иск · пристав</text>
        <line x1="110" y1="76" x2="148" y2="76" stroke="#94a3b8" stroke-width="2"/>
        <rect x="152" y="44" width="56" height="40" rx="6" fill="#eff6ff" stroke="#1e40af"/>
        <text x="180" y="68" text-anchor="middle" fill="#1e40af" font-size="9" font-weight="800">159</text>
        <rect x="216" y="44" width="56" height="40" rx="6" fill="#f0fdf4" stroke="#0f2744"/>
        <text x="244" y="68" text-anchor="middle" fill="#0f2744" font-size="9" font-weight="800">177</text>
        <rect x="24" y="120" width="272" height="56" rx="8" fill="#fafbfc" stroke="#e2e8f0"/>
        <text x="160" y="142" text-anchor="middle" fill="#334155" font-size="8" font-weight="600">умысел до выдачи · суд + ИП + &gt;3,5 млн</text>
        <text x="160" y="158" text-anchor="middle" fill="#64748b" font-size="7">просрочка ≠ тюрьма · защита на проверке</text>
      </svg>
    </aside>
  </div>
</section>
"""


def main():
    handoff = HANDOFF.read_text(encoding="utf-8")
    artur_md = extract_artur_body(handoff)
    body = md_to_html(artur_md)

    body = re.sub(
        r"^<p>Просрочка по кредиту.*?</p>\n\n<p>Ниже — разбор.*?</p>\n\n",
        "",
        body,
        count=1,
        flags=re.DOTALL,
    )

    body = insert_boris(body, extract_boris_html())
    hero = extract_hero_html()
    hero_css = extract_hero_css()
    boris_css = extract_boris_css()
    json_ld = build_json_ld()

    page_css = f"""
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
.{PAGE_CLASS} .l24-code-block {{
  background: #0f172a; color: #e2e8f0; padding: 16px 18px; border-radius: 10px;
  overflow-x: auto; font-size: 0.88rem; line-height: 1.5; margin: 1.25em 0;
}}
.ym-lead {{
  max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.ym-lead__grid {{
  display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
  gap: 28px; align-items: start;
}}
.ym-lead__text {{
  border-left: 4px solid #0f2744; padding: 4px 0 4px 22px; text-align: left;
}}
.ym-lead__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.ym-lead__text p:last-child {{ margin-bottom: 0; }}
.ym-lead__brief {{
  background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px;
  padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; line-height: 1.55;
}}
.ym-lead__decor {{
  background: linear-gradient(160deg, #f1f5f9 0%, #fff 100%);
  border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px;
}}
.ym-lead__chips {{
  display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none;
}}
.ym-lead__chip {{
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.03em;
  padding: 6px 10px; border-radius: 999px; background: #fff;
  border: 1px solid #cbd5e1; color: #475569;
}}
.ym-lead__chip--accent {{ border-color: #1e40af; color: #1e40af; }}
.ym-lead__chip--warn {{ border-color: #a31830; color: #a31830; }}
.ym-lead__chip--navy {{ border-color: #0f2744; color: #0f2744; }}
.ym-lead__route-svg {{ display: block; width: 100%; height: auto; }}
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
.l24-faq-a13 {{
  margin-top: 2.5em; padding: 28px 24px; background: #f8fafc;
  border: 1px solid #e2e8f0; border-radius: 12px;
}}
.l24-faq-a13 > h2 {{ margin-top: 0 !important; }}
.l24-faq-a13__item {{ margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0; }}
.l24-faq-a13__item:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
.l24-faq-a13__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #1a365d; }}
.l24-faq-a13__a {{ margin: 0; color: #334155; }}
.ym-section {{ display: block; }}
{hero_css}
{boris_css}
@media (max-width: 900px) {{
  .ym-lead__grid {{ grid-template-columns: 1fr; }}
}}
"""

    toc_html = (
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

    html = f"""<!-- wp:html -->
<style>
{page_css}
</style>
<main id="primary" class="site-main {PAGE_CLASS}" role="main" tabindex="-1">

{hero}

{INTRO_HTML}

{toc_html}

<section class="ym-section">
<div class="l24-longread-wrap">

{body}

</div>
</section>

<script type="application/ld+json">
{json_ld}
</script>
</main>
<!-- /wp:html -->
"""

    OUT.write_text(html, encoding="utf-8")
    size_kb = len(html.encode("utf-8")) / 1024

    natasha_block = f"""
=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО
SLUG: {SLUG}

**Файл:** `.cursor/page-content-natasha-A13.html`
**Title:** {TITLE}
**Description:** {DESCRIPTION}

Режим **Legis24 MCP-only**: без `<script>` (кроме JSON-LD), без `<canvas>`; hero Алины и блок Бориса — static SVG + inline CSS в общем `<style>`.

```html
{html}
```

## Передача Юре

**Title:** {TITLE}
**Description:** {DESCRIPTION}
**slug:** `{SLUG}`
**page ready for MCP blob publish:** да — файл `.cursor/page-content-natasha-A13.html`, обёртка `<!-- wp:html -->`, `main#primary` класс `{PAGE_CLASS}`, hero `#hero`, Boris `#boris-ug-matrix-a13`, JSON-LD Article + FAQPage в конце.
"""

    if "=== НАТАША (HTML СТРАНИЦЫ) ===" in handoff:
        handoff = handoff.split("=== НАТАША (HTML СТРАНИЦЫ) ===")[0].rstrip() + "\n" + natasha_block
    else:
        handoff = handoff.rstrip() + "\n" + natasha_block
    HANDOFF.write_text(handoff, encoding="utf-8")

    print(f"Wrote {OUT}")
    print(f"Size: {size_kb:.1f} KB")
    print('main#primary:', 'id="primary"' in html)
    print(f'Boris anchor: {"boris-ug-matrix-a13" in html}')
    print(f'No canvas: {"<canvas" not in html}')


if __name__ == "__main__":
    main()
