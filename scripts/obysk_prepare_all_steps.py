#!/usr/bin/env python3
"""Upload all obysk blob steps 1-17 via Kovcheg MCP using active-args JSON files.

Prints one line per step: STEP|bytes_total|response_snippet
Agent must still call CallDynamicTool — this script validates/prepares only.
For automated upload from agent loop:
  python3 scripts/obysk_prepare_step.py N BLOB_ID > /tmp/args.json
  # CallDynamicTool Kovcheg wordpress_content_blob_append json.load(/tmp/args.json)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB = "9E2XonE1JxiC3JzOjubiEWBR"


def main() -> int:
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 17
    blob = sys.argv[3] if len(sys.argv) > 3 else BLOB
    for step in range(start, end + 1):
        if step == 0:
            src = Path("/tmp/obysk-clean-00.json")
            args = json.loads(src.read_text(encoding="utf-8"))
        else:
            src = Path(f"/tmp/obysk-clean-mcp-{step:02d}.json")
            args = json.loads(src.read_text(encoding="utf-8"))
            args["blob_id"] = blob
            args.pop("reset", None)
        out = Path(f"/tmp/obysk-mcp-step-{step:02d}.json")
        out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        print(f"{step}|{len(args['chunk'])}|{out}|finalize={bool(args.get('finalize'))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
