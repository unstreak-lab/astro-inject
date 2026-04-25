"""Parameters describing satellite trails.

This module is a placeholder. Real fields will be added when trail
generation is implemented.
"""

from __future__ import annotations

from attrs import define


@define(frozen=True, slots=True)
class TrailParameters:
    """Configuration for a single synthetic satellite trail.

    Placeholder; concrete fields (entry/exit, brightness profile,
    spectral assumptions, motion blur) will be added in a later
    iteration.
    """
