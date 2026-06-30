#!/usr/bin/env python3
"""Сборка HTML страницы ВС: компенсация ТЗ / Указ № 322 для handoff Наташи."""
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
OUT_HTML = ROOT / ".cursor/page-content-natasha-vs-kompensaciya.html"
SLUG = "vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany"

TITLE = "ВС 2026: защита от компенсации за ТЗ из недружественной страны"
DESCRIPTION = (
    "ВС разъяснил: при иске о компенсации за нарушение товарного знака суды проверяют Указ № 322. "
    "Как ИП на маркетплейсе оспорить иск иностранного правообладателя."
)

H2_IDS = {
    "Позиция Верховного суда 2026: ИП на маркетплейсе и иск о компенсации за «сходное» обозначение": "vs-komp-poziciya-vs",
    "Компенсация за нарушение товарного знака: когда суд обязан проверить происхождение права": "vs-komp-proishozhdenie-prava",
    "Нарушение товарного знака и сходное обозначение на маркетплейсе": "vs-komp-marketplejs-skhodstvo",
    "Иностранный правообладатель и недружественные страны: Указ Президента № 322": "vs-komp-ukaz-322",
    "Ответ на иск по интеллектуальной собственности: линия защиты для бизнеса": "vs-komp-otvet-isk",
    "Цессия и лицензия права на товарный знак: риски для истца": "vs-komp-cessiya-licenziya",
    "Компенсация по ст. 1252.1 ГК РФ и лимит 10 млн ₽ (214-ФЗ с 2026 года)": "vs-komp-1252-1",
    "Злоупотребление правом при защите товарного знака": "vs-komp-zloupotreblenie",
    "СИП, оспаривание и аннулирование ТЗ — кратко (без дубля других материалов)": "vs-komp-sip-osporenie",
    "Когда подключать юриста: защита товарного знака и ответ на иск по ИС": "vs-komp-yurist",
    "Частые вопросы": "vs-komp-faq",
    "Источники и нормативная база": "vs-komp-istochniki",
}

BORIS_AFTER_H2 = "Иностранный правообладатель и недружественные страны: Указ Президента № 322"

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
}}
.{SLUG}-page h2 {{
  margin-top: 2.5em; color: #1a365d; font-size: 1.45rem;
}}
.{SLUG}-page h3 {{
  margin-top: 1.5em; color: #2c5282; font-size: 1.15rem;
}}
.{SLUG}-page table {{
  width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.95rem;
}}
.{SLUG}-page th, .{SLUG}-page td {{
  border: 1px solid #e2e8f0; padding: 10px 12px; text-align: left;
}}
.{SLUG}-page th {{ background: #edf2f7; }}
.{SLUG}-page a {{ color: #1e40af; }}
.{SLUG}-page ol, .{SLUG}-page ul {{ margin: 1em 0; padding-left: 1.4em; }}
.{SLUG}-page li {{ margin-bottom: 0.45em; }}
.{SLUG}-page blockquote {{
  margin: 1.25em 0; padding: 14px 18px; border-left: 4px solid #1e3a8a;
  background: #f8fafc; color: #334155; font-size: 0.98rem;
}}
.{SLUG}-page pre {{
  margin: 1.25em 0; padding: 14px 16px; background: #f1f5f9;
  border: 1px solid #e2e8f0; border-radius: 8px; font-size: 0.85rem;
  overflow-x: auto; line-height: 1.45;
}}
.l24-intro-vs {{
  max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.l24-intro-vs__grid {{
  display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
  gap: 28px; align-items: start;
}}
.l24-intro-vs__text {{
  border-left: 4px solid #a31830; padding: 4px 0 4px 22px; text-align: left;
}}
.l24-intro-vs__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.l24-intro-vs__text p:last-child {{ margin-bottom: 0; }}
.l24-intro-vs__brief {{
  background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px;
  padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; line-height: 1.55;
}}
.l24-intro-vs__decor {{
  background: linear-gradient(160deg, #f1f5f9 0%, #fff 100%);
  border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px;
}}
.l24-intro-vs__chips {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none; }}
.l24-intro-vs__chip {{
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.03em;
  padding: 6px 10px; border-radius: 999px; background: #fff;
  border: 1px solid #cbd5e1; color: #475569;
}}
.l24-intro-vs__chip--accent {{ border-color: #1e40af; color: #1e40af; }}
.l24-intro-vs__chip--warn {{ border-color: #a31830; color: #a31830; }}
.l24-intro-vs__route-svg {{ display: block; width: 100%; height: auto; }}
.ym-toc {{
  max-width: 820px; margin: 24px auto 0; padding: 0 24px 32px;
  text-align: center; font-family: system-ui, sans-serif;
}}
.ym-toc__title {{ font-size: 0.8rem; font-weight: 700; letter-spacing: 0.06em;
  text-transform: uppercase; color: #64748b; margin: 0 0 12px;
}}
.ym-toc__list {{ list-style: none; padding: 0; margin: 0;
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
.l24-faq {{
  margin-top: 2.5em; padding: 28px 24px; background: #f8fafc;
  border: 1px solid #e2e8f0; border-radius: 12px;
}}
.l24-faq > h2 {{ margin-top: 0 !important; }}
.l24-faq__item {{ margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0; }}
.l24-faq__item:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
.l24-faq__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #1a365d; }}
.l24-faq__a {{ margin: 0; color: #334155; }}
.l24-jsonld-vs {{ display: none !important; }}
@media (max-width: 900px) {{
  .l24-intro-vs__grid {{ grid-template-columns: 1fr; }}
}}
"""

INTRO_HTML = """
<section class="l24-intro-vs" aria-label="Введение">
  <div class="l24-intro-vs__grid">
    <div class="l24-intro-vs__text">
      <p><strong>5 июня 2026 года</strong> коллегия по экономическим спорам Верховного суда РФ указала: при <strong>иске о компенсации за нарушение товарного знака</strong>, если право принадлежит иностранной компании из <strong>недружественной юрисдикции</strong>, суды <strong>обязаны проверить</strong> недружественные действия правообладателя и применимость <strong>пп. «в» п. 17 Указа Президента № 322</strong>.</p>
      <p>Ниже — фабула спора с <strong>ИП на маркетплейсе</strong>, цепочка <strong>лицензия → цессия → иск</strong>, чеклист возражений и связь с <strong>ст. 1252.1</strong> (лимит <strong>10 млн ₽</strong> с 2026 года). Номер дела ВС в открытых источниках не опубликован — ориентир <a href="https://rapsinews.ru/judicial_analyst/20260605/311909653.html" target="_blank" rel="noopener noreferrer">РАПСИ</a>.</p>
      <div class="l24-intro-vs__brief">
        <strong>Кратко:</strong> нельзя автоматически отказывать в защите ответчика или удовлетворять иск <strong>только</strong> из‑за иностранного происхождения знака. Апелляция не исследовала <strong>пп. «в» п. 17</strong> → ВС отменил акты → <strong>новое рассмотрение</strong> с проверкой поведения правообладателя и цепочки прав.
      </div>
      <p>При претензии или иске от цессионария с иностранным правообладателем можно <a href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">обсудить ответ на иск и проверку Указа № 322</a> до первого заседания.</p>
    </div>
    <aside class="l24-intro-vs__decor" aria-label="Маршрут спора">
      <ul class="l24-intro-vs__chips">
        <li class="l24-intro-vs__chip l24-intro-vs__chip--accent">ВС 05.06.2026</li>
        <li class="l24-intro-vs__chip">Указ № 322</li>
        <li class="l24-intro-vs__chip l24-intro-vs__chip--warn">пп. «в» п. 17</li>
        <li class="l24-intro-vs__chip">лицензия → цессия</li>
        <li class="l24-intro-vs__chip">ИП · маркетплейс</li>
        <li class="l24-intro-vs__chip">ст. 1252.1 · 10 млн</li>
      </ul>
      <svg class="l24-intro-vs__route-svg" viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Схема: иностранный правообладатель, лицензия, цессия, иск к ИП, проверка Указа № 322">
        <rect x="8" y="8" width="304" height="184" rx="10" fill="#fff" stroke="#cbd5e1"/>
        <text x="24" y="32" fill="#64748b" font-size="10" font-weight="700">ЦЕПОЧКА ПРАВА · ОТВЕТ НА ИСК</text>
        <circle cx="48" cy="88" r="18" fill="#ed8936"/><text x="48" y="93" text-anchor="middle" fill="#fff" font-size="7" font-weight="700">ИН</text>
        <circle cx="120" cy="88" r="18" fill="#3182ce"/><text x="120" y="93" text-anchor="middle" fill="#fff" font-size="7" font-weight="700">ЛИЦ</text>
        <circle cx="192" cy="88" r="18" fill="#805ad5"/><text x="192" y="93" text-anchor="middle" fill="#fff" font-size="7" font-weight="700">ЦЕС</text>
        <circle cx="264" cy="88" r="18" fill="#c53030"/><text x="264" y="93" text-anchor="middle" fill="#fff" font-size="7" font-weight="700">ИСК</text>
        <line x1="66" y1="88" x2="102" y2="88" stroke="#94a3b8" stroke-width="2"/>
        <line x1="138" y1="88" x2="174" y2="88" stroke="#94a3b8" stroke-width="2"/>
        <line x1="210" y1="88" x2="246" y2="88" stroke="#94a3b8" stroke-width="2"/>
        <text x="48" y="130" text-anchor="middle" fill="#475569" font-size="8">иностр. ТЗ</text>
        <text x="120" y="130" text-anchor="middle" fill="#475569" font-size="8">лицензия</text>
        <text x="192" y="130" text-anchor="middle" fill="#475569" font-size="8">цессия</text>
        <text x="264" y="130" text-anchor="middle" fill="#475569" font-size="8">ИП · МП</text>
        <rect x="24" y="148" width="272" height="36" rx="6" fill="#eff6ff" stroke="#bfdbfe"/>
        <text x="160" y="170" text-anchor="middle" fill="#1e40af" font-size="10" font-weight="700">Указ № 322 · пп. «в» п. 17 · ВС 2026</text>
      </svg>
    </aside>
  </div>
</section>

<nav class="ym-toc" aria-label="Содержание статьи">
  <p class="ym-toc__title">По статье</p>
  <ul class="ym-toc__list">
    <li><a href="#vs-komp-poziciya-vs">Позиция ВС 2026</a></li>
    <li><a href="#vs-komp-proishozhdenie-prava">Происхождение права</a></li>
    <li><a href="#vs-komp-marketplejs-skhodstvo">Маркетплейс</a></li>
    <li><a href="#vs-komp-ukaz-322">Указ № 322</a></li>
    <li><a href="#vs-komp-otvet-isk">Ответ на иск</a></li>
    <li><a href="#vs-komp-cessiya-licenziya">Цессия и лицензия</a></li>
    <li><a href="#vs-komp-1252-1">ст. 1252.1</a></li>
    <li><a href="#vs-komp-yurist">Когда юрист</a></li>
    <li><a href="#vs-komp-faq">FAQ</a></li>
  </ul>
</nav>
"""

FAQ_ITEMS = [
    (
        "Можно ли не платить компенсацию только потому, что товарный знак принадлежит иностранцу из недружественной страны?",
        "Нет. ВС 05.06.2026 указал на обязанность проверки по существу, а не на автоматический отказ в иске. Иностранное происхождение — фактор для анализа Указа № 322 и цепочки прав, но не универсальное основание «не платить». С февраля 2025 года (дело А56-2577/2023) линия ВС обратная: нельзя в принципе отказывать в защите правообладателю только из‑за юрисдикции.",
    ),
    (
        "Что такое пп. «в» п. 17 Указа № 322 и зачем оно ответчику?",
        "Это исключение: Указ не применяется к правообладателям из пп. «а» п. 1, которые надлежащим образом исполняют договоры с российскими должниками. Суды должны проверить, подпадает ли иностранная компания под это исключение. Для ответчика довод работает в связке с фактами; победа не гарантирована — при обходе счёта «О» СИП в 2026 году отказывал в применении пп. «в» (дела А50-18845/2024, А50-20994/2024).",
    ),
    (
        "Кто обычно отвечает по иску — продавец или маркетплейс?",
        "По компенсации за нарушение ТЗ ответчиком выступает продавец (ИП или ООО). Маркетплейс в ряде дел признают информационным посредником (ст. 1253.1 ГК РФ) и освобождают от компенсации при своевременном удалении карточки после уведомления (дело № А41-90502/2024). Отдельно с площадкой могут спорить о запоздалой блокировке — это иной предмет.",
    ),
    (
        "Обязателен ли претензионный порядок перед иском?",
        "Да, для юрлиц и ИП — 30 дней (п. 5.1 ст. 1252 ГК РФ). Пропуск ведёт к возврату иска. Ответ на претензию фиксирует позицию по сходству, цессии и Указу № 322 до суда.",
    ),
    (
        "Какой максимум компенсации с 2026 года?",
        "По ст. 1252.1 ГК РФ (214-ФЗ) «твёрдая» компенсация за один способ нарушения одного объекта — до 10 млн ₽ (ранее 5 млн ₽). При нескольких объектах на одном товаре — одна компенсация до двукратного максимума. Добросовестный нарушитель может претендовать на снижение до 10–500 тыс. ₽ (п. 7).",
    ),
    (
        "Что изменил ВС 05.06.2026 для дела на маркетплейсе без номера в РАПСИ?",
        "Коллегия отменила постановления апелляции и кассации и направила дело на новое рассмотрение. Нижестоящие суды не проверили пп. «в» п. 17 Указа № 322 и недружественные действия самого правообладателя. Номер дела и определения ВС в открытом доступе не опубликованы — ориентируйтесь на сообщение РАПСИ.",
    ),
    (
        "Можно ли оспорить не компенсацию, а сам товарный знак?",
        "Да. Оспаривание и аннулирование регистрации — параллельный маршрут, если знак слабый или зарегистрирован с нарушениями. Подробности — в материале об оспаривании регистрации; это не заменяет ответ на иск, но снижает риски в долгую.",
    ),
    (
        "Означает ли «доводы истца заслуживают внимания», что ИП проиграет на пересмотре?",
        "Нет. Формулировка означает, что автоматический отказ в защите только из‑за иностранного происхождения ТЗ неправомерен. Итог нового рассмотрения зависит от сходства, цессии, размера компенсации и фактов по Указу № 322 — с учётом как позиции ВС, так и контрпримеров СИП об обходе счёта «О».",
    ),
]


def extract_hero(handoff: str) -> str:
    start = handoff.index("```html", handoff.index("=== АЛИНА"))
    end = handoff.index("```\n\n=== БОРИС", start)
    hero = handoff[start + len("```html\n") : end].strip()
    return hero


def extract_boris(handoff: str) -> str:
    start = handoff.index("```html", handoff.index("=== БОРИС"))
    end = handoff.index("```\n\n**Чеклист отличий", start)
    return handoff[start + len("```html\n") : end].strip()


def extract_arthur_md(handoff: str) -> tuple[str, str]:
    start = handoff.index("### Полный текст\n", handoff.index("=== АРТУР"))
    end = handoff.index("\n\n### GEO-чеклист", start)
    md = handoff[start + len("### Полный текст\n") : end].strip()
    lines = md.splitlines()
    out: list[str] = []
    for line in lines:
        if line.startswith("# "):
            continue
        out.append(line)
    md = "\n".join(out).strip()
    h2 = md.find("\n## ")
    if h2 >= 0:
        md = md[h2 + 1 :]
    sources_md = ""
    faq_idx = md.find("\n## Частые вопросы")
    if faq_idx >= 0:
        tail = md[faq_idx:]
        src_idx = tail.find("\n## Источники и нормативная база")
        if src_idx >= 0:
            sources_md = tail[src_idx + 1 :].strip()
            # убрать дубль footer-note — добавим отдельно
            note_idx = sources_md.find("\n\n*Материал подготовлен")
            if note_idx >= 0:
                sources_md = sources_md[:note_idx].strip()
        md = md[:faq_idx].rstrip()
    return md.strip(), sources_md


def _inline(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        s,
    )
    s = re.sub(
        r"\[([^\]]+)\]\((/[^)]+)\)",
        r'<a href="\2">\1</a>',
        s,
    )
    return s


def _simple_md(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    in_ul = in_ol = in_bq = in_pre = False
    table_buf: list[str] = []
    pre_buf: list[str] = []

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
        nonlocal in_ul, in_ol, in_bq, in_pre
        if in_pre:
            out.append(f"<pre>{chr(10).join(pre_buf)}</pre>")
            pre_buf.clear()
            in_pre = False
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
        if line.strip().startswith("```"):
            if in_pre:
                out.append(f"<pre>{chr(10).join(pre_buf)}</pre>")
                pre_buf.clear()
                in_pre = False
            else:
                close_lists()
                in_pre = True
            continue
        if in_pre:
            pre_buf.append(line)
            continue
        if line.strip().startswith("|"):
            close_lists()
            table_buf.append(line)
            continue
        flush_table()
        if line.strip() == "---":
            close_lists()
            continue
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
    html = re.sub(r"<hr\s*/?>", "", html)
    return html


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
            return tag
        return tag.replace(">", ' target="_blank" rel="noopener noreferrer">', 1)

    html = re.sub(r"<a\s+[^>]*href=\"[^\"]+\"[^>]*>", repl, html)
    return html


def insert_boris(body: str, boris: str) -> str:
    hid = H2_IDS[BORIS_AFTER_H2]
    marker = f'<h2 id="{hid}">{BORIS_AFTER_H2}</h2>'
    if marker not in body:
        marker = f"<h2>{BORIS_AFTER_H2}</h2>"
    if marker not in body:
        raise RuntimeError("H2 anchor for Boris block not found")
    return body.replace(marker, marker + "\n" + boris, 1)


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
<section id="vs-komp-faq" class="l24-faq" itemscope itemtype="https://schema.org/FAQPage" aria-label="Частые вопросы">
  <h2>Частые вопросы (FAQ)</h2>
{chr(10).join(items_html)}
</section>
"""


def build_jsonld() -> str:
    entities = []
    for q, a in FAQ_ITEMS:
        entities.append(
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
        )
    payload = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}
    return json.dumps(payload, ensure_ascii=False, separators=(",", ": "))


def main() -> None:
    handoff = HANDOFF.read_text(encoding="utf-8")
    hero = strip_scripts(extract_hero(handoff))
    boris = strip_scripts(extract_boris(handoff))
    md, sources_md = extract_arthur_md(handoff)
    body = md_to_html(md)
    body = add_h2_ids(body)
    body = strip_scripts(body)
    body = fix_links(body)
    body = insert_boris(body, boris)

    bottom_cta = """
<aside class="ym-cta ym-cta--legis24 ym-cta--bottom" role="complementary">
  <p class="ym-cta__text"><strong>Legis24</strong> — материалы и консультации по спорам о товарных знаках на маркетплейсах: ответ на иск и претензию, защита от компенсации при иностранном правообладателе, Указ № 322.</p>
  <p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Обсудить спор с юристом</a></p>
</aside>
"""

    if sources_md:
        sources_html = md_to_html(sources_md)
        sources_html = add_h2_ids(sources_html)
        sources_html = fix_links(sources_html)
    else:
        sources_html = ""

    footer = (
        '<p><em>Материал подготовлен для продавцов и ИП, получивших претензию или иск о компенсации за '
        "<strong>сходное обозначение</strong> от правообладателя / цессионария с <strong>иностранным</strong> "
        "происхождением права. Не является индивидуальной юридической консультацией.</em></p>"
    )

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
{bottom_cta}
{sources_html}
{footer}
</div>
{faq}
<pre class="l24-jsonld-vs" aria-hidden="true" hidden>{jsonld}</pre>
</main>
<!-- /wp:html -->
"""
    html = strip_scripts(html)
    html = fix_links(html)

    OUT_HTML.write_text(html, encoding="utf-8")
    size_kb = len(html.encode("utf-8")) / 1024

    natasha_block = f"""
=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО

**SLUG:** `{SLUG}`
**Файл:** `.cursor/page-content-natasha-vs-kompensaciya.html`
**Размер:** {size_kb:.1f} KB ({len(html)} символов)

### Передача Юре
**Title:** {TITLE}
**Description:** {DESCRIPTION}
**slug:** `{SLUG}`
**page_id:** `PLACEHOLDER` (заполнить после wordpress_create_page)

**Публикация:** `commands/nero-publish-mcp.md` — blob flow; без `<script>` и `<canvas>` (hero Алины и блок Бориса — static SVG + inline CSS).
**JSON-LD:** скрытый FAQPage в `<pre class="l24-jsonld-vs">`; дублировать в Rank Math при необходимости.

**Проверка live:**
- `main#primary` + класс `{SLUG}-page`
- hero `#l24-hero-vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany`
- блок Бориса `#l24-boris-vs-kompensaciya-ukaz322` после H2 «Указ № 322»
- breadcrumbs скрыты; CTA только `https://advokat-vsem.ru/`
- нет `<script>` / `<canvas>`

```html
{html}
```
"""

    if "=== НАТАША (HTML СТРАНИЦЫ) ===" in handoff:
        handoff = handoff.split("=== НАТАША (HTML СТРАНИЦЫ) ===")[0].rstrip()
    handoff = handoff.rstrip() + "\n\n" + natasha_block.lstrip() + "\n"
    HANDOFF.write_text(handoff, encoding="utf-8")

    has_script = bool(re.search(r"<script\b", html, re.I))
    has_canvas = bool(re.search(r"<canvas\b", html, re.I))
    has_main = 'id="primary"' in html and f"{SLUG}-page" in html

    print(f"Written {OUT_HTML}")
    print(f"Size: {size_kb:.1f} KB")
    print(f"main#primary: {has_main}")
    print(f"no script: {not has_script}")
    print(f"no canvas: {not has_canvas}")
    print("Handoff updated")


if __name__ == "__main__":
    main()
