#!/usr/bin/env python3
"""Print MCP wordpress_content_blob_append arguments JSON for one step (0-5).

Usage:
  python3 scripts/a16_mcp_call_append.py 1 giTKxs55B6PxPXmXq0
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/a16-blob-mcp")


def main() -> int:
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    d = json.loads((BASE / f"{step:02d}.json").read_text(encoding="utf-8"))
    if step == 0:
        args = {"chunk": d["chunk"], "reset": True, "finalize": False}
    else:
        args = {
            "blob_id": blob_id,
            "chunk": d["chunk"],
            "finalize": bool(d.get("finalize")),
        }
    sys.stdout.write(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
