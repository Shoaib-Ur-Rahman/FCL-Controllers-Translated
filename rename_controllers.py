#!/usr/bin/env python3
"""Rename controller folders and local index.json files by their controller names.

Default mode is a dry run. Run with --apply after reviewing the mapping.
"""

import argparse
import json
import re
from pathlib import Path

REPO_ROOT = Path("repo_json")


def safe_name(name: str) -> str:
    name = re.sub(r'[\\/:*?"<>|]', "-", name).strip(" .")
    return name or "unnamed-controller"


def load_mapping() -> dict[str, str]:
    root = json.loads(Path("index.json").read_text(encoding="utf-8"))
    return {str(item["id"]): str(item["name"]) for item in root if item.get("id") and item.get("name")}


def local_name(folder: Path) -> str | None:
    index = folder / "index.json"
    if not index.is_file():
        return None
    data = json.loads(index.read_text(encoding="utf-8"))
    name = data.get("name")
    return str(name) if name else None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    mapping = load_mapping()

    for folder in sorted(REPO_ROOT.iterdir(), key=lambda p: p.name):
        if not folder.is_dir():
            continue

        controller_id = folder.name
        name = mapping.get(controller_id) or local_name(folder)
        if not name:
            print(f"SKIP {controller_id}: no name found")
            continue

        target_name = safe_name(name)
        target_folder = REPO_ROOT / f"{controller_id} [{target_name}]"
        local_index = folder / "index.json"
        target_index = folder / f"{safe_name(name)}.json"

        print(f"{folder} -> {target_folder}")
        if local_index.is_file():
            print(f"{local_index} -> {target_index}")

        if args.apply:
            if local_index.is_file() and not target_index.exists():
                local_index.rename(target_index)
            if not target_folder.exists():
                folder.rename(target_folder)


if __name__ == "__main__":
    main()
