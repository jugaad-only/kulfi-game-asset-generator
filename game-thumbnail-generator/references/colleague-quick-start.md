# Colleague Quick Start

This is the shortest safe path from a game idea to a complete, exportable asset pack.

## 1. Initialize The Game

From the skill folder:

```bash
python3 scripts/init_asset_pack.py "Chess" \
  --workspace /path/to/project \
  --rules-based \
  --mechanic-source /path/to/chess-rules-or-gameplay-source
```

For a game without formal interaction rules, use `--not-rules-based`. The command never overwrites existing records.

Game folders use hyphenated slugs, while deployment filenames default to Kulfi-style underscores. For example, `Daily Question` works in `game-assets/daily-question/` and exports as `daily_question.webp`. Use `--export-basename nhie` only when an existing app asset uses a legacy alias.

It creates:

```text
<workspace-root>/game-assets/chess/
|-- asset-pack.json
|-- prompt.md
|-- source-notes.md
`-- iterations/
```

## 2. Start With The Skill

Use a request like:

```text
Use $game-thumbnail-generator for Chess. The game folder is game-assets/chess. Read its mechanic source and create only the first 3:4 candidate for approval.
```

The skill will stop at each approval gate. It will not create the partner-turn icon, info-page square logo, completed-state banner, your-turn background, or any other icon-derived asset before the daily game icon is approved.

For thumbnails, read `references/kulfi-house-style.md` and `references/cdn-reference-manifest.md`. Prefer 3-5 CDN references marked `accepted`; use the bundled study sheet and curated portrait/landscape folders as offline fallbacks. Never use a rejected reference or an unrelated same-game-only reference as a house-style anchor.

For daily icons and icon-derived assets, use the CDN tables in the matching reference file and the bundled folders listed in `references/bundled-reference-assets.md` as offline fallbacks. The small derivative families remain bundled by asset type.

Before visual generation, it also runs an internet reference pass and records the search terms, source URLs, recognition cues, and inspiration takeaways in `source-notes.md`. Real-world or cultural references establish what the subject must look like; style examples guide material and composition without being copied.

## 3. Record Approval

After explicit approval, the skill should:

1. Move or copy the approved canonical file to the game-folder root.
2. Set that asset's `status` to `approved` in `asset-pack.json`.
3. Set `approved_at` to an ISO date such as `2026-08-25`.
4. Keep every rejected and replaced version in `iterations/`.

Set an optional asset to `not-required` when the project does not need it. Dependencies accept either `approved` or `not-required`.

## 4. Validate At Any Time

```bash
python3 scripts/validate_asset_pack.py /path/to/project/game-assets/chess
```

The validator checks folder placement, approval dependencies, canonical names, required formats, image dimensions, aspect ratios, and iteration naming. It uses only the Python standard library.

## 5. Preview Deployment Export

The exporter is dry-run by default:

```bash
python3 scripts/export_asset_pack.py \
  /path/to/project/game-assets/chess \
  --target /path/to/app-assets
```

Review the printed mappings, then copy with:

```bash
python3 scripts/export_asset_pack.py \
  /path/to/project/game-assets/chess \
  --target /path/to/app-assets \
  --apply
```

It exports only approved assets. Existing destination files are protected unless `--overwrite` is explicitly supplied. Deployment directories and basenames can be adjusted in `asset-pack.json` for a different app layout.

## Resume Someone Else's Work

Ask the skill to read `asset-pack.json`, `source-notes.md`, `prompt.md`, the approved root assets, and the latest relevant files in `iterations/`. The manifest shows which stage is approved and which dependency is next.
