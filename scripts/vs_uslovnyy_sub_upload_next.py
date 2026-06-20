#!/usr/bin/env python3
"""Upload all vs-uslovnyy sub-chunks via Kovcheg MCP using Cursor internal tool bridge.

Reads /workspace/.cursor/vs-uslovnyy-subchunks/sub-NN.json sequentially.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SUB_DIR = Path("/workspace/.cursor/vs-uslovnyy-subchunks")
STATE = Path("/workspace/.cursor/vs-uslovnyy-upload-state.json")


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"next": 0, "blob_id": ""}


def save_state(state: dict) -> None:
    STATE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def main() -> int:
    meta = json.loads((SUB_DIR / "meta.json").read_text(encoding="utf-8"))
    parts = meta["parts"]
    state = load_state()
    start = int(sys.argv[1]) if len(sys.argv) > 1 else state["next"]
    if start >= parts:
        print(json.dumps({"done": True, "blob_id": state.get("blob_id")}))
        return 0
    args = json.loads((SUB_DIR / f"sub-{start:02d}.json").read_text(encoding="utf-8"))
    if start > 0 and state.get("blob_id"):
        args["blob_id"] = state["blob_id"]
        args.pop("reset", None)
    out = Path(f"/workspace/.cursor/vs-sub-mcp-{start:02d}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "step": start,
                "total": parts,
                "args_path": str(out),
                "chunk_len": len(args["chunk"]),
                "reset": bool(args.get("reset")),
                "finalize": bool(args.get("finalize")),
                "blob_id_in": state.get("blob_id"),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
