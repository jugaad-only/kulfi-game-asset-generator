---
name: game-thumbnail-generator
description: Generate, revise, approve, and organize Kulfi mobile game thumbnails, daily game icons, partner-turn icons, your-turn backgrounds, and dependent assets through staged approval gates.
---

# Game Thumbnail Generator

Use this skill when the user asks to generate, revise, review, approve, finalize, document, or organize mobile game thumbnails or their dependent daily-game icon assets for the Kulfi catalog.

## Core Contract

- Generate the primary asset as a **3:4 portrait mobile game tile first**.
- Do **not** generate or finalize the 16:9 version until the user explicitly approves the 3:4 direction.
- After approval, create the 16:9 asset as an intentional recomposition of the same subject, palette, art style, mechanic, and emotional promise. Do not blindly crop the 3:4 image.
- Do **not** create a `daily_game_icon` until every thumbnail format requested for that game has been explicitly approved.
- Do **not** create `daily_games_partner_turn_icons`, `daily_games_info_page_square_logos`, `daily_games_completed`, `daily_game_your_turn_bg`, or other icon-derived assets until the corresponding `daily_game_icon` has been explicitly approved.
- Treat the approved `daily_game_icon` as the source of truth for the symbol, silhouette, monochrome color family, and positive/negative space used by later icon derivatives. Preserve or simplify the felt material according to the target-specific reference.
- Every `daily_game_icon` must follow the Felt Icon Rules below.
- Run a name-recognition QA before presenting any daily icon: hide the title and ask, `Does this really look like [GAME NAME]?` For a literal object or action name, reject any silhouette that reads more strongly as a generic badge, mascot, unrelated prop, or another object.
- Before visual generation, run a focused internet reference pass unless the user explicitly opts out or browsing is unavailable. Use real-world or category references to verify recognition cues and separate visual references for material or composition inspiration. Record the source URLs and distilled takeaways in `source-notes.md`; never copy one reference's exact artwork, branding, or proprietary character design.
- Keep all working and approved assets for one game under `game-assets/<game-slug>/`. Approved files live at the game-folder root; every draft, rejected version, contact sheet, and replaced final lives in that game's single `iterations/` subfolder.
- Type-based folders are deployment exports only. Generate and review from the game-wise working folder so all references for one game remain together.
- Treat `asset-pack.json` as the portable stage and approval record. Change an asset to `approved` only after explicit user approval; use `not-required` only when the project does not need that asset.
- If the user asks for both ratios in one request, still produce or present the 3:4 candidate first and wait for explicit approval before making the 16:9 derivative.
- Do not move files into final folders or add them to `FINALIZED_ASSETS.md` until the user has explicitly approved that exact asset.
- Every generated, revised, approved, or archived asset must be properly named and placed in the correct folder before the task is considered complete.
- Never leave project-bound generated images only in `$CODEX_HOME/generated_images`, downloads, or a temporary location. Copy them into the workspace folder structure with canonical names.
- For an existing game with incomplete details, ask whether there is an existing repo, source folder, gameplay spec, screenshot, Figma frame, or other source of truth to inspect before guessing.
- Non-negotiable stop condition: for puzzle, board, word, route, grid, or any rules-based game, do not generate, revise, present, or approve a mechanic-accurate candidate until the actual rule system has been verified from a concrete source and recorded in the prompt/source notes.

## Felt Icon Rules

Apply these rules to every `daily_game_icon`. Later icon-derived assets must preserve the approved symbol and silhouette while following their own target-specific material treatment.

- Use one dominant **filled felt silhouette**, not a miniature illustration or layered emblem.
- Use **exactly one visible color** across the entire filled symbol. No second shade or value is allowed.
- The felt texture must be subtle, matte, and uniform. Texture may show fibers or soft cut edges, but it must not create highlights, shadows, depth modeling, seams, or a second color region.
- Use a **genuinely transparent canvas** around the symbol. Never bake in a checkerboard, white square, colored tile, glow, drop shadow, border, or background plate.
- Treat the filled symbol as positive space and the transparent canvas as negative space. Keep balanced breathing room around the full silhouette and do not crop recognition-critical edges.
- Make the **outer contour** carry recognition, while including one controlled area of internal negative space. Use one broad, simple opening that supports recognition and balance; decorative holes, many small cutouts, and lace-like detail are not allowed.
- **Minimal detail means fewer details, not smaller details.** Use only a few large, broad forms. Remove a feature completely instead of shrinking it into a tiny dot, petal, stitch, bead, line, or ornament.
- Minimal does not mean featureless. Preserve the small set of large functional cues that makes the object unmistakable, such as a rakhi's medallion, tying cords, broad knots, and tasselled ends. Reject an over-simplified shape that becomes generic or loses the subject.
- Do not use intricate rosettes, mandalas, lattices, dotted borders, repeated micro-shapes, fine linework, or dense scalloping. A reference may contain these, but the felt icon must simplify them into the outer silhouette plus one broad internal opening.
- Remove faces, pupils, mouths, highlights, beads, embroidery, stitching, outlines, nested shapes, and surface decoration unless the verified game symbol would be unrecognizable without one essential feature. Any exception must still survive the one-color binary-mask test.
- Do not include the game title, letters used as labels, promotional copy, logo lockups, watermarks, or readable UI text. A mark or letter is allowed only when it is an indispensable part of the verified game symbol.
- Check the icon as a two-state mask: **filled felt or transparent**. It must remain balanced and recognizable at the actual mobile display size and when reduced further.
- Check semantic recognition with the title and context hidden: `Does this really look like [GAME NAME]?` Reject a polished icon that first reads as a badge, mascot, token, bell, plate, unrelated prop, or another object.
- Treat silhouette recognition and internal negative space as two independent mandatory gates. The icon fails if either the outer shape does not read as the game subject or the filled silhouette lacks its one broad internal opening. Matching the cyan felt treatment alone is never sufficient.
- Use internet references to learn the real object's or action's defining silhouette and use Kulfi references to match the family treatment. Also search Flaticon for `[SUBJECT] black fill` or `[SUBJECT] glyph` references and study their positive/negative-space economy. Record the URL, author, style, and displayed license. Treat Flaticon assets as references only unless the project deliberately satisfies the applicable license and attribution requirements. Distill common cues; do not copy a specific product, artist, brand, or proprietary character.
- Capture screenshots of the selected web and Flaticon references when they materially guide the icon. Save them as versioned reference files in the game's `iterations/` folder, record their paths in `source-notes.md`, and never promote or export them as production assets. If a reference page blocks capture, screenshot the directly displayed image only and retain the original page URL and licensing metadata in the notes.

## Hard Thumbnail Rules

- The target is a mobile app game catalog, not desktop, web hover, app-store promo, or Steam cover art.
- Do not place the game name, title, title wordmark, promotional copy, store logo, watermark, signature, or readable UI label inside the artwork.
- The app displays the game name separately below the thumbnail.
- Use one dominant subject, object, character, puzzle piece, vehicle, or gameplay action.
- Keep the bottom-left area visually quiet but not empty. Use only small, low-contrast background details there, such as stitching, fabric folds, loose puzzle pieces, paper shapes, crumbs, tiny leaves, or subtle material texture.
- Do not place the primary subject, key gameplay interaction, readable text, or dense prop cluster in the bottom-left area.
- Bias the focal point toward the center, upper area, or right side.
- Ensure strong foreground/background separation, a readable silhouette, and one dominant color identity.
- Preserve mechanic honesty: puzzle, word, choice, racing, action, or social mechanics must not be visually misleading.
- For puzzle, board, word, route, grid, or rules-based games, do not generate from a guessed mechanic. Verify the actual rule system from source files, screenshots, gameplay notes, Figma, or user-provided explanation before writing the prompt. If no source is available, ask for one and stop.
- User special requests, such as specific words, colors, props, or slang, may only be incorporated when they still obey the verified game rules, no-title/no-promo constraint, and quiet lower-left composition rule. For word/puzzle games, requested words must be valid board content, not decorative copy.

## Revision And Scene Discipline

- Treat the sharpest mechanic-correct candidate as the authoritative foreground baseline. When a later background or atmosphere pass softens, simplifies, or distorts the gameplay subject, restart from that sharp baseline instead of compounding edits on the degraded image.
- When the user requests a room, setting, or environmental scene, use a few coherent spatial cues that make the place recognizable, such as wall structure, window/curtains, distant furniture, and one practical light. Match the game's art medium; do not default to an abstract stage, literal bathroom, or photorealistic stock interior unless requested.
- Keep environmental depth of field, haze, bloom, and light spill behind the gameplay subject. The focal object, card, board, character, and any legal gameplay separator must remain crisp, high-contrast, and more detailed than the setting.
- Check vertical balance at shelf size. Keep the dominant cluster near the optical center or upper-middle; reject a composition that sits noticeably low, gives the room more authority than the mechanic, or leaves a large accidental dead zone.
- A request to regenerate means create a new versioned candidate from the best source baseline, preserve the rejected version for traceability, and record why it was rejected. Do not overwrite or silently promote it.

## Project Files

At the active workspace root, read these project files before generating or finalizing when they are present:

- `game-tile-thumbnail-brief.md`
- `MISTAKES_AND_LEARNINGS.md`
- `FINALIZED_ASSETS.md`

These files contain project-local context and are not required for the skill package to be shared. If any file is missing, continue with the rules and bundled references in this skill and note the missing file.

## Portable House Style

Before writing any thumbnail prompt or judging any thumbnail candidate, read [references/kulfi-house-style.md](references/kulfi-house-style.md) and [references/cdn-reference-manifest.md](references/cdn-reference-manifest.md). Use the exact house-style phrase and negative style guardrail unless the user explicitly approves a different art direction. The skill package includes a thumbnail study sheet and a curated offline fallback. Prefer accepted CDN references when available; never use references marked `same-game-only` for unrelated games or any reference marked `rejected`.

For any asset stage that uses visual family references, read [references/bundled-reference-assets.md](references/bundled-reference-assets.md) to choose the bundled reference folder for that asset type.

## Colleague Entry Point

For a new game or a handoff between colleagues, read [references/colleague-quick-start.md](references/colleague-quick-start.md). Use `scripts/init_asset_pack.py` to create the game folder and portable manifest instead of assembling the structure manually.

## Staged Workflow And References

Complete stages 1-3 in order. After the `daily_game_icon` is approved, the partner-turn icon, info-page square logo, completed-state asset, and your-turn background are sibling derivative branches: create them in any order or independently. Approval of one derivative does not imply approval of another.

### 1. Verify The Game

1. Gather the game's real mechanic, palette, UI, assets, and emotional promise from local files, screenshots, Figma, or user-provided references. Use `game-tile-thumbnail-brief.md` for workspace-wide art direction when that project file is present.
2. Classify whether the game is rules-based. Puzzle, board, word, route, grid, logic, racing-path, and choice-rule games are rules-based.
3. For rules-based games, record a `Mechanic verification` note before generation: source path/URL/screenshot/Figma node/user explanation, what rule was verified, and what the thumbnail must not imply. If this cannot be recorded, stop and ask for a mechanic source.
4. Search the internet for relevant real-world objects, cultural forms, gameplay genres, visual materials, and comparable icon silhouettes. Include a Flaticon search for a black-fill or glyph treatment when a relevant result exists. Prefer direct, credible, and culturally grounded sources for factual recognition; use design examples only as inspiration. Capture the selected visual references into the game's `iterations/` folder. Record URLs, local screenshot paths, search terms, author/style/license information for icon-library references, and the cues to preserve or avoid in `source-notes.md`. Internet references do not override the verified game mechanic or user-provided source of truth.
5. Read [references/kulfi-house-style.md](references/kulfi-house-style.md), then [references/prompt-recipes.md](references/prompt-recipes.md), before writing the generation prompt. Read [references/folder-structure.md](references/folder-structure.md) before creating or naming files.
6. Create or reuse the game pack before generation. Prefer `python3 <skill-folder>/scripts/init_asset_pack.py` so `game-assets/<game-slug>/`, `iterations/`, `asset-pack.json`, `prompt.md`, and `source-notes.md` are created consistently.

### 2. Create And Finalize Game Thumbnails

1. Generate the 3:4 portrait thumbnail first, using [references/prompt-recipes.md](references/prompt-recipes.md).
2. Review it at full size and approximately 180 x 240 using the 3:4 section of [references/quality-gates.md](references/quality-gates.md), then request explicit user approval.
3. Only after 3:4 approval, create each requested landscape or alternate-ratio thumbnail as an intentional recomposition. Use the relevant section of [references/quality-gates.md](references/quality-gates.md).
4. Finalize only formats the user explicitly approves. Use [references/folder-structure.md](references/folder-structure.md) for placement and naming, update the matching `asset-pack.json` status and approval date, and use [references/final-asset-list.md](references/final-asset-list.md) when the project keeps a separate registry.
5. Do not start the daily icon stage until all thumbnail formats requested for the game are final.

### 3. Create And Finalize `daily_game_icons`

1. Read [references/bundled-reference-assets.md](references/bundled-reference-assets.md), [references/daily-game-icon-references.md](references/daily-game-icon-references.md), and the Daily Game Icon recipe in [references/derivative-prompt-recipes.md](references/derivative-prompt-recipes.md) before designing or generating a daily icon.
2. Review the recorded internet references before choosing the symbol. For a literal name, use real examples to identify the object's defining outer silhouette rather than relying on generated drafts or memory. Review a relevant Flaticon black-fill or glyph result for economical positive/negative space, but do not copy or import it as production art. Use style references only to guide felt texture, proportions, and visual simplicity.
3. Use the approved thumbnail and verified mechanic to choose one recognizable game symbol. Render it as one filled shape in one flat felt color on genuine transparency. Let the outer silhouette carry recognition; use an interior cutout only when the symbol would otherwise become ambiguous. The icon must still work as a two-state binary mask at small size.
4. Run the name-recognition QA from [references/daily-game-icon-references.md](references/daily-game-icon-references.md). For a literal title, an unfamiliar viewer should be able to identify the named object or action from the silhouette without seeing the title.
5. Review with the Daily Game Icon Gate in [references/quality-gates.md](references/quality-gates.md), save the candidate using [references/folder-structure.md](references/folder-structure.md), and request explicit user approval.
6. Do not start partner-turn or other icon-dependent assets until the exact daily icon is approved and finalized.

### 4A. Create `daily_games_partner_turn_icons`

1. Read [references/bundled-reference-assets.md](references/bundled-reference-assets.md), [references/partner-turn-icon-references.md](references/partner-turn-icon-references.md), and the Partner-Turn Icon recipe in [references/derivative-prompt-recipes.md](references/derivative-prompt-recipes.md) before creating the partner-turn derivative.
2. Use the approved daily icon as the source of truth. Preserve its symbol, silhouette, monochrome palette, and positive/negative space while simplifying it into the flat vector treatment used by this target.
3. Review with the Partner-Turn Icon Gate in [references/quality-gates.md](references/quality-gates.md). Export matching SVG and WebP versions when the asset set requires both, then request explicit user approval before finalizing.

### 4B. Create `daily_games_info_page_square_logos`

1. Start when the corresponding `daily_game_icon` is explicitly approved. This branch does not depend on the partner-turn icon or completed-state asset.
2. Read [references/bundled-reference-assets.md](references/bundled-reference-assets.md), [references/info-page-square-logo-references.md](references/info-page-square-logo-references.md), and the Info-Page Square Logo recipe in [references/derivative-prompt-recipes.md](references/derivative-prompt-recipes.md) before creating the square-logo derivative.
3. Use the approved daily icon as the source of truth. Recompose its symbol on a 1:1 canvas with a pale background from the same monochrome color family, centered visual balance, and generous crop-safe breathing room.
4. Review with the Info-Page Square Logo Gate in [references/quality-gates.md](references/quality-gates.md). Export a 1024 x 1024 WebP unless the project specifies another target, then request explicit user approval before finalizing.

### 4C. Create `daily_games_completed`

1. Start when the corresponding `daily_game_icon` is explicitly approved. This branch does not depend on the partner-turn icon or info-page square logo.
2. Read [references/bundled-reference-assets.md](references/bundled-reference-assets.md), [references/completed-state-references.md](references/completed-state-references.md), and the Completed-State Banner recipe in [references/derivative-prompt-recipes.md](references/derivative-prompt-recipes.md) before creating the completed-state derivative. Ignore the Hangman completed asset entirely; it is not a valid style, color, layout, or background reference.
3. Use the approved daily icon's silhouette as the source of truth. Composite it over the fixed shared completed-state background template: a horizontally uniform dark teal vertical gradient from approximately `#1C272C` at the top through `#0C1B1F` at mid-height to `#03171C` at the bottom. Enlarge the symbol on the right and crop it intentionally while leaving the left side as untouched background for completion UI.
4. Review with the Completed-State Gate in [references/quality-gates.md](references/quality-gates.md). Export a 1626 x 588 WebP unless the project specifies another target; add a matching PNG only where the asset set requires it. Request explicit user approval before finalizing.

### 4D. Create `daily_game_your_turn_bg`

1. Start when the corresponding `daily_game_icon` is explicitly approved. This branch does not depend on the partner-turn icon, info-page square logo, or completed-state asset.
2. Read [references/bundled-reference-assets.md](references/bundled-reference-assets.md), [references/your-turn-background-references.md](references/your-turn-background-references.md), and the Your-Turn Background recipe in [references/derivative-prompt-recipes.md](references/derivative-prompt-recipes.md) before creating the derivative.
3. Use the approved daily icon as the source of truth. Place a small, crisp felt icon on the right over a pale same-family background, with a much larger low-contrast version of the same silhouette acting as a cropped watermark behind it. Keep the left side quiet for application-rendered turn UI.
4. Review with the Your-Turn Background Gate in [references/quality-gates.md](references/quality-gates.md). Export an opaque 813 x 420 WebP unless the project specifies a 2x equivalent, then request explicit user approval before finalizing.

### 5. Create Remaining Icon-Dependent Assets

1. Start only after the corresponding `daily_game_icon` is final.
2. Use the approved daily icon as the primary visual reference and the approved partner-turn icon as a secondary implementation reference when relevant.
3. Obtain or inspect a concrete reference for each new target asset's dimensions, format, background behavior, and UI role before generating it. Do not invent a target specification from the game thumbnail alone.
4. Preserve recognition across derivatives and explicitly approve each new asset class before final placement.

## Validate And Export

- Run `python3 <skill-folder>/scripts/validate_asset_pack.py <game-folder>` before asking for final handoff or deployment export.
- On request, run `python3 <skill-folder>/scripts/export_asset_pack.py <game-folder> --target <deployment-root>` first as a dry run. Add `--apply` only after the printed mappings are accepted.
- The exporter copies approved game-wise sources into type-based deployment directories and never changes the working source files.

## Testing The Skill

For dry-run testing across existing games, read [references/current-game-test-cases.md](references/current-game-test-cases.md) and run:

```bash
cd <skill-folder>
python3 scripts/smoke_test_thumbnail_skill.py
```

The smoke test checks prompt and workflow invariants only. It does not replace visual review or user approval.
