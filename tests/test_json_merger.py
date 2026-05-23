import json
import tempfile
from pathlib import Path
from json_merger import deep_merge, merge_files, __version__


def test_version():
    assert __version__ == "0.2.0"


def test_deep_merge_dicts():
    base = {"a": 1, "b": {"x": 1}}
    override = {"b": {"y": 2}, "c": 3}
    result = deep_merge(base, override)
    assert result == {"a": 1, "b": {"x": 1, "y": 2}, "c": 3}


def test_deep_merge_list_replace():
    base = {"items": [1, 2]}
    override = {"items": [3, 4]}
    result = deep_merge(base, override, "replace")
    assert result["items"] == [3, 4]


def test_deep_merge_list_append():
    base = {"items": [1, 2]}
    override = {"items": [3, 4]}
    result = deep_merge(base, override, "append")
    assert result["items"] == [1, 2, 3, 4]


def test_deep_merge_list_merge():
    base = {"users": [{"name": "Alice", "role": "admin"}, {"name": "Bob"}]}
    override = {"users": [{"role": "superadmin"}, {"name": "Charlie"}]}
    result = deep_merge(base, override, "merge")
    assert result["users"][0]["name"] == "Alice"
    assert result["users"][0]["role"] == "superadmin"
    assert result["users"][1]["name"] == "Bob"
    assert result["users"][2]["name"] == "Charlie"


def test_merge_files():
    with tempfile.TemporaryDirectory() as d:
        a = Path(d, "a.json")
        b = Path(d, "b.json")
        a.write_text(json.dumps({"x": 1, "y": {"z": 1}}))
        b.write_text(json.dumps({"y": {"z": 2, "w": 3}}))
        result = merge_files([str(a), str(b)])
        assert result["x"] == 1
        assert result["y"]["z"] == 2
        assert result["y"]["w"] == 3
