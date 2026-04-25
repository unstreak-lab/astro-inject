"""Tests for the package version string."""

from __future__ import annotations

import re

import astro_inject

_SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+([.\-+].+)?$")


def test_version_is_non_empty_string() -> None:
    assert isinstance(astro_inject.__version__, str)
    assert astro_inject.__version__


def test_version_matches_semver_shape() -> None:
    assert _SEMVER_RE.match(astro_inject.__version__), (
        f"version {astro_inject.__version__!r} is not semver-shaped"
    )
