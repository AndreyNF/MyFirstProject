#!/usr/bin/env python3
"""Assemble Natasha HTML page for FNS vznosy slot."""
import re
import json
from pathlib import Path

SLUG = "fns-strahovye-vznosy-vtoraya-ochered-bankrotstvo-vs"
PAGE_CLASS = f"{SLUG}-page"
ROOT = Path("/workspace/.cursor")
HANDOFF = ROOT / "nero-network-handoff.md"
OUT = ROOT / "page-content-natasha-fns-vznosy.html"

H2_IDS = {
    "Определение ВС от 6 мая 2026 и единый тариф страховых взносов с 2023 года": "fns-vs-opredelenie-2026",
    "Вторая и третья очередь реестра требований кредиторов": "fns-vs-ocheredi-reestr",
    "Банкротство юридического лица и ООО: кто затронут": "fns-vs-bankrotstvo-ooo",
    "Включение требований ФНС в реестр: заявление, сроки, возражения": "fns-vs-vklyuchenie-reestr",
    "Споры с ФНС в арбитраже при банкротстве": "fns-vs-spory-fns",
    "Судебная практика 2026: аналоги и тренд ВС": "fns-vs-praktika-2026",
    "Стратегия до суда: чеклист для кредитора и управляющего": "fns-vs-strategiya",
    "Консультация по арбитражному спору и включению в реестр": "fns-vs-konsultaciya",
}


def extract_html_block(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    m = re.search(r"```html\n(.*?)```", text, re.DOTALL)
    if not m:
        raise ValueError(f"No html block in {path}")
    return m.group(1).strip()


def extract_artur_md(handoff: str) -> str:
    m = re.search(
        r"=== АРТУР \(CTA И РЕКЛАМА\) ===.*?### Полный текст\n\n(.*?)\n\n### Рекламные вставки",
        handoff,
        re.DOTALL,
    )
    if not m:
        raise ValueError("Artur section not found")
    body = m.group(1).strip()
    # drop leading # title
    body = re.sub(r"^# .+\n\n", "", body, count=1)
    return body


def slugify_heading(title: str) -> str:
    return H2_IDS.get(title.strip(), re.sub(r"[^a-z0-9]+", "-", title.lower())[:40].strip("-"))


def inline_md(text: str) -> str:
    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        text,
    )
    text = re.sub(r"\[([^\]]+)\]\((/[^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def parse_table(lines: list[str]) -> str:
    rows = []
    for line in lines:
        if not line.strip() or not line.strip().startswith("|"):
            continue
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
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "BORIS_PLACEHOLDER":
            out.append(boris_html)
            i += 1
            continue
        if line.startswith("<aside") or line.startswith("</aside>"):
            block = [line]
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("</aside>"):
                block.append(lines[i])
                i += 1
            if i < len(lines):
                block.append(lines[i])
                i += 1
            out.append("\n".join(block))
            continue
        if line.startswith("## "):
            title = line[3:].strip()
            hid = slugify_heading(title)
            out.append(f'<h2 id="{hid}">{inline_md(title)}</h2>')
            i += 1
            continue
        if line.startswith("### "):
            title = line[4:].strip()
            out.append(f"<h3>{inline_md(title)}</h3>")
            i += 1
            continue
        if line.strip() == "---":
            i += 1
            continue
        if line.strip().startswith("|"):
            tbl_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl_lines.append(lines[i])
                i += 1
            out.append(parse_table(tbl_lines))
            continue
        if line.strip().startswith(">"):
            bq = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                bq.append(lines[i].strip()[1:].strip())
                i += 1
            out.append(f"<blockquote><p>{inline_md(' '.join(bq))}</p></blockquote>")
            continue
        if re.match(r"^\d+\.\s", line.strip()):
            out.append("<ol>")
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i].strip()):
                item = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                out.append(f"<li>{inline_md(item)}</li>")
                i += 1
            out.append("</ol>")
            continue
        if line.strip():
            para_lines = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith("#") and not lines[i].strip().startswith("|") and not lines[i].strip().startswith(">") and not lines[i].startswith("<aside") and lines[i].strip() != "---" and not re.match(r"^\d+\.\s", lines[i].strip()) and lines[i].strip() != "BORIS_PLACEHOLDER":
                para_lines.append(lines[i])
                i += 1
            out.append(f"<p>{inline_md(' '.join(para_lines))}</p>")
            continue
        i += 1
    return "\n\n".join(out)


def build_lead_block() -> str:
    return """
<p><strong>Лид.</strong> С 1 января 2023 года работодатели платят единый страховой взнос вместо раздельных платежей на ОПС, ОМС и соцстрахование. В банкротстве юридического лица это меняет не только бухгалтерию, но и <strong>реестр требований кредиторов</strong>: ФНС всё чаще добивается включения всей задолженности по взносам во <strong>вторую очередь</strong>, а не в третью. Определение Судебной коллегии по экономическим спорам Верховного суда РФ от <strong>6 мая 2026 года</strong> № 309-ЭС24-8891 (3) по делу № <strong>А47-12711/2023</strong> закрепило линию на сумме <strong>981 628,14 руб.</strong> и стало свежим якорем <strong>обзора верховного суда 2026 по банкротству</strong> в части очередности. Ниже — что это значит для директора должника, кредитора третьей очереди и арбитражного управляющего при <strong>включении в реестр требований кредиторов</strong> и <strong>спорах с ФНС</strong> в арбитраже.</p>
<blockquote><p><strong>Тезис.</strong> После реформы 2023 года основной долг по единому тарифу страховых взносов при банкротстве ООО и иных юрлиц относится ко <strong>второй очереди реестра</strong> (абз. 3 п. 4 ст. 134 Закона о банкротстве). Дробление взносов на «пенсионную» и «немедицинскую» части суды всё ещё допускали по инерции Обзора ВС № 3 (2017) — ВС эту линию закрыл.</p></blockquote>
"""


def build_intro() -> str:
    return """
<section class="l24-intro-vs" aria-label="Введение">
  <div class="l24-intro-vs__grid">
    <div class="l24-intro-vs__text">
      <p>Определение СКЭС Верховного суда РФ от <strong>6 мая 2026 года</strong> по делу № <strong>А47-12711/2023</strong> закрепило: после единого тарифа страховых взносов с <strong>1 января 2023 года</strong> основной долг ФНС по взносам включается во <strong>вторую очередь реестра требований кредиторов</strong>, а не в третью. Для <strong>банкротства юридических лиц</strong> и <strong>банкротства ООО</strong> это меняет расчёт конкурсной массы и тактику <strong>включения в реестр</strong>.</p>
      <p>Ниже — фабула дела «Ташлинский», очередность по <strong>абз. 3 п. 4 ст. 134</strong>, чеклист возражений и линия практики ВС 2025–2026 без дублирования статьи про <a href="/vs-obzor-5-2026-subsidiarnaya-otvetstvennost-kreditora/">субсидиарку кредитора по обзору № 5/2026</a>.</p>
      <div class="l24-intro-vs__brief">
        <strong>Краткий тезис:</strong> единый страховой взнос с 2023 года — элемент расходов на труд; ВС перенёс <strong>981 628,14 руб.</strong> ОМС и соцстрахования из 3-й во 2-ю очередь (~27% заявленных взносов). Ответ на вопрос 2 Обзора ВС № 3 (2017) исключён; опора — <strong>п. 3 обзора № 5/2026</strong> и определения СКЭС 2025–2026.
      </div>
      <p>При подготовке <strong>заявления в реестр</strong> или возражений к УФНС можно <a href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">получить консультацию по арбитражному спору и включению в реестр</a>.</p>
    </div>
    <aside class="l24-intro-vs__decor" aria-label="Ключевые метки">
      <ul class="l24-intro-vs__chips">
        <li class="l24-intro-vs__chip l24-intro-vs__chip--accent">ВС 06.05.2026</li>
        <li class="l24-intro-vs__chip">А47-12711/2023</li>
        <li class="l24-intro-vs__chip l24-intro-vs__chip--warn">2-я очередь</li>
        <li class="l24-intro-vs__chip">единый тариф 2023</li>
        <li class="l24-intro-vs__chip">обзор № 5/2026 п. 3</li>
        <li class="l24-intro-vs__chip">ФНС · реестр</li>
      </ul>
      <svg class="l24-intro-vs__route-svg" viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Схема: единый взнос ФНС из 3-й очереди во 2-ю по определению ВС">
        <rect x="8" y="8" width="304" height="184" rx="10" fill="#fff" stroke="#cbd5e1"/>
        <text x="24" y="32" fill="#64748b" font-size="10" font-weight="700">ОЧЕРЕДИ РЕЕСТРА · ВЗНОСЫ ФНС</text>
        <rect x="24" y="48" width="88" height="36" rx="6" fill="#fee2e2" stroke="#fca5a5"/>
        <text x="68" y="70" text-anchor="middle" fill="#a31830" font-size="8" font-weight="700">3-я · до ВС</text>
        <text x="68" y="82" text-anchor="middle" fill="#64748b" font-size="7">ОМС+соц</text>
        <path d="M112 66 H148" stroke="#a31830" stroke-width="2" marker-end="url(#fns-intro-arr)"/>
        <defs><marker id="fns-intro-arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#a31830"/></marker></defs>
        <rect x="148" y="48" width="88" height="36" rx="6" fill="#fef2f2" stroke="#a31830" stroke-width="1.4"/>
        <text x="192" y="70" text-anchor="middle" fill="#a31830" font-size="8" font-weight="700">2-я · после ВС</text>
        <text x="192" y="82" text-anchor="middle" fill="#64748b" font-size="7">981 628 ₽</text>
        <rect x="24" y="100" width="272" height="32" rx="6" fill="#eff6ff" stroke="#93c5fd"/>
        <text x="160" y="120" text-anchor="middle" fill="#1e40af" font-size="9" font-weight="700">абз. 3 п. 4 ст. 134 · единый тариф</text>
        <rect x="24" y="144" width="128" height="36" rx="6" fill="#fff" stroke="#94a3b8"/>
        <text x="88" y="166" text-anchor="middle" fill="#334155" font-size="8" font-weight="700">кредитор 3-й</text>
        <rect x="168" y="144" width="128" height="36" rx="6" fill="#fff" stroke="#a31830"/>
        <text x="232" y="166" text-anchor="middle" fill="#a31830" font-size="8" font-weight="700">УФНС · возражения</text>
      </svg>
    </aside>
  </div>
</section>
"""


def build_toc() -> str:
    items = [
        ("fns-vs-opredelenie-2026", "Определение ВС 2026"),
        ("fns-vs-ocheredi-reestr", "2-я и 3-я очередь"),
        ("fns-vs-bankrotstvo-ooo", "Банкротство ООО"),
        ("fns-vs-vklyuchenie-reestr", "Включение в реестр"),
        ("fns-vs-spory-fns", "Споры с ФНС"),
        ("fns-vs-praktika-2026", "Практика 2026"),
        ("fns-vs-strategiya", "Чеклист"),
        ("fns-vs-konsultaciya", "Консультация"),
        ("fns-faq", "FAQ"),
    ]
    lis = "\n".join(f'    <li><a href="#{a}">{t}</a></li>' for a, t in items)
    return f"""
<nav class="ym-toc" aria-label="Содержание статьи">
  <p class="ym-toc__title">По статье</p>
  <ul class="ym-toc__list">
{lis}
  </ul>
</nav>
"""


def build_faq() -> str:
    faqs = [
        ("Вся ли задолженность ФНС при банкротстве идёт во 2-ю очередь?",
         "Нет. <strong>Основной долг</strong> по <strong>единому тарифу</strong> с <strong>01.01.2023</strong> — по линии ВС во <strong>2-ю очередь</strong>. <strong>Пени, штрафы, иные налоги</strong> (как в деле Ташлинского — сотни миллионов в 3-й очереди) квалифицируются отдельно."),
        ("Можно ли ссылаться на Обзор ВС № 3 (2017), вопрос 2?",
         "Нет. Ответ <strong>исключён</strong>; суды опираются на <strong>абз. 3 п. 4 ст. 134</strong>, <strong>обзор № 5/2026</strong> и определения <strong>2025–2026</strong>."),
        ("Что делать кредитору третьей очереди?",
         "Подать <strong>возражения</strong> к заявлению ФНС, проверить период и состав суммы, при неблагоприятном определении — <strong>апелляция и кассация</strong> со ссылкой на <strong>А47-12711/2023</strong>, <strong>А05-13820/2023</strong> и <strong>п. 3 обзора № 5/2026</strong>."),
        ("Относится ли позиция к банкротству ИП?",
         "Материал ориентирован на <strong>банкротство ООО</strong> и юрлиц; у ИП иная связка норм — нужен отдельный анализ."),
        ("Чем этот разбор отличается от статьи про обзор № 5/2026 и субсидиарку?",
         "Там — <strong>субсидиарная ответственность</strong> конкурсного кредитора; здесь — <strong>очередность страховых взносов ФНС</strong> и <strong>реестр</strong> по определению <strong>06.05.2026</strong>."),
        ("Нужно ли оспаривать сделки, если спор только о взносах?",
         "Как правило <strong>нет</strong> — достаточно реестрового спора; оспаривание сделок — иной процессуальный трек."),
        ("Какие суммы «переезжают» из 3-й во 2-ю?",
         "Зависит от расчёта ФНС: в каноническом деле <strong>981 628,14 руб.</strong>; в «Арктика-Магистраль» — <strong>854 007 руб.</strong>; в других делах — до <strong>~1,3 млн руб.</strong>"),
    ]
    items = []
    for q, a in faqs:
        items.append(f"""<div class="l24-faq__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
<h3 class="l24-faq__q" itemprop="name">{q}</h3>
<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
<p class="l24-faq__a" itemprop="text">{a}</p>
</div>
</div>""")
    return f"""
<section id="fns-faq" class="l24-faq" itemscope itemtype="https://schema.org/FAQPage" aria-label="Частые вопросы">
<h2>Частые вопросы (FAQ)</h2>
{"".join(items)}
</section>
"""


def build_jsonld() -> str:
    faqs = [
        ("Вся ли задолженность ФНС при банкротстве идёт во 2-ю очередь?",
         "Нет. Основной долг по единому тарифу с 01.01.2023 — по линии ВС во 2-ю очередь. Пени, штрафы и иные налоги квалифицируются отдельно."),
        ("Можно ли ссылаться на Обзор ВС № 3 (2017), вопрос 2?",
         "Нет. Ответ исключён; суды опираются на абз. 3 п. 4 ст. 134, обзор № 5/2026 и определения 2025–2026."),
        ("Что делать кредитору третьей очереди?",
         "Подать возражения к заявлению ФНС, проверить период и состав суммы, при неблагоприятном определении — апелляция и кассация со ссылкой на А47-12711/2023 и п. 3 обзора № 5/2026."),
        ("Относится ли позиция к банкротству ИП?",
         "Материал ориентирован на банкротство ООО и юрлиц; у ИП иная связка норм."),
        ("Чем отличается от статьи про субсидиарку по обзору № 5/2026?",
         "Там — субсидиарная ответственность кредитора; здесь — очередность страховых взносов ФНС по определению 06.05.2026."),
        ("Нужно ли оспаривать сделки, если спор только о взносах?",
         "Как правило нет — достаточно реестрового спора."),
        ("Какие суммы переезжают из 3-й во 2-ю?",
         "В деле Ташлинского — 981 628,14 руб.; в Арктика-Магистраль — 854 007 руб."),
    ]
    main_entity = []
    for q, a in faqs:
        main_entity.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        })
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": main_entity,
    }
    return f'<pre class="l24-jsonld-vs" aria-hidden="true" hidden>{json.dumps(data, ensure_ascii=False)}</pre>'


def page_styles() -> str:
    p = PAGE_CLASS
    ref = (ROOT / "page-content-natasha-vs-obzor.html").read_text(encoding="utf-8")
    m = re.search(r"<style>\n(.*?)\n</style>", ref, re.DOTALL)
    css = m.group(1) if m else ""
    css = css.replace("vs-obzor-5-2026-subsidiarnaya-otvetstvennost-kreditora-page", p)
    return css


def main():
    handoff = HANDOFF.read_text(encoding="utf-8")
    hero = extract_html_block(ROOT / "nero-network-fragments/alina.md")
    boris = extract_html_block(ROOT / "nero-network-fragments/boris.md")
    artur_md = extract_artur_md(handoff)
    # insert boris marker after queue intro paragraph
    marker = "\n\nЗапросы вроде **«вторая очередь реестра требований кредиторов»**"
    if marker in artur_md:
        artur_md = artur_md.replace(
            marker + " и **«в третью очередь реестра требований кредиторов»** отражают практический вопрос: куда попадёт мой долг и сколько останется массы.\n\n",
            marker + " и **«в третью очередь реестра требований кредиторов»** отражают практический вопрос: куда попадёт мой долг и сколько останется массы.\n\nBORIS_PLACEHOLDER\n\n",
            1,
        )
    else:
        artur_md = artur_md.replace(
            "## Вторая и третья очередь реестра требований кредиторов\n\n",
            "## Вторая и третья очередь реестра требований кредиторов\n\nBORIS_PLACEHOLDER\n\n",
            1,
        )

    longread = build_lead_block() + md_to_html(artur_md, boris)

  # sources footer from Artur
    sources = """
<h2>Источники и нормы</h2>
<ul>
<li>Определение СКЭС ВС РФ от 06.05.2026 № 309-ЭС24-8891 (3), дело № А47-12711/2023 — <a href="https://www.garant.ru/products/ipo/prime/doc/414089845/" target="_blank" rel="noopener noreferrer">ГАРАНТ</a></li>
<li>Тематический обзор ВС № 5/2026 — <a href="https://www.garant.ru/hotlaw/federal/2077561/" target="_blank" rel="noopener noreferrer">ГАРАНТ</a></li>
<li>Закон о банкротстве: <strong>п. 4 ст. 134</strong>, <strong>абз. 3 п. 4</strong>, <strong>абз. 3 п. 2 ст. 134</strong></li>
<li>Комментарии: <a href="https://probankrotstvo.ru/news/vs-vkliucil-vznosy-na-medstraxovanie-i-socstraxovanie-vo-vtoruiu-ocered-10505" target="_blank" rel="noopener noreferrer">PROбанкротство</a>, <a href="https://pravo.ru/news/262872/" target="_blank" rel="noopener noreferrer">Право.ру</a>, <a href="https://www.interfax.ru/russia/1067327" target="_blank" rel="noopener noreferrer">Интерфакс</a></li>
</ul>
<p><em>Материал носит информационный характер и не заменяет юридическую консультацию. Состояние практики — на дату публикации (июнь 2026).</em></p>
"""

    # Remove duplicate FAQ/sources from longread if present
    longread = re.split(r"\n## Частые вопросы \(FAQ\)", longread)[0]
    longread = re.split(r"\n## Источники и нормы", longread)[0]

    title = "ВС 2026: страховые взносы ФНС во 2-ю очередь реестра при банкротстве ООО"
    desc = "Определение ВС от 6 мая 2026 (дело № А47-12711/2023): единый тариф с 2023 года — вся задолженность ФНС во 2-ю очередь реестра. Очередность, заявление о включении, спор с налоговой и последствия для кредиторов в арбитраже."

    page = f"""<!-- wp:html -->
<style>

{page_styles()}

</style>
<main id="primary" class="site-main {PAGE_CLASS}" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">
<meta itemprop="headline" content="ВС РФ: страховые взносы ФНС во 2-ю очередь реестра при банкротстве">
<meta itemprop="description" content="{desc}">
<meta itemprop="inLanguage" content="ru-RU">

{hero}

{build_intro()}

{build_toc()}

<div class="l24-longread-wrap" itemprop="articleBody">

{longread}

{sources}

</div>

{build_faq()}

{build_jsonld()}
</main>
<!-- /wp:html -->
"""

    OUT.write_text(page, encoding="utf-8")
    size = OUT.stat().st_size
    print(f"Wrote {OUT} ({size} bytes)")


if __name__ == "__main__":
    main()
