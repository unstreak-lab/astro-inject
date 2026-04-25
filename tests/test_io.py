"""Tests for astro_inject.io."""

from __future__ import annotations

from pathlib import Path

from astropy.nddata import CCDData

from astro_inject.io import load_fits


def test_load_fits_returns_ccddata(synthetic_fits_path: Path) -> None:
    image = load_fits(synthetic_fits_path)
    assert isinstance(image, CCDData)


def test_load_fits_preserves_shape(synthetic_fits_path: Path) -> None:
    image = load_fits(synthetic_fits_path)
    assert image.data.shape == (128, 128)


def test_load_fits_attaches_wcs(synthetic_fits_path: Path) -> None:
    image = load_fits(synthetic_fits_path)
    assert image.wcs is not None
    assert image.wcs.naxis == 2


def test_load_fits_accepts_str_path(synthetic_fits_path: Path) -> None:
    image = load_fits(str(synthetic_fits_path))
    assert isinstance(image, CCDData)
