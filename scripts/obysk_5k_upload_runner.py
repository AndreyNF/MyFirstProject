#!/usr/bin/env python3
"""State machine for obysk 5k blob upload — prepare step args for CallDynamicTool."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/obysk-5k-upload-state.json")
UPLOAD = Path(__file__).resolve().parent / "obysk_mcp_upload_step.py"


def main() -> int:
    if len(sys.argv) < 2:
        print("init | next | advance 'MCP response text'", file=sys.stderr)
        return 2
    cmd = sys.argv[1]

    if cmd == "init":
        st = {"step": 0, "blob_id": None, "bytes": None, "sha256": None}
        STATE.write_text(json.dumps(st, indent=2), encoding="utf-8")
        print(json.dumps(st))
        return 0

    st = json.loads(STATE.read_text(encoding="utf-8"))
    step = st["step"]

    if cmd == "next":
        import subprocess

        blob = st.get("blob_id") or ""
        args = [sys.executable, str(UPLOAD), str(step)]
        if step > 0:
            if not blob:
                raise SystemExit("blob_id missing in state for step >= 1")
            args.append(blob)
        out = subprocess.check_output(args, text=True)
        args_obj = json.loads(out)
        print(
            json.dumps(
                {
                    "step": step,
                    "blob_id": args_obj.get("blob_id"),
                    "chunk_len": len(args_obj["chunk"]),
                    "reset": bool(args_obj.get("reset")),
                    "finalize": bool(args_obj.get("finalize")),
                    "args_path": "/workspace/.cursor/obysk-mcp-active-args.json",
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
        m = re.search(r"bytes(?:_total)?:\s*(\d+)", resp)
        if m:
            st["bytes"] = int(m.group(1))
        m = re.search(r"sha256:\s*(\S+)", resp)
        if m:
            st["sha256"] = m.group(1)
        st["step"] = step + 1
        STATE.write_text(json.dumps(st, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps(st, ensure_ascii=False))
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
