"""Protocol describing the metadata an instrument must expose."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from astropy.units import Quantity


@runtime_checkable
class Instrument(Protocol):
    """Minimal interface for an instrument descriptor.

    Concrete implementations supply enough metadata to drive
    injection physics (sampling, PSF size, gain). Real implementations
    will be added per-survey in a later iteration.
    """

    @property
    def pixel_scale(self) -> Quantity:
        """Pixel scale in arcseconds per pixel."""
        ...  # pragma: no cover

    @property
    def psf_fwhm(self) -> Quantity:
        """Approximate PSF FWHM in arcseconds."""
        ...  # pragma: no cover

    @property
    def gain(self) -> Quantity:
        """Detector gain in electrons per ADU."""
        ...  # pragma: no cover

    @property
    def bandpass(self) -> str:
        """Bandpass name, e.g. "V", "g", "J" — the band magnitudes refer to."""
        ...  # pragma: no cover

    @property
    def zero_point(self) -> Quantity:
        """Magnitude corresponding to 1 count/s (or similar convention)."""
        ...  # pragma: no cover

    @property
    def sky_background(self) -> Quantity:
        """Magnitude / arcsec^2, typical for this instrument/site."""
        ...  # pragma: no cover
