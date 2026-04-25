"""Smoke tests for placeholder modules.

These exist so the stubbed surface area still counts toward coverage
while the real implementations are pending.
"""

from __future__ import annotations

import numpy as np
import pytest
from astropy.nddata import CCDData

from astro_inject.composition import inject
from astro_inject.instruments import Instrument
from astro_inject.instruments.base import Instrument as InstrumentBase
from astro_inject.trails import TrailParameters
from astro_inject.types import InjectionResult


def _empty_image() -> CCDData:
    return CCDData(np.zeros((4, 4), dtype=np.float32), unit="adu")


def test_injection_result_defaults() -> None:
    image = _empty_image()
    result = InjectionResult(contaminated=image)
    assert result.contaminated is image
    assert result.flux_map is None
    assert result.provenance == {}


def test_injection_result_is_frozen() -> None:
    result = InjectionResult(contaminated=_empty_image())
    with pytest.raises(AttributeError):
        result.contaminated = _empty_image()  # type: ignore[misc]


def test_trail_parameters_constructs() -> None:
    params = TrailParameters()
    assert params is not None


def test_inject_raises_not_implemented() -> None:
    image = _empty_image()
    with pytest.raises(NotImplementedError):
        inject(image, [])


def test_instrument_protocol_is_reexported() -> None:
    assert Instrument is InstrumentBase


def test_instrument_protocol_runtime_check_rejects_plain_object() -> None:
    assert not isinstance(object(), Instrument)


def test_instrument_protocol_runtime_check_accepts_duck_type() -> None:
    class _Duck:
        @property
        def pixel_scale(self) -> float:
            return 0.1

        @property
        def psf_fwhm(self) -> float:
            return 2.0

        @property
        def gain(self) -> float:
            return 1.5

    assert isinstance(_Duck(), Instrument)
