#!/usr/bin/env python3
"""Upload one sub-chunk via Kovcheg MCP by printing args for agent, or auto via exec bridge."""
from __future__ import annotations

import json
import os
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


def parse_blob_id(text: str) -> str:
    m = re.search(r"blob_id:\s*(\S+)", text)
    return m.group(1) if m else ""


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: vs_uslovnyy_mcp_upload_one.py STEP [MCP_RESPONSE_FILE]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    meta = json.loads((SUB_DIR / "meta.json").read_text(encoding="utf-8"))
    state = load_state()
    args = json.loads((SUB_DIR / f"sub-{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0 and state.get("blob_id"):
        args["blob_id"] = state["blob_id"]
        args.pop("reset", None)
    if len(sys.argv) >= 3:
        resp = Path(sys.argv[2]).read_text(encoding="utf-8")
        bid = parse_blob_id(resp)
        if bid:
            state["blob_id"] = bid
        state["next"] = step + 1
        save_state(state)
        print(json.dumps({"saved": True, "step": step, "blob_id": state["blob_id"], "next": state["next"]}))
        return 0
    out = Path(f"/workspace/.cursor/vs-sub-mcp-{step:02d}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"step": step, "total": meta["parts"], "args_path": str(out), "chunk_len": len(args["chunk"])}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
