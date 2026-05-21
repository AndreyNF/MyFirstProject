#!/usr/bin/env python3
"""Prepare MCP args for blob upload step."""
import json
import sys
from pathlib import Path


def get_args(i: int, blob_id: str | None = None) -> dict:
    chunk = Path(f"/workspace/.cursor/chunk_body_{i}.txt").read_text(encoding="utf-8")
    meta = json.loads(Path(f"/workspace/.cursor/chunk_meta_{i}.json").read_text(encoding="utf-8"))
    args = {"chunk": chunk, **meta}
    if blob_id and i > 0:
        args["blob_id"] = blob_id
    return args


def main() -> None:
    i = int(sys.argv[1])
    blob = sys.argv[2] if len(sys.argv) > 2 else None
    args = get_args(i, blob)
    out = Path("/workspace/.cursor/MCP_ARGS_NOW.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"step": i, "chunk_len": len(args["chunk"]), "keys": list(args.keys())}))


if __name__ == "__main__":
    main()
