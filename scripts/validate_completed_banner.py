#!/usr/bin/env python3
"""Validate hard invariants for a lossless Kulfi completed-state banner source."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image

from compose_completed_banner import shared_gradient


EXPECTED_SIZE = (1626, 588)
MAX_LIFT = np.array((8, 7, 7), dtype=np.int16)
OVERLAY_THRESHOLD = 3
MIN_RIGHT_COVERAGE = 0.20
MIN_BBOX_WIDTH_SHARE = 0.70
MIN_BBOX_HEIGHT_SHARE = 0.85


def fail(messages: list[str]) -> None:
    for message in messages:
        print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Lossless completed-state PNG source")
    parser.add_argument(
        "--allow-alternate-size",
        action="store_true",
        help="Validate a project-specific size instead of requiring 1626x588",
    )
    args = parser.parse_args()

    errors: list[str] = []
    if args.source.suffix.lower() != ".png":
        errors.append("QA source must be a lossless .png file")
    if not args.source.is_file():
        fail([f"file not found: {args.source}"])

    opened = Image.open(args.source)
    if not args.allow_alternate_size and opened.size != EXPECTED_SIZE:
        errors.append(f"expected 1626x588, got {opened.size[0]}x{opened.size[1]}")
    if opened.mode in {"RGBA", "LA"} and opened.getchannel("A").getextrema() != (255, 255):
        errors.append("completed banner must be fully opaque")

    image = np.asarray(opened.convert("RGB"), dtype=np.int16)
    height, width, _ = image.shape
    background = shared_gradient(width, height).astype(np.int16)
    delta = image - background
    midpoint = width // 2

    if not np.array_equal(image[:, :midpoint], background[:, :midpoint]):
        errors.append("left half differs from the fixed shared gradient")
    if np.any(delta < 0):
        errors.append("candidate darkens the fixed template; only the neutral tonal lift is allowed")
    if np.any(delta > MAX_LIFT):
        allowed = tuple(int(v) for v in MAX_LIFT)
        observed = tuple(int(v) for v in delta.max(axis=(0, 1)))
        errors.append(f"tonal lift exceeds {allowed}; observed {observed}")

    overlay = np.max(delta, axis=2) >= OVERLAY_THRESHOLD
    overlay[:, :midpoint] = False
    ys, xs = np.where(overlay)
    if not len(xs):
        errors.append("no visible right-side symbol overlay detected")
    else:
        right_coverage = float(overlay[:, midpoint:].mean())
        bbox_width_share = (int(xs.max()) - int(xs.min()) + 1) / (width - midpoint)
        bbox_height_share = (int(ys.max()) - int(ys.min()) + 1) / height
        touched = sum(
            (
                int(ys.min()) == 0,
                int(xs.max()) == width - 1,
                int(ys.max()) == height - 1,
            )
        )
        if right_coverage < MIN_RIGHT_COVERAGE:
            errors.append(
                f"symbol covers only {right_coverage:.1%} of the right half; "
                f"minimum is {MIN_RIGHT_COVERAGE:.0%}"
            )
        if bbox_width_share < MIN_BBOX_WIDTH_SHARE:
            errors.append(
                f"symbol bbox spans only {bbox_width_share:.1%} of the right half; "
                f"minimum is {MIN_BBOX_WIDTH_SHARE:.0%}"
            )
        if bbox_height_share < MIN_BBOX_HEIGHT_SHARE:
            errors.append(
                f"symbol bbox spans only {bbox_height_share:.1%} of the height; "
                f"minimum is {MIN_BBOX_HEIGHT_SHARE:.0%}"
            )
        if touched < 2:
            errors.append("symbol must touch and crop beyond at least two of top, right, and bottom")

    if errors:
        fail(errors)
    print(
        f"PASS {args.source}: fixed gradient, protected left half, neutral tonal lift, "
        "and oversized multi-edge crop are valid."
    )


if __name__ == "__main__":
    main()
