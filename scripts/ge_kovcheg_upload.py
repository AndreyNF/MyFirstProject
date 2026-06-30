#!/usr/bin/env python3
"""Emit wordpress_content_blob_append arguments for google-earth page (step 0-4).

Usage:
  python3 scripts/ge_kovcheg_upload.py STEP [BLOB_ID]

Prints one JSON line: {"tool": "wordpress_content_blob_append", "arguments": {...}}
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/google-earth-blob-mcp")
PAGE_ID = 445
EXCERPT = (
    "Верховный суд отменил приговор за мошенничество с земельным участком: снимки Google Earth Pro "
    "нельзя считать единственным доказательством. Линия защиты, кассация и оспаривание цифровых улик."
)


def chunk_args(step: int, blob_id: str = "") -> dict:
    d = json.loads((BASE / f"{step:02d}.json").read_text(encoding="utf-8"))
    args: dict = {"chunk": d["chunk"]}
    if d.get("reset"):
        args["reset"] = True
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
    if d.get("finalize"):
        args["finalize"] = True
    else:
        args["finalize"] = False
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: ge_kovcheg_upload.py STEP [BLOB_ID] | meta", file=sys.stderr)
        return 2
    if sys.argv[1] == "meta":
        print(
            json.dumps(
                {
                    "page_id": PAGE_ID,
                    "excerpt": EXCERPT,
                    "slug": "vs-google-earth-dokazatelstva-moshennichestvo-zashchita-2026",
                    "title": "ВС 2026: Google Earth не доказывает мошенничество — защита по ст. 159",
                },
                ensure_ascii=False,
            )
        )
        return 0
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    if step < 0 or step > 4:
        return 2
    args = chunk_args(step, blob_id)
    print(
        json.dumps(
            {"tool": "wordpress_content_blob_append", "arguments": args},
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
