=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) === ✅ ГОТОВО

**Режим связи с Алиной:** контраст — hero Алины (Canvas, персонажи, «живая» сцена) vs редакционная карта-таблица в теле статьи: статичный сплит с двумя колонками «миф / факт» по 127-ФЗ, без анимации и без конкуренции по высоте с первым экраном.

**Якорь вставки (для Наташи):** после закрывающего `</section>` секции `#srok-30-dnej` («Срок возражений на требование кредитора — 30 дней: кому, от какой даты»), перед секцией `#15-dnej-mif`.

**Паттерн композиции:** сплит 42/58 — слева eyebrow + мини-заголовок + два KPI-чипа (15 ≠ / 30 =); справа таблица миф/факт. На узких экранах — колонка: текст сверху, таблица снизу.

**Как ведёт читателя:** визуально фиксирует главную путаницу статьи до раздела про «15 дней — миф»; подталкивает к следующему H2 с разбором источников ошибки.

---

```html
<section id="srok-vozrazhenij-boris-block" class="boris-article-viz" aria-labelledby="boris-block-title">
<style>
  #srok-vozrazhenij-boris-block {
    margin: 2.75rem 0 3rem;
    font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    color: #0f172a;
  }
  #srok-vozrazhenij-boris-block .boris-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 22px;
    box-shadow: 0 18px 48px rgba(15, 23, 42, 0.07);
    overflow: hidden;
  }
  #srok-vozrazhenij-boris-block .boris-split {
    display: grid;
    grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.35fr);
    gap: 0;
  }
  #srok-vozrazhenij-boris-block .boris-lead {
    padding: 2rem 2rem 2rem 2.25rem;
    background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
    border-right: 1px solid #e2e8f0;
    border-left: 4px solid #ff0000;
  }
  #srok-vozrazhenij-boris-block .boris-eyebrow {
    display: inline-block;
    margin: 0 0 0.75rem;
    padding: 0.28rem 0.65rem;
    font-size: 0.6875rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #64748b;
    background: #f1f5f9;
    border-radius: 999px;
  }
  #srok-vozrazhenij-boris-block .boris-kicker {
    margin: 0 0 0.85rem;
    font-size: 1.375rem;
    line-height: 1.25;
    font-weight: 800;
    color: #0f172a;
  }
  #srok-vozrazhenij-boris-block .boris-bridge {
    margin: 0 0 1.35rem;
    font-size: 0.9375rem;
    line-height: 1.55;
    color: #475569;
  }
  #srok-vozrazhenij-boris-block .boris-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 0.65rem;
  }
  #srok-vozrazhenij-boris-block .boris-chip {
    flex: 1 1 8.5rem;
    min-width: 0;
    padding: 0.85rem 0.95rem;
    border-radius: 14px;
    border: 1px solid #e2e8f0;
    background: #fff;
  }
  #srok-vozrazhenij-boris-block .boris-chip-num {
    display: block;
    font-size: 1.625rem;
    font-weight: 800;
    line-height: 1;
    margin-bottom: 0.25rem;
  }
  #srok-vozrazhenij-boris-block .boris-chip-num.is-myth { color: #dc2626; }
  #srok-vozrazhenij-boris-block .boris-chip-num.is-fact { color: #059669; }
  #srok-vozrazhenij-boris-block .boris-chip-label {
    display: block;
    font-size: 0.75rem;
    line-height: 1.35;
    color: #64748b;
  }
  #srok-vozrazhenij-boris-block .boris-table-wrap {
    padding: 1.5rem 1.5rem 1.65rem;
    overflow-x: auto;
  }
  #srok-vozrazhenij-boris-block .boris-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    font-size: 0.875rem;
    line-height: 1.45;
  }
  #srok-vozrazhenij-boris-block .boris-table caption {
    caption-side: top;
    text-align: left;
    margin: 0 0 0.85rem;
    font-size: 0.8125rem;
    font-weight: 700;
    color: #334155;
  }
  #srok-vozrazhenij-boris-block .boris-table thead th {
    padding: 0.75rem 0.85rem;
    text-align: left;
    font-size: 0.75rem;
    font-weight: 800;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: #fff;
    background: #0f172a;
    border: 1px solid #0f172a;
  }
  #srok-vozrazhenij-boris-block .boris-table thead th:first-child {
    border-radius: 12px 0 0 0;
    background: #991b1b;
    border-color: #991b1b;
  }
  #srok-vozrazhenij-boris-block .boris-table thead th:last-child {
    border-radius: 0 12px 0 0;
    background: #065f46;
    border-color: #065f46;
  }
  #srok-vozrazhenij-boris-block .boris-table tbody td {
    padding: 0.8rem 0.85rem;
    vertical-align: top;
    border: 1px solid #e2e8f0;
    background: #fff;
    color: #334155;
  }
  #srok-vozrazhenij-boris-block .boris-table tbody tr:nth-child(even) td {
    background: #f8fafc;
  }
  #srok-vozrazhenij-boris-block .boris-table tbody tr:last-child td:first-child {
    border-radius: 0 0 0 12px;
  }
  #srok-vozrazhenij-boris-block .boris-table tbody tr:last-child td:last-child {
    border-radius: 0 0 12px 0;
  }
  #srok-vozrazhenij-boris-block .boris-table tbody td:first-child {
    color: #7f1d1d;
    font-weight: 600;
  }
  #srok-vozrazhenij-boris-block .boris-table tbody td:last-child strong {
    color: #0f172a;
  }
  #srok-vozrazhenij-boris-block .boris-footnote {
    margin: 0.85rem 0 0;
    padding-top: 0.75rem;
    border-top: 1px dashed #cbd5e1;
    font-size: 0.75rem;
    line-height: 1.45;
    color: #64748b;
  }
  @media (max-width: 960px) {
    #srok-vozrazhenij-boris-block .boris-split {
      grid-template-columns: 1fr;
    }
    #srok-vozrazhenij-boris-block .boris-lead {
      border-right: none;
      border-bottom: 1px solid #e2e8f0;
    }
  }
  @media (max-width: 640px) {
    #srok-vozrazhenij-boris-block .boris-lead,
    #srok-vozrazhenij-boris-block .boris-table-wrap {
      padding: 1.25rem;
    }
    #srok-vozrazhenij-boris-block .boris-kicker {
      font-size: 1.2rem;
    }
  }
</style>

<div class="boris-card">
  <div class="boris-split">
    <div class="boris-lead">
      <p class="boris-eyebrow">127-ФЗ · банкротство физлица</p>
      <h3 id="boris-block-title" class="boris-kicker">15 дней ≠ возражения<br>30 дней — на спор о реестре</h3>
      <p class="boris-bridge">Две цифры часто смешивают в одну «дедлайн-линию». Ниже — что из них миф из форумов, а что действует в судебной процедуре гражданина.</p>
      <div class="boris-chips" role="list">
        <div class="boris-chip" role="listitem">
          <span class="boris-chip-num is-myth">15</span>
          <span class="boris-chip-label">дней — уведомление кредиторов финуправляющим, не ваш срок на возражение</span>
        </div>
        <div class="boris-chip" role="listitem">
          <span class="boris-chip-num is-fact">30</span>
          <span class="boris-chip-label">дней — базовое окно на возражение против включения требования в реестр</span>
        </div>
      </div>
    </div>

    <div class="boris-table-wrap">
      <table class="boris-table">
        <caption>Миф vs факт: откуда берётся путаница «15 / 30» (ред. 127-ФЗ, 2025–2026)</caption>
        <thead>
          <tr>
            <th scope="col">Миф / совет из интернета</th>
            <th scope="col">Факт по 127-ФЗ</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>«На возражения после введения процедуры — 15 дней»</td>
            <td><strong>15 календарных дней</strong> — срок, в который финуправляющий обязан уведомить известных кредиторов (<strong>ст. 213.8 п. 3</strong>, <strong>213.24 п. 2.1</strong>). Это обязанность ФУ, а не срок участника на подачу возражения.</td>
          </tr>
          <tr>
            <td>«При реструктуризации — 15 дней, при реализации — 30 на возражения»</td>
            <td>На возражения к требованию в реестре — <strong>30 дней</strong> в обеих процедурах. Различие — в точке отсчёта: после 2-месячного окна требований (<strong>ст. 71</strong> через <strong>213.8</strong>) или с даты каждого требования (<strong>ст. 100</strong>).</td>
          </tr>
          <tr>
            <td>«30 дней — универсальный срок на всё в банкротстве»</td>
            <td>Есть и другие периоды: <strong>2 месяца</strong> на предъявление требований при реструктуризации, <strong>2 месяца</strong> на разногласия по продаже имущества, <strong>3 месяца</strong> на исключение уже включённого требования, <strong>6 месяцев</strong> внесудебной процедуры через МФЦ.</td>
          </tr>
          <tr>
            <td>«15 дней после акта о банкротстве через МФЦ — окно на возражения»</td>
            <td>Отдельной 15-дневной нормы на возражения в <strong>гл. XI 127-ФЗ</strong> нет. Процедура — <strong>6 месяцев</strong> (<strong>ст. 223.6</strong>); спорный перевод в суд — через <strong>ст. 223.5 п. 2</strong>, не через 30-дневное окно реестра.</td>
          </tr>
          <tr>
            <td>«Схема юрлиц: наблюдение — 15, конкурс — 30 — работает и для физлиц»</td>
            <td>У граждан нет «наблюдения» как у организаций. После признания заявления обоснованным суд вводит реструктуризацию или реализацию имущества (<strong>ст. 213.6</strong>, <strong>213.24</strong>) — перенос конспектов про юрлиц создаёт ложный дедлайн.</td>
          </tr>
        </tbody>
      </table>
      <p class="boris-footnote">Источник норм: <a href="https://www.sudact.ru/law/federalnyi-zakon-ot-26102002-n-127-fz-o/glava-x/" rel="noopener">127-ФЗ «О несостоятельности (банкротстве)»</a>, гл. X и XI. Дальше — откуда устойчив миф про «15 дней» и как его не перепутать с 30-дневным окном возражений.</p>
    </div>
  </div>
</div>
</section>
```

**Чеклист отличий от hero Алины:**
- Не первый экран, не `100vh`, вставка в теле лонгрида после 2-го H2.
- Без `<canvas>` и `<script>` — статичная редакционная таблица (режим MCP-only).
- Контраст к hero: Алина — сцена/анимация; Борис — сплит + таблица миф/факт.
- Собственный `id` секции `srok-vozrazhenij-boris-block`, без пересечений с hero.
- Светлая карточная подложка, типографика лонгрида, без персонажей и «ленты» hero.
- Фокус на одной оси статьи: 15 ≠ возражения vs 30 = возражение на требование.
