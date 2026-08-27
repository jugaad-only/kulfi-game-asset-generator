#!/usr/bin/env python3
"""Compose a Kulfi completed-state banner from an approved icon alpha mask."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Approved daily icon with alpha")
    parser.add_argument("output", type=Path, help="Output .png or .webp path")
    parser.add_argument("--width", type=int, default=1626)
    parser.add_argument("--height", type=int, default=588)
    parser.add_argument("--symbol-size", type=int, default=1200)
    parser.add_argument("--x", type=int, default=740)
    parser.add_argument("--y", type=int, default=-300)
    parser.add_argument("--quality", type=int, default=96)
    return parser.parse_args()


def shared_gradient(width: int, height: int) -> np.ndarray:
    stops = (
        (0, np.array((28.0, 39.0, 44.0))),
        (height // 2, np.array((12.0, 27.0, 31.0))),
        (height - 1, np.array((3.0, 23.0, 28.0))),
    )
    result = np.zeros((height, width, 3), dtype=np.float32)
    for row in range(height):
        (a_row, a_color), (b_row, b_color) = (
            (stops[0], stops[1]) if row <= height // 2 else (stops[1], stops[2])
        )
        amount = (row - a_row) / (b_row - a_row)
        result[row, :, :] = a_color * (1.0 - amount) + b_color * amount
    return np.rint(result).astype(np.uint8)


def compose(args: argparse.Namespace) -> Image.Image:
    source = Image.open(args.source).convert("RGBA")
    scale = args.symbol_size / max(source.size)
    size = tuple(max(1, round(value * scale)) for value in source.size)
    alpha = source.getchannel("A").resize(size, Image.Resampling.LANCZOS)

    placed = Image.new("L", (args.width, args.height), 0)
    placed.paste(alpha, (args.x, args.y))
    mask = np.asarray(placed, dtype=np.float32).copy() / 255.0
    mask[:, : args.width // 2] = 0.0

    background = shared_gradient(args.width, args.height)
    tonal_lift = np.array((8.0, 7.0, 7.0), dtype=np.float32)
    result = np.clip(
        background.astype(np.float32) + mask[..., None] * tonal_lift, 0, 255
    ).astype(np.uint8)
    return Image.fromarray(result)


def main() -> None:
    args = parse_args()
    if args.width < 2 or args.height < 2 or args.symbol_size < 1:
        raise SystemExit("width, height, and symbol-size must be positive")
    if args.source.resolve() == args.output.resolve():
        raise SystemExit("source and output must be different files")

    output = compose(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.suffix.lower() == ".webp":
        output.save(args.output, "WEBP", quality=args.quality, method=6)
    elif args.output.suffix.lower() == ".png":
        output.save(args.output, "PNG", optimize=True)
    else:
        raise SystemExit("output extension must be .png or .webp")


if __name__ == "__main__":
    main()
