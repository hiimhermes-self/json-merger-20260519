#!/usr/bin/env python3
"""Recursive JSON merge utility with list strategies."""
import argparse
import json
import sys
from pathlib import Path

__version__ = "0.2.0"


def deep_merge(base, override, list_strategy="replace"):
    """Recursively merge override into base.

    list_strategy:
      - replace: override list replaces base list
      - append:  override list items appended to base list
      - merge:   dict items inside lists are merged by matching keys
    """
    if not isinstance(base, dict) or not isinstance(override, dict):
        return override

    for key, val in override.items():
        if key in base and isinstance(base[key], dict) and isinstance(val, dict):
            deep_merge(base[key], val, list_strategy)
        elif key in base and isinstance(base[key], list) and isinstance(val, list):
            if list_strategy == "append":
                base[key] = base[key] + val
            elif list_strategy == "merge" and len(base[key]) > 0 and isinstance(base[key][0], dict):
                merged = []
                for i, bitem in enumerate(base[key]):
                    if i < len(val) and isinstance(val[i], dict):
                        merged.append(deep_merge(dict(bitem), val[i], list_strategy))
                    else:
                        merged.append(bitem)
                if len(val) > len(base[key]):
                    merged.extend(val[len(base[key]):])
                base[key] = merged
            else:
                base[key] = val
        else:
            base[key] = val
    return base


def merge_files(paths, list_strategy="replace"):
    if not paths:
        raise ValueError("No input files provided.")
    result = json.loads(Path(paths[0]).read_text(encoding="utf-8"))
    for p in paths[1:]:
        data = json.loads(Path(p).read_text(encoding="utf-8"))
        result = deep_merge(result, data, list_strategy)
    return result


def main(args=None):
    parser = argparse.ArgumentParser(
        prog="json-merger",
        description="Recursive JSON merge utility. Supports nested dicts, list strategies, and multiple files.",
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("files", nargs="+", help="JSON files to merge (left-to-right priority)")
    parser.add_argument("-o", "--output", default="-", help="Output file (default: stdout)")
    parser.add_argument("-s", "--strategy", choices=["replace", "append", "merge"], default="replace",
                        help="List merge strategy")
    parser.add_argument("--indent", type=int, default=2, help="JSON indent (default: 2)")
    opts = parser.parse_args(args)

    result = merge_files(opts.files, opts.strategy)
    out = json.dumps(result, indent=opts.indent, ensure_ascii=False)
    if opts.output == "-":
        print(out)
    else:
        Path(opts.output).write_text(out + "\n", encoding="utf-8")
        print(f"Merged {len(opts.files)} files -> {opts.output}")


if __name__ == "__main__":
    main()
