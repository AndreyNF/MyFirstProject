#!/usr/bin/env python3
"""Advance obysk upload state after successful MCP append."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/obysk-5k-upload-state.json")


def main() -> int:
    resp = sys.argv[1] if len(sys.argv) > 1 else ""
    st = json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else {
        "step": 2, "blob_id": "9E2XonE1JxiC3JzOjubiEWBR", "total": 18
    }
    m = re.search(r"bytes_total:\s*(\d+)", resp)
    if m:
        st["bytes_total"] = int(m.group(1))
    m = re.search(r"sha256:\s*(\S+)", resp)
    if m:
        st["sha256"] = m.group(1)
    st["step"] = st.get("step", 2) + 1
    STATE.write_text(json.dumps(st, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(st, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
