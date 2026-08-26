#!/usr/bin/env python3
"""Preload all pending chunk args from current state index to 38."""
import json
import subprocess
from pathlib import Path

UPLOAD = Path("/workspace/scripts/kassaciya_mcp_upload.py")
CHUNKS = Path("/workspace/.cursor/kassaciya-2k-chunks")
OUT = Path("/tmp/kassaciya-queue")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    st = json.loads(Path("/workspace/.cursor/kassaciya-upload-state.json").read_text())
    idx = st["index"]
    bid = st["blob_id"]
    for step in range(idx, 39):
        args = json.loads((CHUNKS / f"{step:02d}.json").read_text(encoding="utf-8"))
        if step > 0 and bid:
            args["blob_id"] = bid
        (OUT / f"{step:02d}.json").write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        print(step, len(args["chunk"]), args.get("finalize"))


if __name__ == "__main__":
    main()
