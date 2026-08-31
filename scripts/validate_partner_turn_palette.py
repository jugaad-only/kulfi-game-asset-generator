#!/usr/bin/env python3
"""Validate the fixed Kulfi partner-turn UI-chrome color contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

import numpy as np
from PIL import Image


TARGET = np.array([142, 157, 177], dtype=np.int16)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("webp", type=Path)
    parser.add_argument("--svg", required=True, type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    rgba = np.asarray(Image.open(args.webp).convert("RGBA"), dtype=np.uint8)
    alpha = rgba[:, :, 3]
    core = rgba[:, :, :3][alpha >= 240]
    if not len(core):
        errors.append("WebP has no opaque symbol pixels")
    else:
        median = np.median(core, axis=0).astype(np.int16)
        if np.max(np.abs(median - TARGET)) > 1:
            errors.append(
                f"WebP core color is #{median[0]:02X}{median[1]:02X}{median[2]:02X}; expected #8E9DB1"
            )

    hidden_rgb = rgba[:, :, :3][alpha == 0]
    if len(hidden_rgb) and np.any(hidden_rgb != 0):
        errors.append("fully transparent WebP pixels contain nonzero RGB")

    svg_text = args.svg.read_text().lower()
    paints = set(re.findall(r'(?:fill|stroke)=["\'](#[0-9a-f]{6})["\']', svg_text))
    if "#8e9db1" not in paints:
        errors.append("SVG does not use #8E9DB1")
    extra_paints = paints - {"#8e9db1"}
    if extra_paints:
        errors.append(f"SVG contains additional paint colors: {sorted(extra_paints)}")

    report = {
        "asset_type": "partner_turn_palette",
        "webp": str(args.webp.resolve()),
        "svg": str(args.svg.resolve()),
        "expected_color": "#8E9DB1",
        "status": "fail" if errors else "pass",
        "errors": errors,
    }
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + "\n")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS partner_turn_palette: fixed UI-chrome color and transparent RGB are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
