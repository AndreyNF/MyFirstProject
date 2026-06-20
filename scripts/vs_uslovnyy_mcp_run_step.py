#!/usr/bin/env python3
"""Run one vs-uslovnyy blob append step via Kovcheg MCP (stdin JSON bridge).

Usage:
  python3 scripts/vs_uslovnyy_mcp_run_step.py 0
  python3 scripts/vs_uslovnyy_mcp_run_step.py 1 BLOB_ID
  ...
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/blob-args-vs-uslovnyy")


def load_step(step: int, blob_id: str | None = None) -> dict:
    args = json.loads((BASE / f"chunk-{step:02d}.json").read_text(encoding="utf-8"))
    if step == 0:
        args["reset"] = True
    elif blob_id:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: vs_uslovnyy_mcp_run_step.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else None
    args = load_step(step, blob_id)
    fd = os.environ.get("CURSOR_MCP_FD")
    if fd:
        req = {
            "jsonrpc": "2.0",
            "id": step,
            "method": "tools/call",
            "params": {
                "name": "wordpress_content_blob_append",
                "arguments": args,
            },
        }
        os.write(int(fd), (json.dumps(req) + "\n").encode())
        resp = os.read(int(fd), 10_000_000)
        print(resp.decode())
        return 0
    # Fallback: write args path for agent mcp_call_tool
    out = Path(f"/workspace/.cursor/vs-mcp-step{step}-args.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"step": step, "args_path": str(out), "chunk_len": len(args["chunk"])}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
