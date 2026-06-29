#!/usr/bin/env bash
# Patch for find-it.pro main.js: replace deprecated synthetic click navigation
# that fails in some Firefox new-window contexts with direct location assignment.

set -euo pipefail

URL="${1:-https://f.ai-search.org/script/main.js?v=20}"
OUT_DIR="${2:-./patches/find-it-pro}"

mkdir -p "$OUT_DIR"
SRC="$OUT_DIR/main.js"
PATCHED="$OUT_DIR/main.patched.js"

curl -fsSL "$URL" -o "$SRC"

python3 <<'PY'
from pathlib import Path

src = Path("patches/find-it-pro/main.js")
text = src.read_text()

old = '''function setTopWindowLocation(url, no_referer) {
    var link = $('<a href="' + url + '" target="_top"' + (no_referer ? ' referrerPolicy="no-referrer" rel="noreferrer"' : '') + '>link</a>')[0];
    if (typeof document.createEvent != "undefined")
    {
        var event = document.createEvent('MouseEvents');
        event.initEvent('click', true, true);
        link.dispatchEvent(event);
    }
    else
    {
        link.click();
    }
}'''

new = '''function setTopWindowLocation(url, no_referer) {
    try {
        var targetWindow = window.top || window;
        if (no_referer && targetWindow.location && targetWindow.location.replace) {
            targetWindow.location.replace(url);
            return;
        }
        if (targetWindow.location) {
            targetWindow.location.href = url;
            return;
        }
    } catch (e) {}
    var link = document.createElement('a');
    link.href = url;
    link.target = '_top';
    if (no_referer) {
        link.rel = 'noreferrer';
        link.referrerPolicy = 'no-referrer';
    }
    document.body.appendChild(link);
    link.click();
    link.remove();
}'''

if old not in text:
    raise SystemExit("Expected setTopWindowLocation block not found; main.js may have changed.")

text = text.replace(old, new, 1)
text = text.replace("if (index_mas[url])", "if (index_mas.indexOf(url) >= 0)", 1)

Path("patches/find-it-pro/main.patched.js").write_text(text)
print("Patched main.js written to patches/find-it-pro/main.patched.js")
PY

echo "Deploy patches/find-it-pro/main.patched.js to f.ai-search.org/script/main.js on the find-it.pro CDN."
