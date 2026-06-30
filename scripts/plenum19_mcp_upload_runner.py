#!/usr/bin/env python3
"""State helper for plenum19 blob upload via MCP (steps 0-4)."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

STATE = Path("/tmp/plenum19_upload_state.json")
PAGE_ID = 543
BLOB_SCRIPT = Path("/workspace/scripts/publish_plenum19_mcp_step.py")
META = Path("/workspace/.cursor/plenum19-blob-calls/meta.json")


def load_step(step: int, blob_id: str | None = None) -> dict:
    cmd = ["python3", str(BLOB_SCRIPT), str(step)]
    if blob_id:
        cmd.append(blob_id)
    return json.loads(subprocess.check_output(cmd, text=True))


def cmd_init() -> int:
    STATE.write_text(json.dumps({"step": 0, "blob_id": None, "page_id": PAGE_ID}), encoding="utf-8")
    print(json.dumps({"ok": True, "page_id": PAGE_ID}))
    return 0


def cmd_next() -> int:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    step = st["step"]
    if step > 4:
        print(json.dumps({"done": True, "blob_id": st.get("blob_id")}))
        return 0
    args = load_step(step, st.get("blob_id"))
    out = Path(f"/tmp/plenum19_mcp_current_{step}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "step": step,
                "args_path": str(out),
                "chunk_len": len(args["chunk"]),
                "finalize": bool(args.get("finalize")),
                "blob_id": args.get("blob_id"),
            },
            ensure_ascii=False,
        )
    )
    return 0


def cmd_advance(blob_id: str, bytes_total: int | None = None) -> int:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    st["blob_id"] = blob_id
    if bytes_total is not None:
        st["bytes_total"] = bytes_total
    st["step"] = st.get("step", 0) + 1
    STATE.write_text(json.dumps(st), encoding="utf-8")
    print(json.dumps(st))
    return 0


def cmd_meta() -> int:
    print(META.read_text(encoding="utf-8"))
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print("init | next | advance BLOB_ID [bytes] | meta", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "init":
        return cmd_init()
    if cmd == "next":
        return cmd_next()
    if cmd == "advance" and len(sys.argv) >= 3:
        bt = int(sys.argv[3]) if len(sys.argv) > 3 else None
        return cmd_advance(sys.argv[2], bt)
    if cmd == "meta":
        return cmd_meta()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
