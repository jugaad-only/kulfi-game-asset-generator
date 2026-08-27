#!/usr/bin/env python3
"""Dry-run checks for the game-thumbnail-generator skill.

This verifies prompt/workflow invariants for multiple current games and runs
synthetic candidate-QA regressions. It does not call image generation, approve,
or move project assets.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GameCase:
    name: str
    mechanic: str
    cues: str
    mood: str
    mechanic_source: str
    style: str = "chunky tactile polished mobile game catalog art"


CASES = [
    GameCase(
        "Wordle",
        "guess words on a tile grid with color feedback",
        "chunky square letter tiles, green yellow and gray feedback, clean word-board layout",
        "satisfying, smart, quick",
        "current game test case; production prompts must verify against actual game rules or approved gameplay reference",
    ),
    GameCase(
        "This Or That",
        "choose between two playful options",
        "two opposing option cards, simple divider, playful food or lifestyle props",
        "social, funny, debate-friendly",
        "current game test case; production prompts must verify against actual game rules or approved gameplay reference",
    ),
    GameCase(
        "Snatch the Fries",
        "snatch golden fries with a fast pulling action",
        "red fries bucket, golden fries, cyan kitchen backdrop, magnet/snatch motion",
        "fast, cheeky, arcade",
        "current game test case; production prompts must verify against actual game rules or approved gameplay reference",
    ),
    GameCase(
        "Moodoku",
        "place rule-accurate mood/color puzzle tiles into a clean grid",
        "clean grid, separated cells, soft bright color coding, tactile puzzle tiles",
        "calm, clever, tactile",
        "current game test case; production prompts must verify against actual game rules or approved gameplay reference",
    ),
    GameCase(
        "Pillowtalk Legacy",
        "exchange intimate conversation prompts",
        "two plush pillows, speech-bubble card cue without readable text, cozy fabric",
        "cozy, warm, private",
        "current game test case; production prompts must verify against actual game rules or approved gameplay reference",
    ),
    GameCase(
        "Sperm Racers",
        "race through a maze toward a glowing egg",
        "dark maroon tunnel, rose-pink maze walls, mint route, gold egg glow, playful abstract race forms",
        "competitive, silly, arcade",
        "current game test case; production prompts must verify against actual game rules or approved gameplay reference",
    ),
    GameCase(
        "Weave",
        "must be verified from the actual game source, gameplay screenshot, Figma frame, or user explanation before generation",
        "existing approved Weave asset may guide style/material language only, not the full rule system",
        "cozy, clever, satisfying",
        "known risk case from live QA; do not generate mechanic-accurate Weave thumbnails from guessed rules",
    ),
    GameCase(
        "Chess",
        "move rule-accurate chess pieces to threaten or check the opposing king",
        "recognizable king and knight silhouettes, honest board geometry, focused tactical confrontation",
        "strategic, competitive, premium",
        "current game test case; production prompts must verify against actual chess rules or approved gameplay reference",
    ),
    GameCase(
        "Ludo",
        "race colored tokens from home around a cross-shaped board toward the finish",
        "chunky colored pawns, recognizable cross-board route, one clear race interaction",
        "social, bright, competitive",
        "current game test case; production prompts must verify against actual Ludo rules or approved gameplay reference",
    ),
    GameCase(
        "Jigsaw",
        "assemble interlocking pieces to complete one picture",
        "large tactile puzzle pieces, one obvious placement gap, partial image reveal",
        "calm, satisfying, crafty",
        "current game test case; production prompts must verify against actual jigsaw gameplay or approved gameplay reference",
    ),
]


REQUIRED_3X4 = [
    "3:4 portrait",
    "mobile app game shelf",
    "do not include any title text",
    "logo",
    "watermark",
    "One dominant subject",
    "Mechanic source verified",
    "optical center or upper-middle",
    "foreground edges tack-sharp",
    "lower-left quadrant visually quiet but not empty",
    "readable beside many other mobile game thumbnails",
]

REQUIRED_16X9 = [
    "16:9 landscape",
    "approved 3:4 direction",
    "Recompose",
    "No game title",
    "wordmark",
    "watermark",
    "lower-left visually quiet but not empty",
]

REQUIRED_MANIFEST_ASSETS = {
    "thumbnail_3x4",
    "thumbnail_16x9",
    "daily_game_icon",
    "partner_turn_icon",
    "info_page_square_logo",
    "completed",
    "your_turn_background",
}


def build_3x4_prompt(case: GameCase) -> str:
    return f"""Generate one polished 3:4 portrait mobile game catalog thumbnail for {case.name}.

This is artwork for a mobile app game shelf, not a store poster. The game name will appear separately below the tile, so do not include any title text, logo, watermark, badge, promo copy, readable UI label, or wordmark inside the artwork.

Core mechanic: {case.mechanic}.
Mechanic source verified: {case.mechanic_source}.
Visual world and real game cues: {case.cues}.
Mood: {case.mood}.
Art style: {case.style}.

Composition requirements:
- 3:4 portrait crop.
- One dominant subject or one clear gameplay action.
- Strong silhouette and immediate readability at small mobile thumbnail size.
- Bias the focal point toward the center, upper area, or right side.
- Keep the dominant gameplay cluster near the optical center or upper-middle; do not let it sit noticeably low in the frame.
- Keep the lower-left quadrant visually quiet but not empty: use only tiny, low-contrast background details there.
- Do not let the hero subject, main interaction, board, dense props, or important UI occupy the lower-left quadrant.
- Use clear foreground/background separation, strong lighting, and a simple color identity.
- Keep mechanic-critical foreground edges tack-sharp at small shelf size. Apply depth of field, haze, bloom, and environmental softness only behind the subject.
- Avoid clutter, tiny details, fake store badges, frames, borders, cinematic poster layouts, or desktop/web hover-preview styling.

The final image should feel like an exciting, honest preview of the game's actual play experience and remain readable beside many other mobile game thumbnails.
"""


def build_16x9_prompt(case: GameCase) -> str:
    return f"""Create a 16:9 landscape thumbnail asset for {case.name} based on the approved 3:4 direction.

Preserve the same dominant subject, gameplay mechanic, palette, lighting, art style, and emotional promise. Recompose for landscape intentionally: add horizontal breathing room, keep the main action crop-safe, maintain clear foreground/background separation, and avoid simply stretching or blind-cropping the portrait image.

No game title, wordmark, readable UI label, logo, watermark, badge, promo copy, border, device frame, or store badge inside the artwork. Keep the lower-left visually quiet but not empty with only tiny low-contrast background details.
"""


def assert_contains(prompt: str, required: list[str], label: str) -> None:
    lowered = prompt.lower()
    missing = [term for term in required if term.lower() not in lowered]
    if missing:
        raise AssertionError(f"{label} missing required terms: {', '.join(missing)}")


def assert_folder_invariants() -> None:
    game_root = "game-assets/<game-slug>/"
    draft_3x4 = "game-assets/<game-slug>/iterations/<game-slug>-thumbnail-3x4-v01.png"
    draft_16x9 = "game-assets/<game-slug>/iterations/<game-slug>-thumbnail-16x9-v01.webp"
    final_3x4 = "game-assets/<game-slug>/<game-slug>-thumbnail-3x4.png"
    final_16x9 = "game-assets/<game-slug>/<game-slug>-thumbnail-16x9.webp"
    daily_icon = "game-assets/<game-slug>/<game-slug>-daily-game-icon.webp"
    iterations = "game-assets/<game-slug>/iterations/"
    required = [
        ("game-wise root", game_root, "game-assets/<game-slug>/"),
        ("3:4 iteration naming", draft_3x4, "/iterations/<game-slug>-thumbnail-3x4-v01"),
        ("16:9 iteration naming", draft_16x9, "/iterations/<game-slug>-thumbnail-16x9-v01"),
        ("3:4 approved naming", final_3x4, "<game-slug>-thumbnail-3x4.png"),
        ("16:9 approved naming", final_16x9, "<game-slug>-thumbnail-16x9.webp"),
        ("daily icon beside thumbnails", daily_icon, "<game-slug>-daily-game-icon.webp"),
        ("single iterations folder", iterations, "/iterations/"),
    ]
    for label, value, term in required:
        if term not in value:
            raise AssertionError(f"{label} invariant failed: {value}")


def assert_skill_guardrails() -> None:
    skill_dir = Path(__file__).resolve().parents[1]
    checks = {
        "SKILL.md": [
            "Non-negotiable stop condition",
            "do not generate, revise, present, or approve",
            "Mechanic verification",
            "User special requests",
            "requested words must be valid board content",
            "ask whether there is an existing repo",
            "authoritative foreground baseline",
            "optical center or upper-middle",
            "request to regenerate means create a new versioned candidate",
            "focused internet reference pass",
            "Record URLs, local screenshot paths, search terms, author/style/license information",
            "Felt Icon Rules",
            "exactly one visible color",
            "genuinely transparent canvas",
            "Never bake in a checkerboard",
            "filled felt or transparent",
            "Does this really look like [GAME NAME]?",
            "[SUBJECT] black fill",
            "one controlled area of internal negative space",
            "Minimal detail means fewer details, not smaller details",
            "Minimal does not mean featureless",
            "Do not use intricate rosettes",
            "two independent mandatory gates",
            "Matching the cyan felt treatment alone is never sufficient",
            "Capture screenshots of the selected web and Flaticon references",
            "never promote or export them as production assets",
            "Do not start the daily icon stage until all thumbnail formats requested for the game are final",
            "references/daily-game-icon-references.md",
            "references/partner-turn-icon-references.md",
            "references/info-page-square-logo-references.md",
            "Create `daily_games_info_page_square_logos`",
            "references/completed-state-references.md",
            "Create `daily_games_completed`",
            "Ignore the Hangman completed asset entirely",
            "#1C272C",
            "#03171C",
            "references/your-turn-background-references.md",
            "Create `daily_game_your_turn_bg`",
            "sibling derivative branches",
            "active workspace root",
            "references/colleague-quick-start.md",
            "scripts/init_asset_pack.py",
            "scripts/validate_asset_pack.py",
            "scripts/validate_candidate.py",
            "scripts/export_asset_pack.py",
        ],
        "references/candidate-validation.md": [
            "Resolve the request to exactly one asset type",
            "If the user says only `game icon`",
            "A nonzero exit is a hard stop",
            "partner_turn_icon",
            "your_turn_background",
            "Do not present a failed candidate",
        ],
        "references/prompt-recipes.md": [
            "If the real rule cannot be verified, STOP",
            "Only create a style study if the user explicitly asks",
            "Mechanic verification:",
            "specific words, phrases, slang, colors, or props",
            "existing repo or source folder",
            "Do this before writing a mechanic-accurate prompt",
            "Room Or Setting Revisions",
            "authoritative sharp foreground",
            "regenerate from the earlier sharp baseline",
        ],
        "references/quality-gates.md": [
            "records the mechanic source",
            "Rules-based candidate has no recorded mechanic verification source",
            "User special requests were incorporated without breaking verified mechanics",
            "optical center or upper-middle",
            "Foreground became softer or less accurate after a background/scene edit",
            "Daily Game Icon Gate",
            "Partner-Turn Icon Gate",
            "Info-Page Square Logo Gate",
            "Completed-State Gate",
            "Your-Turn Background Gate",
            "positive and negative space",
            "binary-mask test",
            "one filled felt silhouette",
            "name-recognition QA",
            "Does this really look like [GAME NAME]?",
            "internet reference search terms",
            "were not copied",
            "Flaticon black-fill or glyph reference",
            "one broad, controlled internal negative-space opening",
            "Detail was simplified by removal, not miniaturization",
            "minimal without becoming plain, generic, or featureless",
            "Both independent checks pass",
            "Selected visual references were captured",
            "asset-pack.json",
            "validate_asset_pack.py",
        ],
        "references/folder-structure.md": [
            "For rules-based games, `source-notes.md` is required before generation",
            "<workspace-root>/game-assets/<game-slug>/iterations/",
            "Use exactly one",
            "reference screenshots",
            "<game-slug>-reference-<source>-<subject>-vNN.png",
            "deployment destinations, not generation workspaces",
            "asset-pack.json",
        ],
        "references/derivative-prompt-recipes.md": [
            "Source of truth: [APPROVED THUMBNAIL PATH]",
            "translate the felt icon into a simplified flat single-color vector mark",
            "Center the felt symbol on a pale background",
            "Create the 1626 x 588 completed-state banner",
            "Create the 813 x 420 your-turn background",
        ],
        "references/colleague-quick-start.md": [
            "init_asset_pack.py",
            "validate_asset_pack.py",
            "export_asset_pack.py",
            "dry-run",
            "internet reference pass",
        ],
        "references/daily-game-icon-references.md": [
            "tactile felt-art construction",
            "exactly one visible color",
            "one filled felt silhouette",
            "genuine transparency for the surrounding canvas",
            "binary-mask test",
            "Name-Recognition QA",
            "Does this really look like `[GAME NAME]`?",
            "Internet Reference Pass",
            "Recognition references",
            "Inspiration references",
            "Flaticon reference",
            "one controlled area of internal negative space",
            "Minimal detail means fewer, larger forms",
            "Do not simplify away the subject's large functional identity cues",
            "Run two separate yes/no checks",
            "Capture screenshots of the selected references",
            "daily_games_icon/chess.webp",
            "daily_games_icon/zip_together.webp",
        ],
        "references/partner-turn-icon-references.md": [
            "approved daily icon is the source of truth",
            "daily_games_partner_turn_icons/chess.svg",
            "daily_games_partner_turn_icons/zip_together.webp",
        ],
        "references/info-page-square-logo-references.md": [
            "1024 x 1024 WebP",
            "pale background from the same monochrome color family",
            "daily_games_info_page_square_logos/chess.webp",
            "daily_games_info_page_square_logos/zip_together.webp",
        ],
        "references/completed-state-references.md": [
            "1626 x 588",
            "place it on the right",
            "left side visually quiet",
            "one fixed shared background template",
            "horizontally uniform dark teal vertical gradient",
            "Ignore the Hangman completed asset entirely",
            "Do not open, sample, compare against, cite, or use it",
            "daily_games_completed/chess.png",
            "daily_games_completed/zip_together.webp",
        ],
        "references/your-turn-background-references.md": [
            "813 x 420",
            "left 55%",
            "faint oversized watermark",
            "daily_game_your_turn_bg/chess.webp",
            "daily_game_your_turn_bg/poople_your_turn_bg.webp",
            "daily_game_your_turn_bg/zip_together.webp",
        ],
        "assets/source-notes-template.md": [
            "Internet References",
            "Recognition references and URLs",
            "Flaticon black-fill or glyph reference",
            "Local reference screenshot paths",
            "Distilled silhouette cues to preserve",
            "Details to avoid copying",
        ],
    }
    for relative_path, required_terms in checks.items():
        text = (skill_dir / relative_path).read_text()
        missing = [term for term in required_terms if term not in text]
        if missing:
            raise AssertionError(f"{relative_path} missing guardrails: {', '.join(missing)}")

    forbidden_checks = {
        "SKILL.md": [
            "Start after the partner-turn stage",
            "Start after the info-page square-logo stage",
        ],
        "references/quality-gates.md": [
            "The partner-turn stage is complete",
            "The info-page square-logo stage is complete",
        ],
        "references/info-page-square-logo-references.md": [
            "after the partner-turn stage",
        ],
        "references/completed-state-references.md": [
            "after the info-page square-logo stage",
        ],
        "references/folder-structure.md": [
            "non-final-assets/pending-generated/<game-slug>/",
            "finalised-assets/<game-slug>",
            "finalised-assets-16x9/<game-slug>",
        ],
    }
    for relative_path, forbidden_terms in forbidden_checks.items():
        text = (skill_dir / relative_path).read_text()
        present = [term for term in forbidden_terms if term in text]
        if present:
            raise AssertionError(f"{relative_path} has false derivative dependencies: {', '.join(present)}")

    portability_files = [
        "SKILL.md",
        "references/folder-structure.md",
        "references/final-asset-list.md",
    ]
    forbidden_machine_paths = ["/Users/", "Documents/ChatGPT", ".codex/skills/game-thumbnail-generator"]
    for relative_path in portability_files:
        text = (skill_dir / relative_path).read_text()
        present = [term for term in forbidden_machine_paths if term in text]
        if present:
            raise AssertionError(f"{relative_path} contains machine-specific paths: {', '.join(present)}")


def assert_asset_pack_tooling() -> None:
    skill_dir = Path(__file__).resolve().parents[1]
    with tempfile.TemporaryDirectory(prefix="kulfi-asset-pack-") as temp:
        workspace = Path(temp)
        init = subprocess.run(
            [
                sys.executable,
                str(skill_dir / "scripts/init_asset_pack.py"),
                "Smoke Test",
                "--workspace",
                str(workspace),
                "--rules-based",
                "--mechanic-source",
                "verified smoke fixture",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        if init.returncode != 0:
            raise AssertionError(f"initializer failed: {init.stdout}{init.stderr}")

        game_dir = workspace / "game-assets/smoke-test"
        expected = [
            game_dir / "asset-pack.json",
            game_dir / "prompt.md",
            game_dir / "source-notes.md",
            game_dir / "iterations",
        ]
        missing = [str(path) for path in expected if not path.exists()]
        if missing:
            raise AssertionError("initializer missed: " + ", ".join(missing))

        manifest = json.loads((game_dir / "asset-pack.json").read_text())
        if set(manifest.get("assets", {})) != REQUIRED_MANIFEST_ASSETS:
            raise AssertionError("manifest asset classes do not match the required pipeline")
        if manifest.get("game", {}).get("export_basename") != "smoke_test":
            raise AssertionError("initializer did not translate the folder slug into a Kulfi export basename")
        if manifest["assets"]["daily_game_icon"]["export"]["basename"] != "smoke_test":
            raise AssertionError("asset export mapping does not use the Kulfi export basename")
        your_turn = manifest["assets"]["your_turn_background"]
        if your_turn["constraints"] != {"width": 813, "height": 420}:
            raise AssertionError("your-turn background dimensions do not match the production contract")
        if your_turn["export"]["directory"] != "daily_game_your_turn_bg":
            raise AssertionError("your-turn background export directory is incorrect")

        validator_command = [
            sys.executable,
            str(skill_dir / "scripts/validate_asset_pack.py"),
            str(game_dir),
        ]
        validation = subprocess.run(validator_command, capture_output=True, text=True, check=False)
        if validation.returncode != 0:
            raise AssertionError(f"new pending pack failed validation: {validation.stdout}{validation.stderr}")

        stray = game_dir / "smoke-test-daily-game-icon.webp"
        stray.write_bytes(b"not-a-final-asset")
        rejected = subprocess.run(validator_command, capture_output=True, text=True, check=False)
        if rejected.returncode == 0 or "unapproved canonical file" not in rejected.stdout:
            raise AssertionError("validator did not reject an unapproved canonical asset")
        stray.unlink()

        export_target = workspace / "deployment"
        export = subprocess.run(
            [
                sys.executable,
                str(skill_dir / "scripts/export_asset_pack.py"),
                str(game_dir),
                "--target",
                str(export_target),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        if export.returncode != 0:
            raise AssertionError(f"export dry run failed: {export.stdout}{export.stderr}")
        if export_target.exists():
            raise AssertionError("export dry run created deployment files")


def assert_candidate_validation() -> None:
    skill_dir = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, str(skill_dir / "scripts/test_candidate_validation.py")],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(f"candidate QA regression failed: {result.stdout}{result.stderr}")


def main() -> None:
    for index, case in enumerate(CASES, start=1):
        prompt_3x4 = build_3x4_prompt(case)
        prompt_16x9 = build_16x9_prompt(case)
        assert_contains(prompt_3x4, REQUIRED_3X4, f"{case.name} 3:4")
        assert_contains(prompt_16x9, REQUIRED_16X9, f"{case.name} 16:9")
        print(f"{index}. PASS {case.name}: 3:4 prompt and post-approval 16:9 prompt include required invariants.")

    assert_folder_invariants()
    print(f"{len(CASES) + 1}. PASS folder discipline: game-wise root and single-iterations naming invariants are present.")
    assert_skill_guardrails()
    print(f"{len(CASES) + 2}. PASS rules-based guardrails: mechanic verification hard-stop is present.")
    assert_asset_pack_tooling()
    print(f"{len(CASES) + 3}. PASS asset-pack tooling: initialize, validate, reject stray files, and dry-run export.")
    assert_candidate_validation()
    print(f"{len(CASES) + 4}. PASS candidate QA: all asset contracts and known failure regressions are enforced.")
    print(f"Checked {len(CASES)} current-game cases. No workspace files moved, generated, or finalized.")


if __name__ == "__main__":
    main()
