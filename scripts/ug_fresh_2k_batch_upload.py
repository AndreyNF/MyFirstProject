#!/usr/bin/env python3
"""State + next-args for UG fresh 2k blob upload (page 562).

Agent loop:
  python3 ug_fresh_2k_batch_upload.py status
  # mcp_call_tool Kovcheg wordpress_content_blob_append json.load(/tmp/ug-fresh-mcp-next.json)
  python3 ug_fresh_2k_batch_upload.py advance 'MCP_RESPONSE'
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/ug-fresh-2k-state.json")
CHUNKS = Path("/tmp/ug-fresh-2k")
NEXT = Path("/tmp/ug-fresh-mcp-next.json")
BLOB = "6Gf2WCalZCOIm5LjdnCzUAS7"
# cumulative char offsets after each chunk index (0=reset)
EXPECTED = {
    0: 2000,
    1: 4000,
    2: 6000,
    3: 8310,
    4: 10310,
    5: 12363,
    6: 14688,
    7: 16720,
    8: 18787,
    9: 20795,
    10: 22870,
    11: 24977,
    12: 27102,
    13: 29297,
    14: 32006,
    15: 34197,
    16: 37453,
    17: 40967,
    18: 44363,
    19: 47678,
    20: 51183,
    21: 54585,
    22: 57756,
    23: 60485,
    24: 62485,
    25: 64485,
    26: 66485,
    27: 68485,
    28: 70894,
    29: 73171,
    30: 75599,
    31: 77705,
    32: 79885,
    33: 82188,
    34: 84469,
    35: 87192,
    36: 90255,
    37: 93600,
    38: 96787,
    39: 99785,
    40: 102694,
    41: 105568,
}


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"index": 1, "blob_id": BLOB, "sha256": None, "bytes_total": 2000}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")


def parse_resp(text: str) -> tuple[str | None, int | None, str | None]:
    bid = sha = None
    bt = None
    if m := re.search(r"blob_id:\s*(\S+)", text):
        bid = m.group(1)
    if m2 := re.search(r"bytes_total:\s*(\d+)", text):
        bt = int(m2.group(1))
    if m3 := re.search(r"sha256:\s*(\S+)", text):
        sha = m3.group(1)
    return bid, bt, sha


def cmd_status() -> int:
    st = load_state()
    idx = st["index"]
    if idx > 41:
        print(json.dumps({"done": True, **st}, ensure_ascii=False))
        return 0
    path = CHUNKS / f"{idx:02d}.json"
    args = json.loads(path.read_text(encoding="utf-8"))
    NEXT.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    exp = EXPECTED.get(idx)
    print(
        json.dumps(
            {
                "index": idx,
                "expected_bytes_after": exp,
                "chunk_len": len(args["chunk"]),
                "finalize": bool(args.get("finalize")),
                "args_path": str(NEXT),
                "blob_id": st.get("blob_id", BLOB),
                "bytes_total": st.get("bytes_total"),
            },
            ensure_ascii=False,
        )
    )
    return 0


def cmd_advance(resp: str) -> int:
    st = load_state()
    bid, bt, sha = parse_resp(resp)
    idx = st.get("index", 1)
    exp = EXPECTED.get(idx)
    if bid:
        st["blob_id"] = bid
    if bt is not None:
        st["bytes_total"] = bt
        if exp is not None and bt != exp:
            st["warn"] = f"expected {exp} got {bt}"
    if sha:
        st["sha256"] = sha
    st["index"] = idx + 1
    save_state(st)
    print(json.dumps(st, ensure_ascii=False))
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    if sys.argv[1] == "status":
        return cmd_status()
    if sys.argv[1] == "advance" and len(sys.argv) >= 3:
        return cmd_advance(sys.argv[2])
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
