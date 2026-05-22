#!/usr/bin/env python3
"""Upload HTML to WordPress blob via Kovcheg MCP (4×18k chunks).

Reads payload files from .cursor/a7-blob-payload-*.json and prints
machine-readable lines for the agent. The agent must call mcp_call_tool
for each line OR run this script in an environment with MCP bridge.

When run standalone, validates payloads only.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

PAYLOAD_DIR = Path("/workspace/.cursor")
PAGE_ID = 341
EXCERPT = (
    "Уголовная ответственность за долги: когда это мошенничество (ст. 159) "
    "и злостное уклонение (ст. 177), граница с гражданским спором. "
    "Проверка, возбуждение дела, защита адвокатом — консультация Legis24."
)


def main() -> int:
    payloads = []
    for i in range(4):
        p = PAYLOAD_DIR / f"a7-blob-payload-{i}.json"
        if not p.is_file():
            print(f"Missing {p}", file=sys.stderr)
            return 1
        payloads.append(json.loads(p.read_text(encoding="utf-8")))
    total = sum(len(x["chunk"]) for x in payloads)
    print(json.dumps({"ok": True, "chunks": 4, "total_chars": total, "page_id": PAGE_ID}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
