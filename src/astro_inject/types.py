"""Shared dataclasses describing inputs and outputs of injection."""

from __future__ import annotations

from typing import Any

from astropy.nddata import CCDData, NDData
from attrs import define, field


@define(frozen=True, slots=True)
class InjectionResult:
    """Result of an injection operation.

    This is a placeholder type. Real fields will be filled in when
    injection is implemented.

    Attributes:
        contaminated: The image after injection.
        flux_map: Optional per-pixel ground-truth flux contributed by
            the injected artifacts.
        provenance: Free-form dict describing how the result was
            produced (random seeds, parameter snapshots, etc.).
    """

    contaminated: CCDData
    flux_map: NDData | None = field(default=None)
    provenance: dict[str, Any] = field(factory=dict)
