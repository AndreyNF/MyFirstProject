#!/usr/bin/env python3
"""Upload fns blob steps via stdin JSON lines to stdout MCP args (agent loop).

Or: python3 fns_mcp_upload_steps.py call STEP BLOB_ID
prints one-line JSON args for mcp_call_tool.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/fns-blob-mcp")
BLOB = "HY9sHXaTRnAPMKzp9L2ZdmR"


def load_step(step: int, blob_id: str) -> dict:
    args = json.loads((BASE / f"{step}.json").read_text(encoding="utf-8"))
    if step > 0:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: emit STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else BLOB
    sys.stdout.write(json.dumps(load_step(step, blob_id), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
