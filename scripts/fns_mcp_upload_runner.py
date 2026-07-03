#!/usr/bin/env python3
"""Upload fns blob chunks via Kovcheg MCP using stdio (if KOVCHEG_MCP_CMD set) or print steps.

For cloud agent: prints step metadata; agent calls mcp_call_tool with json.load(path).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/fns-blob-mcp")
STATE = Path("/tmp/fns_blob_upload_state.json")
PAGE_ID = 431
EXCERPT = (
    "Определение ВС от 6 мая 2026 (дело № А47-12711/2023): единый тариф с 2023 года — "
    "вся задолженность ФНС во 2-ю очередь реестра. Очередность, заявление о включении, "
    "спор с налоговой и последствия для кредиторов в арбитраже."
)


def load_step(step: int, blob_id: str | None = None) -> dict:
    args = json.loads((BASE / f"{step}.json").read_text(encoding="utf-8"))
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    return args


def cmd_init() -> int:
    STATE.write_text(json.dumps({"index": 0, "blob_id": None, "total": 7}), encoding="utf-8")
    print(json.dumps({"ok": True, "total": 7, "page_id": PAGE_ID}))
    return 0


def cmd_next() -> int:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    i = st["index"]
    if i >= st["total"]:
        print(json.dumps({"done": True, "blob_id": st.get("blob_id")}))
        return 0
    args = load_step(i, st.get("blob_id"))
    out = Path(f"/tmp/fns_mcp_step_{i}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "step": i,
                "args_path": str(out),
                "chunk_len": len(args["chunk"]),
                "finalize": bool(args.get("finalize")),
                "has_reset": bool(args.get("reset")),
            }
        )
    )
    return 0


def cmd_advance(blob_id: str, bytes_total: int | None = None) -> int:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    st["blob_id"] = blob_id
    if bytes_total is not None:
        st["bytes_total"] = bytes_total
    st["index"] = st.get("index", 0) + 1
    STATE.write_text(json.dumps(st), encoding="utf-8")
    print(json.dumps({"advanced": st["index"], "blob_id": blob_id}))
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print("init | next | advance BLOB_ID [bytes]", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "init":
        return cmd_init()
    if cmd == "next":
        return cmd_next()
    if cmd == "advance" and len(sys.argv) >= 3:
        bt = int(sys.argv[3]) if len(sys.argv) > 3 else None
        return cmd_advance(sys.argv[2], bt)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
