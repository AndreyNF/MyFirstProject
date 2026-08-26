#!/usr/bin/env python3
"""Sequential 15k obysk blob upload state machine for agent CallDynamicTool."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/obysk-full15-upload-state.json")
CHUNK_DIR = Path("/tmp")
ACTIVE = Path("/workspace/.cursor/obysk-mcp-active-args.json")


def chunk_path(step: int) -> Path:
    return CHUNK_DIR / f"obysk-full15-mcp-{step:02d}.json"


def main() -> int:
    if len(sys.argv) < 2:
        print("init | next | advance 'MCP response'", file=sys.stderr)
        return 2
    cmd = sys.argv[1]

    if cmd == "init":
        st = {"step": 0, "blob_id": None, "sha256": None, "bytes": None}
        STATE.write_text(json.dumps(st, indent=2), encoding="utf-8")
        print(json.dumps(st))
        return 0

    st = json.loads(STATE.read_text(encoding="utf-8"))
    step = st["step"]

    if cmd == "next":
        if step >= 6:
            print(json.dumps({"done": True, **st}))
            return 0
        args = json.loads(chunk_path(step).read_text(encoding="utf-8"))
        if st.get("blob_id"):
            args["blob_id"] = st["blob_id"]
            args.pop("reset", None)
        ACTIVE.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        print(
            json.dumps(
                {
                    "step": step,
                    "args_path": str(ACTIVE),
                    "chunk_len": len(args["chunk"]),
                    "reset": bool(args.get("reset")),
                    "finalize": bool(args.get("finalize")),
                    "blob_id": args.get("blob_id"),
                },
                ensure_ascii=False,
            )
        )
        return 0

    if cmd == "advance":
        resp = sys.argv[2] if len(sys.argv) > 2 else ""
        m = re.search(r"blob_id:\s*(\S+)", resp)
        if m:
            st["blob_id"] = m.group(1)
        m = re.search(r"sha256:\s*(\S+)", resp)
        if m:
            st["sha256"] = m.group(1)
        m = re.search(r"bytes:\s*(\d+)", resp)
        if m:
            st["bytes"] = int(m.group(1))
        st["step"] = step + 1
        STATE.write_text(json.dumps(st, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps(st, ensure_ascii=False))
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
