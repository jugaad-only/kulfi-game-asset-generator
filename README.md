# Game Thumbnail Generator

A Codex skill for creating consistent mobile-game asset packs through explicit approval stages. It covers 3:4 and 16:9 thumbnails, felt daily-game icons, partner-turn icons, info-page logos, completed-state banners, and your-turn backgrounds.

The workflow is built for a mobile game catalog. It keeps titles outside thumbnail artwork, verifies rules-based mechanics before generation, preserves a quiet bottom-left composition area, and treats each approved asset as the source of truth for its derivatives.

## Requirements

- Codex with image generation and web research available
- Python 3.9 or newer for the included initialization, validation, export, and smoke-test scripts
- A concrete mechanic source for rules-based games: source code, gameplay screenshots, Figma frames, rules, or a written explanation

## Install

Clone the repository, then copy the skill into your Codex skills directory:

```bash
git clone https://github.com/jugaad-only/game-thumbnail-generator.git
mkdir -p ~/.codex/skills
cp -R game-thumbnail-generator/game-thumbnail-generator ~/.codex/skills/
```

Start a new Codex task after installation. Confirm that this file exists:

```text
~/.codex/skills/game-thumbnail-generator/SKILL.md
```

## Create a game asset pack

Initialize a working folder from a verified mechanic source:

```bash
python3 ~/.codex/skills/game-thumbnail-generator/scripts/init_asset_pack.py "Game Name" \
  --workspace /path/to/project \
  --rules-based \
  --mechanic-source /path/to/game-source
```

Use `--not-rules-based` for games without formal interaction rules.

Then ask Codex:

```text
Use $game-thumbnail-generator for Game Name.
The game folder is game-assets/game-name.
Read the mechanic source and create only the first 3:4 thumbnail candidate for approval.
```

## Approval workflow

The mandatory sequence is:

```text
3:4 thumbnail -> alternate thumbnail ratios -> daily_game_icon
```

After the exact daily icon is approved, its derivative branches may be produced independently:

- partner-turn icon
- info-page square logo
- completed-state banner
- your-turn background

Drafts and rejected versions stay in the game's `iterations/` directory. Approved files live at the game-folder root, with state recorded in `asset-pack.json`.

## Validate and export

Validate a completed pack:

```bash
python3 ~/.codex/skills/game-thumbnail-generator/scripts/validate_asset_pack.py \
  /path/to/project/game-assets/game-name
```

Preview a deployment export:

```bash
python3 ~/.codex/skills/game-thumbnail-generator/scripts/export_asset_pack.py \
  /path/to/project/game-assets/game-name \
  --target /path/to/app-assets
```

Review the mappings, then rerun with `--apply` to copy approved assets.

## Test the skill

```bash
cd game-thumbnail-generator
python3 scripts/smoke_test_thumbnail_skill.py
```

The smoke test checks workflow and prompt invariants without generating or moving assets. Visual review and explicit approval remain required.

## Repository layout

```text
game-thumbnail-generator/
  SKILL.md               Main skill instructions
  agents/openai.yaml     Codex skill metadata
  assets/                Templates and compact visual references
  references/            Workflow, quality gates, and prompt recipes
  scripts/               Initialize, validate, export, and test tools
```

See [`game-thumbnail-generator/SKILL.md`](game-thumbnail-generator/SKILL.md) for the complete operating contract and [`references/colleague-quick-start.md`](game-thumbnail-generator/references/colleague-quick-start.md) for the handoff workflow.
