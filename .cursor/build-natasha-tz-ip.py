#!/usr/bin/env python3
"""Сборка HTML страницы товарный знак / ИС для handoff Наташи."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HANDOFF = ROOT / ".cursor/nero-network-handoff.md"
OUT_HTML = ROOT / ".cursor/page-content-natasha-tz-ip.html"
SLUG = "zashchita-tovarnogo-znaka-isk-po-intellektualnoj-sobstvennosti"

# Hero Алины (static SVG, без script/canvas)
HERO_START = "=== АЛИНА (HERO) ==="
HERO_END = "=== БОРИС"
BORIS_START = "```html"
BORIS_END = "```\n\n**Паспорт блока"

def extract_block(text: str, start_marker: str, end_marker: str) -> str:
    i = text.index(start_marker)
    j = text.index(end_marker, i + len(start_marker))
    chunk = text[i:j]
    if "```html" in chunk:
        chunk = chunk.split("```html", 1)[1]
        chunk = chunk.rsplit("```", 1)[0]
    elif "Статус:" in chunk:
        # hero: skip header lines until <section
        idx = chunk.find("<section")
        chunk = chunk[idx:] if idx >= 0 else chunk
    return chunk.strip()


PAGE_CSS = """
.breadcrumbs, .breadcrumb, .woocommerce-breadcrumb, .rank-math-breadcrumb, .yoast-breadcrumb,
.entry-header, .page-title-section { display: none !important; }
#primary, .site-main, .site-content, #content, .content-area {
  padding-top: 0 !important; margin-top: 0 !important;
}
#sidebar, .sidebar, #secondary, .et_pb_column_1_4 { display: none !important; }
.zashchita-tovarnogo-znaka-isk-po-intellektualnoj-sobstvennosti-page .entry-content {
  max-width: none !important; width: 100% !important; padding: 0 !important;
}
.zashchita-tovarnogo-znaka-isk-po-intellektualnoj-sobstvennosti-page .l24-longread-wrap {
  max-width: 820px; margin: 0 auto; padding: 48px 24px 80px;
  font-size: 1.05rem; line-height: 1.65; color: #1a202c;
}
.zashchita-tovarnogo-znaka-isk-po-intellektualnoj-sobstvennosti-page h2 {
  margin-top: 2.5em; color: #1a365d; font-size: 1.45rem;
}
.zashchita-tovarnogo-znaka-isk-po-intellektualnoj-sobstvennosti-page h3 {
  margin-top: 1.5em; color: #2c5282; font-size: 1.15rem;
}
.zashchita-tovarnogo-znaka-isk-po-intellektualnoj-sobstvennosti-page table {
  width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.95rem;
}
.zashchita-tovarnogo-znaka-isk-po-intellektualnoj-sobstvennosti-page th,
.zashchita-tovarnogo-znaka-isk-po-intellektualnoj-sobstvennosti-page td {
  border: 1px solid #e2e8f0; padding: 10px 12px; text-align: left;
}
.zashchita-tovarnogo-znaka-isk-po-intellektualnoj-sobstvennosti-page th { background: #edf2f7; }
.zashchita-tovarnogo-znaka-isk-po-intellektualnoj-sobstvennosti-page a { color: #1e40af; }
.l24-intro-tz {
  max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-intro-tz__grid {
  display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
  gap: 28px; align-items: start;
}
.l24-intro-tz__text {
  border-left: 4px solid #a31830; padding: 4px 0 4px 22px; text-align: left;
}
.l24-intro-tz__text p { margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }
.l24-intro-tz__text p:last-child { margin-bottom: 0; }
.l24-intro-tz__brief {
  background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px;
  padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; line-height: 1.55;
}
.l24-intro-tz__decor {
  background: linear-gradient(160deg, #f1f5f9 0%, #fff 100%);
  border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px;
}
.l24-intro-tz__chips { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none; }
.l24-intro-tz__chip {
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.03em;
  padding: 6px 10px; border-radius: 999px; background: #fff;
  border: 1px solid #cbd5e1; color: #475569;
}
.l24-intro-tz__chip--accent { border-color: #1e40af; color: #1e40af; }
.l24-intro-tz__chip--warn { border-color: #a31830; color: #a31830; }
.l24-intro-tz__route-svg { display: block; width: 100%; height: auto; }
.ym-toc {
  max-width: 820px; margin: 24px auto 0; padding: 0 24px 32px;
  text-align: center; font-family: system-ui, sans-serif;
}
.ym-toc__title { font-size: 0.8rem; font-weight: 700; letter-spacing: 0.06em;
  text-transform: uppercase; color: #64748b; margin: 0 0 12px;
}
.ym-toc__list { list-style: none; padding: 0; margin: 0;
  display: flex; flex-wrap: wrap; justify-content: center; gap: 8px 10px;
}
.ym-toc__list a {
  display: inline-block; padding: 8px 12px; border-radius: 8px;
  background: #f1f5f9; color: #1e40af; text-decoration: none; font-size: 0.88rem; font-weight: 600;
}
.ym-toc__list a:hover { background: #e2e8f0; }
.ym-cta {
  margin: 28px 0; padding: 22px 24px; border-radius: 10px;
  background: linear-gradient(135deg, #f8fafc 0%, #edf2f7 100%);
  border: 1px solid #cbd5e1; border-left: 4px solid #a31830;
}
.ym-cta__text { margin: 0 0 14px; line-height: 1.55; color: #334155; }
.ym-cta__actions { margin: 0; }
.ym-cta__btn {
  display: inline-block; background: #a31830; color: #fff !important;
  padding: 12px 22px; border-radius: 8px; font-weight: 700; text-decoration: none;
}
.ym-cta__btn:hover { background: #8b1528; }
.l24-faq-tz {
  margin-top: 2.5em; padding: 28px 24px; background: #f8fafc;
  border: 1px solid #e2e8f0; border-radius: 12px;
}
.l24-faq-tz h2 { margin-top: 0 !important; }
.l24-faq-tz__item { margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0; }
.l24-faq-tz__item:last-child { margin-bottom: 0; padding-bottom: 0; border-bottom: none; }
.l24-faq-tz__q { margin: 0 0 8px; font-size: 1.05rem; color: #1a365d; }
.l24-faq-tz__a { margin: 0; color: #334155; }
.l24-jsonld-note {
  display: none; /* JSON-LD для Rank Math — см. блок Передача Юре */
}
@media (max-width: 900px) {
  .l24-intro-tz__grid { grid-template-columns: 1fr; }
}
"""

INTRO_HTML = """
<section class="l24-intro-tz" aria-label="Введение">
  <div class="l24-intro-tz__grid">
    <div class="l24-intro-tz__text">
      <p>Спор вокруг товарного знака в 2026 году редко начинается в суде. Чаще цепочка выглядит так: проверка реестра Роспатента → запуск карточки на маркетплейсе → жалоба правообладателя и блокировка за сутки → досудебная претензия → иск → отзыв по ст. 131 АПК РФ → встречные меры (в том числе по ст. 1486 ГК РФ) и оспаривание компенсации по новой ст. 1252.1 ГК РФ после реформы ФЗ № 214-ФЗ.</p>
      <p>Ниже — практическая дорожная карта для двух ролей: вы защищаете бренд или на вас/ваш магазин пришли с требованиями по интеллектуальной собственности.</p>
      <div class="l24-intro-tz__brief">
        <strong>Кратко:</strong> исключительное право на товарный знак возникает после регистрации; нарушение — использование сходного обозначения без согласия; до иска обычно нужна претензия (30 дней); «твёрдая» компенсация с 04.01.2026 — до 10 млн ₽ (при грубом нарушении — до 20 млн), альтернативно — 2× стоимость товаров или права использования без потолка; ответчику важны отзыв, доказательства отсутствия вины и контрход по неиспользованию знака истца.
      </div>
    </div>
    <aside class="l24-intro-tz__decor" aria-label="Маршрут спора">
      <ul class="l24-intro-tz__chips">
        <li class="l24-intro-tz__chip l24-intro-tz__chip--accent">Роспатент</li>
        <li class="l24-intro-tz__chip">WB / Ozon</li>
        <li class="l24-intro-tz__chip l24-intro-tz__chip--warn">30 дней</li>
        <li class="l24-intro-tz__chip">СИП</li>
        <li class="l24-intro-tz__chip">ст. 1252.1</li>
        <li class="l24-intro-tz__chip">ст. 1486</li>
      </ul>
      <svg class="l24-intro-tz__route-svg" viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Схема: реестр, маркетплейс, претензия, суд">
        <rect x="8" y="8" width="304" height="184" rx="10" fill="#fff" stroke="#cbd5e1"/>
        <text x="24" y="32" fill="#64748b" font-size="10" font-weight="700">СКВОЗНАЯ ШКАЛА</text>
        <circle cx="48" cy="88" r="18" fill="#1e40af"/><text x="48" y="93" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">®</text>
        <circle cx="120" cy="88" r="18" fill="#a31830"/><text x="120" y="93" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">МП</text>
        <circle cx="192" cy="88" r="18" fill="#d97706"/><text x="192" y="93" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">30д</text>
        <circle cx="264" cy="88" r="18" fill="#2f855a"/><text x="264" y="93" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">иск</text>
        <line x1="66" y1="88" x2="102" y2="88" stroke="#94a3b8" stroke-width="2"/>
        <line x1="138" y1="88" x2="174" y2="88" stroke="#94a3b8" stroke-width="2"/>
        <line x1="210" y1="88" x2="246" y2="88" stroke="#94a3b8" stroke-width="2"/>
        <text x="48" y="130" text-anchor="middle" fill="#475569" font-size="8">реестр</text>
        <text x="120" y="130" text-anchor="middle" fill="#475569" font-size="8">блокировка</text>
        <text x="192" y="130" text-anchor="middle" fill="#475569" font-size="8">претензия</text>
        <text x="264" y="130" text-anchor="middle" fill="#475569" font-size="8">отзыв</text>
        <rect x="24" y="148" width="272" height="36" rx="6" fill="#eff6ff" stroke="#bfdbfe"/>
        <text x="160" y="170" text-anchor="middle" fill="#1e40af" font-size="10" font-weight="700">10 млн · 1252.1 · 1486</text>
      </svg>
    </aside>
  </div>
</section>

<nav class="ym-toc" aria-label="Содержание статьи">
  <p class="ym-toc__title">По статье</p>
  <ul class="ym-toc__list">
    <li><a href="#tz-brand">Товарный знак и бренд</a></li>
    <li><a href="#tz-violation">Нарушение</a></li>
    <li><a href="#tz-pretension">Претензия</a></li>
    <li><a href="#tz-lawsuit">Иск в суде</a></li>
    <li><a href="#tz-compensation">Компенсация</a></li>
    <li><a href="#tz-practice">Практика</a></li>
    <li><a href="#tz-faq">FAQ</a></li>
  </ul>
</nav>
"""

# Longread body as HTML (from Женя/Артур)
BODY_HTML = r"""
<h2 id="tz-brand">Товарный знак и бренд: что защищает право и кто правообладатель</h2>

<p>Товарный знак — зарегистрированное обозначение для индивидуализации товаров и услуг (ст. 1477, 1481 ГК РФ ч. 4). <strong>Защита бренда</strong> в разговорном смысле шире: сюда попадают фирменное наименование, коммерческое обозначение, домен, упаковка. Но в спорах с селлерами и в судах по интеллектуальной собственности чаще всего решающим становится именно <strong>исключительное право на товарный знак</strong> — оно даёт правообладателю запретить чужое использование сходного знака в отношении однородных товаров и услуг.</p>

<p><strong>Правообладатель товарного знака</strong> — лицо, внесённое в Госреестр (ст. 1229, 1240 ГК РФ). Права можно передать по договору отчуждения или предоставить по лицензии; без этого любое коммерческое использование чужого знака — зона риска.</p>

<h3>Исключительное право на товарный знак — срок и действие</h3>

<p>Исключительное право действует <strong>10 лет</strong> с даты подачи заявки в Роспатент, продлевается неограниченно (ст. 1491 ГК РФ). Охрана распространяется на обозначение в зарегистрированном виде и <strong>сходные до степени смешения</strong> знаки в отношении товаров и услуг из перечня заявки (классы МКТУ). Суды оценивают восприятие <strong>в целом</strong>, а не «выдёргивают» отдельное слово: так, в 2026 году СИП при отказе в регистрации «IT Таблетка» и «ЦИФРОВОЙ АВТОМОБИЛЬ» (дело С01-1849/2025) подчёркивал необходимость анализа по каждому товару и услуге — это же логика при спорах о нарушении.</p>

<h3>Регистрация товарного знака в Роспатенте как основа защиты</h3>

<p><strong>Регистрация товарного знака</strong> — не формальность, а фундамент судебной защиты. По итогам 2025 года Роспатент принял <strong>156 365</strong> заявок; в реестре — более <strong>1 014 647</strong> действующих знаков; свыше <strong>25 000</strong> заявок — от самозанятых. Класс <strong>35 МКТУ</strong> (реклама, торговля, маркетплейсы) — около <strong>40%</strong> всех регистраций; эксперты указывают на порядка <strong>400 000</strong> знаков только в этом классе — высокий риск коллизий для e-commerce.</p>

<p>Перед выводом бренда на Wildberries или Ozon имеет смысл проверить реестр и сходные обозначения в нужных классах. С <strong>01.03.2026</strong> действуют ограничения на иностранные слова в публичном пространстве (ФЗ № 168-ФЗ) — дополнительный мотив оформить российскую регистрацию заранее.</p>

<aside class="ym-cta ym-cta--primary" role="complementary">
  <p class="ym-cta__text">Планируете выход на маркетплейс или обновляете бренд? Юрист поможет подобрать классы МКТУ, проверить реестр на коллизии и выстроить защиту до первой продажи.</p>
  <p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по защите бренда</a></p>
</aside>

<h3>Защита бренда и товарного знака: в чём разница для бизнеса</h3>

<table>
  <thead><tr><th>Понятие</th><th>Что даёт</th><th>Типичный риск</th></tr></thead>
  <tbody>
    <tr><td>Бренд (имя, слоган, визуал)</td><td>Узнаваемость</td><td>Спор без регистрации — сложнее доказать приоритет</td></tr>
    <tr><td>Товарный знак ®</td><td>Исключительное право, запись в реестре</td><td>Коллизия с чужим знаком в том же классе</td></tr>
    <tr><td>НМПТ, дизайн, фото</td><td>Отдельные объекты ИС</td><td>Кратное взыскание за одну карточку после 2026 ограничено (ст. 1252.1)</td></tr>
  </tbody>
</table>

<p><strong>Защита интеллектуальной собственности</strong> в широком смысле включает мониторинг маркетплейсов, фиксацию нарушений, претензии и иски. Для предпринимателя практичнее мыслить пакетом: знак + доказательства использования + договоры с производителем/дистрибьютором.</p>

<h2 id="tz-violation">Нарушение товарного знака: признаки, риски и ответственность</h2>

<p><strong>Нарушение товарного знака</strong> — использование без согласия правообладателя обозначения, сходного с зарегистрированным, в отношении однородных товаров/услуг, в том числе в сети, на вывеске, в домене, в метаданных карточки (ст. 1484, 1229 ГК РФ). Оборот контрафакта в РФ оценивают эксперты в <strong>~5 трлн ₽</strong> (~10% рынка); число споров в сфере ИС в 2024 году — порядка <strong>55,1 тыс.</strong> (+35% по ряду категорий). Стоимость ошибки после реформы компенсаций выросла — но для добросовестных ответчиков появились и предсказуемые способы снижения требований.</p>

<h3>Нарушение прав на товарный знак и использование без согласия</h3>

<p>Признаки, на которые смотрят правообладатель и суд:</p>
<ul>
  <li>сходство знаков (фонетика, графика, смысл);</li>
  <li>однородность товаров/услуг (классы МКТУ);</li>
  <li>использование в предпринимательской деятельности (карточка МП, упаковка, реклама);</li>
  <li>отсутствие лицензии или иного законного основания.</li>
</ul>

<p><strong>Контрафакт</strong> — товар, маркировка или упаковка которого незаконно несут чужой знак (уточнено в рамках реформы). <strong>Параллельный импорт</strong> оригинальной продукции — отдельный режим: такие товары не уничтожают как контрафакт, хотя споры по знаку возможны в иных конфигурациях.</p>

<h3>Нарушение исключительного права: когда достаточно претензии</h3>

<p>Не каждое обнаруженное совпадение сразу ведёт в суд. Правообладатель часто направляет <strong>претензию по товарному знаку</strong>, требует прекратить использование, снять карточку, выплатить компенсацию или заключить лицензию. Для ответчика критично не игнорировать письмо: молчание укрепляет позицию истца по вине и размеру требований.</p>

<h3>Ответственность за нарушение и компенсация по ГК РФ</h3>

<p>Ответственность — через <strong>защиту исключительного права</strong> (ст. 1250, 1252 ГК РФ): прекращение нарушения, изъятие, публикация решения, <strong>компенсация</strong> вместо доказывания убытков (ст. 1515). С <strong>04.01.2026</strong> (ФЗ № 214-ФЗ от 07.07.2025) действуют обновлённые пределы и новая <strong>ст. 1252.1 ГК РФ</strong> «Компенсация за нарушение исключительного права».</p>

<p><strong>Принцип «один товар — одно нарушение»:</strong> нельзя умножать взыскание за товарный знак, дизайн, фотографию и текст на одной карточке маркетплейса, если каждый способ не имеет самостоятельного экономического значения. Это прямой ответ на практику «наращивания» суммы исков.</p>

<h2 id="tz-pretension">Досудебная защита: претензия по товарному знаку и ответ</h2>

<p>Досудебный этап — обязательная часть <strong>защиты права на товарный знак</strong> по имущественным требованиям: иск по правилам ст. 1252 ГК РФ подаётся, если в течение <strong>30 дней</strong> с направления претензии спор не урегулирован (если стороны не договорились об ином сроке).</p>

<h3>Претензия по использованию товарного знака — сроки и содержание</h3>

<p>В претензии обычно указывают: сведения о правообладателе и знаке (номер свидетельства), описание нарушения (скриншоты карточек, ссылки, даты), требования (прекратить, удалить, выплатить компенсацию, раскрыть поставщика), срок ответа, расчёт компенсации. <strong>Претензия по товарным знакам</strong> на маркетплейсе может дублироваться жалобой в службу бренда площадки — блокировка нередко наступает <strong>до</strong> судебного решения.</p>

<h3>Досудебная претензия: обязательна ли перед судом</h3>

<p>Да, для стандартных требований о компенсации и прекращении нарушения — с соблюдением 30-дневного срока. Исключения и особые процедуры возможны в иных составах (например, обеспечительные меры), но для селлера типовой сценарий — претензия → иск.</p>

<h3>Ответ на претензию по товарному знаку — типовые ошибки</h3>

<ol>
  <li><strong>Игнорирование срока</strong> — истец фиксирует злостность, суд учитывает вину при компенсации.</li>
  <li><strong>Признание «всего подряд»</strong> без анализа сходства и однородности.</li>
  <li><strong>Отсутствие доказательств добросовестности</strong> — закуп по документам, проверка реестра, согласование с дизайнером.</li>
  <li><strong>Публичные споры без стратегии</strong> — до проверки реестра и классов МКТУ.</li>
  <li><strong>Не фиксировать переписку и снятие карточки</strong> — при добровольном урегулировании это основа для снижения суммы.</li>
</ol>

<p>Грамотный <strong>ответ на претензию по товарному знаку</strong> — это возражения по сходству, однородности, наличию прав на ваш знак, предложение лицензии или рассрочки, оговорка о проверке расчёта компенсации.</p>

<aside class="ym-cta ym-cta--primary" role="complementary">
  <p class="ym-cta__text">Получили претензию с расчётом компенсации или требованием снять карточку? До подачи иска у вас окно для переговоров и юридической позиции — важно не пропустить срок и не признать лишнего.</p>
  <p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Помощь при ответе на претензию по товарному знаку</a></p>
</aside>

<!-- BORIS_ANCHOR -->

<h2 id="tz-lawsuit">Иск по товарному знаку и защита интеллектуальной собственности в суде</h2>

<p>Если досудебка не сработала, правообладатель подаёт <strong>иск по товарному знаку</strong> (иск о нарушении исключительных прав, <strong>иск на нарушение товарного знака</strong>). Подсудность — арбитраж для юрлиц и ИП, суды общей юрисдикции — для потребительских сюжетов; значимые споры по ИС часто попадают в <strong>Суд по интеллектуальным правам (СИП)</strong>.</p>

<h3>Иск на нарушение товарного знака и иск о нарушении исключительных прав</h3>

<p>Исковые требования типовые: прекратить нарушение, взыскать <strong>компенсацию</strong>, иногда — опубликовать решение, изъять контрафакт. Истец должен доказать принадлежность права и факт нарушения; <strong>бремя доказывания отсутствия вины</strong> на ответчике (презумпция ст. 1250). По размеру компенсации истец представляет <strong>расчёт и доказательства</strong> (п. 61 ППВС № 10 от 23.04.2019) — это точка для оспаривания завышенных цифр.</p>

<h3>Иск по интеллектуальной собственности: если вы ответчик</h3>

<p>Сценарий «<strong>подали иск по интеллектуальной собственности</strong>» или «<strong>иск по товарному знаку</strong> против магазина» в 2026 году включает:</p>
<ol>
  <li>Получение искового заявления и приложений (копия свидетельства, протоколы осмотра карточек, расчёт).</li>
  <li>Подготовка <strong>отзыва на иск</strong> (ст. 131 АПК РФ) — по каждому доводу истца, с доказательствами.</li>
  <li>Проверка <strong>исковой давности</strong> — суды обязаны учитывать момент, когда истец узнал или должен был узнать о нарушении (актуальна практика ВС, в т.ч. определение № 305-ЭС25-4071 от 14.08.2025).</li>
  <li>Параллельная подача <strong>возражений</strong> на регистрацию или заявление о <strong>досрочном прекращении</strong> охраны знака истца при неиспользовании (ст. 1486).</li>
  <li>Ходатайства о снижении компенсации по п. 7 ст. 1252.1 при отсутствии вины.</li>
</ol>

<p><strong>Ответ на иск по интеллектуальной собственности</strong> и <strong>отзыв на иск товарный знак</strong> — разные документы по смыслу: отзыв — процессуальный ответ в суд; «ответ на иск» в быту — вся стратегия защиты.</p>

<h3>Что делать, если подали иск — сроки, возражения, доказательства</h3>

<table>
  <thead><tr><th>Шаг</th><th>Срок/действие</th><th>Содержание</th></tr></thead>
  <tbody>
    <tr><td>Отзыв</td><td>В срок, установленный судом (ст. 131 АПК)</td><td>Возражения по доводам, доказательства, направление другой стороне</td></tr>
    <tr><td>Доказательства</td><td>До заседания</td><td>Лицензия, договоры поставки, экспертиза несходства, ваш знак</td></tr>
    <tr><td>Встречный иск / заявление</td><td>По стратегии</td><td>Неиспользование знака истца 3 года (ст. 1486)</td></tr>
    <tr><td>Обеспечительные меры</td><td>По обстоятельствам</td><td>Запрет требований или блокировка исполнения</td></tr>
  </tbody>
</table>

<p>Подать <strong>отзыв на исковое заявление</strong> можно через систему «Мой арбитр» или заказным письмом с доказательством вручения. Формальный отказ от отзыва лишает суд аргументов ответчика — ошибка, которую исправляют не всегда.</p>

<h3>Судебная защита товарных знаков и судебная практика</h3>

<p><strong>Судебная защита товарных знаков</strong> в 2025–2026 годах опирается на мотивированное обоснование компенсации: известность знака, характер нарушения, срок, вина, разумность (постановление СИП по делу <strong>С01-1833/2025</strong> от 24.04.2026). Ответчику выгодно поднимать: кратность объектов на одной карточке (ст. 1252.1), отсутствие вины, завышенный расчёт 2× лицензии, <strong>досрочное прекращение охраны</strong> знака истца при неиспользовании — бремя доказывания использования лежит на правообладателе (справка СП-23/20; активизация практики в 2025 году).</p>

<h2 id="tz-compensation">Компенсация и взыскание: как снизить сумму требований</h2>

<p>С 04.01.2026 <strong>верхний предел «твёрдой» компенсации</strong> по товарному знаку — <strong>10 000 000 ₽</strong> (ранее — 5 млн); при <strong>грубом</strong> или <strong>множественном</strong> нарушении — до <strong>20 000 000 ₽</strong> (ст. 1515 ГК РФ в новой редакции). Нижний предел — <strong>10 000 ₽</strong>.</p>

<p>Правообладатель выбирает один из <strong>трёх способов</strong> расчёта (п. 4 ст. 1515):</p>
<ol>
  <li><strong>От 10 тыс. до 10 млн</strong> — по усмотрению суда в указанном диапазоне.</li>
  <li><strong>Двукратная стоимость контрафактных товаров</strong> — зависит от объёма продаж.</li>
  <li><strong>Двукратная стоимость права использования</strong> (лицензионный эквивалент) — <strong>без числового потолка</strong>; в крупных брендах эксперты указывают на суммы в десятки и сотни миллионов рублей.</li>
</ol>

<h3>Компенсация за нарушение товарного знака — расчёт</h3>

<p>Истец обязан показать основания выбора способа и цифры. Ответчик оспаривает: метод (например, завышенная «лицензия»), объём нарушения, период, <strong>один товар — одно нарушение</strong>, отсутствие вины. Суд вправе снизить «твёрдую» компенсацию, если нарушитель <strong>не знал и не должен был знать</strong> о нарушении, — <strong>вплоть до диапазона 10 000–500 000 ₽</strong> (п. 7 ст. 1252.1). Ожидается развитие практики с учётом публичности реестра ТЗ — добросовестный селлер, проверивший реестр, сильнее аргументирует позицию.</p>

<h3>Взыскание компенсации за использование товарного знака</h3>

<p><strong>Взыскание компенсации</strong> может сопровождаться требованиями о прекращении использования и удалении карточек. На маркетплейсах блокировка часто наступает <strong>до суда</strong> — у продавца около <strong>24 часов</strong> на апелляцию с пакетом: свидетельство на ваш знак, лицензия, сравнение обозначений, документы на товар. Wildberries Brand Analytics рассматривает жалобы до <strong>10 рабочих дней</strong>, Ozon «Защита бренда» — <strong>5–14 рабочих дней</strong>.</p>

<p>Переходный период реформы: нарушения, начавшиеся до 04.01.2026, могут оцениваться по правилам, действовавшим на момент нарушения — это важно в длительных спорах.</p>

<aside class="ym-cta ym-cta--primary" role="complementary">
  <p class="ym-cta__text">Иск в СИП, расчёт на миллионы по 2× лицензии или претензия с компенсацией до 10–20 млн — спор, где ошибка в отзыве и доказательствах дороже консультации. Обсудите стратегию: отзыв, ст. 1486, снижение по ст. 1252.1.</p>
  <p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Помощь при иске по интеллектуальной собственности</a></p>
</aside>

<h2 id="tz-practice">Как защитить товарный знак и бренд на практике</h2>

<h3>Способы защиты прав на товарный знак (гражданско-правовые меры)</h3>

<p><strong>Защита товарного знака</strong> и <strong>защита прав правообладателя товарного знака</strong> включают:</p>
<ul>
  <li>подачу претензии и иска о прекращении нарушения;</li>
  <li>взыскание компенсации;</li>
  <li>обращение в таможню (при импорте контрафакта);</li>
  <li>жалобу на маркетплейс (Brand Analytics, «Защита бренда»);</li>
  <li><strong>защиту исключительного права на товарный знак</strong> через публикацию судебного акта.</li>
</ul>

<p>Для ответчика зеркальные инструменты: отзыв, оспаривание расчёта, <strong>возражение на исковое заявление</strong> по существу, заявление по ст. 1486.</p>

<h3>Защита права на товарный знак в РФ и в интернете</h3>

<p><strong>Правовая защита бренда</strong> в онлайне — мониторинг карточек конкурентов, фиксация осмотра сайта (нотариус, протокол), своевременное обновление реестра (продление, изменение адреса). При выходе на МП — отдельная проверка класса 35 и смежных (09, 16, 25 и т.д. по ассортименту).</p>

<p><strong>Как защитить товарный знак</strong> до конфликта:</p>
<ol>
  <li>Регистрация в нужных классах МКТУ.</li>
  <li>Документирование первого использования (если спор о неохраняемом элементе).</li>
  <li>Лицензии и сублицензии в цепочке поставок.</li>
  <li>Мониторинг реестра и маркетплейсов.</li>
  <li>Быстрая реакция на копирование карточки (жалоба + претензия).</li>
</ol>

<h3>Когда нужен юрист по интеллектуальной собственности</h3>

<p>Обращение к специалисту оправдано, если:</p>
<ul>
  <li>сумма компенсации в претензии или иске <strong>сопоставима с оборотом</strong> или превышает его;</li>
  <li>заблокированы ключевые карточки на WB/Ozon;</li>
  <li>истец — крупный бренд с расчётом <strong>2× лицензии</strong>;</li>
  <li>возможен <strong>иск о защите интеллектуальной собственности</strong> в СИП;</li>
  <li>вы правообладатель и нужна связка «мониторинг МП → претензия → иск».</li>
</ul>

<p><strong>Иски о защите интеллектуальной собственности</strong> и <strong>защита товарного знака иск</strong> — одна матрица: роль (истец/ответчик), стадия (МП, претензия, суд), инструмент (отзыв, 1486, 1252.1). На любом этапе можно <a href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">обсудить ситуацию с юристом по ИС</a> — от регистрации знака до ответа на иск.</p>

<h2>Маркетплейсы: что происходит до суда</h2>

<p>Типовой сценарий для селлера:</p>
<ol>
  <li>Жалоба правообладателя → <strong>блокировка карточки</strong> (иногда в течение суток).</li>
  <li>Апелляция с документами (свидетельство, лицензия, сравнение знаков).</li>
  <li>Параллельно — <strong>досудебная претензия</strong> с требованием компенсации.</li>
  <li>При отказе — <strong>иск по товарному знаку</strong>.</li>
</ol>

<p>Чек-лист доказательств для апелляции и суда: скриншоты карточек, классы МКТУ, заключение о несходстве, договоры на товар, ваш знак в реестре, переписка с правообладателем.</p>
"""

FAQ_HTML = """
<section id="tz-faq" class="l24-faq-tz" itemscope itemtype="https://schema.org/FAQPage" aria-label="Частые вопросы">
  <h2>FAQ: короткие ответы</h2>

  <div class="l24-faq-tz__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 class="l24-faq-tz__q" itemprop="name">Что такое нарушение товарного знака?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p class="l24-faq-tz__a" itemprop="text">Использование сходного обозначения без согласия правообладателя в отношении однородных товаров/услуг.</p>
    </div>
  </div>

  <div class="l24-faq-tz__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 class="l24-faq-tz__q" itemprop="name">Обязательна ли претензия перед иском?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p class="l24-faq-tz__a" itemprop="text">По общему правилу ст. 1252 ГК РФ — да, 30 дней с направления претензии по имущественным требованиям.</p>
    </div>
  </div>

  <div class="l24-faq-tz__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 class="l24-faq-tz__q" itemprop="name">Какой максимум «твёрдой» компенсации с 2026 года?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p class="l24-faq-tz__a" itemprop="text">10 млн ₽ (до 20 млн при грубом/множественном нарушении); альтернатива 2× товар или 2× лицензия — без потолка.</p>
    </div>
  </div>

  <div class="l24-faq-tz__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 class="l24-faq-tz__q" itemprop="name">Что такое ст. 1252.1 ГК РФ?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p class="l24-faq-tz__a" itemprop="text">Правила компенсации, в т.ч. «один товар — одно нарушение» и снижение при отсутствии вины до 10–500 тыс. ₽.</p>
    </div>
  </div>

  <div class="l24-faq-tz__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 class="l24-faq-tz__q" itemprop="name">Что делать, если подали иск по товарному знаку?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p class="l24-faq-tz__a" itemprop="text">Подготовить отзыв по ст. 131 АПК, собрать доказательства, проверить давность, рассмотреть заявление по ст. 1486 о неиспользовании знака истца.</p>
    </div>
  </div>

  <div class="l24-faq-tz__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 class="l24-faq-tz__q" itemprop="name">Как снизить компенсацию?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p class="l24-faq-tz__a" itemprop="text">Доказать отсутствие вины, оспорить расчёт, применить п. 7 ст. 1252.1, указать на кратное взыскание за несколько объектов на одной карточке.</p>
    </div>
  </div>

  <div class="l24-faq-tz__item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 class="l24-faq-tz__q" itemprop="name">Можно ли отменить чужой товарный знак?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p class="l24-faq-tz__a" itemprop="text">При неиспользовании более 3 лет подряд — досрочное прекращение охраны (ст. 1486); бремя доказывания использования — на правообладателе.</p>
    </div>
  </div>
</section>
"""

JSONLD_FOR_YURA = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Товарный знак: как защитить бренд и что делать, если подали иск по интеллектуальной собственности",
      "description": "Нарушение товарного знака и иск по ИС: как защитить бренд, ответить на претензию и снизить компенсацию. Регистрация, права правообладателя, суд — консультация юриста Legis24.",
      "author": {"@type": "Organization", "name": "Legis24"},
      "publisher": {"@type": "Organization", "name": "Legis24"},
      "dateModified": "2026-05-22",
      "inLanguage": "ru-RU"
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {"@type": "Question", "name": "Что такое нарушение товарного знака?", "acceptedAnswer": {"@type": "Answer", "text": "Использование сходного обозначения без согласия правообладателя в отношении однородных товаров/услуг."}},
        {"@type": "Question", "name": "Обязательна ли претензия перед иском?", "acceptedAnswer": {"@type": "Answer", "text": "По общему правилу ст. 1252 ГК РФ — да, 30 дней с направления претензии по имущественным требованиям."}},
        {"@type": "Question", "name": "Какой максимум твёрдой компенсации с 2026 года?", "acceptedAnswer": {"@type": "Answer", "text": "10 млн ₽ (до 20 млн при грубом/множественном нарушении); альтернатива 2× товар или 2× лицензия — без потолка."}},
        {"@type": "Question", "name": "Что делать, если подали иск по товарному знаку?", "acceptedAnswer": {"@type": "Answer", "text": "Подготовить отзыв по ст. 131 АПК, собрать доказательства, проверить давность, рассмотреть заявление по ст. 1486."}}
      ]
    }
  ]
}"""


def patch_hero_cta(hero: str) -> str:
    hero = hero.replace(
        'href="https://advokat-vsem.ru/">Консультация',
        'href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация',
    )
    return hero


def main():
    handoff = HANDOFF.read_text(encoding="utf-8")
    hero = extract_block(handoff, HERO_START, HERO_END)
    idx = hero.find("<section")
    hero = hero[idx:] if idx >= 0 else hero
    hero = patch_hero_cta(hero)

    boris = extract_block(handoff, "=== БОРИС", "**Паспорт блока")
    # boris extraction used wrong markers - fix
    bstart = handoff.index("=== БОРИС")
    bend = handoff.index("**Паспорт блока", bstart)
    boris_chunk = handoff[bstart:bend]
    boris = boris_chunk.split("```html", 1)[1].rsplit("```", 1)[0].strip()

    body = BODY_HTML.replace("<!-- BORIS_ANCHOR -->", boris)

    html = f"""<!-- wp:html -->
<style>
{PAGE_CSS}
</style>
<main id="primary" class="site-main {SLUG}-page" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">
{hero}
{INTRO_HTML}
<div class="l24-longread-wrap" itemprop="articleBody">
{body}
{FAQ_HTML}
<h2>Итог</h2>
<p><strong>Защита товарного знака</strong> и <strong>защита бренда</strong> в 2026 году — это регистрация и проверка коллизий (особенно класс 35 МКТУ), быстрая реакция на маркетплейсах, грамотный ответ на претензию и <strong>отзыв на иск</strong> с контрходами по компенсации (214-ФЗ, ст. 1252.1) и <strong>неиспользованию</strong> знака истца (ст. 1486). Независимо от роли — правообладатель или ответчик — выигрывает тот, кто заранее фиксирует доказательства и связывает досудебку, МП и суд в одну стратегию.</p>
<p><em>Материал носит информационный характер и не заменяет юридическую консультацию. Нормы ГК РФ ч. 4, АПК РФ, ФЗ № 214-ФЗ уточняйте по официальным текстам и с учётом вашей ситуации.</em></p>
</div>
</main>
<!-- /wp:html -->
"""

    OUT_HTML.write_text(html, encoding="utf-8")

    natasha_block = f"""
=== НАТАША (HTML СТРАНИЦЫ) ===
Статус: ✅ ГОТОВО

SLUG: {SLUG}
ВНИМАНИЕ: без `<script>` и `<canvas>` — MCP publish удаляет scripts; hero и Борис — static SVG + inline CSS. FAQ — microdata FAQPage; JSON-LD для Rank Math — в «Передача Юре» (не в blob).

```html
{html}
```

## Передача Юре

**Title:** Защита товарного знака и бренда: иск, претензия, компенсация — что делать  
**Description:** Нарушение товарного знака и иск по ИС: как защитить бренд, ответить на претензию и снизить компенсацию. Регистрация, права правообладателя, суд — консультация юриста Legis24.  
**slug:** `{SLUG}`  
**page_id:** `PLACEHOLDER` (заполнить после `wordpress_create_page`)

**Публикация:** `commands/nero-publish-mcp.md` — blob flow, удалить `<script>` если появятся; обернуть в `<!-- wp:html -->`.

**JSON-LD** (добавить через Rank Math / Custom HTML head, не в blob):

```json
{JSONLD_FOR_YURA}
```

**Проверка live:** `main#primary`, класс `{SLUG}-page`, hero `#l24-hero-tz-ip`, блок `#l24-boris-tz-ip-track`, breadcrumbs скрыты, CTA только https://advokat-vsem.ru/
"""

    if "=== НАТАША (HTML СТРАНИЦЫ) ===" in handoff:
        handoff = handoff.split("=== НАТАША (HTML СТРАНИЦЫ) ===")[0].rstrip() + "\n" + natasha_block
    else:
        handoff = handoff.rstrip() + "\n" + natasha_block

    HANDOFF.write_text(handoff, encoding="utf-8")
    print(f"HTML: {OUT_HTML} ({len(html)} bytes)")
    print(f"Handoff updated ({len(handoff)} bytes)")


if __name__ == "__main__":
    main()
