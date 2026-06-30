#!/usr/bin/env python3
"""Print MCP append args for steps 0-4 from prepared payload files.

Usage:
  python3 scripts/vs-komp-mcp-upload-all.py STEP [BLOB_ID]

Agent: mcp_call_tool Kovcheg wordpress_content_blob_append with printed JSON.
After step 4 finalize, call wordpress_update_page_from_blob and wordpress_update_page.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

PAYLOAD_DIR = Path("/tmp")
BASE = Path("/workspace/.cursor/vs-komp-blob-mcp")


def load_step(step: int, blob_id: str = "") -> dict:
    p = PAYLOAD_DIR / f"vs-komp-payload-{step}.json"
    if not p.is_file():
        p = BASE / f"{step}.json"
    args = json.loads(p.read_text(encoding="utf-8"))
    if step > 0:
        if not blob_id:
            raise SystemExit(f"blob_id required for step {step}")
        args["blob_id"] = blob_id
        args.pop("reset", None)
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: vs-komp-mcp-upload-all.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    args = load_step(step, blob_id)
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
