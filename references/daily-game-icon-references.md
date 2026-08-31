# Daily Game Icon References

Read this file only after all requested thumbnail formats for the game are approved and before creating its `daily_game_icon`.

## Direction

- Use the approved thumbnail and verified mechanic to select one recognizable symbol.
- Match the reference family's tactile felt-art construction.
- Use one filled felt silhouette in one dominant color. Add the approved family's subtle stitched perimeter using tonal thread from the same color family. Do not introduce contrasting thread, gradients, highlights, shadows, bevels, layered color regions, or illustrative interior detail.
- Use genuine transparency for the surrounding canvas. The filled symbol is the positive space; the open canvas around it is the negative space.
- Let the outer silhouette carry recognition and include one controlled area of internal negative space. Use one broad, simple opening that supports recognition and balance; do not add decorative holes or many small cutouts.
- Minimal detail means fewer, larger forms rather than the same complexity at a smaller scale. Preserve the family-defining perimeter seam, but delete decorative stitches, tiny dots, petals, beads, repeated scallops, fine lines, and ornamental patterns.
- Do not simplify away the subject's large functional identity cues. A minimal icon may retain a few broad knots, cords, handles, openings, or ends when those forms are what distinguish the object from a generic badge or shape.
- Do not translate an intricate Flaticon or craft reference literally. Reduce it to the subject's outer contour and one broad internal negative-space opening.
- Keep the detail budget minimal. Do not render faces, pupils, mouths, unrelated surface decoration, decorative embroidery, dense interior stitchwork, beads, or nested layers unless one of those forms is the game symbol itself.
- Apply the binary-mask test before approval: when the icon is reduced to one solid fill on transparency, it must remain balanced and recognizable at small mobile size.
- Felt grain and the restrained stitched perimeter are the allowed material treatments. Use matte non-woven nap, soft fibers, and subtly fuzzy cut edges. The seam must remain tonal, evenly spaced, and subordinate to the silhouette rather than becoming a contrasting outline.
- Do not include a title, word, wordmark, promotional copy, logo, watermark, or readable UI label.
- These references define the visual system; do not copy another game's symbol for a new game.

## Internet Reference Pass

Before sketching or generating the icon, search for both the thing and the treatment:

- **Recognition references:** real objects, actions, cultural forms, or verified gameplay examples that reveal what makes the subject identifiable. Prefer direct, credible, and culturally grounded sources over generated imagery or generic icon libraries.
- **Inspiration references:** felt craft, cut-paper forms, simple silhouettes, and comparable small icons that help with material, proportions, and positive/negative-space balance.
- **Flaticon reference:** search Flaticon for `[SUBJECT] black fill` or `[SUBJECT] glyph`. Study the economy of its silhouette and internal negative space, then record the result URL, author, style, and displayed license. Do not download, trace, or reuse the asset as production art unless its license and attribution requirements are deliberately satisfied.
- Capture screenshots of the selected references and save them as `iterations/<game-slug>-reference-<source>-<subject>-vNN.png`. Capture the relevant object or icon cleanly rather than an unreadable full-page thumbnail. Record each local screenshot path beside its page URL in `source-notes.md`.
- A reference screenshot is research material only. Do not promote it to the game-folder root, include it in deployment export, or present it as original production art.
- Record the search terms, source URLs, and two or three silhouette cues in the game's `source-notes.md`.
- Distill common category cues across references. Do not trace, closely reproduce, or combine distinctive details from one artist, product, brand, or proprietary character.
- If internet access is unavailable or the user opts out, record that limitation and rely on verified local or user-provided references.
- Internet inspiration never overrides the game's verified mechanic, approved thumbnail, or the one-color filled-felt rules.

## Name-Recognition QA

Before presenting a candidate, hide the game title, prompt, thumbnail, and source context. Ask:

> Does this really look like `[GAME NAME]`?

- For a literal object name such as `Rakhi`, the filled silhouette must first read as that object to an unfamiliar viewer. Reject a shape that reads more strongly as a badge, face, bell, plate, token, or generic ornament.
- Identify the two or three outer-silhouette cues that make the named object unique before generation. Preserve those cues even when removing interior detail.
- For an action name, the silhouette must imply that action without explanatory text.
- For an abstract or invented name, test whether the symbol clearly represents the verified game mechanic instead of forcing literal title recognition.
- Do not accept an icon merely because its color, felt texture, or execution matches the family. Semantic recognition is a separate required gate.
- Run two separate yes/no checks: `Does the outer silhouette read as [GAME NAME]?` and `Is there one broad, meaningful area of internal negative space?` Reject the icon if either answer is no.

## Reference Set

Bundled local reference folder: `assets/style-references/approved-daily-game-icons/`. Prefer the CDN URLs when available and use the bundled files as an offline fallback. Existing production icons may contain legacy detail; use them for felt material and family recognition only. They do not override the stricter one-color, one-filled-silhouette, broad-negative-space, and binary-mask rules for new icons.

| Game | WebP reference |
| --- | --- |
| Chess | [chess.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/chess.webp) |
| Daily Question | [daily_question.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/daily_question.webp) |
| Doodle It | [doodle_it.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/doodle_it.webp) |
| Four in a Row | [four_in_a_row.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/four_in_a_row.webp) |
| Hangman | [hangman.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/hangman.webp) |
| Jigsaw | [jigsaw.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/jigsaw.webp) |
| Ludo | [ludo.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/ludo.webp) |
| Mini Sudoku | [mini_sudoku.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/mini_sudoku.webp) |
| Moodoku | [moodoku.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/moodoku.webp) |
| Never Have I Ever | [never_have_i_ever.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/never_have_i_ever.webp) |
| Poople | [poople_game_icon.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/poople_game_icon.webp) |
| Quiz | [quiz.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/quiz.webp) |
| Sperm and Egg | [sperm_and_egg.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/sperm_and_egg.webp) |
| This or That | [this_or_that.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/this_or_that.webp) |
| Weave | [weave.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/weave.webp) |
| Who More Likely To | [who_more_likely_to.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/who_more_likely_to.webp) |
| Wordle Duel | [wordle_duel.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/wordle_duel.webp) |
| Zip Together | [zip_together.webp](https://asset-data.kulfiapp.com/media/home_game_v2/daily_games_icon/zip_together.webp) |
