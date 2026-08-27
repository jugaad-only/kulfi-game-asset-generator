#!/usr/bin/env python3
"""Validate a game-wise Kulfi asset pack using only the Python standard library."""

from __future__ import annotations

import argparse
import json
import re
import struct
import xml.etree.ElementTree as ET
from pathlib import Path


ALLOWED_STATUSES = {"pending", "approved", "not-required"}
REQUIRED_ASSETS = {
    "thumbnail_3x4",
    "thumbnail_16x9",
    "daily_game_icon",
    "partner_turn_icon",
    "info_page_square_logo",
    "completed",
    "your_turn_background",
}


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("invalid PNG header")
    return struct.unpack(">II", header[16:24])


def webp_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:64]
    if len(data) < 30 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise ValueError("invalid WebP header")
    chunk = data[12:16]
    if chunk == b"VP8X":
        return 1 + int.from_bytes(data[24:27], "little"), 1 + int.from_bytes(data[27:30], "little")
    if chunk == b"VP8L":
        if data[20] != 0x2F:
            raise ValueError("invalid VP8L signature")
        bits = int.from_bytes(data[21:25], "little")
        return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
    if chunk == b"VP8 ":
        marker = data.find(b"\x9d\x01\x2a")
        if marker < 0 or marker + 7 > len(data):
            raise ValueError("invalid VP8 frame header")
        width, height = struct.unpack("<HH", data[marker + 3 : marker + 7])
        return width & 0x3FFF, height & 0x3FFF
    raise ValueError(f"unsupported WebP chunk {chunk!r}")


def svg_dimensions(path: Path) -> tuple[int, int]:
    root = ET.parse(path).getroot()

    def number(value: str | None) -> int | None:
        if value is None:
            return None
        match = re.fullmatch(r"\s*([0-9]+(?:\.[0-9]+)?)\s*(?:px)?\s*", value)
        return round(float(match.group(1))) if match else None

    width, height = number(root.get("width")), number(root.get("height"))
    if width and height:
        return width, height
    view_box = root.get("viewBox")
    if view_box:
        values = [float(value) for value in re.split(r"[\s,]+", view_box.strip())]
        if len(values) == 4:
            return round(values[2]), round(values[3])
    raise ValueError("SVG must define numeric width/height or viewBox")


def dimensions(path: Path) -> tuple[int, int]:
    suffix = path.suffix.lower()
    if suffix == ".png":
        return png_dimensions(path)
    if suffix == ".webp":
        return webp_dimensions(path)
    if suffix == ".svg":
        return svg_dimensions(path)
    raise ValueError(f"unsupported image format {suffix}")


def constraints_for(asset: dict[str, object], path: Path) -> dict[str, object]:
    by_extension = asset.get("constraints_by_extension", {})
    if isinstance(by_extension, dict) and path.suffix.lower() in by_extension:
        value = by_extension[path.suffix.lower()]
        return value if isinstance(value, dict) else {}
    value = asset.get("constraints", {})
    return value if isinstance(value, dict) else {}


def check_dimensions(path: Path, constraints: dict[str, object]) -> str | None:
    try:
        width, height = dimensions(path)
    except (OSError, ValueError, ET.ParseError) as error:
        return f"{path.name}: cannot read dimensions ({error})"
    expected_width, expected_height = constraints.get("width"), constraints.get("height")
    if isinstance(expected_width, int) and width != expected_width:
        return f"{path.name}: width {width}, expected {expected_width}"
    if isinstance(expected_height, int) and height != expected_height:
        return f"{path.name}: height {height}, expected {expected_height}"
    ratio = constraints.get("aspect_ratio")
    if isinstance(ratio, str) and ":" in ratio:
        left, right = ratio.split(":", 1)
        expected = float(left) / float(right)
        actual = width / height
        if abs(actual - expected) > 0.005:
            return f"{path.name}: ratio {width}:{height}, expected {ratio}"
    return None


def validate_pack(game_dir: Path) -> list[str]:
    game_dir = game_dir.expanduser().resolve()
    errors: list[str] = []
    manifest_path = game_dir / "asset-pack.json"
    if not manifest_path.is_file():
        return [f"missing {manifest_path}"]
    try:
        manifest = json.loads(manifest_path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        return [f"cannot read asset-pack.json: {error}"]

    if manifest.get("schema_version") != 1:
        errors.append("asset-pack.json: schema_version must be 1")
    game = manifest.get("game")
    assets = manifest.get("assets")
    if not isinstance(game, dict):
        return errors + ["asset-pack.json: game must be an object"]
    if not isinstance(assets, dict):
        return errors + ["asset-pack.json: assets must be an object"]

    slug = game.get("slug")
    if not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        errors.append("asset-pack.json: game.slug must use lowercase letters, digits, and single hyphens")
    elif game_dir.name != slug:
        errors.append(f"game folder is '{game_dir.name}', but manifest slug is '{slug}'")
    if not isinstance(game.get("rules_based"), bool):
        errors.append("asset-pack.json: game.rules_based must be true or false")
    if game.get("rules_based") is True and not str(game.get("mechanic_source", "")).strip():
        errors.append("asset-pack.json: rules-based games require game.mechanic_source")

    missing_assets = sorted(REQUIRED_ASSETS - set(assets))
    if missing_assets:
        errors.append("asset-pack.json: missing asset entries: " + ", ".join(missing_assets))

    known_root_files: set[str] = set()
    for asset_name, asset_value in assets.items():
        if not isinstance(asset_value, dict):
            errors.append(f"assets.{asset_name} must be an object")
            continue
        status = asset_value.get("status")
        if status not in ALLOWED_STATUSES:
            errors.append(f"assets.{asset_name}.status must be pending, approved, or not-required")
            continue
        dependencies = asset_value.get("depends_on", [])
        if not isinstance(dependencies, list) or not all(isinstance(item, str) for item in dependencies):
            errors.append(f"assets.{asset_name}.depends_on must be a list of asset names")
            dependencies = []
        if status == "approved":
            for dependency in dependencies:
                dependency_asset = assets.get(dependency)
                dependency_status = dependency_asset.get("status") if isinstance(dependency_asset, dict) else None
                if dependency_status not in {"approved", "not-required"}:
                    errors.append(f"assets.{asset_name} is approved before dependency {dependency}")
            if not asset_value.get("approved_at"):
                errors.append(f"assets.{asset_name} is approved but approved_at is empty")

        files = asset_value.get("files")
        if not isinstance(files, list) or not files:
            errors.append(f"assets.{asset_name}.files must be a non-empty list")
            continue
        for file_value in files:
            if not isinstance(file_value, dict) or not isinstance(file_value.get("path"), str):
                errors.append(f"assets.{asset_name}.files contains an invalid entry")
                continue
            relative = Path(file_value["path"])
            if relative.is_absolute() or len(relative.parts) != 1:
                errors.append(f"assets.{asset_name}: canonical files must live at the game-folder root")
                continue
            known_root_files.add(relative.name)
            path = game_dir / relative
            required = file_value.get("required") is True
            if status == "approved" and required and not path.is_file():
                errors.append(f"assets.{asset_name}: missing approved file {relative.name}")
            if status != "approved" and path.exists():
                errors.append(f"assets.{asset_name}: unapproved canonical file is at the game-folder root: {relative.name}")
            if path.is_file():
                issue = check_dimensions(path, constraints_for(asset_value, path))
                if issue:
                    errors.append(f"assets.{asset_name}: {issue}")

    for record in ("prompt.md", "source-notes.md"):
        if not (game_dir / record).is_file():
            errors.append(f"missing {record}")
    iterations = game_dir / "iterations"
    if not iterations.is_dir():
        errors.append("missing iterations/ folder")
    else:
        valid_iteration = re.compile(r"(?:-v\d{2,}|-replaced-\d{4}-\d{2}-\d{2}|contact-sheet)")
        for path in iterations.iterdir():
            if path.is_file() and path.suffix.lower() in {".png", ".webp", ".svg"} and not valid_iteration.search(path.stem):
                errors.append(f"iterations/{path.name}: image iterations need -vNN, -replaced-YYYY-MM-DD, or contact-sheet")

    for path in game_dir.iterdir():
        if path.is_file() and path.suffix.lower() in {".png", ".webp", ".svg"} and path.name not in known_root_files:
            errors.append(f"unexpected root asset not listed in asset-pack.json: {path.name}")
        if path.is_file() and re.search(r"-v\d{2,}", path.stem):
            errors.append(f"versioned candidate must be inside iterations/: {path.name}")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("game_folder", type=Path, help="Path to game-assets/<game-slug>.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate_pack(args.game_folder)
    if errors:
        print(f"FAIL {args.game_folder}: {len(errors)} issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS {args.game_folder}: asset pack structure, dependencies, names, and dimensions are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
