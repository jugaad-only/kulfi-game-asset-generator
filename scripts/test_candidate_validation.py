#!/usr/bin/env python3
"""Regression tests for the pre-presentation Kulfi candidate validator."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


SKILL_DIR = Path(__file__).resolve().parents[1]
VALIDATOR = SKILL_DIR / "scripts/validate_candidate.py"
COMPOSITOR = SKILL_DIR / "scripts/compose_completed_banner.py"


def run(asset_type: str, candidate: Path, *extra: str, should_pass: bool) -> None:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), asset_type, str(candidate), *extra],
        capture_output=True,
        text=True,
        check=False,
    )
    passed = result.returncode == 0
    if passed != should_pass:
        expectation = "pass" if should_pass else "fail"
        raise AssertionError(
            f"expected {asset_type} to {expectation}:\n{result.stdout}{result.stderr}"
        )


def ring_mask(size: int, outer: float = 0.72, inner: float = 0.30) -> Image.Image:
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    margin = round(size * (1 - outer) / 2)
    draw.ellipse((margin, margin, size - margin - 1, size - margin - 1), fill=255)
    inner_margin = round(size * (1 - inner) / 2)
    draw.ellipse(
        (inner_margin, inner_margin, size - inner_margin - 1, size - inner_margin - 1),
        fill=0,
    )
    return mask


def daily_icon(path: Path) -> None:
    size = 287
    rng = np.random.default_rng(7)
    base = np.zeros((size, size, 4), dtype=np.uint8)
    noise = rng.normal(0, 2.0, (size, size, 1))
    color = np.array((195, 105, 76), dtype=np.float32)
    base[:, :, :3] = np.clip(color + noise, 0, 255).astype(np.uint8)
    base[:, :, 3] = np.asarray(ring_mask(size))
    Image.fromarray(base).save(path, "WEBP", lossless=True)


def partner_pair(webp: Path, svg: Path) -> None:
    image = Image.new("RGBA", (84, 84), (0, 0, 0, 0))
    fill = Image.new("RGBA", (84, 84), (142, 157, 177, 255))
    image.paste(fill, (0, 0), ring_mask(84))
    image.save(webp, "WEBP", lossless=True)
    svg.write_text(
        """<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 28 28">
<path fill="#8E9DB1" fill-rule="evenodd" d="M14 3a11 11 0 1 0 0 22 11 11 0 1 0 0-22zm0 7a4 4 0 1 1 0 8 4 4 0 1 1 0-8z"/>
</svg>
"""
    )


def bad_partner_palette(webp: Path, svg: Path) -> None:
    image = Image.new("RGBA", (84, 84), (184, 116, 69, 0))
    image.putalpha(ring_mask(84))
    image.save(webp, "WEBP", lossless=True)
    svg.write_text(
        """<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 28 28">
<path fill="#B87445" fill-rule="evenodd" d="M14 3a11 11 0 1 0 0 22 11 11 0 1 0 0-22zm0 7a4 4 0 1 1 0 8 4 4 0 1 1 0-8z"/>
</svg>
"""
    )


def info_square(path: Path) -> None:
    image = Image.new("RGB", (1024, 1024), (246, 235, 229))
    symbol = Image.new("RGBA", (620, 620), (194, 105, 76, 0))
    symbol.putalpha(ring_mask(620))
    image.paste(symbol, (202, 202), symbol)
    image.save(path, "WEBP", lossless=True)


def your_turn(path: Path) -> None:
    image = Image.new("RGBA", (813, 420), (246, 235, 229, 255))
    watermark = Image.new("RGBA", (470, 470), (194, 105, 76, 20))
    watermark.putalpha(ring_mask(470).point(lambda value: round(value * 0.10)))
    image.alpha_composite(watermark, (500, -25))
    symbol = Image.new("RGBA", (116, 116), (194, 105, 76, 255))
    symbol.putalpha(ring_mask(116))
    image.alpha_composite(symbol, (640, 152))
    image.convert("RGB").save(path, "WEBP", lossless=True)


def bad_checkerboard(path: Path) -> None:
    size = 287
    tile = 16
    image = Image.new("RGB", (size, size), "white")
    pixels = image.load()
    for y in range(size):
        for x in range(size):
            shade = 238 if ((x // tile) + (y // tile)) % 2 else 250
            pixels[x, y] = (shade, shade, shade)
    draw = ImageDraw.Draw(image)
    draw.ellipse((58, 58, 229, 229), fill=(50, 185, 188))
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path)


def bad_partner_background(path: Path) -> None:
    image = Image.new("RGB", (520, 260), (249, 243, 245))
    draw = ImageDraw.Draw(image)
    draw.ellipse((110, 115, 135, 140), outline=(190, 95, 122), width=3)
    draw.ellipse((352, 96, 425, 169), outline=(190, 95, 122), width=5)
    image.save(path)


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="kulfi-candidate-qa-") as temp:
        root = Path(temp)
        daily = root / "daily.webp"
        partner = root / "partner.webp"
        svg = root / "partner.svg"
        info = root / "info.webp"
        turn = root / "turn.webp"
        completed = root / "completed.png"
        bad_daily = root / "bad-checkerboard.png"
        bad_partner = root / "bad-partner.png"
        bad_palette = root / "bad-partner-palette.webp"
        bad_palette_svg = root / "bad-partner-palette.svg"

        daily_icon(daily)
        partner_pair(partner, svg)
        info_square(info)
        your_turn(turn)
        bad_checkerboard(bad_daily)
        bad_partner_background(bad_partner)
        bad_partner_palette(bad_palette, bad_palette_svg)

        portrait = Image.new("RGB", (600, 800), (40, 80, 120))
        ImageDraw.Draw(portrait).ellipse((120, 180, 520, 580), fill=(230, 150, 60))
        portrait_path = root / "portrait.png"
        portrait.save(portrait_path)
        landscape = Image.new("RGB", (1600, 900), (40, 80, 120))
        ImageDraw.Draw(landscape).ellipse((550, 170, 1050, 670), fill=(230, 150, 60))
        landscape_path = root / "landscape.webp"
        landscape.save(landscape_path, "WEBP", lossless=True)

        run("thumbnail_3x4", portrait_path, should_pass=True)
        run("thumbnail_16x9", landscape_path, should_pass=True)
        run("daily_game_icon", daily, should_pass=True)
        run(
            "partner_turn_icon",
            partner,
            "--source",
            str(daily),
            "--svg",
            str(svg),
            should_pass=True,
        )
        run("info_page_square_logo", info, "--source", str(daily), should_pass=True)
        run("your_turn_background", turn, "--source", str(daily), should_pass=True)

        compose = subprocess.run(
            [sys.executable, str(COMPOSITOR), str(daily), str(completed)],
            capture_output=True,
            text=True,
            check=False,
        )
        if compose.returncode != 0:
            raise AssertionError(f"completed fixture composition failed: {compose.stdout}{compose.stderr}")
        run("completed", completed, "--source", str(daily), should_pass=True)

        # Regression: an opaque checkerboard preview must never pass as a daily icon.
        run("daily_game_icon", bad_daily, should_pass=False)
        # Regression: a wide, opaque two-symbol layout must never pass as partner-turn.
        run(
            "partner_turn_icon",
            bad_partner,
            "--source",
            str(daily),
            "--svg",
            str(svg),
            should_pass=False,
        )
        # Regression: correct geometry with the wrong color or dirty transparent RGB must fail.
        run(
            "partner_turn_icon",
            bad_palette,
            "--source",
            str(daily),
            "--svg",
            str(bad_palette_svg),
            should_pass=False,
        )

    print("PASS candidate QA: all seven asset contracts and three failure regressions behaved correctly")


if __name__ == "__main__":
    main()
