#!/usr/bin/env python3
"""Export approved game-wise assets into type-wise deployment folders."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from validate_asset_pack import validate_pack


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("game_folder", type=Path, help="Path to game-assets/<game-slug>.")
    parser.add_argument("--target", type=Path, required=True, help="Deployment export root.")
    parser.add_argument("--asset", action="append", dest="assets", help="Export only this manifest asset key; repeat as needed.")
    parser.add_argument("--apply", action="store_true", help="Copy files. Without this flag the command is a dry run.")
    parser.add_argument("--overwrite", action="store_true", help="Allow --apply to replace existing destination files.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    game_dir = args.game_folder.expanduser().resolve()
    errors = validate_pack(game_dir)
    if errors:
        print("Export blocked because validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    target = args.target.expanduser().resolve()
    if target == Path(target.anchor) or target == Path.home().resolve():
        print(f"Refusing broad export target: {target}")
        return 1

    manifest = json.loads((game_dir / "asset-pack.json").read_text())
    assets = manifest["assets"]
    selected = set(args.assets or assets.keys())
    unknown = sorted(selected - set(assets))
    if unknown:
        print("Unknown asset key(s): " + ", ".join(unknown))
        return 1

    operations: list[tuple[Path, Path]] = []
    for asset_name, asset in assets.items():
        if asset_name not in selected or asset["status"] != "approved":
            continue
        export = asset.get("export", {})
        directory, basename = export.get("directory"), export.get("basename")
        if not isinstance(directory, str) or not directory or not isinstance(basename, str) or not basename:
            print(f"Asset {asset_name} has invalid export.directory or export.basename")
            return 1
        if Path(directory).name != directory or directory in {".", ".."}:
            print(f"Asset {asset_name} has unsafe export.directory: {directory}")
            return 1
        if Path(basename).name != basename or basename in {".", ".."}:
            print(f"Asset {asset_name} has unsafe export.basename: {basename}")
            return 1
        for file_entry in asset["files"]:
            source = game_dir / file_entry["path"]
            if not source.is_file():
                if file_entry.get("required") is True:
                    print(f"Missing required approved file: {source}")
                    return 1
                continue
            destination = target / directory / f"{basename}{source.suffix.lower()}"
            operations.append((source, destination))

    if not operations:
        print("No approved assets matched the export selection.")
        return 0

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"{mode}: {len(operations)} file(s)")

    if args.apply and not args.overwrite:
        conflicts = [destination for _, destination in operations if destination.exists()]
        if conflicts:
            print("Export blocked because destination files already exist:")
            for destination in conflicts:
                print(f"- {destination}")
            print("Use --overwrite only after reviewing every conflict.")
            return 1

    for source, destination in operations:
        print(f"{source} -> {destination}")
        if not args.apply:
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
