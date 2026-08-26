#!/usr/bin/env python3
import json, sys
from pathlib import Path
step = int(sys.argv[1])
args = json.loads(Path(f"/tmp/kreditor-blob-step-{step}.json").read_text(encoding="utf-8"))
print(json.dumps(args, ensure_ascii=False))
