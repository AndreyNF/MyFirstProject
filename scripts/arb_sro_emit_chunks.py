#!/usr/bin/env python3
"""Upload arb-sro blob chunks START..END via stdin JSON lines to stdout for agent.

Each line: {"index": N, "arguments": {...}}
Agent must call mcp_call_tool Kovcheg wordpress_content_blob_append sequentially.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB = "9GPJWFouleTtzarVf3xgZwnY"
DIR = Path("/tmp/arb-sro-2k")


def main() -> int:
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 43
    for i in range(start, end + 1):
        d = json.loads((DIR / f"{i:02d}.json").read_text(encoding="utf-8"))
        args = {"blob_id": BLOB, "chunk": d["chunk"], "finalize": bool(d.get("finalize", False))}
        print(json.dumps({"index": i, "arguments": args}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
