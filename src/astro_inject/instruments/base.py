"""Protocol describing the metadata an instrument must expose."""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class Instrument(Protocol):
    """Minimal interface for an instrument descriptor.

    Concrete implementations supply enough metadata to drive
    injection physics (sampling, PSF size, gain). Real implementations
    will be added per-survey in a later iteration.
    """

    @property
    def pixel_scale(self) -> float:
        """Pixel scale in arcseconds per pixel."""
        ...  # pragma: no cover

    @property
    def psf_fwhm(self) -> float:
        """Approximate PSF FWHM in pixels."""
        ...  # pragma: no cover

    @property
    def gain(self) -> float:
        """Detector gain in electrons per ADU."""
        ...  # pragma: no cover
