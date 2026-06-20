#!/usr/bin/env python3
"""Emit wordpress_content_blob_append arguments for vs-uslovnyy page chunks."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/blob-args-vs-uslovnyy")
PAGE_ID = 527
EXCERPT = (
    "Верховный суд в деле № 18-УД26-4-К4 отказал в ужесточении условного срока по ст. 159 УК РФ: "
    "разбираем, какие смягчающие обстоятельства — малолетние дети, иждивенец, первая судимость — "
    "защищают от реального лишения свободы и почему «поворот к худшему» в кассации требует "
    "конкретной мотивировки — консультация адвоката."
)


def load_step(step: int, blob_id: str | None = None) -> dict:
    args = json.loads((BASE / f"chunk-{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("emit STEP [BLOB_ID] | meta", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "meta":
        print(
            json.dumps(
                {
                    "page_id": PAGE_ID,
                    "excerpt": EXCERPT,
                    "slug": "vs-uslovnyy-srok-moshennichestvo-st-73-kassaciya-zashchita-2026",
                    "title": "ВС 2026: условный срок за мошенничество — кассация не вправе ужесточить приговор | Legis24",
                },
                ensure_ascii=False,
            )
        )
        return 0
    if cmd == "emit":
        step = int(sys.argv[2])
        blob_id = sys.argv[3] if len(sys.argv) > 3 else None
        args = load_step(step, blob_id)
        print(json.dumps(args, ensure_ascii=False))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
