#!/usr/bin/env python3
"""Load blob append args for vs-osparivanie step N (0-4). Prints JSON to stdout."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/vs-osparivanie-blob-calls")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: vs_osparivanie_kovcheg_upload.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    d = json.loads((BASE / f"call-{step:02d}.json").read_text(encoding="utf-8"))
    args: dict = {"chunk": d["chunk"]}
    if step == 0 or d.get("reset"):
        args["reset"] = True
    elif blob_id:
        args["blob_id"] = blob_id
    if d.get("finalize"):
        args["finalize"] = True
    sys.stdout.write(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
