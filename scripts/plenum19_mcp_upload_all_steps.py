#!/usr/bin/env python3
"""Emit MCP append args for plenum19 steps 0-4 (stdout one JSON line per step).

Agent workflow:
  for step in 0..4:
    args=$(python3 publish_plenum19_mcp_step.py $step $BLOB_ID)
    mcp_call_tool Kovcheg wordpress_content_blob_append with json.loads(args)
    update BLOB_ID from response
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path("/workspace/scripts/publish_plenum19_mcp_step.py")
OUT_DIR = Path("/tmp/plenum19_mcp_upload")


def load_step(step: int, blob_id: str | None) -> dict:
    cmd = ["python3", str(SCRIPT), str(step)]
    if step > 0:
        if not blob_id:
            raise SystemExit(f"blob_id required for step {step}")
        cmd.append(blob_id)
    return json.loads(subprocess.check_output(cmd, text=True))


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    blob_id = sys.argv[1] if len(sys.argv) > 1 else None
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    end = int(sys.argv[3]) if len(sys.argv) > 3 else 4

    manifest = []
    for step in range(start, end + 1):
        args = load_step(step, blob_id)
        path = OUT_DIR / f"step{step:02d}.json"
        path.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        import re

        latin = len(re.findall(r"st\. 158", args.get("chunk", "")))
        entry = {
            "step": step,
            "path": str(path),
            "chunk_len": len(args["chunk"]),
            "reset": bool(args.get("reset")),
            "finalize": bool(args.get("finalize")),
            "blob_id_in_args": args.get("blob_id"),
            "latin_st158": latin,
        }
        manifest.append(entry)
        print(json.dumps(entry, ensure_ascii=False))

    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
