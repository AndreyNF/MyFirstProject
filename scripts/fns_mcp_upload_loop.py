#!/usr/bin/env python3
"""Upload all fns blob chunks via subprocess curl to MCP (agent fallback: mcp_call_tool).

Reads /workspace/.cursor/fns-blob-mcp/{0..6}.json and prints one JSON line per step:
  {"step": N, "arguments": {...}}

Agent: mcp_call_tool Kovcheg wordpress_content_blob_append with each arguments object.
After step 6 finalize, call wordpress_update_page_from_blob and wordpress_update_page.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/fns-blob-mcp")
EXCERPT = (
    "Определение ВС от 6 мая 2026 (дело № А47-12711/2023): единый тариф с 2023 года — "
    "вся задолженность ФНС во 2-ю очередь реестра. Очередность, заявление о включении, "
    "спор с налоговой и последствия для кредиторов в арбитраже."
)


def load_step(step: int, blob_id: str | None = None) -> dict:
    args = json.loads((BASE / f"{step}.json").read_text(encoding="utf-8"))
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
        print(json.dumps({"page_id": 431, "excerpt": EXCERPT, "slug": "fns-strahovye-vznosy-vtoraya-ochered-bankrotstvo-vs"}))
        return 0
    if cmd == "emit":
        step = int(sys.argv[2])
        blob_id = sys.argv[3] if len(sys.argv) > 3 else None
        args = load_step(step, blob_id)
        print(json.dumps({"step": step, "arguments": args}, ensure_ascii=False))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
