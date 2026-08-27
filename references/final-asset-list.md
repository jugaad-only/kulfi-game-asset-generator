# Final Asset List Updates

Always update the game folder's `asset-pack.json` after explicit approval. When the project also uses a finalized-asset registry, update `<workspace-root>/FINALIZED_ASSETS.md`. If the project has no separate registry, `asset-pack.json` and the approved canonical files remain the source of truth.

## Required Entry Fields

Add or update the game in the approved list:

```markdown
- Game Name: `game-assets/game-slug/game-slug-thumbnail-3x4.png`, `game-assets/game-slug/game-slug-thumbnail-3x4.webp`
```

For 16:9 and icon-derived assets, list the approved canonical files from the same game folder.

Under `Generation Prompts`, add a compact record:

```markdown
- **Game Name:** Generated from scratch or revised from `[source path]`. Final asset uses [dominant subject/mechanic], no title/wordmark/promotional copy/logo/watermark/readable UI label, quiet bottom-left, and [asset type] crop-safe composition. Source iteration: `game-assets/<game-slug>/iterations/<versioned-file>`. Prompt record: `game-assets/<game-slug>/prompt.md`. Tool: [model/tool]. Approved date: YYYY-MM-DD.
```

## Approval Boundary

Do not add a draft to the approved list because it looks good. The user must explicitly say the asset is approved/final or ask to move/finalize it.

If the user approves one asset class but not another, list only the approved canonical file. Keep every unapproved candidate in that game's `iterations/` folder until separately approved.
