#!/usr/bin/env python3
"""Emit MCP append args for gumanizaciya blob step (0-4). Usage: step [blob_id]"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/blob-args-gumanizaciya")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: gumanizaciya_mcp_upload.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else None
    args = json.loads((BASE / f"chunk-{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
