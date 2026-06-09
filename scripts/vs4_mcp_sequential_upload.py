#!/usr/bin/env python3
"""Sequential vs4 blob upload via Kovcheg MCP — reads args from /tmp/mcp-inline-step{N}.json.

Usage:
  python3 scripts/vs4_mcp_sequential_upload.py STEP [BLOB_ID]

Prints JSON result metadata to stdout. Agent should use mcp_call_tool per step;
this script validates args and prints envelope for verification.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def load_step(step: int, blob_id: str = "") -> dict:
    path = Path(f"/tmp/mcp-inline-step{step}.json")
    if not path.is_file():
        path = Path(f"/tmp/mcp-args-{step}-only.json")
    args = json.loads(path.read_text(encoding="utf-8"))
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit(f"refusing PLACEHOLDER in step {step}")
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: vs4_mcp_sequential_upload.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    args = load_step(step, blob_id)
    meta = {
        "step": step,
        "server": "Kovcheg",
        "toolName": "wordpress_content_blob_append",
        "arguments": args,
        "chunk_len": len(args["chunk"]),
        "blob_id": args.get("blob_id"),
        "finalize": bool(args.get("finalize")),
    }
    out = Path(f"/tmp/vs4-mcp-call-step{step}.json")
    out.write_text(json.dumps(meta, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: v for k, v in meta.items() if k != "arguments"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
