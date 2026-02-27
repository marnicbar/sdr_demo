#!/usr/bin/env python3
"""Render and export Gray-coded square QAM constellation diagrams."""

from __future__ import annotations

import argparse
import math
from pathlib import Path
from typing import Iterable

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from gnuradio import digital

SUPPORTED_EXTENSIONS = {".png", ".svg", ".pdf"}
VALID_ORDERS = (4, 16, 64, 256)
CM_PER_INCH = 2.54
FIGURE_SIZE_CM = 8.0
LABEL_FONT_BY_ORDER = {
    4: 8,
    16: 7,
    64: 5,
    256: 3.8,
}
LABEL_YOFFSET_BY_ORDER = {
    4: 7,
    16: 5,
    64: 3,
    256: 2,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate a publication-ready QAM constellation plot. "
            "Supported output formats: PNG, SVG, PDF."
        )
    )
    order_group = parser.add_mutually_exclusive_group(required=True)
    order_group.add_argument("--qam4", action="store_const", const=4, dest="order")
    order_group.add_argument("--qam16", action="store_const", const=16, dest="order")
    order_group.add_argument("--qam64", action="store_const", const=64, dest="order")
    order_group.add_argument("--qam256", action="store_const", const=256, dest="order")
    order_group.add_argument(
        "--order",
        type=int,
        choices=VALID_ORDERS,
        dest="order",
        help="QAM order, one of: 4, 16, 64, 256.",
    )
    parser.add_argument(
        "output",
        type=Path,
        help="Output file path (must end in .png, .svg, or .pdf).",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        help="Raster DPI used for PNG export (default: 300).",
    )
    return parser.parse_args()


def validate_output_path(path: Path) -> Path:
    ext = path.suffix.lower()
    if ext not in SUPPORTED_EXTENSIONS:
        allowed = ", ".join(sorted(SUPPORTED_EXTENSIONS))
        raise ValueError(f"Unsupported output format '{ext}'. Use one of: {allowed}.")
    if path.parent and not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
    return path


def get_qam_points(order: int) -> Iterable[complex]:
    constellation = digital.qam.qam_constellation(order, True, "gray", True)
    return constellation.points()


def make_symbol_label(symbol_index: int, order: int) -> tuple[str, str]:
    bits_per_symbol = int(math.log2(order))
    return str(symbol_index), f"{symbol_index:0{bits_per_symbol}b}"


def make_plot(order: int, points: Iterable[complex]) -> plt.Figure:
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.size": 9,
            "axes.titlesize": 10,
            "axes.labelsize": 10,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
        }
    )

    real_parts = [p.real for p in points]
    imag_parts = [p.imag for p in points]
    figure_size_inches = FIGURE_SIZE_CM / CM_PER_INCH
    fig, ax = plt.subplots(
        figsize=(figure_size_inches, figure_size_inches),
        constrained_layout=True,
    )
    fig.patch.set_facecolor("white")
    ax.set_facecolor("#fcfcfc")

    ax.scatter(
        real_parts,
        imag_parts,
        s=58,
        c="black",
        edgecolors="white",
        linewidths=0.8,
        zorder=3,
    )

    label_size = LABEL_FONT_BY_ORDER[order]
    y_offset = LABEL_YOFFSET_BY_ORDER[order]

    for idx, point in enumerate(points):
        decimal_label, binary_label = make_symbol_label(idx, order)
        ax.annotate(
            decimal_label,
            xy=(point.real, point.imag),
            xytext=(0, y_offset),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=label_size,
            color="#1f1f1f",
        )
        ax.annotate(
            binary_label,
            xy=(point.real, point.imag),
            xytext=(0, -y_offset),
            textcoords="offset points",
            ha="center",
            va="top",
            fontsize=label_size,
            color="#1f1f1f",
        )

    ax.axhline(0, color="#6b6b6b", linewidth=1.0, zorder=1)
    ax.axvline(0, color="#6b6b6b", linewidth=1.0, zorder=1)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("In-phase (I)")
    ax.set_ylabel("Quadrature (Q)")
    ax.set_title(f"{order}-QAM", pad=8)
    ax.grid(which="major", linestyle="--", linewidth=0.6, color="#d5dbe5")
    ax.set_axisbelow(True)

    return fig


def main() -> int:
    args = parse_args()
    output_path = validate_output_path(args.output)
    points = list(get_qam_points(args.order))
    fig = make_plot(args.order, points)
    # Keep the exported canvas at the exact configured physical size.
    fig.savefig(output_path, dpi=args.dpi)
    plt.close(fig)
    print(f"Saved {args.order}-QAM constellation to: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
