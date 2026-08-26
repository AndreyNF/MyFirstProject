#!/usr/bin/env python3
"""Prepare wordpress_content_blob_append args for obysk 5k step N with blob_id."""
from __future__ import annotations

import json
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/obysk-5k-upload-state.json")


def step_path(n: int) -> Path:
    return Path(f"/workspace/.cursor/mcp-out-step-{n}.json")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: obysk_5k_sequential_upload.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    st = json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else {}
    blob_id = sys.argv[2] if len(sys.argv) > 2 else st.get("blob_id")
    args = json.loads(step_path(step).read_text(encoding="utf-8"))
    if step == 0:
        args["reset"] = True
        args.pop("blob_id", None)
    else:
        if not blob_id:
            raise SystemExit("blob_id required for step >= 1")
        args["blob_id"] = blob_id
        args.pop("reset", None)
    out = Path("/workspace/.cursor/obysk-mcp-active-args.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "step": step,
                "args_path": str(out),
                "blob_id": args.get("blob_id"),
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
