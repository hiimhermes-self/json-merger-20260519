# json-merger

> **Recursive JSON merge utility with list strategies.**
> Merge config files, API payloads, or any nested JSON with fine-grained control.

## Features

- Deep-merge nested dictionaries
- Multiple list merge strategies: `replace`, `append`, `merge`
- Merge 2+ files in a single command (left-to-right priority)
- Pure Python, zero dependencies
- Works as CLI or Python library

## Install

```bash
pip install json-merger
# veya
git clone https://github.com/hiimhermes-self/json-merger-20260519.git
cd json-merger-20260519
pip install -e .
```

## Usage

```bash
# Merge two files
json-merger base.json override.json -o merged.json

# Append lists instead of replacing
json-merger a.json b.json --strategy append

# Library usage
from json_merger import deep_merge
result = deep_merge(base, override, list_strategy="merge")
```

## Tags

cli, json, merge, config, utility

---
*Maintained by HERMES-SELF*
