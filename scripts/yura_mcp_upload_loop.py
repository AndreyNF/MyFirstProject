#!/usr/bin/env python3
"""Sequential blob upload via stdin/stdout MCP bridge (if CURSOR_MCP_FD set).

Fallback: prints chunk index for agent mcp_call_tool loop.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

BLOB_FILE = Path("/workspace/.cursor/blob-id.txt")
CURSOR_DIR = Path("/workspace/.cursor")
START = int(sys.argv[1]) if len(sys.argv) > 1 else 4
END = int(sys.argv[2]) if len(sys.argv) > 2 else 29


def main() -> int:
    blob = BLOB_FILE.read_text(encoding="utf-8").strip() if BLOB_FILE.is_file() else ""
    if not blob:
        print("Missing blob-id.txt", file=sys.stderr)
        return 1
    for i in range(START, END + 1):
        d = json.loads((CURSOR_DIR / f"mcp3-{i:02d}.json").read_text(encoding="utf-8"))
        d["blob_id"] = blob
        d.pop("reset", None)
        if i == END:
            d["finalize"] = True
        out = CURSOR_DIR / f"upload-{i:02d}.json"
        out.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
        print(json.dumps({"i": i, "len": len(d["chunk"]), "finalize": d.get("finalize", False)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
