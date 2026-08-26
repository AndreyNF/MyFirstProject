#!/usr/bin/env python3
"""Prepare wordpress_content_blob_append args for obysk page upload step N (0-5)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ARGS_DIR = Path("/workspace/.cursor/obysk-mcp-args")
OUT = Path("/workspace/.cursor/obysk-mcp-active-args.json")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: obysk_mcp_prepare_step.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else None
    args = json.loads((ARGS_DIR / f"step_{step:02d}.json").read_text(encoding="utf-8"))
    if step == 0:
        args["reset"] = True
        args.pop("blob_id", None)
    else:
        if not blob_id:
            raise SystemExit("blob_id required for step > 0")
        args["blob_id"] = blob_id
        args.pop("reset", None)
    if step == 5:
        args["finalize"] = True
    OUT.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "step": step,
                "args_path": str(OUT),
                "chunk_len": len(args["chunk"]),
                "reset": bool(args.get("reset")),
                "finalize": bool(args.get("finalize")),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
