"""Tests for astro_inject.viz."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pytest
from matplotlib.axes import Axes

from astro_inject.io import load_fits
from astro_inject.viz import plot_image


def test_plot_image_returns_axes(synthetic_fits_path: Path) -> None:
    image = load_fits(synthetic_fits_path)
    fig, ax = plt.subplots()
    try:
        result = plot_image(image, ax=ax)
        assert isinstance(result, Axes)
        assert result is ax
        assert len(ax.images) == 1
    finally:
        plt.close(fig)


def test_plot_image_creates_axes_when_none(synthetic_fits_path: Path) -> None:
    image = load_fits(synthetic_fits_path)
    ax = plot_image(image)
    try:
        assert isinstance(ax, Axes)
        assert len(ax.images) == 1
    finally:
        plt.close(ax.figure)


def test_plot_image_rejects_unknown_stretch(synthetic_fits_path: Path) -> None:
    image = load_fits(synthetic_fits_path)
    with pytest.raises(ValueError, match="Unsupported stretch"):
        plot_image(image, stretch="linear")
