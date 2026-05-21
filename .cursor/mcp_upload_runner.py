#!/usr/bin/env python3
"""Print next MCP upload args from queue. Usage: mcp_upload_runner.py [advance BLOB_ID]"""
import json
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/upload_queue.json")
CHUNKS_DIR = Path("/workspace/.cursor/payload4k")
BLOB_ID = "2TQd06NW0muKsu0QW8GtQhsd"

def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"index": 2, "blob_id": BLOB_ID, "strategy": "payload4k_continue"}

def save_state(state):
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

def main():
    state = load_state()
    if len(sys.argv) >= 3 and sys.argv[1] == "advance":
        state["index"] = int(sys.argv[2])
        if len(sys.argv) >= 4:
            state["blob_id"] = sys.argv[3]
        save_state(state)
        print(f"advanced to index {state['index']}")
        return

    idx = state["index"]
    if idx > 20:
        print("DONE")
        return

    data = json.loads((CHUNKS_DIR / f"chunk-{idx}.json").read_text(encoding="utf-8"))
    args = {"chunk": data["chunk"], "blob_id": state["blob_id"]}
    if data.get("finalize"):
        args["finalize"] = True

    out = Path("/workspace/.cursor/mcp_next_call.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(f"NEXT index={idx} payload={len(json.dumps(args, ensure_ascii=False))} finalize={args.get('finalize', False)}")

if __name__ == "__main__":
    main()
