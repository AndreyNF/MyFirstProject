#!/usr/bin/env python3
"""Load next chunk args for sequential MCP upload. Usage: upload_remaining.py [index]"""
import json
import sys
from pathlib import Path

BLOB = "ML8z3SJXDL3ZF8PKlNrgomNI"
READY = Path("/workspace/.cursor/mcp4k_ready")
STATE = Path("/workspace/.cursor/upload_state.json")


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "status":
        if STATE.exists():
            print(STATE.read_text(encoding="utf-8"))
        else:
            print(json.dumps({"next": 2, "blob_id": BLOB}))
        return

    if len(sys.argv) > 1 and sys.argv[1] == "done":
        idx = int(sys.argv[2])
        STATE.write_text(
            json.dumps({"next": idx + 1, "blob_id": BLOB}, ensure_ascii=False),
            encoding="utf-8",
        )
        print(f"advanced to {idx + 1}")
        return

    idx = int(sys.argv[1]) if len(sys.argv) > 1 else (
        json.loads(STATE.read_text(encoding="utf-8"))["next"] if STATE.exists() else 2
    )
    if idx > 18:
        print("ALL_DONE")
        return

    args = json.loads((READY / f"args_{idx:02d}.json").read_text(encoding="utf-8"))
    out = Path("/workspace/.cursor/NEXT_MCP_ARGS.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({
        "index": idx,
        "chunk_len": len(args["chunk"]),
        "finalize": bool(args.get("finalize")),
        "blob_id": args["blob_id"],
    }))


if __name__ == "__main__":
    main()
