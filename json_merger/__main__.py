#!/usr/bin/env python3
"""Recursive JSON merge utility."""
import json
import sys
from pathlib import Path

def deep_merge(base, override):
    for key, val in override.items():
        if key in base and isinstance(base[key], dict) and isinstance(val, dict):
            deep_merge(base[key], val)
        else:
            base[key] = val
    return base

def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <base.json> <override.json> [output.json]")
        sys.exit(1)
    base = json.loads(Path(sys.argv[1]).read_text())
    override = json.loads(Path(sys.argv[2]).read_text())
    result = deep_merge(base, override)
    out = sys.argv[3] if len(sys.argv) > 3 else "-"
    if out == "-":
        print(json.dumps(result, indent=2))
    else:
        Path(out).write_text(json.dumps(result, indent=2))
        print(f"Merged -> {out}")

if __name__ == "__main__":
    main()
