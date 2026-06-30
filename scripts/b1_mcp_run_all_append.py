#!/usr/bin/env python3
"""Run remaining blob append steps via agent MCP (prints step + args path).

Usage: python3 scripts/b1_mcp_run_all_append.py <start_step> <blob_id>
Agent: for each printed line, mcp_call_tool Kovcheg wordpress_content_blob_append
       with json.load(open(args_path)).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/b1-blob-mcp")


def load_args(step: int, blob_id: str) -> dict:
    d = json.loads((BASE / f"{step:02d}.json").read_text(encoding="utf-8"))
    args: dict = {"chunk": d["chunk"]}
    if d.get("reset"):
        args["reset"] = True
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
    if d.get("finalize"):
        args["finalize"] = True
    return args


def main() -> int:
    start = int(sys.argv[1])
    blob_id = sys.argv[2]
    for step in range(start, 12):
        args = load_args(step, blob_id)
        p = Path(f"/workspace/.cursor/b1-args-only-{step:02d}.json")
        p.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        print(json.dumps({"step": step, "args_path": str(p), "chunk_len": len(args["chunk"]), "finalize": bool(args.get("finalize"))}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
