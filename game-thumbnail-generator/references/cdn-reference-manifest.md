# CDN Reference Manifest

Use this manifest before selecting any Kulfi CDN asset as a style reference. A file being live in production does not automatically make it a valid house-style exemplar.

## Status Meanings

- `accepted` - suitable as a visual-family reference for new work in the same asset class.
- `same-game-only` - valid production art, but its game-specific treatment must not define the general Kulfi house style.
- `rejected` - do not use for style prompting, generation, or QA. Keep the URL only for inventory and migration traceability.

## Thumbnail And Banner Families

Portrait base URL:

`https://asset-data.kulfiapp.com/media/home_game_v2/games_banner/v2/`

Landscape base URL:

`https://asset-data.kulfiapp.com/media/home_game_v2/banners_16x9/`

Apply the same status to the portrait filename and its corresponding `_16x9` landscape filename.

### Accepted House-Style References

`aloo_golf`, `bhag_simran_bhag`, `bomb_party`, `chess`, `daily_question`, `doodle_it`, `jigsaw`, `legacy_game_pillow_talk_banner`, `ludo`, `mini_sudoku`, `moodoku`, `nhie`, `penalty`, `poople`, `snatch_the_fries`, `this_or_that`, `weave`, `wordle`, `zip_together`

These are the reference pool for bright, tactile, toy-like, small-size-readable Kulfi catalog art. Use only 3-5 relevant examples per prompt.

### Same-Game-Only References

- `basketball_rivalry` - polished production art, but the neon arena lighting is not the default house-style lighting.
- `sperm_racers` - approved game-specific maroon biological maze world; use only for Sperm Racers derivatives or closely related revisions.

### Rejected Thumbnail References

- `connect_four` - unusually dark, realistic room staging; it pulls prompts away from the bright tactile catalog family.
- `hangman` - flat 2D platform-game treatment that does not match the dominant polished 3D thumbnail family.
- `sync_or_sink` - dark cinematic adventure key art rather than a bright, chunky mobile catalog tile.
- `wmlt` - contains a prominent readable `YOU!` callout and should not teach the no-text thumbnail system.
- `sperm-racers-v3-keyart-d` - duplicate alternate key art; use canonical `sperm_racers` only, and only as a same-game reference.

## Completed-State Classification

An earlier pasted block labelled `daily_games_completed` pointed to `games_banner/v2/`; reject that earlier block for completed-state work because it contains ordinary portrait game banners.

Actual completed-state assets use:

`https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/`

The corrected `daily_games_completed/` list is valid inventory. Read `completed-state-references.md` for its exact accepted URLs and fixed dark-teal layout.

- `accepted`: `chess` PNG/WebP, `daily_question`, `doodle_it`, `four_in_a_row`, `jigsaw`, `ludo`, `mini_sudoku`, `moodoku`, `never_have_i_ever`, `quiz`, `sperm_and_egg`, `this_or_that`, `weave` PNG/WebP, `who_more_likely_to`, `wordle_duel`, `zip_together`.
- `same-game-only`: `poople.webp` is a darker legacy variation. It may guide Poople symbol placement only; never sample its background for a new game.
- `rejected`: `hangman.webp` at `https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/hangman.webp`. Keep the URL for inventory traceability, but do not open, sample, cite, compare against, or use it for generation or QA.

## Derivative Families

The following CDN families are accepted as asset-class references. Their exact per-game URLs are stored in the matching reference file.

| Asset class | CDN base URL | Reference file |
| --- | --- | --- |
| Daily game icon | `https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/` | `daily-game-icon-references.md` |
| Partner-turn icon | `https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_partner_turn_icons/` | `partner-turn-icon-references.md` |
| Info-page square logo | `https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_info_page_square_logos/` | `info-page-square-logo-references.md` |
| Completed state | `https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_completed/` | `completed-state-references.md` |
| Your-turn background | `https://asset-data.kulfiapp.com/media/home_game_v2/daily_game_your_turn_bg/` | `your-turn-background-references.md` |

Existing daily icons include legacy complexity and are accepted as production-family material references, not as permission to repeat faces, multiple shades, tiny cutouts, or decorative stitching. New icons must still pass the stricter Felt Icon Rules and binary-mask gate in `SKILL.md`.

## Selection Rule

Prefer CDN links when network access is available. Use bundled files as an offline fallback. Never use a `same-game-only` or `rejected` asset among the 3-5 dominant references for a new unrelated game.
