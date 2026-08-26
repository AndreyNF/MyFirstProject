#!/usr/bin/env python3
"""Print next obysk upload step index and args file path for agent MCP loop."""
from __future__ import annotations

import json
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/obysk-5k-upload-state.json")
BLOB = "9E2XonE1JxiC3JzOjubiEWBR"


def main() -> int:
    st = json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else {
        "step": 2, "blob_id": BLOB, "total": 18
    }
    step = st.get("step", 2)
    blob = st.get("blob_id", BLOB)
    if step >= st.get("total", 18):
        print(json.dumps({"done": True, "blob_id": blob, "sha256": st.get("sha256")}))
        return 0
    args_path = Path(f"/tmp/obysk-mcp-step-{step:02d}.json")
    if not args_path.is_file():
        import subprocess
        subprocess.check_call([
            "python3", "/workspace/scripts/obysk_prepare_all_steps.py",
            str(step), str(step), blob
        ])
    args = json.loads(args_path.read_text(encoding="utf-8"))
    out = Path("/workspace/.cursor/obysk-mcp-active-args.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({
        "step": step,
        "blob_id": blob,
        "chunk_len": len(args["chunk"]),
        "finalize": bool(args.get("finalize")),
        "args_path": str(out),
        "args_json_path": str(args_path),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
