#!/usr/bin/env python3
"""Validate a generated Kulfi asset candidate before it is presented.

This validator enforces machine-checkable stage contracts. Semantic checks such
as mechanic honesty, subject recognition, and art direction still require the
human/visual quality gate.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import deque
from pathlib import Path
from typing import Optional, Tuple

import numpy as np
from PIL import Image


ASSET_TYPES = (
    "thumbnail_3x4",
    "thumbnail_16x9",
    "daily_game_icon",
    "partner_turn_icon",
    "info_page_square_logo",
    "completed",
    "your_turn_background",
)


def image_rgba(path: Path) -> Image.Image:
    if not path.is_file():
        raise ValueError(f"file not found: {path}")
    try:
        return Image.open(path).convert("RGBA")
    except Exception as error:  # Pillow raises several format-specific errors.
        raise ValueError(f"cannot open image: {error}") from error


def alpha_mask(image: Image.Image, threshold: int = 16) -> np.ndarray:
    return np.asarray(image.getchannel("A"), dtype=np.uint8) >= threshold


def components(mask: np.ndarray) -> list[dict[str, object]]:
    height, width = mask.shape
    seen = np.zeros_like(mask, dtype=bool)
    found: list[dict[str, object]] = []
    for start_y, start_x in np.argwhere(mask):
        if seen[start_y, start_x]:
            continue
        queue = deque([(int(start_y), int(start_x))])
        seen[start_y, start_x] = True
        area = 0
        min_x = max_x = int(start_x)
        min_y = max_y = int(start_y)
        touches_edge = False
        while queue:
            y, x = queue.popleft()
            area += 1
            min_x, max_x = min(min_x, x), max(max_x, x)
            min_y, max_y = min(min_y, y), max(max_y, y)
            touches_edge = touches_edge or x in {0, width - 1} or y in {0, height - 1}
            for next_y, next_x in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if (
                    0 <= next_y < height
                    and 0 <= next_x < width
                    and mask[next_y, next_x]
                    and not seen[next_y, next_x]
                ):
                    seen[next_y, next_x] = True
                    queue.append((next_y, next_x))
        found.append(
            {
                "area": area,
                "bbox": (min_x, min_y, max_x + 1, max_y + 1),
                "touches_edge": touches_edge,
            }
        )
    return sorted(found, key=lambda item: int(item["area"]), reverse=True)


def normalized_mask(mask: np.ndarray, size: int = 96, padding: int = 6) -> np.ndarray:
    ys, xs = np.where(mask)
    if not len(xs):
        return np.zeros((size, size), dtype=bool)
    crop = mask[ys.min() : ys.max() + 1, xs.min() : xs.max() + 1]
    target = size - 2 * padding
    scale = min(target / crop.shape[1], target / crop.shape[0])
    width = max(1, round(crop.shape[1] * scale))
    height = max(1, round(crop.shape[0] * scale))
    resized = Image.fromarray((crop * 255).astype(np.uint8)).resize((width, height), Image.Resampling.NEAREST)
    canvas = np.zeros((size, size), dtype=np.uint8)
    x = (size - width) // 2
    y = (size - height) // 2
    canvas[y : y + height, x : x + width] = np.asarray(resized)
    return canvas >= 128


def mask_iou(first: np.ndarray, second: np.ndarray) -> float:
    union = np.logical_or(first, second).sum()
    return float(np.logical_and(first, second).sum() / union) if union else 0.0


def require_size(image: Image.Image, expected: tuple[int, int], errors: list[str]) -> None:
    if image.size != expected:
        errors.append(f"expected {expected[0]}x{expected[1]}, got {image.size[0]}x{image.size[1]}")


def require_opaque(image: Image.Image, errors: list[str]) -> None:
    alpha = np.asarray(image.getchannel("A"), dtype=np.uint8)
    if np.any(alpha != 255):
        errors.append("asset must be fully opaque")


def require_transparency(image: Image.Image, errors: list[str]) -> np.ndarray:
    alpha = np.asarray(image.getchannel("A"), dtype=np.uint8)
    transparent_share = float((alpha <= 8).mean())
    visible_share = float((alpha >= 16).mean())
    if transparent_share < 0.05:
        errors.append("genuine transparency is required; the canvas is opaque or a background is baked in")
    if visible_share < 0.03:
        errors.append("no substantial visible symbol was detected")
    border = np.concatenate((alpha[0], alpha[-1], alpha[:, 0], alpha[:, -1]))
    if float((border <= 8).mean()) < 0.85:
        errors.append("at least 85% of the outer border must be transparent and crop-safe")
    return alpha >= 16


def require_dominant_component(mask: np.ndarray, errors: list[str], minimum: float = 0.94) -> None:
    found = components(mask)
    if not found:
        errors.append("no symbol component was detected")
        return
    total = sum(int(item["area"]) for item in found)
    share = int(found[0]["area"]) / total
    if share < minimum:
        errors.append(f"multiple disconnected symbols detected; largest component is only {share:.1%} of the fill")


def require_source(
    source: Optional[Path], errors: list[str]
) -> Tuple[Optional[Image.Image], Optional[np.ndarray]]:
    if source is None:
        errors.append("--source must name the approved daily game icon for this derivative")
        return None, None
    try:
        image = image_rgba(source)
    except ValueError as error:
        errors.append(f"approved source is invalid: {error}")
        return None, None
    mask = alpha_mask(image)
    if float((np.asarray(image.getchannel("A")) <= 8).mean()) < 0.05:
        errors.append("approved source does not contain genuine transparency")
    return image, mask


def validate_thumbnail(image: Image.Image, ratio: float, errors: list[str]) -> None:
    actual = image.width / image.height
    if abs(actual - ratio) > 0.005:
        errors.append(f"aspect ratio {image.width}:{image.height} does not match the required stage")
    require_opaque(image, errors)
    rgb = np.asarray(image.convert("RGB"), dtype=np.float32)
    if float(rgb.std()) < 8.0:
        errors.append("candidate is nearly blank or lacks enough visual information")


def validate_daily_icon(image: Image.Image, errors: list[str]) -> None:
    require_size(image, (287, 287), errors)
    mask = require_transparency(image, errors)
    coverage = float(mask.mean())
    if not 0.10 <= coverage <= 0.78:
        errors.append(f"filled-symbol coverage is {coverage:.1%}; expected 10%-78% with breathing room")
    require_dominant_component(mask, errors)

    holes = [item for item in components(~mask) if not bool(item["touches_edge"])]
    broad_holes = [item for item in holes if int(item["area"]) >= image.width * image.height * 0.0025]
    if not broad_holes:
        errors.append("no broad internal negative-space opening was detected")
    if len(broad_holes) > 3:
        errors.append(f"too many broad internal cutouts detected ({len(broad_holes)}); use one controlled opening")

    rgba = np.asarray(image, dtype=np.uint8)
    core = np.asarray(image.getchannel("A"), dtype=np.uint8) >= 240
    pixels = rgba[:, :, :3][core]
    if len(pixels):
        channel_spread = float(pixels.astype(np.float32).std(axis=0).mean())
        if channel_spread < 0.7:
            errors.append("symbol is perfectly flat; daily icons require subtle, uniform felt grain")
        if channel_spread > 24.0:
            errors.append("symbol has excessive tonal/color variation for a one-color felt silhouette")


def svg_number(value: Optional[str]) -> Optional[float]:
    if value is None:
        return None
    value = value.strip().removesuffix("px")
    try:
        return float(value)
    except ValueError:
        return None


def validate_partner_svg(path: Optional[Path], errors: list[str]) -> None:
    if path is None:
        errors.append("--svg is required for the partner-turn SVG/WebP pair")
        return
    if not path.is_file():
        errors.append(f"SVG file not found: {path}")
        return
    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError) as error:
        errors.append(f"cannot parse SVG: {error}")
        return
    width, height = svg_number(root.get("width")), svg_number(root.get("height"))
    view_box = root.get("viewBox", "").replace(",", " ").split()
    view_size = None
    if len(view_box) == 4:
        try:
            view_size = (float(view_box[2]), float(view_box[3]))
        except ValueError:
            pass
    if (width, height) != (28.0, 28.0) and view_size != (28.0, 28.0):
        errors.append("partner-turn SVG must define a 28x28 canvas or viewBox")

    forbidden = {"text", "image", "foreignObject", "script", "style"}
    paints: set[str] = set()
    drawable = 0
    for element in root.iter():
        tag = element.tag.rsplit("}", 1)[-1]
        if tag in forbidden:
            errors.append(f"SVG contains forbidden <{tag}> content")
        if tag in {"path", "circle", "ellipse", "polygon", "polyline", "rect"}:
            drawable += 1
        for attribute in ("fill", "stroke"):
            value = element.get(attribute)
            if value and value not in {"none", "transparent", "currentColor"}:
                paints.add(value.strip().lower())
        for value in element.attrib.values():
            if "http://" in value or "https://" in value or "data:" in value:
                errors.append("SVG contains an external or embedded resource")
    if drawable == 0:
        errors.append("SVG contains no drawable symbol")
    if len(paints) > 1:
        errors.append(f"SVG uses multiple visible paint colors: {sorted(paints)}")


def validate_partner(
    image: Image.Image,
    source: Optional[Path],
    svg: Optional[Path],
    errors: list[str],
) -> None:
    require_size(image, (84, 84), errors)
    mask = require_transparency(image, errors)
    require_dominant_component(mask, errors, minimum=0.90)
    source_image, source_mask = require_source(source, errors)
    if source_image is not None and source_mask is not None:
        similarity = mask_iou(normalized_mask(mask), normalized_mask(source_mask))
        if similarity < 0.62:
            errors.append(
                f"partner-turn silhouette does not match the approved daily icon (normalized mask IoU {similarity:.2f})"
            )

    rgba = np.asarray(image, dtype=np.uint8)
    core = np.asarray(image.getchannel("A"), dtype=np.uint8) >= 240
    pixels = rgba[:, :, :3][core]
    if len(pixels) and float(pixels.astype(np.float32).std(axis=0).mean()) > 8.0:
        errors.append("partner-turn symbol is not a flat single-color treatment")
    validate_partner_svg(svg, errors)


def background_color(image: Image.Image) -> np.ndarray:
    rgb = np.asarray(image.convert("RGB"), dtype=np.float32)
    edge = max(2, min(image.size) // 30)
    corners = np.concatenate(
        (
            rgb[:edge, :edge].reshape(-1, 3),
            rgb[:edge, -edge:].reshape(-1, 3),
            rgb[-edge:, :edge].reshape(-1, 3),
            rgb[-edge:, -edge:].reshape(-1, 3),
        )
    )
    return np.median(corners, axis=0)


def foreground_from_background(image: Image.Image, threshold: float = 14.0) -> np.ndarray:
    rgb = np.asarray(image.convert("RGB"), dtype=np.float32)
    return np.linalg.norm(rgb - background_color(image), axis=2) >= threshold


def validate_info_square(image: Image.Image, source: Optional[Path], errors: list[str]) -> None:
    require_size(image, (1024, 1024), errors)
    require_opaque(image, errors)
    _, source_mask = require_source(source, errors)
    foreground = foreground_from_background(image)
    found = components(foreground)
    if not found:
        errors.append("no foreground symbol was detected")
        return
    largest = found[0]
    min_x, min_y, max_x, max_y = largest["bbox"]
    center_x = (int(min_x) + int(max_x)) / 2 / image.width
    center_y = (int(min_y) + int(max_y)) / 2 / image.height
    if abs(center_x - 0.5) > 0.08 or abs(center_y - 0.5) > 0.08:
        errors.append(f"foreground symbol is not centered (center {center_x:.1%}, {center_y:.1%})")
    if source_mask is not None:
        similarity = mask_iou(normalized_mask(foreground), normalized_mask(source_mask))
        if similarity < 0.50:
            errors.append(f"info-page symbol does not match the approved daily icon (mask IoU {similarity:.2f})")


def validate_your_turn(image: Image.Image, source: Optional[Path], errors: list[str]) -> None:
    require_size(image, (813, 420), errors)
    require_opaque(image, errors)
    require_source(source, errors)
    rgb = np.asarray(image.convert("RGB"), dtype=np.float32)
    split = round(image.width * 0.55)
    background = background_color(image)
    distance = np.linalg.norm(rgb - background, axis=2)
    left_active = float((distance[:, :split] >= 18.0).mean())
    right_active = float((distance[:, split:] >= 18.0).mean())
    if left_active > 0.08:
        errors.append(f"left 55% is not quiet enough ({left_active:.1%} high-contrast pixels)")
    if right_active < 0.02:
        errors.append("right side lacks the required foreground icon/watermark treatment")
    if left_active >= right_active:
        errors.append("visual activity is not biased to the right side")


def validate_completed(path: Path, errors: list[str]) -> None:
    validator = Path(__file__).with_name("validate_completed_banner.py")
    result = subprocess.run(
        [sys.executable, str(validator), str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        messages = [line.removeprefix("FAIL: ") for line in result.stdout.splitlines() if line.strip()]
        errors.extend(messages or [result.stderr.strip() or "completed-state validator failed"])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("asset_type", choices=ASSET_TYPES)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--source", type=Path, help="Approved daily icon required for icon-derived assets.")
    parser.add_argument("--svg", type=Path, help="Matching 28x28 SVG required for partner_turn_icon.")
    parser.add_argument("--report", type=Path, help="Optional JSON QA report path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    if args.asset_type == "completed":
        require_source(args.source, errors)
        validate_completed(args.candidate, errors)
    else:
        try:
            image = image_rgba(args.candidate)
        except ValueError as error:
            errors.append(str(error))
            image = None
        if image is not None:
            if args.asset_type == "thumbnail_3x4":
                validate_thumbnail(image, 3 / 4, errors)
            elif args.asset_type == "thumbnail_16x9":
                validate_thumbnail(image, 16 / 9, errors)
            elif args.asset_type == "daily_game_icon":
                validate_daily_icon(image, errors)
            elif args.asset_type == "partner_turn_icon":
                validate_partner(image, args.source, args.svg, errors)
            elif args.asset_type == "info_page_square_logo":
                validate_info_square(image, args.source, errors)
            elif args.asset_type == "your_turn_background":
                validate_your_turn(image, args.source, errors)

    report = {
        "asset_type": args.asset_type,
        "candidate": str(args.candidate.resolve()),
        "source": str(args.source.resolve()) if args.source else None,
        "svg": str(args.svg.resolve()) if args.svg else None,
        "status": "fail" if errors else "pass",
        "errors": errors,
    }
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n")
    if errors:
        print(f"FAIL {args.asset_type}: {len(errors)} issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS {args.asset_type}: machine-checkable candidate contract is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
