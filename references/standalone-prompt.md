# Standalone Thumbnail Prompt

Use this when the generator has no other context. Replace bracketed fields before generating.

```text
Generate one polished 3:4 portrait mobile game catalog thumbnail for [GAME NAME].

This is artwork for a mobile app game shelf, not a store poster. The game name will appear separately below the tile, so do not include any title text, logo, watermark, badge, promo copy, readable UI label, or wordmark inside the artwork.

Core mechanic: [WHAT THE PLAYER DOES].
Visual world and real game cues: [COLORS, OBJECTS, CHARACTERS, MATERIALS, UI MOTIFS, ENVIRONMENT].
Mood: [PLAYFUL / COZY / COMPETITIVE / SILLY / MAGICAL / FAST].
Art style: Kulfi house style: chunky tactile polished 3D mobile-game illustration, toy-like objects and game pieces, soft rounded forms, clean readable silhouettes, friendly studio lighting, crisp foreground edges, bright controlled colors, simple material depth, playful tabletop/game-piece energy, and strong small-size mobile catalog readability. Use `assets/style-references/kulfi-approved-thumbnail-study-sheet.png` as the shelf-fit anchor and attach 3-5 relevant individual references from `assets/style-references/approved-thumbnails-3x4/` when available.

Composition requirements:
- 3:4 portrait crop.
- One dominant subject or one clear gameplay action.
- Strong silhouette and immediate readability at small mobile thumbnail size.
- Bias the focal point toward the center, upper area, or right side.
- Keep the dominant gameplay cluster near the optical center or upper-middle; do not let it sit noticeably low in the frame.
- Keep the lower-left quadrant visually quiet but not empty: use only tiny, low-contrast background details there.
- Do not let the hero subject, main interaction, board, dense props, or important UI occupy the lower-left quadrant.
- Use clear foreground/background separation, strong lighting, and a simple color identity.
- Keep mechanic-critical foreground edges tack-sharp at small shelf size. Apply depth of field, haze, bloom, and environmental softness only behind the subject.
- Avoid clutter, tiny details, fake store badges, frames, borders, cinematic poster layouts, desktop/web hover-preview styling, comic-book ink, halftone grain, risograph print texture, noir lighting, gritty texture, horror/thriller/romance cover styling, photorealistic hands, realistic adult props, satin/candle boudoir mood, dark product-catalog lighting, excessive shadows, realistic stock-photo surfaces, and any style that would not sit beside the approved Kulfi thumbnail sheet.

The final image should feel like an exciting, honest preview of the game's actual play experience and remain readable beside many other mobile game thumbnails.
```

After the user approves the 3:4 direction, adapt the prompt for 16:9:

```text
Create a 16:9 landscape derivative of the approved 3:4 thumbnail for [GAME NAME].

Preserve the same dominant subject, palette, art style, lighting, mechanic, and emotional promise. Recompose the scene intentionally for landscape rather than cropping: keep the focal subject readable, add lateral breathing room, preserve foreground/background separation, and keep all critical action crop-safe.

Still follow the same rules: no game title, wordmark, promotional copy, logo, watermark, store badge, or readable UI label inside the artwork. Keep bottom-left visually quiet but not empty.
```
