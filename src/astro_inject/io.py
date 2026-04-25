"""I/O helpers for reading astronomical image data."""

from __future__ import annotations

from pathlib import Path

from astropy.nddata import CCDData


def load_fits(path: str | Path) -> CCDData:
    """Load a FITS file into a `CCDData` object.

    Falls back to `unit='adu'` when the input file does not specify a
    `BUNIT` header, which is common for raw frames.

    Args:
        path: Filesystem path to a FITS file.

    Returns:
        The loaded image as a `CCDData` instance.
    """
    fits_path = Path(path)
    try:
        return CCDData.read(fits_path)
    except ValueError:
        return CCDData.read(fits_path, unit="adu")
