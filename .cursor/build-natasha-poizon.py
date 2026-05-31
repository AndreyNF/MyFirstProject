#!/usr/bin/env python3
"""Сборка HTML страницы POIZON / СИП для handoff Наташи."""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

try:
    import markdown
except ImportError:
    markdown = None

ROOT = Path(__file__).resolve().parents[1]
HANDOFF = ROOT / ".cursor/nero-network-handoff.md"
ALINA = ROOT / ".cursor/nero-network-fragments/alina.md"
BORIS = ROOT / ".cursor/nero-network-fragments/boris.md"
OUT_HTML = ROOT / ".cursor/page-content-natasha-poizon-sip.html"
SLUG = "poizon-tovarnyj-znak-sip-osporenie-registracii"

TITLE = "POIZON в СИП: оспаривание товарного знака и признание регистрации недействительной | Legis24"
DESCRIPTION = (
    "Решение Суда по интеллектуальным правам по товарным знакам POIZON и «Пойзон»: "
    "недобросовестная конкуренция, основания признания регистрации недействительной, "
    "отличие от возражения в Роспатенте и что делать правообладателю и ответчику. Консультация Legis24."
)

H2_IDS = {
    "Что решил Суд по интеллектуальным правам по товарным знакам POIZON и «Пойзон»": "poizon-sip-reshenie",
    "Оспаривание регистрации товарного знака: когда идут в СИП, а не только в Роспатент": "poizon-osporenie-sip",
    "Судебная защита товарного знака: практика СИП после дела POIZON": "poizon-sudebnaya-zashchita",
    "Защита товарного знака и бренда: чек-лист для правообладателя": "poizon-cheklist",
    "Товарный знак на маркетплейсе: как защитить бренд, если на вас ссылаются на чужой знак": "poizon-marketplejs",
    "Если на вас подали или вы проиграли оспаривание: действия ответчика": "poizon-dejstviya-otvetchika",
    "Частые вопросы (FAQ)": "poizon-faq",
}

BORIS_AFTER_H2 = "Оспаривание регистрации товарного знака: когда идут в СИП, а не только в Роспатент"

PAGE_CSS = f"""
.breadcrumbs, .breadcrumb, .woocommerce-breadcrumb, .rank-math-breadcrumb, .yoast-breadcrumb,
.entry-header, .page-title-section {{ display: none !important; }}
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
.{SLUG}-page th,
.{SLUG}-page td {{
  border: 1px solid #e2e8f0; padding: 10px 12px; text-align: left;
}}
.{SLUG}-page th {{ background: #edf2f7; }}
.{SLUG}-page a {{ color: #1e40af; }}
.{SLUG}-page ol, .{SLUG}-page ul {{ margin: 1em 0; padding-left: 1.4em; }}
.{SLUG}-page li {{ margin-bottom: 0.45em; }}
.l24-intro-tz {{
  max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}}
.l24-intro-tz__grid {{
  display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
  gap: 28px; align-items: start;
}}
.l24-intro-tz__text {{
  border-left: 4px solid #a31830; padding: 4px 0 4px 22px; text-align: left;
}}
.l24-intro-tz__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.l24-intro-tz__text p:last-child {{ margin-bottom: 0; }}
.l24-intro-tz__brief {{
  background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px;
  padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; line-height: 1.55;
}}
.l24-intro-tz__decor {{
  background: linear-gradient(160deg, #f1f5f9 0%, #fff 100%);
  border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px;
}}
.l24-intro-tz__chips {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none; }}
.l24-intro-tz__chip {{
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.03em;
  padding: 6px 10px; border-radius: 999px; background: #fff;
  border: 1px solid #cbd5e1; color: #475569;
}}
.l24-intro-tz__chip--accent {{ border-color: #1e40af; color: #1e40af; }}
.l24-intro-tz__chip--warn {{ border-color: #a31830; color: #a31830; }}
.l24-intro-tz__route-svg {{ display: block; width: 100%; height: auto; }}
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
.l24-faq-tz {{
  margin-top: 2.5em; padding: 28px 24px; background: #f8fafc;
  border: 1px solid #e2e8f0; border-radius: 12px;
}}
.l24-faq-tz h2 {{ margin-top: 0 !important; }}
.l24-faq-tz__item {{ margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0; }}
.l24-faq-tz__item:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
.l24-faq-tz__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #1a365d; }}
.l24-faq-tz__a {{ margin: 0; color: #334155; }}
@media (max-width: 900px) {{
  .l24-intro-tz__grid {{ grid-template-columns: 1fr; }}
}}
"""

INTRO_HTML = """
<section class="l24-intro-tz" aria-label="Введение">
  <div class="l24-intro-tz__grid">
    <div class="l24-intro-tz__text">
      <p>В мае 2026 года Суд по интеллектуальным правам (СИП) огласил резолютивную часть решения, которое в медиа описывают как поражение российского правообладателя знака <strong>POIZON</strong>: охрана товарного знака на <strong>ООО «Пойзон»</strong> признана <strong>недействительной</strong> по иску <strong>Shanghai Shizhuang</strong> (маркетплейс <strong>Dewu</strong> / <strong>Poizon</strong>).</p>
      <p>Ниже — разбор дела <strong>СИП-1182/2024</strong>, отличия <strong>возражения в Роспатенте</strong> от иска в СИП, чек-лист для правообладателя и ответчика, маркетплейс-контекст и ответы на частые вопросы.</p>
      <div class="l24-intro-tz__brief">
        <strong>Кратко:</strong> регистрация в Роспатенте не закрывает риски при сильном глобальном бренде; после отклонения возражения следующий рубеж — <strong>судебное оспаривание</strong> по ст. 1513 п. 4 ГК РФ и недобросовестная конкуренция; ООО «Пойзон» обжалует в <strong>президиум СИП</strong> (кассация 1 месяц).
      </div>
      <p>Если нужна оценка рисков по вашему знаку или стратегия оспаривания чужой регистрации, можно <a href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">получить консультацию по защите бренда и оспариванию регистрации</a>.</p>
    </div>
    <aside class="l24-intro-tz__decor" aria-label="Ключевые метки дела">
      <ul class="l24-intro-tz__chips">
        <li class="l24-intro-tz__chip l24-intro-tz__chip--accent">СИП-1182/2024</li>
        <li class="l24-intro-tz__chip">№ 983757</li>
        <li class="l24-intro-tz__chip">№ 1026380</li>
        <li class="l24-intro-tz__chip l24-intro-tz__chip--warn">ст. 1512–1513</li>
        <li class="l24-intro-tz__chip">класс 35 МКТУ</li>
        <li class="l24-intro-tz__chip">президиум СИП</li>
      </ul>
      <svg class="l24-intro-tz__route-svg" viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Схема: регистрация знака, возражение в Роспатенте, иск в СИП, кассация">
        <rect x="8" y="8" width="304" height="184" rx="10" fill="#fff" stroke="#cbd5e1"/>
        <text x="24" y="32" fill="#64748b" font-size="10" font-weight="700">ПОСТРЕГИСТРАЦИОННОЕ ОСПАРИВАНИЕ</text>
        <circle cx="48" cy="88" r="18" fill="#3182ce"/><text x="48" y="93" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">Рег</text>
        <circle cx="120" cy="88" r="18" fill="#2b6cb0"/><text x="120" y="93" text-anchor="middle" fill="#fff" font-size="7" font-weight="700">Росп</text>
        <circle cx="192" cy="88" r="18" fill="#c53030"/><text x="192" y="93" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">СИП</text>
        <circle cx="264" cy="88" r="18" fill="#d69e2e"/><text x="264" y="93" text-anchor="middle" fill="#fff" font-size="7" font-weight="700">Касс</text>
        <line x1="66" y1="88" x2="102" y2="88" stroke="#94a3b8" stroke-width="2"/>
        <line x1="138" y1="88" x2="174" y2="88" stroke="#94a3b8" stroke-width="2"/>
        <line x1="210" y1="88" x2="246" y2="88" stroke="#94a3b8" stroke-width="2"/>
        <text x="48" y="130" text-anchor="middle" fill="#475569" font-size="8">12.2023</text>
        <text x="120" y="130" text-anchor="middle" fill="#475569" font-size="8">возраж.</text>
        <text x="192" y="130" text-anchor="middle" fill="#475569" font-size="8">май 2026</text>
        <text x="264" y="130" text-anchor="middle" fill="#475569" font-size="8">1 мес.</text>
        <rect x="24" y="148" width="272" height="36" rx="6" fill="#eff6ff" stroke="#bfdbfe"/>
        <text x="160" y="170" text-anchor="middle" fill="#1e40af" font-size="10" font-weight="700">DEWU vs ООО «Пойзон»</text>
      </svg>
    </aside>
  </div>
</section>

<nav class="ym-toc" aria-label="Содержание статьи">
  <p class="ym-toc__title">По статье</p>
  <ul class="ym-toc__list">
    <li><a href="#poizon-sip-reshenie">Решение СИП по POIZON</a></li>
    <li><a href="#poizon-osporenie-sip">Оспаривание в СИП</a></li>
    <li><a href="#poizon-sudebnaya-zashchita">Судебная защита</a></li>
    <li><a href="#poizon-cheklist">Чек-лист правообладателя</a></li>
    <li><a href="#poizon-marketplejs">Маркетплейс</a></li>
    <li><a href="#poizon-dejstviya-otvetchika">Действия ответчика</a></li>
    <li><a href="#poizon-faq">FAQ</a></li>
  </ul>
</nav>
"""

BOTTOM_CTA = """
<aside class="ym-cta ym-cta--legis24 ym-cta--bottom" role="complementary">
  <p class="ym-cta__text"><strong>Legis24</strong> — консультации по оспариванию регистрации товарного знака, защите бренда на маркетплейсе и стратегии в СИП после дела POIZON: возражение в Роспатенте, иск по ст. 1513 п. 4, кассация в президиум.</p>
  <p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по защите бренда и оспариванию регистрации</a></p>
</aside>
"""


def extract_hero() -> str:
    text = ALINA.read_text(encoding="utf-8")
    idx = text.find("<section")
    return text[idx:].strip()


def extract_boris() -> str:
    text = BORIS.read_text(encoding="utf-8")
    return text.split("```html", 1)[1].rsplit("```", 1)[0].strip()


def extract_arthur_md() -> str:
    handoff = HANDOFF.read_text(encoding="utf-8")
    start = handoff.index("### Полный текст\n", handoff.index("=== АРТУР"))
    end = handoff.index("\n\n### Рекламные вставки", start)
    md = handoff[start + len("### Полный текст\n") : end].strip()
    lines = md.splitlines()
    out: list[str] = []
    for line in lines:
        if line.startswith("# ") or line.startswith("*Дело DEWU"):
            continue
        out.append(line)
    md = "\n".join(out).strip()
    # ввод — в блоке l24-intro-tz; тело с первого H2
    h2 = md.find("\n## ")
    if h2 >= 0:
        md = md[h2 + 1 :]
    return md.strip()


def md_to_html(md: str) -> str:
    if markdown:
        html = markdown.markdown(
            md,
            extensions=["tables", "sane_lists"],
        )
    else:
        html = _simple_md(md)
    html = re.sub(r"<hr\s*/?>", "", html)
    return html


def _simple_md(md: str) -> str:
    """Минимальный fallback без python-markdown."""
    lines = md.splitlines()
    out: list[str] = []
    in_ul = in_ol = False
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
            if i == 0:
                pass
        out.append("</tbody></table>")
        table_buf = []

    def close_lists():
        nonlocal in_ul, in_ol
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
        if line.strip() == "---":
            close_lists()
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
        if line.strip().startswith("<a ") or (line.strip() and not line.startswith("<")):
            close_lists()
            if line.strip():
                out.append(f"<p>{_inline(line)}</p>" if not line.strip().startswith("<") else line)
            continue
        if line.strip().startswith("<"):
            close_lists()
            out.append(line)
            continue
        if not line.strip():
            close_lists()
            continue
    flush_table()
    close_lists()
    return "\n".join(out)


def _inline(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
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


def add_h2_ids(html: str) -> str:
    for title, hid in H2_IDS.items():
        esc = re.escape(title)
        html = re.sub(
            rf"<h2>({esc})</h2>",
            rf'<h2 id="{hid}">\1</h2>',
            html,
        )
    return html


def strip_scripts(html: str) -> str:
    html = re.sub(r"<script\b[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<script\b[^>]*/>", "", html, flags=re.IGNORECASE)
    return html


def fix_links(html: str) -> str:
    def repl(m: re.Match[str]) -> str:
        tag = m.group(0)
        if 'target="_blank"' in tag:
            return tag
        if tag.endswith("/>"):
            return tag[:-2] + ' target="_blank" rel="noopener noreferrer" />'
        return tag.replace(">", ' target="_blank" rel="noopener noreferrer">', 1)

    html = re.sub(r'<a\s+[^>]*href="https?://[^"]+"[^>]*>', repl, html)
    return html


def insert_boris(body: str, boris: str) -> str:
    marker = f'<h2 id="poizon-osporenie-sip">{BORIS_AFTER_H2}</h2>'
    if marker not in body:
        marker = f"<h2>{BORIS_AFTER_H2}</h2>"
    if marker not in body:
        raise RuntimeError("H2 anchor for Boris block not found")
    return body.replace(marker, marker + "\n" + boris, 1)


FAQ_ITEMS = [
    (
        "Можно ли оспорить регистрацию товарного знака после выдачи свидетельства?",
        "Да. <strong>Возражение в Роспатент</strong> и <strong>иск в СИП</strong> (после решения Роспатента) — основные инструменты. Сроки зависят от основания (<strong>ст. 1512</strong>, <strong>1513</strong> ГК РФ).",
    ),
    (
        "Чем это отличается от отказа в регистрации?",
        "При <strong>отказе</strong> знак <strong>не выдан</strong> — спор об <strong>отказе</strong> (административный и судебный порядок, близко к A15). В POIZON знак <strong>был зарегистрирован</strong> в декабре 2023 года, затем <strong>оспорен</strong> успешным правообладателем глобального бренда.",
    ),
    (
        "Сколько длятся дела в СИП по товарным знакам?",
        "Зависит от сложности и стадии; дело <strong>СИП-1182/2024</strong> от иска (осень 2024) до оглашения резолютивной части (май 2026) — ориентир <strong>около полутора лет</strong> на первую инстанцию. Кассация добавляет месяцы.",
    ),
    (
        "Что такое недействительный товарный знак?",
        "Знак, в отношении которого суд или Роспатент <strong>признали регистрацию (или часть охраны) недействительной</strong> с момента, определённым решением. Исключительное право <strong>не применяется</strong> в аннулированном объёме.",
    ),
    (
        "Остался ли у ООО «Пойзон» знак «Пойзон» по № 1026380?",
        "По публичным сообщениям мая 2026 акцент на <strong>POIZON</strong> (латиница). Статус <strong>№ 1026380</strong> уточняйте по полному тексту решения СИП и реестру ФИПС после вступления акта в силу.",
    ),
    (
        "Нужно ли иностранной компании регистрировать знак в России до выхода на рынок?",
        "Да, если планируются <strong>маркетплейс</strong>, реклама и защита от «локальных» регистраций. История DEWU vs poizon.ru — прямой аргумент <strong>не откладывать</strong> filing в РФ.",
    ),
    (
        "Что делать, если на меня подали иск о нарушении, а не о недействительности регистрации?",
        "Это другой тип спора (защита от иска о <strong>использовании</strong> знака). Смотрите материал об <strong>ответе на иск по ИС</strong> (B2); в POIZON-контексте ключ — <strong>аннулирование</strong> чужой или своей регистрации.",
    ),
]


def build_faq_section() -> str:
    items_html = []
    for q, a in FAQ_ITEMS:
        items_html.append(
            f"""  <div class="l24-faq-tz__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 class="l24-faq-tz__q" itemprop="name">{q}</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p class="l24-faq-tz__a" itemprop="text">{a}</p>
    </div>
  </div>"""
        )
    return f"""
<section id="poizon-faq" class="l24-faq-tz" itemscope itemtype="https://schema.org/FAQPage" aria-label="Частые вопросы">
  <h2>Частые вопросы (FAQ)</h2>
{chr(10).join(items_html)}
</section>
"""


def strip_faq_from_body(body: str) -> str:
    return re.sub(
        r'<h2[^>]*id="poizon-faq"[^>]*>Частые вопросы \(FAQ\)</h2>.*?(?=<p><em>Материал подготовлен|$)',
        "",
        body,
        flags=re.DOTALL,
    ).strip()


def main() -> None:
    hero = extract_hero()
    boris = extract_boris()
    md = extract_arthur_md()
    body = md_to_html(md)
    body = add_h2_ids(body)
    body = strip_scripts(body)
    body = fix_links(body)
    body = insert_boris(body, boris)
    body = strip_faq_from_body(body)
    faq = build_faq_section()

    # footer note from Arthur
    footer = ""
    fm = re.search(r"<p><em>Материал подготовлен.*?</em></p>", body, re.DOTALL)
    if fm:
        footer = fm.group(0)
        body = body.replace(footer, "").strip()

    html = f"""<!-- wp:html -->
<style>
{PAGE_CSS}
</style>
<main id="primary" class="site-main {SLUG}-page" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">
{hero}
{INTRO_HTML}
<div class="l24-longread-wrap" itemprop="articleBody">
{body}
{faq}
{BOTTOM_CTA}
{footer}
</div>
</main>
<!-- /wp:html -->
"""
    html = strip_scripts(html)

    OUT_HTML.write_text(html, encoding="utf-8")
    char_count = len(html)

    natasha_block = f"""
=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО

### HTML
```html
{html}
```

### Передача Юре
**slug:** `{SLUG}`
**title:** {TITLE}
**excerpt (Description):** {DESCRIPTION}
**page_id:** `PLACEHOLDER` (заполнить после wordpress_create_page)

**Публикация:** обернуть в `<!-- wp:html -->`; без `<script>` (hero и Борис — static SVG + CSS). FAQ — microdata FAQPage.
**Проверка:** `main#primary`, класс `{SLUG}-page`, hero `#l24-hero-ip-poizon-sip`, блок `#l24-boris-poizon-sip-osporenie`, breadcrumbs скрыты, CTA https://advokat-vsem.ru/
**Размер HTML:** {char_count} символов
"""

    handoff = HANDOFF.read_text(encoding="utf-8")
    if "=== НАТАША (HTML СТРАНИЦЫ) ===" in handoff:
        handoff = handoff.split("=== НАТАША (HTML СТРАНИЦЫ) ===")[0].rstrip()
    handoff = handoff.rstrip() + "\n\n" + natasha_block.lstrip()

    HANDOFF.write_text(handoff, encoding="utf-8")
    print(f"Written {OUT_HTML} ({char_count} chars)")


if __name__ == "__main__":
    main()
