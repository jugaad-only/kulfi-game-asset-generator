# Quality Gates

Run the matching command in `candidate-validation.md` first. Use this human/visual gate only after machine QA passes, then use it again before finalizing. A candidate needs both passes before presentation.

## 3:4 Candidate Gate

- A saved `validate_candidate.py thumbnail_3x4` report passes for the exact candidate before the file is shown.
- Ratio is 3:4 portrait.
- Asset is saved in the correct draft folder with a versioned `-3x4-vNN` name.
- For puzzle, board, word, grid, route, or rules-based games, the actual mechanic was verified from a source before generation.
- For rules-based games, `source-notes.md` or `prompt.md` records the mechanic source, verified rule, what the thumbnail must show, and what it must not imply.
- No game title, wordmark, promotional copy, logo, watermark, badge, signature, or readable UI label inside the art.
- One dominant subject or one obvious gameplay action.
- Mechanic reads without title text.
- Main subject is center, upper area, or right-biased, not in the lower-left quadrant.
- Lower-left quadrant is quiet but not empty, using only tiny low-contrast background details.
- Strong silhouette and foreground/background separation.
- Dominant gameplay cluster sits near the optical center or upper-middle and does not read noticeably low.
- Foreground edges, material details, and mechanic-critical objects remain crisp at approximately 180 x 240 pixels; background blur, haze, or bloom does not spill across them.
- When a room or setting is requested, it reads as one coherent place through a few consistent spatial cues but remains secondary to the gameplay subject.
- Color identity is simple and memorable.
- Visual style matches the bundled Kulfi house-style references: chunky tactile polished 3D mobile-game illustration, toy-like game pieces, soft rounded forms, friendly lighting, clean staging, and bright controlled colors.
- Candidate was compared against the contact sheet and at least 3 relevant individual approved portrait references when those bundled files are available.
- Every comparison reference is marked `accepted` in `cdn-reference-manifest.md`; no rejected or unrelated same-game-only reference was used.
- Looks readable at small mobile catalog size beside many neighboring games.
- Puzzle/word/choice/racing/action rules are visually honest.
- User special requests were incorporated without breaking verified mechanics, folder naming, no-title rules, or lower-left quiet-zone rules.

## 16:9 Gate

- A saved `validate_candidate.py thumbnail_16x9` report passes for the exact candidate before the file is shown.
- User explicitly approved the 3:4 direction before this was made.
- It is recomposed for landscape, not blind-cropped from portrait.
- Asset is saved in the correct draft folder with a versioned `-16x9-vNN` name until final approval.
- Same subject, palette, art style, mechanic, and emotional promise as the approved 3:4.
- Candidate was compared against relevant bundled individual approved landscape references when those files are available.
- Every landscape comparison reference is marked `accepted` in `cdn-reference-manifest.md`.
- Critical action remains crop-safe.
- Same no-text/no-logo/no-watermark rules.
- Bottom-left remains quiet but not barren.

## Daily Game Icon Gate

- A saved `validate_candidate.py daily_game_icon` report passes for the exact candidate before the file is shown.
- Every thumbnail format requested for the game is explicitly approved before icon work begins.
- `source-notes.md` records the internet reference search terms, source URLs, and distilled recognition or silhouette cues. If browsing was unavailable or declined, that limitation is recorded.
- A relevant Flaticon black-fill or glyph reference was checked when available, with its URL, author, style, and displayed license recorded. It was used for silhouette study only unless reuse was deliberately licensed and attributed.
- Selected visual references were captured as clearly named screenshots in `iterations/`, and their local paths are recorded beside the source URLs. Reference screenshots are excluded from production assets and deployment exports.
- Recognition cues come from real-world, cultural, or verified gameplay references; style examples were used only as inspiration and were not copied.
- The symbol honestly represents the verified game mechanic and is recognizable without a label.
- The name-recognition QA was run with the title and source context hidden: `Does this really look like [GAME NAME]?`
- For a literal game name, the outer silhouette reads first as the named object or action rather than as a generic badge, mascot, token, or unrelated prop.
- The candidate preserves the two or three silhouette cues that make the named object distinctive.
- Both independent checks pass: the outer silhouette reads as the game subject, and one broad internal negative-space opening is clearly present.
- The icon is one filled felt silhouette in one dominant color, with a subtle tonal stitched seam following the outer contour and any major internal opening. There are no contrasting threads, gradients, highlights, shadows, bevels, layered color regions, or illustrative interior detail.
- The surrounding canvas is genuinely transparent. The filled symbol and open canvas form balanced positive and negative space at the final mobile-icon size.
- The outer silhouette carries recognition and the icon includes one broad, controlled internal negative-space opening that improves recognition or balance. It does not contain many small or decorative cutouts.
- Detail was simplified by removal, not miniaturization. The icon uses only a few large forms. Family-defining perimeter stitching is present, while decorative embroidery, dense interior stitches, tiny dots, petals, beads, fine lines, lattices, ornamental patterns, and repeated micro-shapes are absent.
- Simplification did not remove the few large functional cues needed for recognition; the icon is minimal without becoming plain, generic, or featureless.
- The icon passes the binary-mask test: reduced to one solid fill on transparency, its silhouette and identity remain clear.
- Felt grain and tonal perimeter stitching remain tactile and legible without becoming a contrasting outline or collapsing into noise.
- No title, word, wordmark, promotional copy, logo, watermark, or readable UI label appears inside the icon.
- The candidate was compared with the provided Kulfi daily game icon reference set for family consistency.
- The exact candidate receives explicit approval before it becomes the source for later derivatives.

## Partner-Turn Icon Gate

- A saved `validate_candidate.py partner_turn_icon` report passes for the exact WebP/SVG pair and approved daily-icon source before the files are shown. This includes the fixed-palette and transparent-RGB checks.
- The corresponding daily game icon is explicitly approved and finalized.
- The derivative preserves the approved symbol, silhouette, and positive/negative space while simplifying the felt source into a flat single-color vector treatment.
- Both SVG and WebP use the fixed shared UI-chrome fill `#8E9DB1`; inheriting the daily icon's game-specific color fails this gate.
- Fully transparent WebP pixels have cleared RGB values.
- Any compositional change is justified by the partner-turn UI role and does not create a new visual identity.
- It remains recognizable and uncluttered at its actual display size.
- SVG and WebP exports are visually equivalent when both formats are required.
- No title, word, wordmark, promotional copy, logo, watermark, or readable UI label appears inside the asset.
- The exact partner-turn candidate receives explicit approval before final placement.

## Info-Page Square Logo Gate

- A saved `validate_candidate.py info_page_square_logo` report passes for the exact candidate and approved daily-icon source before the file is shown.
- The corresponding daily game icon is explicitly approved and finalized; no other derivative asset is a prerequisite.
- The asset is square and exported at 1024 x 1024 WebP unless the project specifies another target.
- The derivative preserves the approved daily icon's symbol, silhouette, monochrome color family, felt material, and positive/negative space.
- The symbol is centered with generous, visually even breathing room and no unsafe edge crop.
- A pale same-family background separates cleanly from the darker or more saturated felt symbol.
- No game title, promotional copy, logo lockup, watermark, or readable UI label appears. A mechanic-critical letter or mark appears only when it belongs to the approved game symbol.
- The asset remains recognizable at its actual info-page display size.
- The exact square-logo candidate receives explicit approval before final placement.

## Completed-State Gate

- A saved `validate_candidate.py completed` report passes for the exact lossless candidate and approved daily-icon source before the file is shown.
- The corresponding daily game icon is explicitly approved and finalized; no other derivative asset is a prerequisite.
- The production candidate was created with `scripts/compose_completed_banner.py`; generative image output, manual painting, arbitrary recoloring, and substitute compositors are rejected even if visually similar.
- A lossless PNG QA source exists in `iterations/`, and `scripts/validate_completed_banner.py <lossless-png>` passes before the candidate is presented. A validator failure blocks presentation, approval, promotion, and export.
- The asset uses a 1626 x 588 canvas unless the project specifies another target; alternate resolutions preserve the same aspect ratio.
- The approved daily icon's alpha silhouette and positive/negative space remain recognizable; its game-specific color and felt texture are not carried into this target.
- The background uses the fixed shared template: a horizontally uniform dark teal vertical gradient near `#1C272C` at the top, `#0C1B1F` at mid-height, and `#03171C` at the bottom.
- The underlying gradient is identical across games and is not recolored from the approved icon. It contains no texture, grain, noise, vignette, spotlight, glow, or game-specific atmospheric variation.
- Hangman was excluded entirely from reference selection and QA.
- The symbol is a subtle neutral dark-teal tonal lift over the template, approximately matching the reference family's `+8, +7, +7` RGB lift at full mask opacity. The underlying vertical gradient remains visible through it; no flat game-colored fill appears.
- The symbol materially fills the right half, is intentionally cropped beyond multiple edges where its shape permits, and remains recognizable. Reject a small isolated corner badge.
- The overlay is clipped to the right half. The entire left half of the lossless source is pixel-identical to the bare shared template, not merely visually quiet; minor WebP encoding differences are acceptable.
- No title, completion copy, score, button, badge, logo, watermark, or readable UI label is baked into the asset.
- WebP is present for the standard set. The lossless PNG QA source is retained as an iteration; a canonical PNG is included only when required by the project or matching reference set.
- The exact completed-state candidate receives explicit approval before final placement.

## Your-Turn Background Gate

- A saved `validate_candidate.py your_turn_background` report passes for the exact candidate and approved daily-icon source before the file is shown.
- The corresponding daily game icon is explicitly approved and finalized; no other derivative asset is a prerequisite.
- The asset is an opaque 813 x 420 WebP unless the project specifies a 2x equivalent at the same aspect ratio.
- The small foreground felt icon preserves the approved symbol, silhouette, color family, material treatment, and positive/negative space.
- The small foreground icon is positioned in the upper-right, with its visual center approximately 25%-38% down the canvas. A vertically centered or lower-right foreground icon fails this gate.
- A much larger version of the same silhouette appears as a very faint, low-contrast, intentionally cropped watermark behind the foreground icon.
- The foreground icon and watermark remain on the right; roughly the left 55% stays visually quiet for application-rendered turn UI.
- The background is pale and belongs to the approved icon's color family. It does not compete with the foreground icon or reduce UI readability.
- Hangman was excluded entirely from your-turn reference selection and QA.
- No title, turn message, player name, button, badge, logo, watermark text, or readable UI label is baked into the asset.
- The exact your-turn background candidate receives explicit approval before final placement.

## Folder And Naming Gate

- No project-bound generated image remains only in `$CODEX_HOME/generated_images`, `/tmp`, Downloads, or chat-only context.
- All files for one game live under `game-assets/<game-slug>/`.
- `asset-pack.json` exists at the game-folder root and accurately records each stage as `pending`, `approved`, or `not-required`.
- Approved assets live at the game-folder root with canonical, unversioned filenames.
- Every candidate, rejected version, contact sheet, and replaced final lives in the game's single `iterations/` subfolder with an asset-type and `-vNN` suffix.
- `prompt.md` and `source-notes.md` live at the game-folder root.
- Type-based folders are used only for requested deployment exports.
- Replaced finals move into `iterations/` before the approved root file is replaced.
- `scripts/validate_asset_pack.py` passes before final handoff or deployment export.

## Fast Rejection Triggers

Reject or revise when any of these appear:

- Title or logo inside the image.
- Fake badge, store icon, watermark, promo text, or readable app UI label.
- Too many focal subjects.
- Main action hidden in the bottom-left.
- Board state or implied action contradicts actual game rules.
- Prompt uses an assumed or invented mechanic for a rules-based game.
- Rules-based candidate has no recorded mechanic verification source.
- Cinematic poster art that no longer feels like a mobile catalog tile.
- Dark comic-book, halftone, risograph, noir, gritty thriller, erotic romance cover, or product-catalog styling that does not match the approved Kulfi thumbnail sheet.
- Dark, cluttered, over-detailed, or realistic stock-like image that fails small-size readability.
- Photorealistic hands, realistic adult props, satin/candle boudoir mood, or moody lifestyle staging that overpowers playful game-piece readability.
- Choice-game thumbnails that show two static product cards without a lively game interaction or playful tabletop context.
- Foreground became softer or less accurate after a background/scene edit.
- Focal cluster sits too low or the environment occupies more visual authority than the mechanic.
- Requested room reads as an abstract stage, incoherent prop collage, or unintended bathroom rather than the requested setting.
- Daily icon was started before all requested game thumbnails were approved.
- A daily icon was generated without a recorded internet reference pass or a documented browsing exception.
- A relevant Flaticon black-fill or glyph reference was not checked or recorded when one was available.
- A reference screenshot is unlabeled, stored as a canonical root asset, missing its source metadata, or mistaken for production art.
- A candidate copies the distinctive artwork, branding, or proprietary character design of an internet reference instead of distilling common category cues.
- A daily icon uses multiple shades, tonal modeling, gradients, highlights, shadows, outlines, colored interior layers, or illustrative detail instead of one filled felt silhouette.
- A daily icon relies on facial rendering, many small pieces, unnecessary internal cutouts, or surface decoration that fails the binary-mask test.
- A daily icon is intricate, or preserves reference complexity by shrinking details instead of removing them.
- A daily icon is so plain or over-simplified that its subject-specific cords, knots, ends, openings, or other functional identity cues disappear.
- A daily icon is visually polished but fails the name-recognition QA or reads more strongly as another object.
- A daily icon passes the felt-style check but fails either subject-silhouette recognition or the internal-negative-space requirement.
- Partner-turn or another icon-derived asset was started before the daily game icon was approved.
- An icon derivative changes the approved symbol, palette, felt treatment, or positive/negative space without a target-specific reason.
- An info-page square logo is off-center, tightly cropped, uses a mismatched background hue, or introduces an unapproved symbol.
- A completed-state asset is bright, inherits the daily icon's game-specific color, uses a flat opaque symbol fill, centers the symbol, changes any left-half template pixel, presents a small corner badge, crops the symbol into an unrecognizable shape, lacks a lossless QA source, bypasses the deterministic compositor, or fails the completed-banner validator.
- A completed-state background is recolored per game, varies horizontally, adds texture or lighting effects, or uses the Hangman asset as a reference.
- A your-turn background fills the quiet left UI area, omits the faint oversized watermark, vertically centers the crisp icon instead of placing it upper-right, moves it away from the right, uses a dark completed-state treatment, introduces a symbol not present in the approved daily icon, or uses the rejected Hangman card as a reference.
