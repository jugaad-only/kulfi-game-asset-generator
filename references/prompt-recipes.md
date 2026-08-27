# Prompt Recipes

Use these recipes to write prompts for actual generation. Prefer game-specific facts over generic adjectives.

## Mechanic Source Required

Before prompting a puzzle, board, word, grid, route, or rules-based game, identify the actual gameplay rule source. Use one or more of:

- existing repo or source folder
- game source files or design docs
- screenshots or recorded gameplay
- Figma gameplay frames
- existing approved final only when it clearly encodes a known-correct rule
- user-provided rule explanation

For an existing game, if the user has not provided enough detail and no source is already known, ask: "Is there an existing repo, source folder, gameplay spec, screenshot, or Figma frame I should refer to?" Do this before writing a mechanic-accurate prompt.

If the real rule cannot be verified, STOP. Do not generate, revise, present, or approve a mechanic-accurate thumbnail candidate. Ask the user for a rule source. Only create a style study if the user explicitly asks for a style study, and label it as not mechanic-accurate.

Record the verification in `source-notes.md` or `prompt.md` before generation:

```text
Mechanic verification:
- Source: [file path / Figma node / screenshot / user explanation]
- Verified rule: [specific board/path/word/choice/racing logic]
- Thumbnail must show: [rule-accurate visual action]
- Thumbnail must avoid implying: [common wrong mechanic]
```

## 3:4 First Candidate

Read `kulfi-house-style.md` and `cdn-reference-manifest.md` first. Start from `standalone-prompt.md`, then add:

- The bundled approved reference sheet: `assets/style-references/kulfi-approved-thumbnail-study-sheet.png`.
- 3-5 individual Kulfi portrait references marked `accepted`, chosen for similar mechanic, subject type, or mood. Use CDN links when available and the curated bundled files as fallback.
- For 16:9 work after approval, use 3-5 landscape references marked `accepted` in addition to the approved 3:4 source.
- Never use a `same-game-only` reference for an unrelated game and never use a `rejected` reference.
- Additional project-local approved Kulfi thumbnail references when available.
- The exact Kulfi house-style phrase and negative style guardrail from `kulfi-house-style.md`.
- The real game mechanic in one plain sentence.
- The source used to verify that mechanic.
- The true color/material world from the game, not an invented genre skin.
- One sentence describing the intended focal subject and where it sits in the crop.
- One sentence describing what belongs in the lower-left quiet zone.
- For board, card, or grid games, explicitly keep the board/card/grid out of the lower-left quadrant rather than only saying "bottom-left quiet."
- If the user requests specific words, phrases, slang, colors, or props, translate the request into legal gameplay content or small secondary props. Do not let the request become title text, promo copy, decorative labels, or a rule-breaking board state.

Avoid asking for multiple competing subjects. If the game has many mechanics, choose the one that best sells the catalog tile.

For cheeky, romantic, horror-adjacent, or adult-coded game topics, keep the treatment inside Kulfi's playful mobile catalog style. Translate props into simplified toy-like game pieces, cards, tokens, plush objects, or tactile tabletop elements. Do not let the subject pull the artwork into noir, gritty comic art, thriller key art, erotic romance cover styling, or product-catalog realism.

## 16:9 After Approval

Use this only after explicit user approval of the 3:4 direction:

```text
Create a 16:9 landscape thumbnail asset for [GAME NAME] based on the approved 3:4 direction.

Preserve the same dominant subject, gameplay mechanic, palette, lighting, art style, and emotional promise. Recompose for landscape intentionally: add horizontal breathing room, keep the main action crop-safe, maintain clear foreground/background separation, and avoid simply stretching or blind-cropping the portrait image.

No game title, wordmark, readable UI label, logo, watermark, badge, promo copy, border, device frame, or store badge inside the artwork. Keep the bottom-left visually quiet but not empty with only small low-contrast background details.
```

## Revision Prompts

Keep revisions narrow. Name the specific approved candidate or file, then state the correction:

```text
Revise the attached thumbnail while preserving the approved subject, palette, lighting, and 3:4 composition. Fix only this issue: [ISSUE]. Keep all hard rules: no title/logo/watermark/readable label, one dominant subject, quiet bottom-left, readable at small mobile shelf size.
```

### Room Or Setting Revisions

When adding or replacing a room, background, atmosphere, or setting:

- Name one image as the authoritative sharp foreground and any other image only as the environment reference.
- Describe 3-5 coherent spatial cues that establish the requested place. Keep them distant, lower contrast, and partially behind the dominant subject.
- State that depth of field, haze, bloom, and light spill apply only to the background and must not soften the focal subject.
- Specify the intended optical-center placement of the gameplay cluster. Do not merely say `centered`; check that it does not sit visually low after generation.
- Match the room to the foreground's art medium and palette while preserving enough color/value separation for the subject to read.
- If a generated scene damages foreground sharpness or mechanic accuracy, reject it and regenerate from the earlier sharp baseline rather than editing the damaged candidate again.

If the user says `regenerate`, create a new versioned candidate and record the previous candidate's rejection reason. Do not overwrite the earlier file.

## Prompt Records

Before finalization, save the exact prompt that produced the accepted image. If the final came from revisions, save both the original generation prompt and final revision prompt.
