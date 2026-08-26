#!/usr/bin/env python3
"""Assemble Natasha HTML page for vs-obysk-bez-upakovki."""
import re
import json
from pathlib import Path

SLUG = "vs-obysk-bez-upakovki-ekspertiza-dokazatelstva-zashchita-2026"
PAGE_CLASS = f"{SLUG}-page"
TITLE = "ВС: обыск без упаковки изъятого — экспертиза и защита 2026"
DESCRIPTION = (
    "ВС по делу № 32-УД26-10-К1: упаковка изъятого при обыске не обязательна "
    "(ч. 10 ст. 182 УПК). Когда КТЭ на неупакованных ноутбуках допустима и как снизить наказание в кассации."
)
H1 = "ВС разрешил не упаковывать изъятие при обыске: экспертиза, доказательства и защита по делу № 32-УД26-10-К1"

H2_IDS = [
    ("l24-h2-1", "ВС по делу № 32-УД26-10-К1: снижение наказания и позиция по упаковке изъятого"),
    ("l24-h2-2", "Обыск без упаковки изъятого: что изменилось после позиции ВС"),
    ("l24-h2-3", "Ч. 10 ст. 182 УПК: упаковка изъятого «при необходимости» — разбор нормы"),
    ("l24-h2-4", "Оспаривание обыска: процессуальные нарушения и перспективы ходатайства"),
    ("l24-h2-5", "Недопустимость доказательств по ст. 75 УПК: когда нарушение процедуры «не спасает»"),
    ("l24-h2-6", "Компьютерно-техническая экспертиза в уголовном деле: ст. 88 УПК и противоречащие заключения"),
    ("l24-h2-7", "Защита по уголовному делу: тактика при спорных доказательствах обыска"),
    ("l24-h2-8", "Кассация и снижение наказания: уроки дела № 32-УД26-10-К1 для защиты"),
]

H3_IDS = [
    ("l24-h3-1-1", "Что изъяли при обыске и почему спорили об упаковке"),
    ("l24-h3-1-2", "Два экспертных заключения: как это повлияло на срок"),
    ("l24-h3-2-1", "Когда следователь обязан упаковывать, а когда — «при необходимости»"),
    ("l24-h3-2-2", "Почему неупакованные ноутбуки не лишили экспертизу силы"),
    ("l24-h3-3-1", "Что требует закон от следователя при изъятии цифровых носителей"),
    ("l24-h3-3-2", "Типичные ошибки при оформлении изъятия (и когда они критичны)"),
    ("l24-h3-4-1", "Какие нарушения обыска суды признают существенными"),
    ("l24-h3-4-2", "Когда формальный дефект не ведёт к исключению доказательств"),
    ("l24-h3-5-1", "Ст. 75 УПК: перечень оснований и «существенность» нарушения"),
    ("l24-h3-5-2", "Связь с позицией ВС в деле о Google Earth — общий принцип оценки доказательств"),
    ("l24-h3-6-1", "Допустимость КТЭ при спорном изъятии цифровых носителей"),
    ("l24-h3-6-2", "Как оспорить экспертное заключение: повторная, дополнительная, комплексная экспертиза"),
    ("l24-h3-7-1", "Что фиксировать защитнику во время и сразу после обыска"),
    ("l24-h3-7-2", "Ходатайство об исключении доказательств: структура и сроки"),
    ("l24-h3-8-1", "Почему ВС снизил срок, не исключив экспертизу целиком"),
    ("l24-h3-8-2", "FAQ: обязательна ли упаковка ноутбуков; можно ли исключить КТЭ; когда нужен адвокат на обыске"),
]

FAQ_ITEMS = [
    (
        "Обязательна ли упаковка ноутбуков при обыске?",
        "По ч. 10 ст. 182 УПК — не всегда. Упаковка производится при необходимости. Следователь оценивает необходимость и фиксирует в протоколе. После определения ВС от 24.08.2026 отсутствие упаковки само по себе не делает КТЭ недопустимой. Но защитник вправе и должен настаивать на упаковке — это создаёт процессуальный след для будущего оспаривания.",
    ),
    (
        "Можно ли исключить КТЭ из-за неупакованного изъятия?",
        "Можно, но недостаточно ссылаться только на отсутствие упаковки. Нужно доказать: (а) разрыв цепочки идентификации; (б) факт или высокую вероятность изменения данных; (в) нарушение ст. 164.1 при изъятии ЭНИ; (г) несоответствие описания в протоколе и в заключении эксперта. Без этого перспектива низкая — как в деле № 32-УД26-10-K1.",
    ),
    (
        "Когда нужен адвокат на обыске?",
        "Адвокат по уголовным делам на обыске нужен всегда, когда есть риск изъятия цифровых носителей, документов, веществ. Особенно критично при делах о уголовных рисках, связанных с финансовым давлением, и при делах о наркотиках, экономических преступлениях, мошенничестве. Участие защитника фиксирует нарушения в момент их совершения — это нельзя воспроизвести задним числом.",
    ),
    (
        "Что делать, если два экспертных заключения расходятся?",
        "Проверить: отвечают ли эксперты на один и тот же вопрос? Если да — ходатайство о повторной экспертизе по ст. 207 УПК. Если нет (как в № 32-УД26-10-K1, где в 2013 году методики не было) — искать иные основания: квалификация, размер, процессуальные нарушения при изъятии.",
    ),
]


def inline_md(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def parse_table(lines: list[str], start: int) -> tuple[str, int]:
    rows = []
    i = start
    while i < len(lines) and lines[i].strip().startswith("|"):
        row = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        rows.append(row)
        i += 1
    if len(rows) < 2:
        return "", start
    header = rows[0]
    body_rows = [r for r in rows[2:] if r and not all(set(c) <= {"-", ":"} for c in r)]
    html = ["<table>", "<thead><tr>"]
    for h in header:
        html.append(f"<th>{inline_md(h)}</th>")
    html.append("</tr></thead><tbody>")
    for row in body_rows:
        html.append("<tr>")
        for cell in row:
            html.append(f"<td>{inline_md(cell)}</td>")
        html.append("</tr>")
    html.append("</tbody></table>")
    return "".join(html), i


def markdown_to_html(md: str) -> str:
    lines = md.split("\n")
    out: list[str] = []
    i = 0
    h2_idx = 0
    h3_idx = 0

    while i < len(lines):
        line = lines[i]

        if line.strip().startswith("<aside"):
            block = [line]
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("</aside>"):
                block.append(lines[i])
                i += 1
            if i < len(lines):
                block.append(lines[i])
            out.append("\n".join(block))
            i += 1
            continue

        if line.startswith("## "):
            title = line[3:].strip()
            hid = H2_IDS[h2_idx][0] if h2_idx < len(H2_IDS) else f"l24-h2-{h2_idx+1}"
            h2_idx += 1
            out.append(f'<h2 id="{hid}">{inline_md(title)}</h2>')
            i += 1
            continue

        if line.startswith("### "):
            title = line[4:].strip()
            hid = H3_IDS[h3_idx][0] if h3_idx < len(H3_IDS) else f"l24-h3-{h3_idx+1}"
            h3_idx += 1
            out.append(f'<h3 id="{hid}">{inline_md(title)}</h3>')
            i += 1
            continue

        if line.strip().startswith("|"):
            table_html, i = parse_table(lines, i)
            out.append(table_html)
            continue

        if line.startswith("> "):
            quote_lines = []
            while i < len(lines) and lines[i].startswith("> "):
                quote_lines.append(lines[i][2:])
                i += 1
            out.append(f"<blockquote>{inline_md(' '.join(quote_lines))}</blockquote>")
            continue

        if line.strip() == "```":
            i += 1
            code_lines = []
            while i < len(lines) and lines[i].strip() != "```":
                code_lines.append(lines[i])
                i += 1
            i += 1
            out.append(
                '<pre class="l24-code-chain" style="margin:1.25em 0;padding:14px 18px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;font-size:0.9rem;line-height:1.5;overflow-x:auto;">'
                + "\n".join(code_lines)
                + "</pre>"
            )
            continue

        if re.match(r"^- \[ \] ", line):
            items = []
            while i < len(lines) and re.match(r"^- \[ \] ", lines[i]):
                items.append(re.sub(r"^- \[ \] ", "", lines[i]))
                i += 1
            out.append("<ul class=\"l24-checklist\">")
            for item in items:
                out.append(f"<li>{inline_md(item)}</li>")
            out.append("</ul>")
            continue

        if line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(lines[i][2:])
                i += 1
            out.append("<ul>")
            for item in items:
                out.append(f"<li>{inline_md(item)}</li>")
            out.append("</ul>")
            continue

        if re.match(r"^\d+\. ", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
                items.append(re.sub(r"^\d+\. ", "", lines[i]))
                i += 1
            out.append("<ol>")
            for item in items:
                out.append(f"<li>{inline_md(item)}</li>")
            out.append("</ol>")
            continue

        if line.strip() == "---":
            i += 1
            continue

        if line.strip().startswith("**Источники:**"):
            src = inline_md(line.strip())
            out.append(f'<ul class="l24-sources"><li>{src[14:]}</li></ul>')
            i += 1
            continue

        if line.strip().startswith("**") and line.strip().endswith("**") and "?" in line:
            # FAQ inline under h3 - skip, handled separately
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith("#") and not lines[i].startswith("<aside"):
                i += 1
            continue

        if not line.strip():
            i += 1
            continue

        if line.startswith("# ") or (line.startswith("*") and line.endswith("*") and line.count("*") == 2):
            i += 1
            continue

        out.append(f"<p>{inline_md(line)}</p>")
        i += 1

    return "\n\n".join(out)


def extract_artur_md() -> str:
    handoff = Path("/workspace/.cursor/nero-network-handoff.md").read_text(encoding="utf-8")
    marker_start = "### Полный текст\n"
    marker_end = "### Рекламные вставки для Наташи"
    start = handoff.find(marker_start, handoff.find("=== АРТУР (CTA И РЕКЛАМА) ==="))
    start += len(marker_start)
    end = handoff.find(marker_end, start)
    md = handoff[start:end].strip()
    # Remove duplicate H1, subtitle, and opening intro paragraphs (added in template)
    md = re.sub(r"^# .+\n\n", "", md, count=1)
    md = re.sub(r"^\*[^*]+\*\n\n", "", md, count=1)
    md = re.sub(
        r"^24 августа 2026 года Судебная коллегия.*?\n\n"
        r"Для читателя, который ищет ответы.*?\n\n",
        "",
        md,
        count=1,
        flags=re.DOTALL,
    )
    # Remove bottom CTA and sources/footer - we'll add separately
    md = re.sub(
        r"\n<aside class=\"ym-cta ym-cta--legis24 ym-cta--bottom\".*?</aside>\s*\n+---\s*\n+\*\*Источники:\*\*.*$",
        "",
        md,
        flags=re.DOTALL,
    )
    return md


def load_hero() -> str:
    alina = Path("/workspace/.cursor/nero-network-fragments/alina.md").read_text(encoding="utf-8")
    m = re.search(r"(<section id=\"l24-hero.*?</section>)", alina, re.DOTALL)
    return m.group(1) if m else ""


def load_boris() -> str:
    boris = Path("/workspace/.cursor/nero-network-fragments/boris.md").read_text(encoding="utf-8")
    m = re.search(r"```html\n(.*?)```", boris, re.DOTALL)
    return m.group(1).strip() if m else ""


def insert_boris(longread: str, boris: str) -> str:
    marker = 'href="/zashchita-po-ugolovnomu-delu-stadiya-proverki/">'
    idx = longread.find(marker)
    if idx == -1:
        raise ValueError("Boris insertion marker not found")
    end_p = longread.find("</p>", idx)
    insert_at = end_p + len("</p>")
    return longread[:insert_at] + "\n\n" + boris + "\n\n" + longread[insert_at:]


def page_css() -> str:
    pc = PAGE_CLASS
    return f"""
/* ===== RESET / BREADCRUMBS / PADDING ===== */
.breadcrumbs, .breadcrumb, .woocommerce-breadcrumb, .rank-math-breadcrumb, .yoast-breadcrumb,
.entry-header, .page-title-section,
.entry-title, .main_title, h1.entry-title {{ display: none !important; }}
#primary, .site-main, .site-content, #content, .content-area {{
  padding-top: 0 !important; margin-top: 0 !important;
}}
#sidebar, .sidebar, #secondary, .et_pb_column_1_4 {{ display: none !important; }}

/* ===== PAGE SCOPE ===== */
.{pc} .entry-content {{
  max-width: none !important; width: 100% !important; padding: 0 !important;
}}
.{pc} .l24-longread-wrap {{
  max-width: 820px; margin: 0 auto; padding: 48px 24px 80px;
  font-size: 1.05rem; line-height: 1.65; color: #1a202c;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.{pc} h2 {{
  margin-top: 2.5em; color: #1a365d; font-size: 1.45rem; font-weight: 800;
}}
.{pc} h3 {{
  margin-top: 1.5em; color: #312e81; font-size: 1.15rem; font-weight: 700;
}}
.{pc} table {{
  width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.95rem;
}}
.{pc} th, .{pc} td {{
  border: 1px solid #e2e8f0; padding: 10px 12px; text-align: left;
}}
.{pc} th {{ background: #fef2f2; color: #a31830; }}
.{pc} a {{ color: #a31830; }}
.{pc} ol, .{pc} ul {{ margin: 1em 0; padding-left: 1.4em; }}
.{pc} li {{ margin-bottom: 0.45em; }}
.{pc} blockquote {{
  margin: 1.5em 0; padding: 16px 22px; border-left: 4px solid #a31830;
  background: #fff7f7; color: #334155; font-style: italic; border-radius: 0 6px 6px 0;
  font-size: 0.98rem; line-height: 1.6;
}}
.{pc} p {{ margin: 0 0 1.1em; }}
.{pc} .l24-checklist {{ list-style: none; padding-left: 0; }}
.{pc} .l24-checklist li {{ padding-left: 1.6em; position: relative; }}
.{pc} .l24-checklist li::before {{ content: "☐"; position: absolute; left: 0; color: #a31830; }}

/* ===== INTRO GRID ===== */
.l24-intro-ug {{
  max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.l24-intro-ug__grid {{
  display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
  gap: 28px; align-items: start;
}}
.l24-intro-ug__text {{
  border-left: 4px solid #a31830; padding: 4px 0 4px 22px;
}}
.l24-intro-ug__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.l24-intro-ug__text p:last-child {{ margin-bottom: 0; }}
.l24-intro-ug__brief {{
  background: #fff7f7; border: 1px solid #fecaca; border-radius: 10px;
  padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; line-height: 1.55; color: #334155;
}}
.l24-intro-ug__decor {{
  background: linear-gradient(160deg, #fff7f7 0%, #fff 100%);
  border: 1px solid #fecaca; border-radius: 12px; padding: 18px;
}}
.l24-intro-ug__chips {{
  display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none;
}}
.l24-intro-ug__chip {{
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.03em;
  padding: 6px 10px; border-radius: 999px; background: #fff;
  border: 1px solid #cbd5e1; color: #475569;
}}
.l24-intro-ug__chip--accent {{ border-color: #a31830; color: #a31830; background: #fff7f7; }}
.l24-intro-ug__chip--ok    {{ border-color: #059669; color: #047857; background: #ecfdf5; }}
.l24-intro-ug__chip--warn  {{ border-color: #dc2626; color: #991b1b; background: #fef2f2; }}
.l24-intro-ug__chip--blue  {{ border-color: #4338ca; color: #4338ca; background: #f5f3ff; }}
.l24-intro-ug__chip--navy  {{ border-color: #1e40af; color: #1e40af; background: #eff6ff; }}
.l24-intro-ug__route-svg {{ display: block; width: 100%; height: auto; }}

/* ===== TOC ===== */
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
  background: #fff7f7; color: #a31830; text-decoration: none;
  font-size: 0.88rem; font-weight: 600; border: 1px solid #fecaca;
}}
.ym-toc__list a:hover {{ background: #fef2f2; }}

/* ===== CTA ===== */
.ym-cta {{
  margin: 28px 0; padding: 22px 24px; border-radius: 10px;
  background: linear-gradient(135deg, #f8fafc 0%, #fff7f7 100%);
  border: 1px solid #fecaca; border-left: 4px solid #a31830;
}}
.ym-cta--primary {{ border-left-color: #a31830; }}
.ym-cta--legis24.ym-cta--bottom {{
  border-left-color: #4338ca;
  background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);
  border-color: #c4b5fd;
}}
.ym-cta p {{ margin: 0 0 14px; line-height: 1.55; color: #334155; font-size: 0.98rem; }}
.ym-cta h3 {{ margin: 0 0 12px; color: #1a365d; font-size: 1.1rem; font-weight: 800; }}
.ym-cta a[href] {{
  display: inline-block; background: #a31830; color: #fff !important;
  padding: 12px 22px; border-radius: 8px; font-weight: 700;
  text-decoration: none; font-size: 0.93rem;
}}
.ym-cta a[href]:hover {{ background: #8b1528; }}
.ym-cta--legis24.ym-cta--bottom a[href] {{ background: #4338ca; }}
.ym-cta--legis24.ym-cta--bottom a[href]:hover {{ background: #312e81; }}
.ym-cta__text {{ margin: 0 0 14px; line-height: 1.55; color: #334155; font-size: 0.98rem; }}
.ym-cta__actions {{ margin: 0; }}
.ym-cta__btn {{ display: inline-block; background: #a31830; color: #fff !important; padding: 12px 22px; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 0.93rem; }}
.ym-cta__btn:hover {{ background: #8b1528; }}
.ym-cta--legis24 {{ border-left-color: #4338ca; background: linear-gradient(135deg, #f5f3ff 0%, #fff7f7 100%); border-color: #c4b5fd; }}
.ym-cta--legis24 .ym-cta__btn {{ background: #4338ca; }}
.ym-cta--legis24 .ym-cta__btn:hover {{ background: #312e81; }}

/* ===== FAQ ===== */
.l24-faq {{
  margin-top: 2.5em; padding: 28px 24px; background: #f8fafc;
  border: 1px solid #e2e8f0; border-radius: 12px;
}}
.l24-faq > h2 {{ margin-top: 0 !important; color: #1a365d; }}
.l24-faq__item {{
  margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0;
}}
.l24-faq__item:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
.l24-faq__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #1a365d; font-weight: 700; }}
.l24-faq__a {{ margin: 0; color: #334155; font-size: 0.97rem; line-height: 1.6; }}

/* ===== JSON-LD hidden ===== */
.l24-jsonld-ug {{ display: none !important; }}

/* ===== SOURCES ===== */
.{pc} .l24-sources {{
  margin-top: 2em; font-size: 0.88rem; color: #64748b;
  border-top: 1px solid #e2e8f0; padding-top: 1.2em;
}}
.{pc} .l24-sources li {{ margin-bottom: 0.3em; }}
.{pc} .l24-sources a {{ color: #64748b; }}

/* ===== RESPONSIVE ===== */
@media (max-width: 900px) {{
  .l24-intro-ug__grid {{ grid-template-columns: 1fr; }}
  .l24-hero-vs-obysk-bez-upakovki-ekspertiza-dokazatelstva-zashchita-2026__inner {{ grid-template-columns: 1fr !important; }}
  .l24-hero-vs-obysk-bez-upakovki-ekspertiza-dokazatelstva-zashchita-2026 {{
    min-height: auto !important; padding: 96px 20px 56px !important;
  }}
  .l24-hero-vs-obysk-bez-upakovki-ekspertiza-dokazatelstva-zashchita-2026__visual {{ order: -1; max-height: 320px; overflow: hidden; }}
}}
"""


def intro_section() -> str:
    return """
<section class="l24-intro-ug">
  <div class="l24-intro-ug__grid">
    <div class="l24-intro-ug__text">
      <p>24 августа 2026 года СК по уголовным делам ВС РФ вынесла определение по делу № <strong>32-УД26-10-К1</strong>: изъятые при обыске <strong>два ноутбука и телефон</strong> передали на КТЭ <strong>без упаковки</strong>. Защита настаивала на недопустимости экспертизы — ВС отклонил довод, сославшись на <strong>ч. 10 ст. 182 УПК</strong>.</p>
      <p>Для практики UG это кейс о границе между формальным нарушением и существенным: когда «не упаковали» <strong>не лишает</strong> КТЭ допустимости (ст. 75, 88 УПК) — и когда параллельная линия по <strong>ст. 9 УК</strong> и Пленуму № 14 даёт <strong>снижение наказания</strong> в кассации: 10 лет 6 мес. → 10 лет 3 мес.</p>
      <div class="l24-intro-ug__brief">Материал разбирает ч. 10 ст. 182 УПК, цепочку идентификации цифровых носителей, двухконтурную защиту (процесс + квалификация), чек-лист адвоката на обыске и перспективы оспаривания КТЭ после позиции ВС 2026 года.</div>
    </div>
    <div class="l24-intro-ug__decor">
      <ul class="l24-intro-ug__chips">
        <li class="l24-intro-ug__chip l24-intro-ug__chip--accent">ч. 10 ст. 182 УПК</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--warn">неупакованные ноутбуки</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--accent">дело № 32-УД26-10-К1</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--blue">ст. 75 УПК</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--navy">ст. 88 УПК · КТЭ</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--ok">10,5 → 10 лет 3 мес.</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--blue">ст. 9 УК</li>
        <li class="l24-intro-ug__chip">Пленум № 14</li>
        <li class="l24-intro-ug__chip">проверочная закупка</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--navy">ст. 164.1 УПК</li>
        <li class="l24-intro-ug__chip">24.08.2026</li>
      </ul>
      <svg class="l24-intro-ug__route-svg" viewBox="0 0 390 128" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Маршрут дела № 32-УД26-10-К1: обыск без упаковки → КТЭ допустима → снижение срока в кассации">
        <defs>
          <marker id="introo-arr" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7Z" fill="#a31830"/></marker>
          <marker id="introo-grn" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7Z" fill="#059669"/></marker>
          <marker id="introo-blu" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7Z" fill="#4338ca"/></marker>
        </defs>
        <rect x="4" y="38" width="72" height="48" rx="6" fill="#fff7f7" stroke="#fca5a5" stroke-width="1.2"/>
        <text x="40" y="57" text-anchor="middle" fill="#a31830" font-size="6" font-weight="700">ОБЫСК</text>
        <text x="40" y="68" text-anchor="middle" fill="#991b1b" font-size="5.5">2 ноутбука</text>
        <text x="40" y="78" text-anchor="middle" fill="#991b1b" font-size="5.5">без упаковки</text>
        <line x1="78" y1="62" x2="88" y2="62" stroke="#a31830" stroke-width="1.5" marker-end="url(#introo-arr)"/>
        <rect x="92" y="38" width="68" height="48" rx="6" fill="#f5f3ff" stroke="#c4b5fd" stroke-width="1.2"/>
        <text x="126" y="55" text-anchor="middle" fill="#4338ca" font-size="5.5" font-weight="700">КТЭ 2013</text>
        <text x="126" y="66" text-anchor="middle" fill="#4338ca" font-size="5.5">допустима</text>
        <text x="126" y="77" text-anchor="middle" fill="#64748b" font-size="5">ст. 88 УПК</text>
        <line x1="162" y1="62" x2="172" y2="62" stroke="#4338ca" stroke-width="1.5" marker-end="url(#introo-blu)"/>
        <rect x="176" y="38" width="72" height="48" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
        <text x="212" y="55" text-anchor="middle" fill="#991b1b" font-size="5.5" font-weight="700">довод защиты</text>
        <text x="212" y="66" text-anchor="middle" fill="#b91c1c" font-size="5.5">отклонён</text>
        <text x="212" y="77" text-anchor="middle" fill="#64748b" font-size="5">ч. 10 ст. 182</text>
        <line x1="250" y1="62" x2="260" y2="62" stroke="#059669" stroke-width="1.5" marker-end="url(#introo-grn)"/>
        <rect x="264" y="24" width="118" height="76" rx="7" fill="#0f172a" stroke="#059669" stroke-width="1.2"/>
        <text x="323" y="46" text-anchor="middle" fill="#e2e8f0" font-size="6.5" font-weight="700">ВС РФ</text>
        <text x="323" y="58" text-anchor="middle" fill="#6ee7b7" font-size="5.5">покушение · ст. 9 УК</text>
        <text x="323" y="70" text-anchor="middle" fill="#6ee7b7" font-size="5.5">10,5 → 10 лет 3 мес.</text>
        <text x="323" y="83" text-anchor="middle" fill="#fcd34d" font-size="5">24.08.2026</text>
        <text x="195" y="20" text-anchor="middle" fill="#64748b" font-size="6" font-weight="600">№ 32-УД26-10-К1 · обыск без упаковки · двухконтурная защита</text>
        <text x="195" y="116" text-anchor="middle" fill="#94a3b8" font-size="5.5">ч. 10 ст. 182 · ст. 75/88 УПК · Пленум № 14 · кассация</text>
      </svg>
    </div>
  </div>
</section>
"""


def toc_section() -> str:
    items = [
        ("l24-h2-1", "Дело № 32-УД26-10-К1"),
        ("l24-h2-2", "Обыск без упаковки"),
        ("l24-h2-3", "ч. 10 ст. 182 УПК"),
        ("l24-h2-4", "Оспаривание обыска"),
        ("l24-h2-5", "ст. 75 УПК"),
        ("l24-h2-6", "КТЭ и ст. 88 УПК"),
        ("l24-h2-7", "Тактика защиты"),
        ("boris-obysk-upakovka-flow", "Два контура защиты"),
        ("l24-h2-8", "Кассация и снижение"),
        ("faq", "FAQ"),
    ]
    links = "\n".join(f'    <li><a href="#{aid}">{label}</a></li>' for aid, label in items)
    return f"""
<nav class="ym-toc" aria-label="Содержание статьи">
  <p class="ym-toc__title">Содержание</p>
  <ul class="ym-toc__list">
{links}
  </ul>
</nav>
"""


def faq_section() -> str:
    items_html = []
    for q, a in FAQ_ITEMS:
        items_html.append(
            f'<div class="l24-faq__item"><h3 class="l24-faq__q">{q}</h3><p class="l24-faq__a">{a}</p></div>'
        )
    return f"""
<section id="faq" class="l24-faq" aria-label="Часто задаваемые вопросы">
<h2>Частые вопросы (FAQ)</h2>
{"".join(items_html)}
</section>
"""


def jsonld_block() -> str:
    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": H1,
        "description": DESCRIPTION,
        "inLanguage": "ru-RU",
        "datePublished": "2026-08-26",
        "author": {"@type": "Organization", "name": "Legis24"},
        "publisher": {"@type": "Organization", "name": "Legis24"},
    }
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in FAQ_ITEMS
        ],
    }
    return f"""
<div class="l24-jsonld-ug" hidden aria-hidden="true">
<pre aria-hidden="true">{json.dumps(article, ensure_ascii=False)}</pre>
<pre aria-hidden="true">{json.dumps(faq, ensure_ascii=False)}</pre>
</div>
"""


def footer_bits() -> str:
    return """
<ul class="l24-sources">
  <li>РАПСИ, 24.08.2026: <a href="https://rapsinews.ru/judicial_analyst/20260824/312126159.html" target="_blank" rel="noopener noreferrer">rapsinews.ru</a></li>
  <li>ст. 75, 88, 164.1, 182, 195, 207 УПК РФ; Пленум ВС № 14 (п. 13, 13.1); Пленум ВС № 1; Шапошников А.Ю., «Уголовный процесс» № 7, 2026</li>
</ul>
<p><em>Материал носит информационно-аналитический характер и не является юридической консультацией. Для оценки конкретной ситуации обратитесь к специалисту по уголовному праву.</em></p>

<aside class="ym-cta ym-cta--legis24 ym-cta--bottom" role="complementary">
<p class="ym-cta__text">Дело № 32-УД26-10-К1 показало: даже при сохранении КТЭ кассация может снизить срок за счёт правильной квалификации. Оценим перспективы защиты на вашей стадии — следствие, суд или кассация.</p>
<p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Получить консультацию по защите</a></p>
</aside>
"""


def build_page() -> str:
    md = extract_artur_md()
    longread = markdown_to_html(md)
    longread = insert_boris(longread, load_boris())

    # Remove inline FAQ h3 section from longread (we have dedicated FAQ)
    longread = re.sub(
        r'<h3 id="l24-h3-8-2">.*?</h3>.*?(?=<h2 id="l24-h2-8">|<ul class="l24-sources">|$)',
        "",
        longread,
        flags=re.DOTALL,
    )
    # Fix: remove h3-8-2 and content until next h2 or end - actually h3-8-2 is last h3 before sources
    longread = re.sub(
        r'<h3 id="l24-h3-8-2">FAQ:.*?</h3>.*$',
        "",
        longread,
        flags=re.DOTALL,
    )

    hero = load_hero()

    page = f"""<!-- wp:html -->
<style>
{page_css()}
</style>

<main id="primary" class="site-main {PAGE_CLASS}" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">
<meta itemprop="headline" content="{H1}">
<meta itemprop="description" content="{DESCRIPTION}">
<meta itemprop="inLanguage" content="ru-RU">

{hero}

{intro_section()}

{toc_section()}

<div class="l24-longread-wrap">

<p>24 августа 2026 года Судебная коллегия по уголовным делам Верховного Суда РФ вынесла определение по делу № <strong>32-УД26-10-К1</strong>, которое сразу попало в фокус практикующих адвокатов. Речь идёт не о «разрешении» следователям игнорировать процедуру, а о более тонком вопросе: <strong>когда отсутствие упаковки изъятого при обыске не делает компьютерно-техническую экспертизу (КТЭ) недопустимым доказательством</strong> — и при каких условиях защита всё же может добиться снижения наказания в кассации.</p>

<p>Для читателя, который ищет ответы на запросы вроде «недопустимость доказательств уголовное дело», «обыск без упаковки изъятого» или «снижение наказания кассация», это определение — не абстрактная новость, а рабочий кейс с конкретной фабулой, двумя противоречащими экспертными заключениями и итогом: <strong>10,5 лет → 10 лет 3 месяца</strong> лишения свободы в исправительной колонии строгого режима.</p>

{longread}

{footer_bits()}

{faq_section()}

</div>

{jsonld_block()}

</main>
<!-- /wp:html -->
"""
    assert "<script" not in page.lower()
    assert "<canvas" not in page.lower()
  # verify CTA hrefs
    for bad in re.findall(r'href="([^"]+)"', page):
        if "advokat-vsem" in bad and bad != "https://advokat-vsem.ru/":
            if bad.startswith("/"):
                continue  # internal links ok
            raise ValueError(f"Bad CTA href: {bad}")
    return page


def update_handoff(html: str, size: int) -> None:
    handoff_path = Path("/workspace/.cursor/nero-network-handoff.md")
    content = handoff_path.read_text(encoding="utf-8")

    natasha_block = f"""=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО

### Передача Юре
**SLUG:** {SLUG}
**Title:** {TITLE}
**Description:** {DESCRIPTION}
**Размер HTML:** {size} символов

```html
{html}
```
"""

    # Replace existing Natasha section or append
    pattern = r"=== НАТАША \(HTML СТРАНИЦЫ\) ===.*"
    if re.search(pattern, content, re.DOTALL):
        # Find the Natasha section for obysk - the handoff may have maugli natasha at end
        # Insert new section before maugli natasha or replace if obysk exists
        if "vs-obysk-bez-upakovki" in content[content.find("=== НАТАША"):]:
            content = re.sub(pattern, natasha_block.rstrip(), content, count=1, flags=re.DOTALL)
        else:
            # Prepend new Natasha block before existing one
            idx = content.find("=== НАТАША (HTML СТРАНИЦЫ) ===")
            content = content[:idx] + natasha_block + "\n\n" + content[idx:]
    else:
        content += "\n\n" + natasha_block

    handoff_path.write_text(content, encoding="utf-8")


def main():
    html = build_page()
    out = Path("/workspace/.cursor/page-content-natasha-obysk-upakovka.html")
    out.write_text(html, encoding="utf-8")
    size = len(html)
    print(f"HTML size: {size} chars")
    print(f"Written to {out}")
    update_handoff(html, size)
    print("Handoff updated")


if __name__ == "__main__":
    main()
