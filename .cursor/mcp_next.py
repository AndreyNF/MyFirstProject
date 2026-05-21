import json, sys
from pathlib import Path
STATE = Path("/workspace/.cursor/blob_state.json")
CHUNKS = Path("/workspace/.cursor/payload4k")
state = json.loads(STATE.read_text()) if STATE.exists() else {"index": 0, "blob_id": None}
idx = state["index"]
args = json.loads((CHUNKS / f"chunk-{idx}.json").read_text(encoding="utf-8"))
if state.get("blob_id"):
    args["blob_id"] = state["blob_id"]
Path("/workspace/.cursor/mcp_now.json").write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
if len(sys.argv) > 1 and sys.argv[1] == "advance":
    blob_id = sys.argv[2]
    state["index"] += 1
    state["blob_id"] = blob_id
    STATE.write_text(json.dumps(state, ensure_ascii=False))
    print("advanced to", state["index"], "blob", blob_id)
else:
    print("next", idx, "blob", state.get("blob_id"), "payload", len(json.dumps(args, ensure_ascii=False)))
