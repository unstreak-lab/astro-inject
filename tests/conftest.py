"""Shared pytest fixtures for the astro-inject test suite."""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

import numpy as np
import pytest
from astropy.io import fits
from astropy.wcs import WCS


@pytest.fixture(scope="session")
def synthetic_image_array() -> np.ndarray:
    """A small reproducible 2D image with a few Gaussian sources."""
    rng = np.random.default_rng(seed=42)
    shape = (128, 128)
    image = rng.normal(loc=100.0, scale=5.0, size=shape).astype(np.float32)

    sources = [
        (32, 32, 800.0, 2.0),
        (96, 64, 1500.0, 1.5),
        (48, 100, 500.0, 2.5),
    ]
    yy, xx = np.mgrid[: shape[0], : shape[1]]
    for y0, x0, amp, sigma in sources:
        image += (amp * np.exp(-((yy - y0) ** 2 + (xx - x0) ** 2) / (2 * sigma**2))).astype(
            np.float32
        )
    return image


@pytest.fixture(scope="session")
def synthetic_wcs() -> WCS:
    """A trivial TAN WCS centered on the image."""
    wcs = WCS(naxis=2)
    wcs.wcs.crpix = [64.0, 64.0]
    wcs.wcs.crval = [10.0, -20.0]
    wcs.wcs.cdelt = [-0.0001, 0.0001]
    wcs.wcs.ctype = ["RA---TAN", "DEC--TAN"]
    return wcs


@pytest.fixture(scope="session")
def synthetic_fits_path(
    tmp_path_factory: pytest.TempPathFactory,
    synthetic_image_array: np.ndarray,
    synthetic_wcs: WCS,
) -> Iterator[Path]:
    """Write the synthetic image to a FITS file and yield its path."""
    path = tmp_path_factory.mktemp("data") / "synthetic.fits"
    header = synthetic_wcs.to_header()
    hdu = fits.PrimaryHDU(data=synthetic_image_array, header=header)
    hdu.writeto(path)
    yield path
