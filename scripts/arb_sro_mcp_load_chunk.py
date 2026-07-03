#!/usr/bin/env python3
"""Load chunk N args for arb-sro blob upload (agent → mcp_call_tool)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB = "9GPJWFouleTtzarVf3xgZwnY"
DIR = Path("/tmp/arb-sro-2k")
OUT = Path("/tmp/arb-sro-active-args.json")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: arb_sro_mcp_load_chunk.py CHUNK_INDEX", file=sys.stderr)
        return 2
    i = int(sys.argv[1])
    d = json.loads((DIR / f"{i:02d}.json").read_text(encoding="utf-8"))
    args = {"blob_id": BLOB, "chunk": d["chunk"], "finalize": bool(d.get("finalize", False))}
    OUT.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"index": i, "chunk_len": len(args["chunk"]), "finalize": args["finalize"], "args_path": str(OUT)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
