# Kulfi House Style

Read this before writing any thumbnail generation prompt or judging a thumbnail candidate. This file defines the portable visual style for Kulfi mobile game catalog thumbnails.

## Required Style Direction

Kulfi thumbnails should feel like chunky, tactile, polished mobile-game illustrations. Favor toy-like 3D objects, soft rounded geometry, clean silhouettes, crisp foreground edges, friendly lighting, and simple bright-but-controlled color identities. The artwork should read instantly at small mobile shelf size and sit naturally beside other casual game tiles.

Use approved Kulfi thumbnail references whenever possible. This skill package includes:

- `assets/style-references/kulfi-approved-thumbnail-study-sheet.png`
- `assets/style-references/approved-thumbnails-3x4/`
- `assets/style-references/approved-thumbnails-16x9/`

Treat the contact sheet as the quick house-style anchor and the individual approved images as the stronger per-game reference set. Use the folder that matches the asset type being created: 3:4 thumbnails should reference `approved-thumbnails-3x4/`; 16:9 recompositions should reference `approved-thumbnails-16x9/` after the 3:4 direction is approved. Preserve the broad family traits: playful game-piece energy, tactile boards/cards/objects, soft material depth, clean staging, clear foreground/background separation, and cheerful catalog readability.

When prompting an image model, attach or cite 3-5 individual approved references that are closest to the new game's mechanic and mood. Prefer mechanic-near matches over color-only matches: board games with board games, choice games with choice/social games, action games with action games, and object-led games with object-led games. Use the contact sheet for overall shelf fit.

## Prompt Phrase

Use this exact style phrase, then adapt the subject details to the game:

```text
Kulfi house style: chunky tactile polished 3D mobile-game illustration, toy-like objects and game pieces, soft rounded forms, clean readable silhouettes, friendly studio lighting, crisp foreground edges, bright controlled colors, simple material depth, playful tabletop/game-piece energy, and strong small-size mobile catalog readability.
```

## Negative Style Guardrail

Include this guardrail unless the user explicitly approves a different art direction:

```text
Avoid comic-book ink, halftone grain, risograph print texture, noir lighting, cinematic poster drama, gritty texture, horror/thriller/romance cover styling, photorealistic hands, realistic adult props, satin/candle boudoir mood, dark product-catalog lighting, excessive shadows, realistic stock-photo surfaces, and any style that would not sit beside the approved Kulfi thumbnail sheet.
```

## Subject And Tone

- Make the game mechanic feel playful and interactive, not like a static product display.
- Use one dominant subject or one clear gameplay action.
- For choice games, avoid two perfectly equal product cards as the whole composition. Put the choice inside a single lively tabletop/game moment, with a small tap, selection, divider, token, or motion cue when it helps.
- Even cheeky or adult-coded game themes should be rendered as safe, stylized, playful casual-game objects. Do not lean into erotic, noir, horror, or thriller mood.
- Use simplified props that communicate the mechanic without creating a second genre, scene, or product category.

## Candidate Rejection

Reject and regenerate any thumbnail that is structurally compliant but visually off-family. Common failures:

- dark graphic-novel, comic, or halftone poster art
- cinematic key art with dramatic shadows or moody realism
- photorealistic product-shot props or hands
- gritty adult romance/thriller cover mood
- static product comparison cards without playful game interaction
- cluttered mood props in the lower-left quiet zone
- polished artwork that looks good alone but mismatches the approved Kulfi shelf
