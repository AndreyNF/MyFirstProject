#!/usr/bin/env python3
"""Upload all 4x20k chunks via stdin/stdout protocol for agent MCP relay."""
import json
import sys
from pathlib import Path

BLOB_STATE = Path('/workspace/.cursor/final_blob_state.json')

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'init'
    if cmd == 'init':
        BLOB_STATE.write_text(json.dumps({'step': 0, 'blob_id': None, 'sha256': None}), encoding='utf-8')
        print('init ok')
        return
    if cmd == 'get':
        state = json.loads(BLOB_STATE.read_text(encoding='utf-8'))
        step = state['step']
        if step > 3:
            print(json.dumps({'done': True, 'blob_id': state['blob_id'], 'sha256': state.get('sha256')}))
            return
        args = json.loads(Path(f'/workspace/.cursor/mcp20k_{step}.json').read_text(encoding='utf-8'))
        if state.get('blob_id') and step > 0:
            args['blob_id'] = state['blob_id']
        print(json.dumps({'step': step, 'args': args}))
        return
    if cmd == 'save':
        blob_id = sys.argv[2]
        step = int(sys.argv[3])
        sha256 = sys.argv[4] if len(sys.argv) > 4 else None
        state = {'step': step + 1, 'blob_id': blob_id, 'sha256': sha256}
        BLOB_STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')
        print(json.dumps(state))
        return
    print('unknown cmd', cmd, file=sys.stderr)
    sys.exit(1)

if __name__ == '__main__':
    main()
