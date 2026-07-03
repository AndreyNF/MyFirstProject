#!/usr/bin/env python3
"""Сборка HTML: ВС малозначительность кража ч. 2 ст. 14 УК."""
from __future__ import annotations

import json
import re
from pathlib import Path

try:
    import markdown
except ImportError:
    markdown = None

ROOT = Path(__file__).resolve().parents[1]
HANDOFF = ROOT / ".cursor/nero-network-handoff.md"
ALINA = ROOT / ".cursor/nero-network-fragments/alina.md"
BORIS = ROOT / ".cursor/nero-network-fragments/boris.md"
OUT_HTML = ROOT / ".cursor/natasha-page-vs-maloznachitelnost.html"
SLUG = "vs-maloznachitelnost-krazha-st-14-zashchita-kassaciya-2026"

TITLE = "ВС прекратил кражу как малозначительное: ч. 2 ст. 14 УК"
DESCRIPTION = (
    "Кассация ВС № 11-УД26-3-К6: дело о краже в гипермаркете прекращено по ч. 2 ст. 14 УК. "
    "Критерии малозначительности, защита в кассации и реабилитация."
)

BORIS_AFTER_H2 = "Признаки и критерии малозначительности: п. 25.4 Пленума ВС № 29"

H2_IDS = {
    "ВС РФ прекратил дело о краже в гипермаркете: кассация № 11-УД26-3-К6": "vs-mal-kassaciya",
    "Фабула дела: кража на 5 674 ₽, подросток 16 лет, возмещение родственниками": "vs-mal-fabula",
    "Ч. 2 ст. 14 УК РФ: что такое малозначительность преступления": "vs-mal-st14",
    BORIS_AFTER_H2: "vs-mal-plenum-254",
    "Формальный состав кражи (ч. 1 ст. 158 УК) vs реальная общественная опасность": "vs-mal-sostav",
    "Прекращение уголовного дела по малозначительности: основания и порядок": "vs-mal-prekrashchenie",
    "Защита в кассации: как добиться пересмотра приговора по ст. 158": "vs-mal-kassaciya-zashchita",
    "Реабилитация и возмещение издержек после прекращения дела": "vs-mal-reabilitaciya",
    "Переносимость позиции ВС: долги, ст. 159 УК и гражданско-правовые споры": "vs-mal-159",
    "Консультация по уголовному делу о краже и кассационной жалобе": "vs-mal-konsultaciya",
}

PAGE_CSS = f"""
.breadcrumbs, .breadcrumb, .woocommerce-breadcrumb, .rank-math-breadcrumb, .yoast-breadcrumb,
.entry-header, .page-title-section,
.entry-title, .main_title, h1.entry-title {{ display: none !important; }}
#primary, .site-main, .site-content, #content, .content-area {{
  padding-top: 0 !important; margin-top: 0 !important;
}}
#sidebar, .sidebar, #secondary, .et_pb_column_1_4 {{ display: none !important; }}
.{SLUG}-page .entry-content {{
  max-width: none !important; width: 100% !important; padding: 0 !important;
}}
.{SLUG}-page .l24-longread-wrap {{
  max-width: 820px; margin: 0 auto; padding: 48px 24px 80px;
  font-size: 1.05rem; line-height: 1.65; color: #1a202c;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.{SLUG}-page h2 {{
  margin-top: 2.5em; color: #1e1b4b; font-size: 1.45rem; font-weight: 800;
}}
.{SLUG}-page h3 {{
  margin-top: 1.5em; color: #312e81; font-size: 1.15rem; font-weight: 700;
}}
.{SLUG}-page table {{
  width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.95rem;
}}
.{SLUG}-page th, .{SLUG}-page td {{
  border: 1px solid #e2e8f0; padding: 10px 12px; text-align: left;
}}
.{SLUG}-page th {{ background: #f5f3ff; color: #312e81; }}
.{SLUG}-page a {{ color: #4338ca; }}
.{SLUG}-page ol, .{SLUG}-page ul {{ margin: 1em 0; padding-left: 1.4em; }}
.{SLUG}-page li {{ margin-bottom: 0.45em; }}
.{SLUG}-page blockquote {{
  margin: 1.5em 0; padding: 16px 22px; border-left: 4px solid #4f46e5;
  background: #f5f3ff; color: #334155; font-style: italic; border-radius: 0 6px 6px 0;
  font-size: 0.98rem; line-height: 1.6;
}}
.{SLUG}-page p {{ margin: 0 0 1.1em; }}
.l24-intro-ug {{
  max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.l24-intro-ug__grid {{
  display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
  gap: 28px; align-items: start;
}}
.l24-intro-ug__text {{
  border-left: 4px solid #4f46e5; padding: 4px 0 4px 22px; text-align: left;
}}
.l24-intro-ug__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.l24-intro-ug__text p:last-child {{ margin-bottom: 0; }}
.l24-intro-ug__brief {{
  background: #f0fdf4; border: 1px solid #6ee7b7; border-radius: 10px;
  padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; line-height: 1.55; color: #334155;
}}
.l24-intro-ug__decor {{
  background: linear-gradient(160deg, #f5f3ff 0%, #fff 100%);
  border: 1px solid #c4b5fd; border-radius: 12px; padding: 18px;
}}
.l24-intro-ug__chips {{
  display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none;
}}
.l24-intro-ug__chip {{
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.03em;
  padding: 6px 10px; border-radius: 999px; background: #fff;
  border: 1px solid #cbd5e1; color: #475569;
}}
.l24-intro-ug__chip--accent {{ border-color: #4f46e5; color: #312e81; background: #f5f3ff; }}
.l24-intro-ug__chip--ok {{ border-color: #059669; color: #047857; background: #ecfdf5; }}
.l24-intro-ug__chip--warn {{ border-color: #b91c1c; color: #b91c1c; background: #fef2f2; }}
.l24-intro-ug__chip--law {{ border-color: #4338ca; color: #4338ca; background: #eef2ff; }}
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
  background: #f5f3ff; color: #312e81; text-decoration: none;
  font-size: 0.88rem; font-weight: 600; border: 1px solid #ddd6fe;
}}
.ym-toc__list a:hover {{ background: #ede9fe; }}
.ym-cta {{
  margin: 28px 0; padding: 22px 24px; border-radius: 10px;
  background: linear-gradient(135deg, #f8fafc 0%, #f5f3ff 100%);
  border: 1px solid #c4b5fd; border-left: 4px solid #4f46e5;
}}
.ym-cta--primary {{ border-left-color: #4f46e5; }}
.ym-cta--legis24.ym-cta--bottom {{
  border-left-color: #4338ca;
  background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);
  border-color: #c4b5fd;
}}
.ym-cta__text {{ margin: 0 0 14px; line-height: 1.55; color: #334155; font-size: 0.98rem; }}
.ym-cta__actions {{ margin: 0; }}
.ym-cta__btn {{
  display: inline-block; background: #312e81; color: #fff !important;
  padding: 12px 22px; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 0.93rem;
}}
.ym-cta__btn:hover {{ background: #1e1b4b; }}
.ym-cta--legis24.ym-cta--bottom .ym-cta__btn {{ background: #4338ca; }}
.ym-cta--legis24.ym-cta--bottom .ym-cta__btn:hover {{ background: #312e81; }}
.l24-faq {{
  max-width: 820px; margin: 0 auto 80px; padding: 28px 24px;
  background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.l24-faq > h2 {{ margin-top: 0 !important; color: #1e1b4b; }}
.l24-faq__item {{
  margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0;
}}
.l24-faq__item:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
.l24-faq__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #1e1b4b; font-weight: 700; }}
.l24-faq__a {{ margin: 0; color: #334155; font-size: 0.97rem; line-height: 1.6; }}
.l24-jsonld-ug {{ display: none !important; }}
@media (max-width: 900px) {{
  .l24-intro-ug__grid {{ grid-template-columns: 1fr; }}
}}
"""

INTRO_HTML = """
<section class="l24-intro-ug" aria-label="Введение">
  <div class="l24-intro-ug__grid">
    <div class="l24-intro-ug__text">
      <p>В апреле 2026 года Верховный Суд РФ вынес кассационное определение <strong>№ 11-УД26-3-К6</strong> по делу о краже в гипермаркете «Магнит» на сумму <strong>5 674,25 ₽</strong>. Три нижестоящие инстанции признали вину по <strong>ч. 1 ст. 158 УК</strong> и применили «мягкий» исход — <strong>ст. 92 УК</strong> с ПМВВ. ВС отменил все акты и прекратил дело по <strong>ч. 2 ст. 14 УК</strong>.</p>
      <p>Для практики защиты это сигнал: формальный состав кражи не равен осуждению. Суды обязаны оценивать общественную опасность по <strong>п. 25.4 Пленума ВС № 29</strong> — и при её отсутствии прекращать дело, а не подменять вопрос о составе смягчением наказания.</p>
      <div class="l24-intro-ug__brief">
        <strong>Кратко:</strong> кража через кассу самообслуживания, несовершеннолетняя 16 лет, полное возмещение родственниками до суда — ВС прекратил дело с правом на <strong>реабилитацию (ст. 133 УПК)</strong>. Прецедент вошёл в дайджест «Уголовный процесс» № 7, июль 2026.
      </div>
    </div>
    <aside class="l24-intro-ug__decor" aria-label="Ключевые параметры дела">
      <ul class="l24-intro-ug__chips">
        <li class="l24-intro-ug__chip l24-intro-ug__chip--accent">ВС 14.04.2026</li>
        <li class="l24-intro-ug__chip">№ 11-УД26-3-К6</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--warn">5 674,25 ₽</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--ok">ч. 2 ст. 14 УК</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--warn">ч. 1 ст. 158 УК</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--law">п. 25.4 Пленума № 29</li>
        <li class="l24-intro-ug__chip">«Магнит» · Бугульма</li>
        <li class="l24-intro-ug__chip">16 лет</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--ok">реабилитация</li>
        <li class="l24-intro-ug__chip l24-intro-ug__chip--warn">ст. 92 ≠ прекращение</li>
      </ul>
      <svg class="l24-intro-ug__route-svg" viewBox="0 0 390 128" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Маршрут дела № 11-УД26-3-К6: три инстанции признали вину, ВС прекратил по малозначительности">
        <defs>
          <marker id="introug-arr-red" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7Z" fill="#b91c1c"/>
          </marker>
          <marker id="introug-arr-grn" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7Z" fill="#059669"/>
          </marker>
        </defs>
        <text x="195" y="16" text-anchor="middle" fill="#64748b" font-size="6" font-weight="700" font-family="system-ui,sans-serif">КРАЖА · 5 674,25 ₽ · КАССАЦИЯ ВС</text>
        <rect x="8" y="34" width="58" height="40" rx="5" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
        <text x="37" y="50" text-anchor="middle" fill="#b91c1c" font-size="5.5" font-weight="700" font-family="system-ui,sans-serif">мировой</text>
        <text x="37" y="62" text-anchor="middle" fill="#94a3b8" font-size="5" font-family="system-ui,sans-serif">виновна</text>
        <line x1="68" y1="54" x2="78" y2="54" stroke="#b91c1c" stroke-width="1.2" marker-end="url(#introug-arr-red)"/>
        <rect x="82" y="34" width="58" height="40" rx="5" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
        <text x="111" y="50" text-anchor="middle" fill="#b91c1c" font-size="5.5" font-weight="700" font-family="system-ui,sans-serif">апелл.</text>
        <text x="111" y="62" text-anchor="middle" fill="#94a3b8" font-size="5" font-family="system-ui,sans-serif">без изм.</text>
        <line x1="142" y1="54" x2="152" y2="54" stroke="#b91c1c" stroke-width="1.2" marker-end="url(#introug-arr-red)"/>
        <rect x="156" y="34" width="58" height="40" rx="5" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
        <text x="185" y="48" text-anchor="middle" fill="#b91c1c" font-size="5" font-weight="700" font-family="system-ui,sans-serif">6-й КС</text>
        <text x="185" y="62" text-anchor="middle" fill="#94a3b8" font-size="5" font-family="system-ui,sans-serif">без изм.</text>
        <line x1="216" y1="54" x2="226" y2="54" stroke="#4f46e5" stroke-width="1.5" marker-end="url(#introug-arr-grn)"/>
        <rect x="230" y="28" width="152" height="52" rx="6" fill="#312e81" stroke="#4f46e5" stroke-width="1.2"/>
        <text x="306" y="46" text-anchor="middle" fill="#e0e7ff" font-size="6" font-weight="700" font-family="system-ui,sans-serif">ВС РФ · 14.04.2026</text>
        <text x="306" y="58" text-anchor="middle" fill="#6ee7b7" font-size="5.5" font-weight="700" font-family="system-ui,sans-serif">отмена · ч. 2 ст. 14 УК</text>
        <text x="306" y="70" text-anchor="middle" fill="#a7f3d0" font-size="5" font-family="system-ui,sans-serif">прекращение · реабилитация</text>
        <path d="M37 78 Q195 108 306 82" fill="none" stroke="#34d399" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
        <text x="195" y="118" text-anchor="middle" fill="#94a3b8" font-size="5.5" font-family="system-ui,sans-serif">возмещение родственниками · ущерб «Магниту» отсутствует</text>
      </svg>
    </aside>
  </div>
</section>

<nav class="ym-toc" aria-label="Содержание статьи">
  <p class="ym-toc__title">Содержание</p>
  <ul class="ym-toc__list">
    <li><a href="#vs-mal-kassaciya">Кассация ВС</a></li>
    <li><a href="#vs-mal-fabula">Фабула дела</a></li>
    <li><a href="#vs-mal-st14">Ч. 2 ст. 14 УК</a></li>
    <li><a href="#vs-mal-plenum-254">П. 25.4 Пленума</a></li>
    <li><a href="#vs-mal-sostav">Состав vs опасность</a></li>
    <li><a href="#vs-mal-prekrashchenie">Прекращение дела</a></li>
    <li><a href="#vs-mal-kassaciya-zashchita">Защита в кассации</a></li>
    <li><a href="#vs-mal-reabilitaciya">Реабилитация</a></li>
    <li><a href="#vs-mal-159">Ст. 159 и долги</a></li>
    <li><a href="#faq">FAQ</a></li>
  </ul>
</nav>
"""

FAQ_ITEMS = [
    (
        "При какой сумме кражу могут прекратить как малозначительную?",
        "Закон не устанавливает фиксированной суммы. В № 11-УД26-3-К6 — 5 674,25 ₽ (уголовная ч. 1 ст. 158). В делах по ст. 159 — 5 300 ₽ и 7 800 ₽. Критерий — совокупность: размер относительно потерпевшего, возмещение, последствия, личность. Сумма выше порога ч. 1 ст. 158 не блокирует малозначительность.",
    ),
    (
        "Помогает ли возмещение ущерба до суда?",
        "Да. Полное возмещение до суда — сильный фактор. В деле о «Магните» родственники возместили ущерб до рассмотрения в ВС; фактического материального ущерба не осталось. Возмещение не гарантирует прекращение, но при прочих обстоятельствах существенно повышает шансы.",
    ),
    (
        "Можно ли заявить малозначительность на стадии проверки?",
        "Да. На стадии доследственной проверки и предварительного следствия защита вправе ходатайствовать о прекращении дела. На практике следователи и прокуратура реже применяют малозначительность без давления защиты. Ранняя подача ходатайства с п. 25.4 и фактами — часть стратегии защиты на стадии проверки.",
    ),
    (
        "Нужен ли адвокат для кассационной жалобы?",
        "Закон не запрещает подачу жалобы самостоятельно, но кассация по малозначительности требует точной правовой аргументации, ссылок на пленумы и прецеденты ВС, процессуальной безупречности. Практика № 11-УД26-3-К6 — результат работы адвоката Королёвой. Ошибки в жалобе или пропуск сроков закрывают путь к пересмотру.",
    ),
]


def extract_html_block(text: str) -> str:
    start = text.index("```html")
    end = text.index("```", start + 7)
    return text[start + len("```html\n") : end].strip()


def extract_hero() -> str:
    return extract_html_block(ALINA.read_text(encoding="utf-8"))


def extract_boris() -> str:
    return extract_html_block(BORIS.read_text(encoding="utf-8"))


def extract_arthur_md(handoff: str) -> str:
    start = handoff.index("### Полный текст\n", handoff.index("=== АРТУР"))
    for end_marker in ("\n\n### Рекламные вставки", "\n\n### GEO-чеклист", "\n\n## Передача пайплайну"):
        try:
            end = handoff.index(end_marker, start)
            break
        except ValueError:
            continue
    else:
        raise ValueError("Artur block end marker not found")
    md = handoff[start + len("### Полный текст\n") : end].strip()
    lines = md.splitlines()
    out: list[str] = []
    for line in lines:
        if line.startswith("# "):
            continue
        out.append(line)
    md = "\n".join(out).strip()
    faq_idx = md.find("\n## Частые вопросы")
    consult_idx = md.find("\n## Консультация по уголовному делу")
    if faq_idx >= 0 and consult_idx > faq_idx:
        md = md[:faq_idx].rstrip() + "\n\n" + md[consult_idx + 1 :].strip()
    elif faq_idx >= 0:
        md = md[:faq_idx].rstrip()
    return md.strip()


def _inline(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        s,
    )
    s = re.sub(r"\[([^\]]+)\]\((/[^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def _simple_md(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    in_ul = in_ol = in_bq = False
    table_buf: list[str] = []

    def flush_table():
        nonlocal table_buf
        if not table_buf:
            return
        rows = [r for r in table_buf if "|" in r and not re.match(r"^\|[\s\-:|]+\|$", r)]
        if len(rows) < 2:
            table_buf = []
            return
        out.append("<table>")
        for i, row in enumerate(rows):
            cells = [c.strip() for c in row.strip("|").split("|")]
            tag = "th" if i == 0 else "td"
            if i == 0:
                out.append("<thead><tr>")
            elif i == 1:
                out.append("</tr></thead><tbody><tr>")
            else:
                out.append("<tr>")
            for c in cells:
                out.append(f"<{tag}>{_inline(c)}</{tag}>")
            out.append("</tr>")
        out.append("</tbody></table>")
        table_buf = []

    def close_lists():
        nonlocal in_ul, in_ol, in_bq
        if in_bq:
            out.append("</blockquote>")
            in_bq = False
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    for line in lines:
        if line.strip().startswith("|"):
            close_lists()
            table_buf.append(line)
            continue
        flush_table()
        if line.startswith("> "):
            if not in_bq:
                close_lists()
                out.append("<blockquote>")
                in_bq = True
            out.append(f"<p>{_inline(line[2:])}</p>")
            continue
        if line.startswith("### "):
            close_lists()
            out.append(f"<h3>{_inline(line[4:])}</h3>")
            continue
        if line.startswith("## "):
            close_lists()
            title = line[3:].strip()
            hid = H2_IDS.get(title, "")
            if hid:
                out.append(f'<h2 id="{hid}">{_inline(title)}</h2>')
            else:
                out.append(f"<h2>{_inline(title)}</h2>")
            continue
        if re.match(r"^\d+\.\s", line):
            if not in_ol:
                close_lists()
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{_inline(re.sub(r'^\d+\.\s', '', line))}</li>")
            continue
        if line.startswith("- "):
            if not in_ul:
                close_lists()
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{_inline(line[2:])}</li>")
            continue
        if line.strip().startswith("<aside") or line.strip().startswith("</aside"):
            close_lists()
            out.append(line)
            continue
        if line.strip().startswith("<"):
            close_lists()
            out.append(line)
            continue
        if line.strip():
            close_lists()
            out.append(f"<p>{_inline(line)}</p>")
        else:
            close_lists()
    flush_table()
    close_lists()
    return "\n".join(out)


def md_to_html(md: str) -> str:
    if markdown:
        html = markdown.markdown(md, extensions=["tables", "sane_lists", "fenced_code"])
    else:
        html = _simple_md(md)
    return re.sub(r"<hr\s*/?>", "", html)


def add_h2_ids(html: str) -> str:
    for title, hid in H2_IDS.items():
        esc = re.escape(title)
        html = re.sub(rf"<h2>({esc})</h2>", rf'<h2 id="{hid}">\1</h2>', html)
    return html


def strip_scripts(html: str) -> str:
    html = re.sub(r"<script\b[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<script\b[^>]*/>", "", html, flags=re.IGNORECASE)
    html = re.sub(r"<canvas\b[^>]*>.*?</canvas>", "", html, flags=re.DOTALL | re.IGNORECASE)
    return html


def fix_links(html: str) -> str:
    def repl(m: re.Match[str]) -> str:
        tag = m.group(0)
        href_m = re.search(r'href="([^"]+)"', tag)
        if not href_m:
            return tag
        href = href_m.group(1)
        if href.startswith("/") or href.startswith("#"):
            return tag
        if 'target="_blank"' in tag:
            if 'rel="noopener noreferrer"' not in tag:
                return tag.replace(">", ' rel="noopener noreferrer">', 1)
            return tag
        return tag.replace(">", ' target="_blank" rel="noopener noreferrer">', 1)

    return re.sub(r"<a\s+[^>]*href=\"[^\"]+\"[^>]*>", repl, html)


def insert_boris(body: str, boris: str) -> str:
    hid = H2_IDS[BORIS_AFTER_H2]
    for marker in (
        f'<h2 id="{hid}">{BORIS_AFTER_H2}</h2>',
        f"<h2>{BORIS_AFTER_H2}</h2>",
    ):
        if marker in body:
            # After H3 sections under plenum H2, before next H2 — insert after last H3 of plenum section
            pass
    # Insert after the plenum H2 section content (after "Игнорирование — основание для отмены в кассации." paragraph)
    anchor = f'<h2 id="{hid}">{BORIS_AFTER_H2}</h2>'
    if anchor not in body:
        anchor = f"<h2>{BORIS_AFTER_H2}</h2>"
    if anchor not in body:
        raise RuntimeError("H2 anchor for Boris block not found")
    next_h2 = body.find('<h2 id="vs-mal-sostav">')
    if next_h2 < 0:
        next_h2 = body.find("<h2>Формальный состав")
    if next_h2 < 0:
        raise RuntimeError("Next H2 after Boris anchor not found")
    return body[:next_h2].rstrip() + "\n\n" + boris + "\n\n" + body[next_h2:]


def build_faq_section() -> str:
    items_html = []
    for q, a in FAQ_ITEMS:
        a_html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", a)
        items_html.append(
            f"""  <div class="l24-faq__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 class="l24-faq__q" itemprop="name">{q}</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p class="l24-faq__a" itemprop="text">{a_html}</p>
    </div>
  </div>"""
        )
    return f"""
<section id="faq" class="l24-faq" itemscope itemtype="https://schema.org/FAQPage" aria-label="Частые вопросы о малозначительности кражи">
  <h2>Частые вопросы о малозначительности кражи и защите в кассации</h2>
{chr(10).join(items_html)}
  <aside class="ym-cta ym-cta--primary" role="complementary" style="margin-top:24px;margin-bottom:0">
    <p class="ym-cta__text">Грозит уголовное дело о краже или приговор уже вступил в силу без обсуждения малозначительности? Разберём позицию по делу № 11-УД26-3-К6 и подготовим стратегию — от ходатайства до кассации в ВС.</p>
    <p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по уголовному делу о краже</a></p>
  </aside>
</section>
"""


def build_jsonld() -> str:
    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": TITLE,
        "description": DESCRIPTION,
        "inLanguage": "ru-RU",
        "author": {"@type": "Organization", "name": "Legis24"},
        "publisher": {"@type": "Organization", "name": "Legis24"},
    }
    faq_entities = [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in FAQ_ITEMS
    ]
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_entities}
    return (
        json.dumps(article, ensure_ascii=False, separators=(",", ": "))
        + "\n"
        + json.dumps(faq, ensure_ascii=False, separators=(",", ": "))
    )


def main() -> None:
    handoff = HANDOFF.read_text(encoding="utf-8")
    hero = strip_scripts(extract_hero())
    boris = strip_scripts(extract_boris())
    md = extract_arthur_md(handoff)
    body = md_to_html(md)
    body = add_h2_ids(body)
    body = strip_scripts(body)
    body = fix_links(body)
    body = insert_boris(body, boris)

    faq = build_faq_section()
    jsonld = build_jsonld()

    html = f"""<!-- wp:html -->
<style>
{PAGE_CSS}
</style>
<main id="primary" class="site-main {SLUG}-page" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">
<meta itemprop="headline" content="{TITLE}">
<meta itemprop="description" content="{DESCRIPTION}">
<meta itemprop="inLanguage" content="ru-RU">
{hero}
{INTRO_HTML}
<div class="l24-longread-wrap" itemprop="articleBody">
{body}
</div>
{faq}
<div class="l24-jsonld-ug" hidden aria-hidden="true">
<pre aria-hidden="true">{jsonld.split(chr(10))[0]}</pre>
<pre aria-hidden="true">{jsonld.split(chr(10))[1] if chr(10) in jsonld else ""}</pre>
</div>
</main>
<!-- /wp:html -->
"""
    html = strip_scripts(html)
    html = fix_links(html)

    OUT_HTML.write_text(html, encoding="utf-8")
    size_bytes = len(html.encode("utf-8"))

    natasha_block = f"""=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО
SLUG: {SLUG}
ВНИМАНИЕ: MCP-only — без `<script>` и `<canvas>`; hero Алины и блок Бориса — static SVG + inline CSS. Обернуть в `<!-- wp:html -->` при публикации.

```html
{html}
```

## Передача Юре
SLUG: {SLUG}
Title: {TITLE}
Description: {DESCRIPTION}
Контент без `<script>` и `<canvas>` — static SVG/CSS only. Публикация: `commands/nero-publish-mcp.md` (blob flow).
Файл: `.cursor/natasha-page-vs-maloznachitelnost.html`
Размер: {size_bytes} байт
main#primary: да (класс `{SLUG}-page`)
Hero: `#l24-hero-vs-maloznachitelnost-krazha-st-14`
Блок Бориса: `#l24-boris-vs-maloznachitelnost-k6-path` (после H2 п. 25.4)
CTA: только https://advokat-vsem.ru/
"""

    if "=== НАТАША (HTML СТРАНИЦЫ) ===" in handoff:
        handoff = handoff.split("=== НАТАША (HTML СТРАНИЦЫ) ===")[0].rstrip()
    handoff = handoff.rstrip() + "\n\n" + natasha_block
    HANDOFF.write_text(handoff, encoding="utf-8")

    has_main = 'id="primary"' in html
    has_script = bool(re.search(r"<script\b", html, re.I))
    print(f"Written {OUT_HTML}")
    print(f"Size: {size_bytes} bytes")
    print(f"main#primary: {has_main}")
    print(f"no script: {not has_script}")
    print("Handoff updated")


if __name__ == "__main__":
    main()
