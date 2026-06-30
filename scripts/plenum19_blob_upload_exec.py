#!/usr/bin/env python3
"""Sequential plenum19 blob upload state manager.

Agent workflow per step:
  1. python3 plenum19_blob_upload_exec.py prepare STEP [BLOB_ID]
  2. mcp_call_tool Kovcheg wordpress_content_blob_append with json.load(args_path)
  3. python3 plenum19_blob_upload_exec.py record STEP BLOB_ID [BYTES]
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

STATE = Path("/tmp/plenum19_blob_upload_exec_state.json")
PAGE_ID = 543
SCRIPT = Path("/workspace/scripts/publish_plenum19_mcp_step.py")
META = Path("/workspace/.cursor/plenum19-blob-calls/meta.json")


def load_step(step: int, blob_id: str | None = None) -> dict:
    cmd = ["python3", str(SCRIPT), str(step)]
    if step > 0:
        if not blob_id:
            raise SystemExit(f"blob_id required for step {step}")
        cmd.append(blob_id)
    return json.loads(subprocess.check_output(cmd, text=True))


def cmd_init() -> int:
    STATE.write_text(json.dumps({"step": 0, "blob_id": None, "page_id": PAGE_ID}), encoding="utf-8")
    print(json.dumps({"ok": True, "page_id": PAGE_ID}))
    return 0


def cmd_prepare(step: int, blob_id: str | None) -> int:
    args = load_step(step, blob_id)
    out = Path(f"/tmp/plenum19_exec_args_{step}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "step": step,
                "args_path": str(out),
                "chunk_len": len(args["chunk"]),
                "reset": bool(args.get("reset")),
                "finalize": bool(args.get("finalize")),
                "latin_st158": args["chunk"].count("st. 158"),
                "cyr_st158": args["chunk"].count("ст. 158"),
            },
            ensure_ascii=False,
        )
    )
    return 0


def cmd_record(step: int, blob_id: str, bytes_total: int | None = None) -> int:
    st = json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else {"page_id": PAGE_ID}
    st["blob_id"] = blob_id
    st["last_step"] = step
    if bytes_total is not None:
        st["bytes_total"] = bytes_total
    st["step"] = step + 1
    STATE.write_text(json.dumps(st), encoding="utf-8")
    print(json.dumps(st, ensure_ascii=False))
    return 0


def cmd_meta() -> int:
    print(META.read_text(encoding="utf-8"))
    return 0


def cmd_status() -> int:
    if STATE.is_file():
        print(STATE.read_text(encoding="utf-8"))
    else:
        print("{}")
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print("init | prepare STEP [BLOB_ID] | record STEP BLOB_ID [bytes] | meta | status", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "init":
        return cmd_init()
    if cmd == "meta":
        return cmd_meta()
    if cmd == "status":
        return cmd_status()
    if cmd == "prepare":
        step = int(sys.argv[2])
        bid = sys.argv[3] if len(sys.argv) > 3 else None
        return cmd_prepare(step, bid)
    if cmd == "record" and len(sys.argv) >= 4:
        step = int(sys.argv[2])
        bid = sys.argv[3]
        bt = int(sys.argv[4]) if len(sys.argv) > 4 else None
        return cmd_record(step, bid, bt)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
