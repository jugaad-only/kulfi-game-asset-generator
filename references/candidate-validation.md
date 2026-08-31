# Candidate Validation

Run machine QA immediately after every asset generation or deterministic composition and before displaying, presenting, requesting approval for, promoting, or exporting the candidate. A nonzero exit is a hard stop: keep the failed file in `iterations/`, record the reason, revise it, and validate the new version. Do not present a failed candidate.

The validator enforces dimensions, aspect ratio, opacity/transparency behavior, symbol structure, and selected derivative-source checks. It does not replace the visual and semantic review in `quality-gates.md`.

## Asset-Type Lock

Resolve the request to exactly one asset type before reading a recipe or generating anything:

| User intent | Validator asset type | Output contract |
| --- | --- | --- |
| Primary portrait catalog tile | `thumbnail_3x4` | Opaque 3:4 artwork |
| Approved landscape catalog derivative | `thumbnail_16x9` | Opaque 16:9 artwork |
| Daily game icon | `daily_game_icon` | 287 x 287 one-color felt symbol on transparency |
| Partner-turn icon | `partner_turn_icon` | One 28 x 28 SVG plus equivalent 84 x 84 transparent WebP, both using fixed UI chrome `#8E9DB1` with cleared RGB beneath fully transparent WebP pixels |
| Info-page square logo | `info_page_square_logo` | 1024 x 1024 opaque square with centered felt symbol |
| Completed-state banner | `completed` | 1626 x 588 lossless PNG QA source using the fixed dark-teal vertical gradient: `#1C272C` top, `#0C1B1F` middle, and `#03171C` bottom; protected left half; subtle neutral symbol lift near `+8, +7, +7` RGB; oversized right-side crop |
| Your-turn background | `your_turn_background` | 813 x 420 opaque wide UI background |

If the user says only `game icon`, `icon`, `turn asset`, or another phrase that could map to more than one row, ask which exact asset type they mean. Never infer a wide background from `partner turn`, and never infer a partner-turn icon from generic `game icon`.

## Commands

Replace paths with the current versioned candidate and approved source paths. Save the report beside the candidate in `iterations/`.

```bash
python3 <skill-folder>/scripts/validate_candidate.py thumbnail_3x4 <candidate> --report <qa-report.json>
python3 <skill-folder>/scripts/validate_candidate.py thumbnail_16x9 <candidate> --report <qa-report.json>
python3 <skill-folder>/scripts/validate_candidate.py daily_game_icon <candidate> --report <qa-report.json>
python3 <skill-folder>/scripts/validate_candidate.py partner_turn_icon <candidate.webp> --source <approved-daily-icon.webp> --svg <candidate.svg> --report <qa-report.json>
python3 <skill-folder>/scripts/validate_candidate.py info_page_square_logo <candidate.webp> --source <approved-daily-icon.webp> --report <qa-report.json>
python3 <skill-folder>/scripts/validate_candidate.py completed <lossless-candidate.png> --source <approved-daily-icon.webp> --report <qa-report.json>
python3 <skill-folder>/scripts/validate_candidate.py your_turn_background <candidate.webp> --source <approved-daily-icon.webp> --report <qa-report.json>
```

After a machine-QA pass, run the matching visual gate in `quality-gates.md`. Both checks must pass before the candidate may be shown.

## Coverage Boundary

Machine QA catches contract violations such as a baked checkerboard, missing alpha, wrong dimensions, an opaque wide layout submitted as partner-turn, an incorrect partner-turn palette or dirty transparent RGB, multiple disconnected symbols, excessive color variation, and a derivative whose mask materially differs from the approved daily icon. Human visual QA still decides subject recognition, mechanic honesty, felt quality, composition, cultural accuracy, text/watermarks, and family resemblance.
