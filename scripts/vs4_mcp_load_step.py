#!/usr/bin/env python3
"""Load MCP append args for vs4 step N (0-4) from /tmp/vs4_upload_step{N}.json."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    step = int(sys.argv[1])
    path = Path(f"/tmp/vs4_upload_step{step}.json")
    if not path.is_file():
        # fallback: generate from chunks
        from vs4_upload_blob import args_for_step  # type: ignore

        blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
        args = args_for_step(step, blob_id)
    else:
        args = json.loads(path.read_text(encoding="utf-8"))
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit("refusing placeholder chunk")
    sys.stdout.write(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
