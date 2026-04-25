"""Top-level composition: combine an image with synthetic artifacts."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from astropy.nddata import CCDData

from astro_inject.types import InjectionResult


def inject(
    image: CCDData,
    artifacts: Iterable[Any],
    **kwargs: Any,
) -> InjectionResult:
    """Inject `artifacts` into `image`.

    This is the top-level entry point for synthetic-artifact injection.
    The signature is the contract; the implementation will land in a
    later iteration.

    Args:
        image: The clean image to contaminate.
        artifacts: An iterable of artifact specifications (e.g.
            `TrailParameters`).
        **kwargs: Implementation-specific options (random seed,
            instrument overrides, etc.).

    Returns:
        An `InjectionResult` containing the contaminated image and
        provenance metadata.

    Raises:
        NotImplementedError: Always, until the real implementation lands.
    """
    raise NotImplementedError("astro_inject.composition.inject() is not implemented yet.")
