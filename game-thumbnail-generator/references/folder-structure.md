# Folder Structure

Use this game-wise working structure inside the active project root, represented below as `<workspace-root>`.

All references and deliverables for one game stay together. A task is incomplete until every project-bound generated file has been copied out of the generation/download location and placed in that game's folder with a canonical or versioned name.

## Canonical Game Folder

```text
<workspace-root>/game-assets/<game-slug>/
|-- <game-slug>-thumbnail-3x4.png
|-- <game-slug>-thumbnail-3x4.webp
|-- <game-slug>-thumbnail-16x9.webp
|-- <game-slug>-daily-game-icon.webp
|-- <game-slug>-partner-turn-icon.svg
|-- <game-slug>-partner-turn-icon.webp
|-- <game-slug>-info-page-square-logo.webp
|-- <game-slug>-completed.webp
|-- <game-slug>-completed.png             # only when required
|-- <game-slug>-your-turn-bg.webp
|-- asset-pack.json
|-- prompt.md
|-- source-notes.md
`-- iterations/
    |-- <game-slug>-thumbnail-3x4-v01.png
    |-- <game-slug>-thumbnail-3x4-v01.webp
    |-- <game-slug>-thumbnail-16x9-v01.webp
    |-- <game-slug>-daily-game-icon-v01.webp
    |-- <game-slug>-reference-flaticon-<subject>-v01.png
    |-- <game-slug>-reference-web-<subject>-v01.png
    |-- <game-slug>-partner-turn-icon-v01.webp
    |-- <game-slug>-info-page-square-logo-v01.webp
    |-- <game-slug>-completed-v01.webp
    `-- <game-slug>-your-turn-bg-v01.webp
```

Only explicitly approved assets belong at the game-folder root. A game folder may contain fewer approved files while later stages are still pending.

## Single Iterations Folder

- Use exactly one `<workspace-root>/game-assets/<game-slug>/iterations/` folder for all candidates, experiments, reference screenshots, contact sheets, rejected versions, and replaced finals for that game.
- Do not create separate draft trees by asset type or ratio.
- Include the asset type and `-vNN` in every candidate filename.
- Name web reference captures `<game-slug>-reference-<source>-<subject>-vNN.png`. Keep the original page URL, creator, style, license, and local screenshot path in `source-notes.md`.
- Reference screenshots are research-only files. Never promote them to the game-folder root or copy them into deployment exports.
- When replacing an approved file, move the previous final into `iterations/` with `-replaced-YYYY-MM-DD` before placing the newly approved file at the root.
- Keep rejected versions for traceability; do not overwrite them.

## Records

- Keep `asset-pack.json` at the game-folder root as the portable stage, dependency, filename, constraint, and export record.
- Keep `prompt.md` and `source-notes.md` at the game-folder root so they apply to the complete asset family.
- For rules-based games, `source-notes.md` is required before generation and must include mechanic verification.
- Record stage-specific prompts and revision history in `prompt.md`; do not create separate prompt files scattered across asset-type folders.

## Deployment Export

Type-based folders such as `daily_games_icon/` or `daily_games_completed/` are deployment destinations, not generation workspaces. When an upload/export is requested, copy the approved canonical files from `<workspace-root>/game-assets/<game-slug>/` into the required type-based destination without moving or renaming the working source files.

## Naming And Approval

- Use one lowercase game slug consistently.
- Use hyphens in the game-wise folder slug. Deployment basenames default to the same identifier with underscores and may be overridden in `asset-pack.json` for a legacy app alias.
- Approved files have no version suffix and use the canonical names shown above.
- Iterations always include the asset type and `-vNN`.
- Do not overwrite or promote an asset without explicit user approval.
- Do not leave generated assets only in `$CODEX_HOME/generated_images`, `/tmp`, Downloads, or chat attachments.
- Existing legacy folders do not need to be migrated unless the user explicitly requests it. Use this structure for new work.

## Handoff Check

Before finishing, run `scripts/validate_asset_pack.py` and report the exact paths for approved files, pending iterations, replaced finals, `asset-pack.json`, `prompt.md`, and `source-notes.md`.
