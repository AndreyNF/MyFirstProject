#!/usr/bin/env python3
"""Load wordpress_content_blob_append args for step N (0-6) with optional blob_id.

Usage:
  python3 scripts/fns_mcp_run_append.py 0
  python3 scripts/fns_mcp_run_append.py 3 BLOB_ID

Stdout: JSON object suitable for mcp_call_tool(..., arguments=...).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/fns-blob-mcp")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: fns_mcp_run_append.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else None
    args = json.loads((BASE / f"{step}.json").read_text(encoding="utf-8"))
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    sys.stdout.write(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
