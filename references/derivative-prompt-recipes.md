# Derivative Prompt Recipes

Read the recipe for the current stage only. Replace bracketed placeholders with verified game facts and name the approved source file explicitly.

## Daily Game Icon

Use only after all requested thumbnail formats are approved.

```text
Create the daily game icon for [GAME NAME] using the approved thumbnail and verified mechanic as references.

Source of truth: [APPROVED THUMBNAIL PATH]. Represent one recognizable game symbol: [SYMBOL]. Render it as one filled silhouette in exactly one flat [COLOR] felt color on genuine transparency. The filled symbol is the positive space and the surrounding transparent canvas is the negative space. Do not use lighter/darker shades, gradients, highlights, shadows, outlines, layered color regions, or illustrative interior detail.

Keep the symbol centered and crop-safe. Let the outer silhouette carry recognition, and include one broad, simple internal negative-space opening that supports recognition and balance. Minimal detail means fewer, larger forms, not intricate details made smaller. Delete tiny dots, petals, stitches, beads, repeated scallops, fine lines, ornamental patterns, decorative holes, and multiple small cutouts. The icon must still work as a binary `filled felt`/`transparent` mask at 287 x 287 pixels and smaller. Felt grain is the only surface treatment and must not read as another shade. Do not include the game title, promotional copy, logo lockup, watermark, badge, or readable UI label. A mechanic-critical letter or mark is allowed only when it is part of the verified game symbol.

Before generation, review a relevant Flaticon `[SYMBOL] black fill` or `[SYMBOL] glyph` result for silhouette economy and positive/negative-space balance. Record its URL, author, style, and displayed license. Use it as reference only; do not trace, copy, download, or import it into production art unless the project deliberately satisfies its license and attribution requirements.

Name-recognition QA: hide all context and ask, "Does this really look like [GAME NAME]?" For a literal title, list the outer-silhouette cues that make the named object unmistakable and reject any candidate that reads as a different object or generic badge.
```

Save the candidate as `iterations/<game-slug>-daily-game-icon-vNN.webp`. Promote it to `<game-slug>-daily-game-icon.webp` only after explicit approval.

## Partner-Turn Icon

Use only after the daily game icon is approved.

```text
Create the partner-turn icon for [GAME NAME] from the approved daily game icon at [APPROVED DAILY ICON PATH].

Preserve the exact symbol, silhouette, and positive/negative space, but translate the felt icon into a simplified flat single-color vector mark. Use the same monochrome color family in a muted partner-turn tone. Remove felt texture, lighting, shadows, and small surface detail. Keep the silhouette crisp on a transparent background and readable at 28 x 28 SVG display size and 84 x 84 WebP export size.

Do not introduce a new symbol, title, wordmark, promotional copy, badge, watermark, or readable UI label.
```

Produce visually equivalent SVG and WebP candidates with the same version number.

## Info-Page Square Logo

Use only after the daily game icon is approved.

```text
Create the 1024 x 1024 info-page square logo for [GAME NAME] from the approved daily game icon at [APPROVED DAILY ICON PATH].

Preserve the approved symbol, felt material, monochrome color family, silhouette, and positive/negative space. Center the felt symbol on a pale background from the same color family. Keep the symbol darker or more saturated than the background and preserve generous, visually even crop-safe breathing room.

Do not include a game title, promotional copy, logo lockup, watermark, badge, or readable UI label. A mechanic-critical letter or mark is allowed only when it belongs to the approved symbol.
```

## Completed-State Banner

Use only after the daily game icon is approved.

```text
Create the 1626 x 588 completed-state banner for [GAME NAME] from the approved daily game icon at [APPROVED DAILY ICON PATH].

Composite the approved symbol over the fixed shared completed-state background template. The background is a horizontally uniform dark teal vertical gradient, approximately `#1C272C` at the top, `#0C1B1F` at mid-height, and `#03171C` at the bottom. It is identical across games and must not be recolored from the icon palette. Do not add texture, noise, vignette, spotlight, glow, or generated atmospheric variation.

Translate the approved symbol into a subdued flat tonal overlay. Enlarge it, position it on the right, and crop it intentionally beyond the top, right, or bottom edge while keeping it recognizable. Leave the left side as untouched background for completion UI rendered by the application. Ignore the Hangman completed asset entirely when researching or judging this target.

Do not bake in a title, completion message, score, button, badge, logo, watermark, or readable UI label. Do not use a bright icon-tile treatment or detailed gameplay scene.
```

Export WebP by default and PNG only when the target asset set requires it.

## Your-Turn Background

Use only after the daily game icon is approved.

```text
Create the 813 x 420 your-turn background for [GAME NAME] from the approved daily game icon at [APPROVED DAILY ICON PATH].

Use a pale, low-contrast background from the approved icon's color family. Keep roughly the left 55% visually quiet for application-rendered turn UI. On the right, place a small, crisp version of the approved felt icon with its exact recognizable silhouette and positive/negative space. Behind it, place a much larger, very faint tonal version of the same silhouette as a cropped watermark. The watermark must remain subordinate to the foreground icon and must not reduce UI readability.

Preserve the approved felt treatment on the small foreground icon. The watermark may be flat and tone-only, but it must not introduce another symbol or decorative illustration. Do not include a title, turn message, player name, button, badge, logo, watermark text, or readable UI label. Export an opaque WebP.
```

## Revision Rule

For every derivative revision, name the approved source and the exact issue to fix. Preserve all other approved identity features. Save a new `-vNN` candidate in `iterations/`; never overwrite the rejected version.
