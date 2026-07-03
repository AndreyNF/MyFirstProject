#!/usr/bin/env python3
"""Print arguments JSON for one fns blob step (stdout = mcp_call_tool arguments only).

Usage:
  python3 scripts/fns_mcp_invoke_step.py 0
  python3 scripts/fns_mcp_invoke_step.py 1 BLOB_ID
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/fns-blob-mcp")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: fns_mcp_invoke_step.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    args = json.loads((BASE / f"{step}.json").read_text(encoding="utf-8"))
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    sys.stdout.write(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
