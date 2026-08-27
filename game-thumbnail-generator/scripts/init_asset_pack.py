#!/usr/bin/env python3
"""Create a portable, game-wise Kulfi asset-pack workspace."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from datetime import date
from pathlib import Path


def slugify(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_value.lower()).strip("-")
    if not slug:
        raise ValueError("game name must contain at least one ASCII letter or digit")
    return slug


def asset_specs(slug: str, export_basename: str) -> dict[str, dict[str, object]]:
    return {
        "thumbnail_3x4": {
            "status": "pending",
            "depends_on": [],
            "approved_at": None,
            "files": [
                {"path": f"{slug}-thumbnail-3x4.png", "required": True},
                {"path": f"{slug}-thumbnail-3x4.webp", "required": True},
            ],
            "constraints": {"aspect_ratio": "3:4"},
            "export": {"directory": "game_thumbnails_3x4", "basename": export_basename},
        },
        "thumbnail_16x9": {
            "status": "pending",
            "depends_on": ["thumbnail_3x4"],
            "approved_at": None,
            "files": [{"path": f"{slug}-thumbnail-16x9.webp", "required": True}],
            "constraints": {"aspect_ratio": "16:9"},
            "export": {"directory": "game_thumbnails_16x9", "basename": f"{export_basename}_16x9"},
        },
        "daily_game_icon": {
            "status": "pending",
            "depends_on": ["thumbnail_3x4", "thumbnail_16x9"],
            "approved_at": None,
            "files": [{"path": f"{slug}-daily-game-icon.webp", "required": True}],
            "constraints": {"width": 287, "height": 287},
            "export": {"directory": "daily_games_icon", "basename": export_basename},
        },
        "partner_turn_icon": {
            "status": "pending",
            "depends_on": ["daily_game_icon"],
            "approved_at": None,
            "files": [
                {"path": f"{slug}-partner-turn-icon.svg", "required": True},
                {"path": f"{slug}-partner-turn-icon.webp", "required": True},
            ],
            "constraints_by_extension": {
                ".svg": {"width": 28, "height": 28},
                ".webp": {"width": 84, "height": 84},
            },
            "export": {"directory": "daily_games_partner_turn_icons", "basename": export_basename},
        },
        "info_page_square_logo": {
            "status": "pending",
            "depends_on": ["daily_game_icon"],
            "approved_at": None,
            "files": [{"path": f"{slug}-info-page-square-logo.webp", "required": True}],
            "constraints": {"width": 1024, "height": 1024},
            "export": {"directory": "daily_games_info_page_square_logos", "basename": export_basename},
        },
        "completed": {
            "status": "pending",
            "depends_on": ["daily_game_icon"],
            "approved_at": None,
            "files": [
                {"path": f"{slug}-completed.webp", "required": True},
                {"path": f"{slug}-completed.png", "required": False},
            ],
            "constraints": {"width": 1626, "height": 588},
            "export": {"directory": "daily_games_completed", "basename": export_basename},
        },
        "your_turn_background": {
            "status": "pending",
            "depends_on": ["daily_game_icon"],
            "approved_at": None,
            "files": [{"path": f"{slug}-your-turn-bg.webp", "required": True}],
            "constraints": {"width": 813, "height": 420},
            "export": {"directory": "daily_game_your_turn_bg", "basename": export_basename},
        },
    }


def render_template(path: Path, replacements: dict[str, str]) -> str:
    rendered = path.read_text()
    for key, value in replacements.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    return rendered


def write_if_missing(path: Path, content: str) -> str:
    if path.exists():
        return "kept"
    path.write_text(content)
    return "created"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("game_name", help="Human-readable game name, for example 'Chess Duel'.")
    parser.add_argument("--workspace", type=Path, default=Path.cwd(), help="Project root. Defaults to the current directory.")
    parser.add_argument("--slug", help="Optional lowercase game slug. Defaults to a slug made from the game name.")
    parser.add_argument(
        "--export-basename",
        help="Optional deployment filename stem. Defaults to the game slug with underscores instead of hyphens.",
    )
    rules = parser.add_mutually_exclusive_group(required=True)
    rules.add_argument("--rules-based", action="store_true", help="Mark the game as rules-based.")
    rules.add_argument("--not-rules-based", action="store_true", help="Mark the game as not rules-based.")
    parser.add_argument("--mechanic-source", default="", help="Concrete mechanic source path, URL, Figma node, or user explanation.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    slug = args.slug or slugify(args.game_name)
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise SystemExit("--slug must use lowercase letters, digits, and single hyphens")
    export_basename = args.export_basename or slug.replace("-", "_")
    if not re.fullmatch(r"[a-z0-9]+(?:_[a-z0-9]+)*", export_basename):
        raise SystemExit("--export-basename must use lowercase letters, digits, and single underscores")
    if args.rules_based and not args.mechanic_source.strip():
        raise SystemExit("--mechanic-source is required for a rules-based game")

    workspace = args.workspace.expanduser().resolve()
    if not workspace.exists() or not workspace.is_dir():
        raise SystemExit(f"workspace does not exist or is not a directory: {workspace}")

    game_dir = workspace / "game-assets" / slug
    iterations_dir = game_dir / "iterations"
    iterations_dir.mkdir(parents=True, exist_ok=True)

    skill_root = Path(__file__).resolve().parents[1]
    replacements = {
        "GAME_NAME": args.game_name,
        "GAME_SLUG": slug,
        "RULES_BASED": "yes" if args.rules_based else "no",
        "MECHANIC_SOURCE": args.mechanic_source.strip() or "Not required; game marked not rules-based.",
    }
    prompt = render_template(skill_root / "assets" / "prompt-template.md", replacements)
    notes = render_template(skill_root / "assets" / "source-notes-template.md", replacements)

    manifest = {
        "schema_version": 1,
        "game": {
            "name": args.game_name,
            "slug": slug,
            "export_basename": export_basename,
            "rules_based": bool(args.rules_based),
            "mechanic_source": args.mechanic_source.strip(),
            "created_at": date.today().isoformat(),
        },
        "assets": asset_specs(slug, export_basename),
    }

    outputs = {
        game_dir / "prompt.md": prompt,
        game_dir / "source-notes.md": notes,
        game_dir / "asset-pack.json": json.dumps(manifest, indent=2) + "\n",
    }
    for path, content in outputs.items():
        print(f"{write_if_missing(path, content):7} {path}")
    print(f"ready   {iterations_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
