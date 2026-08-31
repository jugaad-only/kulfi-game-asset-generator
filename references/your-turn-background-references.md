# Your-Turn Background References

Read this file when the corresponding `daily_game_icon` is approved and before creating `daily_game_your_turn_bg`. This asset does not depend on the partner-turn icon, info-page square logo, or completed-state derivative.

## Direction

- Use an opaque 813 x 420 WebP canvas unless the project specifies a 2x equivalent at the same aspect ratio. The Wordle Duel reference is 1626 x 840 and demonstrates the 2x form.
- Treat the approved daily icon as the source of truth for the game symbol, silhouette, felt color family, material treatment, and positive/negative space.
- Use a pale, low-contrast background from the icon's color family.
- Keep roughly the left 55% visually quiet for application-rendered turn UI.
- Place a small, crisp felt version of the approved icon in the upper-right. Keep it comfortably inside the canvas rather than edge-cropping the foreground icon. Its visual center should sit approximately 25%-38% down the canvas; vertical centering is incorrect.
- Place a much larger, very faint tonal version of the same silhouette behind the foreground icon as an intentionally cropped watermark aligned to the same upper-right cluster. Preserve its broad recognizable shape, but keep it subordinate to the foreground icon and UI.
- The foreground icon retains felt texture. The faint oversized watermark may be flat and tone-only.
- Do not introduce a second game symbol, gameplay scene, title, turn message, player name, button, badge, logo, watermark text, or readable UI label.
- Ignore the Hangman your-turn background entirely. It is a rejected legacy outlier and must not be opened, sampled, compared against, cited, or used for generation or QA.
- Poople is the only supplied filename with a legacy suffix (`poople_your_turn_bg.webp`). New games use their normal deployment basename unless the app requires a legacy alias.

## Reference Set

Bundled local reference folder: `assets/style-references/approved-your-turn-backgrounds/`. Prefer the bundled files when available; the URLs below identify their original CDN source.

| Game | WebP reference |
| --- | --- |
| Chess | [chess.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/chess.webp) |
| Daily Question | [daily_question.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/daily_question.webp) |
| Doodle It | [doodle_it.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/doodle_it.webp) |
| Four in a Row | [four_in_a_row.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/four_in_a_row.webp) |
| Jigsaw | [jigsaw.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/jigsaw.webp) |
| Ludo | [ludo.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/ludo.webp) |
| Mini Sudoku | [mini_sudoku.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/mini_sudoku.webp) |
| Moodoku | [moodoku.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/moodoku.webp) |
| Never Have I Ever | [never_have_i_ever.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/never_have_i_ever.webp) |
| Poople | [poople_your_turn_bg.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/poople_your_turn_bg.webp) |
| Quiz | [quiz.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/quiz.webp) |
| Sperm and Egg | [sperm_and_egg.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/sperm_and_egg.webp) |
| This or That | [this_or_that.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/this_or_that.webp) |
| Weave | [weave.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/weave.webp) |
| Who More Likely To | [who_more_likely_to.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/who_more_likely_to.webp) |
| Wordle Duel | [wordle_duel.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/wordle_duel.webp) |
| Zip Together | [zip_together.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/zip_together.webp) |

## Rejected Inventory

- Hangman: `https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/hangman.webp` — retained only for inventory traceability; never use it as a visual reference.
