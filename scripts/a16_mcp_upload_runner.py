#!/usr/bin/env python3
"""Print paths to per-step MCP append arg JSON files (agent calls mcp_call_tool per file).

Usage:
  python3 scripts/a16_mcp_upload_runner.py XF6qpuajszKb1u1JOKZeDaNb 2 5
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path("/workspace/scripts/a16_mcp_run_append.py")
OUT_DIR = Path("/tmp/a16-mcp-upload")


def main() -> int:
    if len(sys.argv) < 4:
        print("usage: a16_mcp_upload_runner.py BLOB_ID START_STEP END_STEP", file=sys.stderr)
        return 2
    blob_id = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for step in range(start, end + 1):
        out = subprocess.check_output(
            ["python3", str(SCRIPT), str(step), blob_id], text=True
        )
        path = OUT_DIR / f"step_{step}.json"
        path.write_text(out, encoding="utf-8")
        args = json.loads(out)
        print(
            json.dumps(
                {
                    "step": step,
                    "path": str(path),
                    "chunk_len": len(args["chunk"]),
                    "finalize": args.get("finalize"),
                }
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
