# Completed-State References

Read this file when the corresponding `daily_game_icon` is approved and before creating `daily_games_completed` assets. This asset does not depend on the partner-turn or info-page square-logo derivative.

Do not use URLs under `games_banner/v2/` for this stage, even if a list labels them `daily_games_completed`; those are ordinary portrait banners. Completed-state references come only from the `daily_games_completed/` CDN family below.

## Direction

- Use a 1626 x 588 canvas unless the project specifies another target. The legacy Chess WebP reference is 813 x 294 at the same aspect ratio.
- Treat the approved daily icon's silhouette and positive/negative space as the source of truth.
- Use one fixed shared background template for every new completed banner. The background is not derived from the game's icon color.
- At 1626 x 588, the template is a horizontally uniform dark teal vertical gradient: approximately `#1C272C` at the top, `#0C1B1F` at mid-height, and `#03171C` at the bottom. Minor WebP compression differences are acceptable; visible hue drift is not.
- Keep the left UI area as untouched background. Do not add texture, grain, noise, a vignette, spotlight, glow, game-specific tint, or generated atmospheric variation.
- Treat the enlarged game symbol as a separate low-contrast overlay above the fixed background. Changing the symbol must never change the underlying gradient.
- Enlarge the symbol, place it on the right, and let it crop intentionally beyond the top, right, or bottom edges.
- Keep the left side visually quiet and low-contrast for completion-state UI content rendered by the application.
- The symbol should be recognizable but subdued; do not turn this into a bright icon tile or a detailed gameplay illustration.
- Do not bake titles, completion copy, scores, buttons, badges, logos, or watermarks into the image.
- Export WebP for the standard set. Provide a matching PNG only where the project or existing asset set requires it; Chess and Weave references include both.
- Ignore the Hangman completed asset entirely. Do not open, sample, compare against, cite, or use it for generation or QA. Poople is a darker legacy variation; use the majority shared template above for new games.

## Reference Set

Bundled local reference folder: `assets/style-references/approved-completed-banners/`. Prefer the bundled files when available; the URLs below identify their original CDN source. Still ignore Hangman for completed-state generation and QA.

| Game | PNG reference | WebP reference |
| --- | --- | --- |
| Chess | [chess.png](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/chess.png) | [chess.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/chess.webp) |
| Daily Question | Not provided | [daily_question.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/daily_question.webp) |
| Doodle It | Not provided | [doodle_it.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/doodle_it.webp) |
| Four in a Row | Not provided | [four_in_a_row.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/four_in_a_row.webp) |
| Jigsaw | Not provided | [jigsaw.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/jigsaw.webp) |
| Ludo | Not provided | [ludo.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/ludo.webp) |
| Mini Sudoku | Not provided | [mini_sudoku.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/mini_sudoku.webp) |
| Moodoku | Not provided | [moodoku.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/moodoku.webp) |
| Never Have I Ever | Not provided | [never_have_i_ever.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/never_have_i_ever.webp) |
| Poople | Not provided | [poople.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/poople.webp) |
| Quiz | Not provided | [quiz.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/quiz.webp) |
| Sperm and Egg | Not provided | [sperm_and_egg.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/sperm_and_egg.webp) |
| This or That | Not provided | [this_or_that.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/this_or_that.webp) |
| Weave | [weave.png](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/weave.png) | [weave.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/weave.webp) |
| Who More Likely To | Not provided | [who_more_likely_to.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/who_more_likely_to.webp) |
| Wordle Duel | Not provided | [wordle_duel.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/wordle_duel.webp) |
| Zip Together | Not provided | [zip_together.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/zip_together.webp) |
