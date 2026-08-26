#!/usr/bin/env python3
"""Upload remaining VPR blob chunks via agent mcp_call_tool helper.

Prints JSON arguments for each step to stdout (one line per step).
Agent should pipe each line to mcp_call_tool Kovcheg wordpress_content_blob_append.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB = sys.argv[1] if len(sys.argv) > 1 else None
START = int(sys.argv[2]) if len(sys.argv) > 2 else 2
END = int(sys.argv[3]) if len(sys.argv) > 3 else 6
BASE = Path("/workspace/.cursor/vpr-blob-calls")


def main() -> int:
    if not BLOB:
        print("usage: vpr_emit_mcp_args.py BLOB_ID [START] [END]", file=sys.stderr)
        return 2
    for step in range(START, END + 1):
        args = json.loads((BASE / f"{step:02d}.json").read_text(encoding="utf-8"))
        args["blob_id"] = BLOB
        args.pop("reset", None)
        print(json.dumps({"step": step, "arguments": args}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
