#!/usr/bin/env python3
"""Load wordpress_content_blob_append args from JSON and invoke via Cursor agent socket if supported."""
from __future__ import annotations

import json
import socket
import sys
from pathlib import Path


def load_args(path: Path) -> dict:
    args = json.loads(path.read_text(encoding="utf-8"))
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit("refusing PLACEHOLDER chunk")
    return args


def try_socket_call(args: dict) -> str | None:
    sock_path = "/run/cursor/api.sock"
    if not Path(sock_path).exists():
        return None
    body = {
        "namespace": "Kovcheg",
        "toolName": "wordpress_content_blob_append",
        "arguments": args,
    }
    payload = json.dumps(body).encode()
    req = (
        f"POST /v1/mcp/call HTTP/1.0\r\n"
        f"Host: localhost\r\n"
        f"Content-Type: application/json\r\n"
        f"Content-Length: {len(payload)}\r\n"
        f"Connection: close\r\n\r\n"
    ).encode() + payload
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        s.connect(sock_path)
        s.sendall(req)
        data = b""
        while True:
            chunk = s.recv(65536)
            if not chunk:
                break
            data += chunk
    finally:
        s.close()
    text = data.decode("utf-8", errors="replace")
    if "404 Not Found" in text or "not_found" in text:
        return None
    return text


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: obysk_mcp_call_json.py ARGS_JSON", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    args = load_args(path)
    resp = try_socket_call(args)
    if resp:
        print(resp)
        return 0
    # Fallback: print args for agent CallDynamicTool
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
