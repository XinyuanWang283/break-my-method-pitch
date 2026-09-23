"""Assemble a self-contained slide deck from a template plus embedded assets.

Usage: python3 build.py [template] [output]
Defaults: src/deckB.tpl.html -> index.html

Token substitution:
  {{IMG:name}}  -> base64 data URI from assets/manifest.json (images, video, QR)
  {{TEX:name}}  -> pre-rendered SVG from assets/math.json (see render-math.mjs)
  {{DATA}}      -> contents of assets/data.json (exported by the analysis
                   pipeline; never hand-edited)

Fails loudly if any token in the template has no matching asset.
"""
import json
import re
import sys

def build(tpl, out):
    manifest = json.load(open("assets/manifest.json"))
    math = json.load(open("assets/math.json"))
    s = open(tpl).read()
    s = re.sub(r"\{\{IMG:([a-z0-9-]+)\}\}", lambda m: manifest[m.group(1)], s)
    s = re.sub(r"\{\{TEX:([a-z0-9]+)\}\}", lambda m: math[m.group(1)], s)
    s = s.replace("{{DATA}}", open("assets/data.json").read().strip())
    missing = re.findall(r"\{\{[A-Z]+:?[^}]*\}\}", s)
    if missing:
        sys.exit(f"missing assets for tokens: {missing}")
    open(out, "w").write(s)
    print(f"{out}: {len(s) // 1024} KB")

if __name__ == "__main__":
    tpl = sys.argv[1] if len(sys.argv) > 1 else "src/deckB.tpl.html"
    out = sys.argv[2] if len(sys.argv) > 2 else "index.html"
    build(tpl, out)
