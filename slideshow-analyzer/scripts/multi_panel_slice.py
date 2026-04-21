#!/usr/bin/env python3
"""
multi_panel_slice.py — slice a 2x2 multi-panel image into 4 clean panels.

The AI model often leaves a thin (5-15px) pure-white or pure-black buffer band
along the internal seams of a single-pass quad render. A naive `width/2` split
dumps this band onto the right/bottom edge of the left/top panels.

This script auto-detects the buffer band by scanning brightness along the
central horizontal and vertical strips, then crops the four panels with the
band fully excluded.

Usage:
    python multi_panel_slice.py <input_image> <output_dir> [--threshold 250]

Outputs:
    <output_dir>/panel_tl.png   (top-left)
    <output_dir>/panel_tr.png   (top-right)
    <output_dir>/panel_bl.png   (bottom-left)
    <output_dir>/panel_br.png   (bottom-right)
"""
from __future__ import annotations

import argparse
import os
import sys
from typing import Tuple

import numpy as np
from PIL import Image


def find_band_bounds(arr: np.ndarray, axis: str, threshold_white: int = 250,
                     threshold_black: int = 10, search_radius: int = 60) -> Tuple[int, int]:
    """
    Detect the buffer band along the central axis.

    Args:
        arr: HxWx3 numpy array of the image.
        axis: "vertical" -> scan around x=W/2 looking for a vertical band.
              "horizontal" -> scan around y=H/2 looking for a horizontal band.
        threshold_white / threshold_black: a band is detected when the mean
            channel intensity along that line is >= white_threshold (white band)
            or <= black_threshold (black band).
        search_radius: how many pixels to scan to either side of the center.

    Returns:
        (low_bound, high_bound) — inclusive pixel indices the band occupies.
        If no band is detected, both equal the centerline (single pixel split).
    """
    H, W, _ = arr.shape
    if axis == "vertical":
        center = W // 2
        line_means = arr.mean(axis=(0, 2))  # mean per column
    elif axis == "horizontal":
        center = H // 2
        line_means = arr.mean(axis=(1, 2))  # mean per row
    else:
        raise ValueError("axis must be 'vertical' or 'horizontal'")

    def is_band(value: float) -> bool:
        return value >= threshold_white or value <= threshold_black

    # Walk left/up from center to find the first non-band pixel
    low = center
    for i in range(center, max(0, center - search_radius) - 1, -1):
        if is_band(line_means[i]):
            low = i
        else:
            break
    # Walk right/down from center
    upper_limit = W if axis == "vertical" else H
    high = center
    for i in range(center, min(upper_limit, center + search_radius)):
        if is_band(line_means[i]):
            high = i
        else:
            break

    return low, high


def slice_quad(image_path: str, output_dir: str, threshold_white: int = 250,
               threshold_black: int = 10) -> None:
    img = Image.open(image_path).convert("RGB")
    arr = np.array(img)
    H, W, _ = arr.shape

    if abs(W - H) > 8:
        print(f"[warn] Source is not square ({W}x{H}); proceeding anyway.")

    vL, vR = find_band_bounds(arr, "vertical", threshold_white, threshold_black)
    hT, hB = find_band_bounds(arr, "horizontal", threshold_white, threshold_black)

    print(f"Source: {W}x{H}")
    print(f"Detected vertical band:   x={vL}..{vR}  (width={vR - vL + 1}px)")
    print(f"Detected horizontal band: y={hT}..{hB}  (height={hB - hT + 1}px)")

    os.makedirs(output_dir, exist_ok=True)
    quads = {
        "panel_tl.png": (0, 0, vL, hT),
        "panel_tr.png": (vR + 1, 0, W, hT),
        "panel_bl.png": (0, hB + 1, vL, H),
        "panel_br.png": (vR + 1, hB + 1, W, H),
    }
    for name, box in quads.items():
        sub = img.crop(box)
        out_path = os.path.join(output_dir, name)
        sub.save(out_path, optimize=True)
        print(f"  -> {out_path}: {sub.size}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input_image", help="Path to the 2x2 multi-panel image")
    parser.add_argument("output_dir", help="Directory to write the 4 sliced panels")
    parser.add_argument("--threshold-white", type=int, default=250,
                        help="Brightness >= this is treated as a white buffer band (default 250)")
    parser.add_argument("--threshold-black", type=int, default=10,
                        help="Brightness <= this is treated as a black buffer band (default 10)")
    args = parser.parse_args()

    if not os.path.isfile(args.input_image):
        print(f"[error] Input image not found: {args.input_image}", file=sys.stderr)
        return 1
    slice_quad(args.input_image, args.output_dir, args.threshold_white, args.threshold_black)
    return 0


if __name__ == "__main__":
    sys.exit(main())
