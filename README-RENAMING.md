# Rename controller folders

This branch contains `rename_controllers.py` for renaming controller directories and local `index.json` files.

## Preview

```bash
python3 rename_controllers.py
```

## Apply

```bash
python3 rename_controllers.py --apply
```

Folder format:

```text
repo_json/<id> [<controller name>] /
```

A local JSON file is renamed from `index.json` to `<controller name>.json`.

Names are first read from the root `index.json`. If an entry is missing there, the script reads the folder's local `index.json`.
