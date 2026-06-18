#!/usr/bin/env python3
"""Generate Avito Autoload XML (formatVersion 3) for Legis24 service ads.

Canonical field values: shared/legis24-avito-xml-rules.md
Validated via autoload.avito.ru/format/xmlcheck/
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

ADS = [
    {
        "id": "legis24-vozrazhenie-fns-001",
        "title": "Возражение на акт ФНС — за 24 часа Legis24",
        "price": 70000,
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/06/image_1781767794739_21f3jk.jpg",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/file_000000004c4071f583c27d339ad32aa1.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/file_00000000e3e471fd91bfd6735fa8c287.png",
        ],
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
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/06/file_0000000035b8722f8b52df17dde994ab.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/file_000000009fa0720cb6b656751e24fee3.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/image_1781768470799_y9yu91.jpg",
        ],
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
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/06/file_000000003224720c8816d3c847109d89.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/file_00000000fd64722fa91588f1b751f981.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/file_000000004e3871f5a4cbdf50e35358e6.png",
        ],
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
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/06/image_1781768867206_qlk75q.jpg",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/image_1781768982807_y9ojet.jpg",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/file_000000009c2c71f78a197f755c84cd4d.png",
        ],
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
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/06/file_0000000035f871f590d002e76257d0a6.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/file_000000008d6c71f5b6245ab233a627ad.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/image_1781769401637_qim6hl.jpg",
        ],
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
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/06/image_1781769667751_z8faej.jpg",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/image_1781769796266_opjcug.jpg",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/image_1781769898587_ttbyhg.jpg",
        ],
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
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/06/file_00000000fa8071f585754376d566e86d.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/image_1781770273028_btebjd.jpg",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/file_00000000ad2071fdafe328342b17dc9a.png",
        ],
        "description": """Клиент получил акт ФНС или попал в арбитраж?

Передайте кейс Legis24 — стратегия за 24 часа, партнёрское вознаграждение до 30%.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
    {
        "id": "legis24-sk-poziciya-009",
        "title": "ФНС передала в СК — позиция за 24 часа",
        "price": 25000,
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/06/file_00000000a49871f5b8f6678159680633.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/image_1781770571116_8hqxps.jpg",
            "https://advokat-vsem.online/wp-content/uploads/2026/06/file_00000000425471f591be37088ae187e3.png",
        ],
        "description": """Материалы в СКР, допрос через 2–3 дня?

За 24 часа: анализ документов, процессуальные нарушения, линия защиты до допроса.

25 000 ₽ (анализ). Не заменяем адвоката по УПК — даём правовую базу.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
]

CONTACT_PHONE = "79126994560"  # в кабинете может храниться; в карточке — только чат
CONTACT_METHOD = "В сообщениях"  # не «По телефону» / не «По телефону и в сообщениях»
ADDRESS = "Россия"
CATEGORY = "Предложение услуг"
# Иерархия Avito: Предложение услуг → Деловые услуги → Юридические услуги
SERVICE_TYPE = "Деловые услуги"
SERVICE_SUBTYPE = "Юридические услуги"  # обязательный «Тип услуги» (ServiceSubtype)
# Поля как в опубликованном объявлении id 8159283806 (Legis24)
SERVICE_SUBSPECIES = "Составление договоров, доверенностей, исков"
PREPAYMENT = "Нужна"
WORK_WITH_CONTRACT = "Да"
CONSULTATIONS = "Нет"
PLACE = "Удалённо"
WORK_EXPERIENCE = "4–7 лет"
DESCRIPTION_SUFFIX = "\n\nСвязь только в чате Avito, звонки не принимаем."


def _add_images(el: ET.Element, image_urls: str | list[str]) -> None:
    urls = [image_urls] if isinstance(image_urls, str) else image_urls
    images = ET.SubElement(el, "Images")
    for url in urls:
        ET.SubElement(images, "Image", url=url)


def _add_legal_service_fields(el: ET.Element) -> None:
    """Обязательные параметры категории «Юридические услуги» (по живому объявлению)."""
    ET.SubElement(el, "ServiceSubspecies").text = SERVICE_SUBSPECIES
    ET.SubElement(el, "WorkExperience").text = WORK_EXPERIENCE
    ET.SubElement(el, "Prepayment").text = PREPAYMENT
    ET.SubElement(el, "WorkWithContract").text = WORK_WITH_CONTRACT
    ET.SubElement(el, "Consultations").text = CONSULTATIONS
    ET.SubElement(el, "Place").text = PLACE


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
        ET.SubElement(el, "ServiceSubtype").text = SERVICE_SUBTYPE
        _add_legal_service_fields(el)
        ET.SubElement(el, "Title").text = ad["title"]
        desc = ET.SubElement(el, "Description")
        desc.text = ad["description"].rstrip() + DESCRIPTION_SUFFIX
        _add_images(el, ad["image_urls"])
        ET.SubElement(el, "Price").text = str(ad["price"])
        ET.SubElement(el, "Address").text = ADDRESS
        ET.SubElement(el, "ContactPhone").text = CONTACT_PHONE
        ET.SubElement(el, "ContactMethod").text = CONTACT_METHOD
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
