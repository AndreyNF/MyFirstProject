#!/usr/bin/env python3
"""Sequential UG blob upload via agent MCP loop.

Usage:
  python3 scripts/ug_mcp_sequential_upload.py status
  python3 scripts/ug_mcp_sequential_upload.py next   # print args_path for mcp_call_tool
  python3 scripts/ug_mcp_sequential_upload.py advance 'MCP_RESPONSE'
  python3 scripts/ug_mcp_sequential_upload.py reset  # restart from step 0
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/ug-sequential-upload-state.json")
STEPS_DIR = Path("/tmp/ug-mcp-steps")
TOTAL = 5


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"index": 0, "blob_id": None, "sha256": None}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")


def parse_blob(resp: str) -> tuple[str | None, int | None, str | None]:
    bid = None
    m = re.search(r"blob_id:\s*(\S+)", resp)
    if m:
        bid = m.group(1)
    bt = None
    m2 = re.search(r"bytes_total:\s*(\d+)", resp)
    if m2:
        bt = int(m2.group(1))
    sha = None
    m3 = re.search(r"sha256:\s*(\S+)", resp)
    if m3:
        sha = m3.group(1)
    return bid, bt, sha


def ensure_steps() -> None:
    if not STEPS_DIR.is_dir() or not (STEPS_DIR / "step-00.json").is_file():
        import subprocess

        subprocess.check_call(["python3", "/workspace/scripts/ug_mcp_emit_steps.py", "prepare"])


def patch_blob_id(step: int, blob_id: str | None) -> Path:
    src = STEPS_DIR / f"step-{step:02d}.json"
    args = json.loads(src.read_text(encoding="utf-8"))
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    out = STEPS_DIR / f"step-{step:02d}-active.json"
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    return out


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    ensure_steps()
    st = load_state()

    if cmd == "reset":
        save_state({"index": 0, "blob_id": None, "sha256": None})
        print(json.dumps({"reset": True}))
        return 0

    if cmd == "status":
        print(json.dumps(st, ensure_ascii=False))
        return 0

    if cmd == "next":
        i = st["index"]
        if i >= TOTAL:
            print(json.dumps({"done": True, "blob_id": st.get("blob_id"), "sha256": st.get("sha256")}))
            return 0
        path = patch_blob_id(i, st.get("blob_id"))
        args = json.loads(path.read_text(encoding="utf-8"))
        print(
            json.dumps(
                {
                    "step": i,
                    "args_path": str(path),
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
        bid, bt, sha = parse_blob(resp)
        if bid:
            st["blob_id"] = bid
        if bt is not None:
            st["bytes_total"] = bt
        if sha:
            st["sha256"] = sha
        st["index"] = st.get("index", 0) + 1
        save_state(st)
        print(json.dumps(st, ensure_ascii=False))
        return 0

    print(f"unknown: {cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
