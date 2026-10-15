# Production Manifest Game Map

The [Kulfiverse production game manifest](https://verse.kulfiapp.com/game-manifest) is the source of truth for finalized games and their user-facing names. Local asset packs are working records; their validation state does not change production finalization.

Snapshot checked on 2026-10-15: 53 finalized records, comprising 43 active and 10 inactive records. Active and inactive describe availability, not finalization.

Use the **Game** display name in user-facing reports and derive the canonical local folder slug from it. Retain internal keys and legacy export basenames only for technical mapping and deployment compatibility.

## Local Workspace Mapping

| Manifest game name | Internal key | Production state | Canonical local folder | Notes |
|---|---|---:|---|---|
| aloo golf | `POTATO_GOLF` | Active | `game-assets/aloo-golf/` | Legacy export basename remains `aloo_golf`. |
| bare minimum vs princess treatment | `BARE_MINIMUM_VS_PRINCESS_TREATMENT` | Active | `game-assets/bare-minimum-vs-princess-treatment/` | — |
| BASKETBALL_RIVALRY | `BASKETBALL_RIVALRY` | Active | `game-assets/basketball-rivalry/` | — |
| bhaag simran bhaag | `BHAG_SIMRAN_BHAG` | Active | `game-assets/bhaag-simran-bhaag/` | — |
| bro zoned | `BRO_ZONED` | Active | `game-assets/bro-zoned/` | — |
| hangman | `HANGMAN` | Active | `game-assets/hangman/` | — |
| hot swipes | `LIVE_OPS_HOT_SWIPES` | Active | `game-assets/hot-swipes/` | — |
| bade vs chotte | `LAND_IO_V2` | Active | `game-assets/bade-vs-chotte/` | Former local folder: `bade-vs-chotte`. |
| last card! | `UNO` | Active | `game-assets/last-card/` | `uno` and `uno-duel` are preserved as legacy histories. |
| don't fry me! | `LAVA_FLOOR` | Active | `game-assets/dont-fry-me/` | Former local folder: `lava-leap`. |
| pen fight | `PEN_FIGHT` | Active | `game-assets/pen-fight/` | — |
| PILLOW_TALK | `PILLOW_TALK` | Active | `game-assets/pillow-talk/` | — |
| rock, paper, scissors | `ROCK_PAPER_SCISSORS` | Active | `game-assets/rock-paper-scissors/` | Distinct from **rock, paper, strip**. |
| SNATCH_THE_FRIES | `SNATCH_THE_FRIES` | Active | `game-assets/snatch-the-fries/` | — |
| pirate escape | `SYNC_OR_SINK` | Active | `game-assets/pirate-escape/` | Former local folder: `sync-or-sink`. |
| thumb kiss | `THUMBKISS` | Active | `game-assets/thumb-kiss/` | Former local folder: `thumbkiss`. |
| what men like | `LIVE_OPS_WHAT_MEN_LIKE` | Active | `game-assets/what-men-like/` | — |
| word spill | `BOMB_PARTY` | Active | `game-assets/word-spill/` | — |
| yeet the spider | `YEET_THE_SPIDER` | Active | `game-assets/yeet-the-spider/` | — |

## Local-Only And Legacy Records

| Local name | Local location | Status |
|---|---|---|
| Khopdi Fod | `game-assets/khopdi-fod/` | No matching production manifest record in the 2026-10-15 snapshot. |
| Rakhi | `game-assets/rakhi/` | No matching production manifest record in the 2026-10-15 snapshot. |
| Sketch Relay | `game-assets/sketch-relay/` | Development deployment record exists; no matching production record in this snapshot. |
| UNO legacy pack | `legacy-assets/game-assets/uno/` | Historical working pack for **last card!**. |
| UNO Duel staging pack | `legacy-assets/game-assets/uno-duel/` | Historical staging pack consolidated into **last card!**. |
