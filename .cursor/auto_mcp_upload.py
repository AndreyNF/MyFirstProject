#!/usr/bin/env python3
"""Upload all remaining 4k chunks via Kovcheg MCP (stdio proxy through agent relay files)."""
import json
import sys
from pathlib import Path

BLOB = "ML8z3SJXDL3ZF8PKlNrgomNI"
READY = Path("/workspace/.cursor/mcp4k_ready")
STATE = Path("/workspace/.cursor/blob_upload_progress.json")


def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"next": 3, "blob_id": BLOB, "done": False}


def save_state(state):
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def get_args(idx: int) -> dict:
    return json.loads((READY / f"args_{idx:02d}.json").read_text(encoding="utf-8"))


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "next"
    state = load_state()

    if cmd == "mark":
        idx = int(sys.argv[2])
        state["next"] = idx + 1
        if state["next"] > 18:
            state["done"] = True
        save_state(state)
        print(json.dumps(state))
        return

    if state.get("done") or state["next"] > 18:
        print("ALL_DONE")
        return

    idx = state["next"]
    args = get_args(idx)
    out = Path("/workspace/.cursor/CURRENT_MCP_INVOKE.json")
    invoke = {
        "server": "Kovcheg",
        "toolName": "wordpress_content_blob_append",
        "arguments": args,
    }
    out.write_text(json.dumps(invoke, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({
        "index": idx,
        "chunk_len": len(args["chunk"]),
        "finalize": bool(args.get("finalize")),
        "blob_id": args["blob_id"],
    }))


if __name__ == "__main__":
    main()
