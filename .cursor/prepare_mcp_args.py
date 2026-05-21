#!/usr/bin/env python3
"""Upload blob chunks by loading args from prepared JSON files."""
import json
import subprocess
import sys
from pathlib import Path


def load_args(step: int, blob_id: str | None = None) -> dict:
    meta_path = Path(f"/workspace/.cursor/chunk_meta_{step}.json")
    body_path = Path(f"/workspace/.cursor/chunk_body_{step}.txt")
    args = {"chunk": body_path.read_text(encoding="utf-8"), **json.loads(meta_path.read_text(encoding="utf-8"))}
    if blob_id and step > 0:
        args["blob_id"] = blob_id
    return args


def main() -> None:
    step = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    blob_id = sys.argv[2] if len(sys.argv) > 2 else None
    args = load_args(step, blob_id)
    out = Path("/workspace/.cursor/MCP_ARGS_NOW.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"step": step, "chunk_len": len(args["chunk"]), "keys": list(args.keys())}))


if __name__ == "__main__":
    main()
