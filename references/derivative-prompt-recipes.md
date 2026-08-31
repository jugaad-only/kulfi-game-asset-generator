# Derivative Prompt Recipes

Read the recipe for the current stage only. Replace bracketed placeholders with verified game facts and name the approved source file explicitly.

## Daily Game Icon

Use only after all requested thumbnail formats are approved.

```text
Create the daily game icon for [GAME NAME] using the approved thumbnail and verified mechanic as references.

Source of truth: [APPROVED THUMBNAIL PATH]. Represent one recognizable game symbol: [SYMBOL]. Render it as one filled silhouette in one dominant [COLOR] felt color on genuine transparency. Add a subtle, evenly spaced stitched seam around the outer contour and any major internal opening, using tonal thread from the same color family. The filled symbol is the positive space and the surrounding transparent canvas is the negative space. Do not use contrasting thread, gradients, highlights, shadows, bevels, layered color regions, or illustrative interior detail.

Keep the symbol centered and crop-safe. Let the outer silhouette carry recognition, and include one broad, simple internal negative-space opening that supports recognition and balance. Minimal detail means fewer, larger forms, not intricate details made smaller. Preserve the family-defining perimeter stitching, but delete decorative embroidery, dense interior stitchwork, tiny dots, petals, beads, repeated scallops, fine lines, ornamental patterns, decorative holes, and multiple small cutouts. The icon must still work as a binary `filled felt`/`transparent` mask at 287 x 287 pixels and smaller when the stitched seam is ignored. Use tactile matte felt with visible soft fibers, irregular non-woven nap, subtly fuzzy cut edges, and no directional lighting or modeled depth. Do not include the game title, promotional copy, logo lockup, watermark, badge, or readable UI label. A mechanic-critical letter or mark is allowed only when it is part of the verified game symbol.

Before generation, review a relevant Flaticon `[SYMBOL] black fill` or `[SYMBOL] glyph` result for silhouette economy and positive/negative-space balance. Record its URL, author, style, and displayed license. Use it as reference only; do not trace, copy, download, or import it into production art unless the project deliberately satisfies its license and attribution requirements.

Name-recognition QA: hide all context and ask, "Does this really look like [GAME NAME]?" For a literal title, list the outer-silhouette cues that make the named object unmistakable and reject any candidate that reads as a different object or generic badge.
```

Save the candidate as `iterations/<game-slug>-daily-game-icon-vNN.webp`. Promote it to `<game-slug>-daily-game-icon.webp` only after explicit approval.

## Partner-Turn Icon

Use only after the daily game icon is approved.

```text
Create the partner-turn icon for [GAME NAME] from the approved daily game icon at [APPROVED DAILY ICON PATH].

Preserve the exact symbol, silhouette, and positive/negative space, but translate the felt icon into a simplified flat single-color vector mark. Use fixed shared UI chrome `#8E9DB1`; partner-turn icons do not inherit the daily icon's game-specific color. Remove felt texture, lighting, shadows, and small surface detail. Keep the silhouette crisp on a transparent background and readable at 28 x 28 SVG display size and 84 x 84 WebP export size. Clear RGB beneath fully transparent WebP pixels.

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

Use only the approved symbol's alpha silhouette; do not preserve its game-specific color or felt texture. Render it as a very subtle neutral dark-teal tonal lift over the template so the underlying vertical gradient remains visible through the symbol. A useful reference match is approximately `+8, +7, +7` RGB at full mask opacity. Do not use a flat orange, cyan, or other game-colored fill.

Enlarge the symbol until it materially fills the right half, position it on the right, and crop it intentionally beyond multiple canvas edges where possible while keeping the defining silhouette recognizable. Clip the overlay to the right half so every lossless-source pixel left of the horizontal midpoint remains identical to the bare template; minor WebP encoding differences are acceptable. A small corner badge is incorrect. Ignore the Hangman completed asset entirely when researching or judging this target.

Do not bake in a title, completion message, score, button, badge, logo, watermark, or readable UI label. Do not use a bright icon-tile treatment or detailed gameplay scene.
```

Production rule: use `scripts/compose_completed_banner.py` and tune only the symbol scale and position. Image-generation output, manual painting, arbitrary recoloring, and custom replacement compositors are ineligible for this target. Retain a lossless PNG QA source in `iterations/` even when WebP is the only deployment deliverable. Run `scripts/validate_completed_banner.py <lossless-png>` and treat any failure as a hard stop before presentation, approval, promotion, or export.

Export WebP by default. Keep the lossless PNG as a QA/source iteration; promote a canonical PNG only when the target asset set requires it.

## Your-Turn Background

Use only after the daily game icon is approved.

```text
Create the 813 x 420 your-turn background for [GAME NAME] from the approved daily game icon at [APPROVED DAILY ICON PATH].

Use a pale, low-contrast background from the approved icon's color family. Keep roughly the left 55% visually quiet for application-rendered turn UI. In the upper-right, place a small, crisp version of the approved felt icon with its exact recognizable silhouette and positive/negative space. Its visual center should sit approximately 25%-38% down the canvas; do not vertically center it. Behind it, place a much larger, very faint tonal version of the same silhouette as a cropped watermark aligned to the same upper-right cluster. The watermark must remain subordinate to the foreground icon and must not reduce UI readability.

Preserve the approved felt treatment on the small foreground icon. The watermark may be flat and tone-only, but it must not introduce another symbol or decorative illustration. Do not include a title, turn message, player name, button, badge, logo, watermark text, or readable UI label. Export an opaque WebP.

Ignore the legacy Hangman your-turn background entirely when researching or judging this target; it is a rejected outlier, not a family reference.
```

## Revision Rule

For every derivative revision, name the approved source and the exact issue to fix. Preserve all other approved identity features. Save a new `-vNN` candidate in `iterations/`; never overwrite the rejected version.
