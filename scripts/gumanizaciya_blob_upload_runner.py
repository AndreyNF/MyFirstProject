#!/usr/bin/env python3
"""Print MCP append args JSON for step N (agent: mcp_call_tool with output).

Usage: gumanizaciya_blob_upload_runner.py STEP BLOB_ID
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gumanizaciya_mcp_sequential_call import load_step  # noqa: E402


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: gumanizaciya_blob_upload_runner.py STEP BLOB_ID", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2]
    args = load_step(step, blob_id)
    out = Path(f"/tmp/gum-runner-step{step}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    meta = {
        "step": step,
        "path": str(out),
        "blob_id": args.get("blob_id"),
        "chunk_len": len(args["chunk"]),
        "finalize": bool(args.get("finalize")),
    }
    print(json.dumps(meta, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
