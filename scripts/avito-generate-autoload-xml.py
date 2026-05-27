#!/usr/bin/env python3
"""Generate Avito Autoload XML (formatVersion 3) for Legis24 service ads."""

from __future__ import annotations

import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

ADS = [
    {
        "id": "legis24-vozrazhenie-fns-001",
        "title": "Возражение на акт ФНС — за 24 часа Legis24",
        "price": 70000,
        "description": """Пришёл акт налоговой проверки или решение ФНС — срок на возражение ограничен.

Legis24 готовит возражение на акт камеральной или выездной проверки за 24 часа:
• разбор акта и материалов;
• правовая позиция с судебной практикой;
• документ, готовый к подаче.

70 000 ₽. Кейс: 150 млн → 43 млн после возражений.
По всей РФ, удалённо. Без НДС (УСН).

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
    {
        "id": "legis24-otvet-trebovanie-fns-002",
        "title": "Ответ на требование ФНС — от 10 000 ₽ за 24 ч",
        "price": 10000,
        "description": """ФНС запросила пояснения, документы или прислала уведомление?

Подготовим за 24 часа:
• ответ на требование о документах;
• пояснения по НДС, прибыли, УСН, НДФЛ;
• письмо в инспекцию с обоснованной позицией.

От 10 000 ₽. Legis24 — не шаблон, а позиция под вашу ситуацию.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
    {
        "id": "legis24-analiz-spor-003",
        "title": "Анализ налогового спора — заключение за 24 ч",
        "price": 25000,
        "description": """Нужно понять перспективы до суда или возражения?

Правовое заключение Legis24 за 24 часа:
• оценка позиции ФНС и ваших документов;
• прогноз рисков;
• рекомендации: возражение, иск, допрос.

25 000 ₽. Для собственника, финдиректора, юриста.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
    {
        "id": "legis24-isk-nalog-arbitr-004",
        "title": "Иск в арбитраж по налогу — за 24 часа",
        "price": 45000,
        "description": """УФНС отказала, срок обжалования на исходе?

Иск в арбитражный суд за 24 часа:
• исковое заявление по налоговому спору;
• расчёт требований;
• процессуальная стратегия.

45 000 ₽. Кейс: иск подан за 26 часов, дело принято.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
    {
        "id": "legis24-paket-akt-isk-005",
        "title": "Акт ФНС + иск в арбитраж — пакет 60 000 ₽",
        "price": 60000,
        "description": """Одна правовая позиция от акта до суда.

Пакет Legis24:
1. анализ акта ФНС;
2. возражение при необходимости;
3. иск в арбитраж.

60 000 ₽ (экономия 10 000 ₽). От 24 часов на ключевые документы.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
    {
        "id": "legis24-otzyv-isk-006",
        "title": "Отзыв на иск в арбитраж — за 24 часа",
        "price": 30000,
        "description": """Иск от контрагента, заседание через несколько дней?

Отзыв на иск за 24 часа:
• разбор иска и приложений;
• правовая позиция;
• ходатайства при необходимости.

30 000 ₽. Кейс: требования снижены на 2,1 млн ₽.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
    {
        "id": "legis24-buhgalteram-008",
        "title": "Бухгалтерам: акт ФНС — решение за 24 ч",
        "price": 25000,
        "description": """Клиент получил акт ФНС или попал в арбитраж?

Передайте кейс Legis24 — стратегия за 24 часа, партнёрское вознаграждение до 30%.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
    {
        "id": "legis24-sk-poziciya-009",
        "title": "ФНС передала в СК — позиция за 24 часа",
        "price": 25000,
        "description": """Материалы в СКР, допрос через 2–3 дня?

За 24 часа: анализ документов, процессуальные нарушения, линия защиты до допроса.

25 000 ₽ (анализ). Не заменяем адвоката по УПК — даём правовую базу.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
]

CONTACT_PHONE = "79126994560"
ADDRESS = "Россия"
CATEGORY = "Предложение услуг"
SERVICE_TYPE = "Деловые услуги"  # уточнить по шаблону кабинета при ошибке валидации


def build_xml() -> ET.Element:
    root = ET.Element("Ads", formatVersion="3", target="Avito.ru")
    today = date.today().isoformat()

    for ad in ADS:
        el = ET.SubElement(root, "Ad")
        ET.SubElement(el, "Id").text = ad["id"]
        ET.SubElement(el, "DateBegin").text = today
        ET.SubElement(el, "ListingFee").text = "Package"
        ET.SubElement(el, "AdStatus").text = "Free"
        ET.SubElement(el, "Category").text = CATEGORY
        ET.SubElement(el, "ServiceType").text = SERVICE_TYPE
        ET.SubElement(el, "Title").text = ad["title"]
        desc = ET.SubElement(el, "Description")
        desc.text = ad["description"]
        ET.SubElement(el, "Price").text = str(ad["price"])
        ET.SubElement(el, "Address").text = ADDRESS
        ET.SubElement(el, "ContactPhone").text = CONTACT_PHONE
        ET.SubElement(el, "ContactMethod").text = "По телефону и в сообщениях"
        ET.SubElement(el, "CompanyName").text = "Legis24"

    return root


def main() -> None:
    out = Path(__file__).resolve().parents[1] / "avito" / "autoload" / "legis24-new-ads.xml"
    out.parent.mkdir(parents=True, exist_ok=True)
    tree = ET.ElementTree(build_xml())
    ET.indent(tree, space="  ")
    tree.write(out, encoding="utf-8", xml_declaration=True)
    print(f"Wrote {len(ADS)} ads to {out}")


if __name__ == "__main__":
    main()
