# Game Category Asset Requirements

This file is the workspace source of truth for category-level asset requests.

When the user asks for "assets for a sync game," "assets for a live ops game," or "assets for an async game," create the complete bundle listed for that category. Follow the staged approval, validation, naming, and dependency rules in the game-thumbnail workflow; a request for the complete bundle does not bypass those gates.

Treat `daily game` and `async game` as the same category unless the user explicitly distinguishes them.

## Sync Games

Sync games can be played multiple times.

Required asset bundle:

1. 3:4 mobile catalog thumbnail.
2. 16:9 thumbnail or banner.
3. 1:1 Daily Activity tile.
4. Your-turn background without a prominent foreground icon.
5. Win, lose, and draw result icons.
6. Game-name title artwork. Keep this separate from catalog thumbnails.
7. Game video-preview prompt.

## Live Ops Games

Live Ops usually run on Saturdays. Their themes are commonly sexual or intimacy-related, but may use other event themes.

Required asset bundle:

1. Your-turn background without a prominent foreground icon.
2. Win, lose, and draw result icons.
3. Game-name title artwork. Keep this separate from catalog thumbnails.
4. Game video-preview prompt.
5. Daily game icon.
6. Partner-turn icon.
7. Info-page square logo.
8. Completed-game banner.

The user's original Live Ops list repeated the your-turn background, result icons, and title artwork. Those duplicates are normalized to one deliverable each. Do not add 3:4 thumbnails, 16:9 thumbnails, or 1:1 Daily Activity tiles to the Live Ops bundle unless the user explicitly requests them.

## Async Games

Async games are the once-per-day games.

Required asset bundle:

1. 3:4 mobile catalog thumbnail.
2. 16:9 thumbnail or banner.
3. 1:1 Daily Activity tile when required.
4. Daily game icon.
5. Partner-turn icon.
6. Info-page square logo.
7. Completed-game banner.
8. Standard your-turn background.
9. Win, lose, and draw result icons.
10. Game-name title artwork. Keep this separate from catalog thumbnails.
11. Game video-preview prompt.

## Shared Interpretation Rules

- Use the production manifest's user-facing **Game** display name for game folders, records, and user-facing reports. Keep the internal manifest key only as technical mapping metadata.
- Treat the production game manifest as the source of truth for finalization. Local folders, exports, and `FINALIZED_ASSETS.md` are working records rather than authoritative finalized-game lists.
- Sync games always require a 1:1 Daily Activity tile.
- `1:1 Daily Activity tile when required` remains conditional for Async games and any other category that uses that wording.
- The 1:1 Daily Activity tile is exempt from the quiet bottom-left composition rule used for 3:4 and 16:9 thumbnails.
- A title artwork file is allowed for in-game or campaign use, but must never be composited into catalog thumbnail artwork.
- An optional `vertical titled game banner` may be created as a separate experimental or promotional 3:4 asset when explicitly requested. It does not replace the title-free catalog thumbnail.
- For every vertical titled game banner, generate the scene and title as one unified composition and place the complete game title in the bottom section of the canvas. Keep the title fully inside crop-safe margins; never place it at the top or visual center.
- A video-preview prompt is a saved production prompt, not a generated video, unless the user explicitly requests video generation.
- The three result states are separate deliverables: win, lose, and draw.
- The no-prominent-icon your-turn treatment for Sync and Live Ops overrides the default foreground-icon composition used by the standard Async your-turn background.
- Keep every game in its own `game-assets/<game-slug>/` working folder and track stages in `asset-pack.json`.

## Live Ops Sync Clarification

For Live Ops Sync games, use the Sync asset bundle above and start with the 3:4 catalog thumbnail. The user clarified on 2026-10-01 that daily-game icons and their partner-turn, info-page, and completed-banner derivatives belong to Async/Daily games and are not needed for Live Ops Sync. This overrides the broader Live Ops list for synchronized games, including What Men Like.
