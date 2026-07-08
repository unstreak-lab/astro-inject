# astro-inject — Design Document

## Scope

This document covers the design of `astro-inject` through Phase 2 (trail
physics complete). Benchmark and detector designs live in separate docs.

## Architectural overview

The library decomposes cleanly into five layers:

1. **Types** — data structures carrying images, artifacts, parameters
2. **I/O** — reading FITS, producing Astropy-native objects, writing results
3. **Artifact physics** — per-artifact-type flux map generation
4. **Composition** — combining a clean image with artifact flux maps
5. **Visualization** — rendering any object in the system to a matplotlib figure

Only layer 3 is artifact-specific. Layers 1, 2, 4, 5 are shared across
all artifact types and should be designed once, correctly.

## Public API sketch

```python
import astro_inject as ai
from astropy.nddata import CCDData

# Load a clean exposure
clean = ai.io.load_fits("hsc_clean_exposure.fits")

# Specify trail parameters in physical units
trail = ai.trails.TrailParameters(
    start_ra=150.0 * u.deg,
    start_dec=2.3 * u.deg,
    angular_velocity=0.5 * u.deg / u.s,
    exposure_time=30 * u.s,
    apparent_magnitude=7.5 * u.mag,
    position_angle=45 * u.deg,
)

# Generate the injection
result = ai.inject(
    clean,
    artifacts=[trail],
    instrument="hsc",
    rng=np.random.default_rng(42),
)

# result is an InjectionResult with:
#   .contaminated   — CCDData, the clean + artifact image
#   .flux_map       — NDData, per-pixel artifact flux contribution
#   .mask           — NDData, binary mask at configurable threshold
#   .artifacts      — list of injected artifact records
#   .provenance     — dict of parameters for reproducibility

# First-class visualization
result.plot()           # Three-panel: clean | contaminated | flux map
result.contaminated.plot()  # Single image with proper astronomical stretch
result.flux_map.plot(log=True)
```

## Type system

### `CleanImage`

Thin wrapper around `astropy.nddata.CCDData` that guarantees WCS,
units, and uncertainty are present. If a loaded FITS file is missing
any of these, the loader fills in sensible defaults with warnings.

### `ArtifactParameters`

Abstract base class. Concrete subclasses per artifact type. Uses
`attrs` or `pydantic` for validation; all parameters have physical
units via `astropy.units.Quantity`.

### `InjectionResult`

Dataclass bundling the contaminated image, flux map, mask, artifact
records, and provenance dict. Provides `.plot()` and `.to_fits()`
methods.

### `Instrument`

Protocol specifying the minimum information needed to inject artifacts
into an instrument's data: pixel scale, PSF model, detector response,
filter bandpass. Concrete implementations live in `astro_inject.instruments.*`.

## Decisions to make in week 1

Listed as ADRs to be written before any implementation:

- **ADR-001**: Package layout (src layout vs. flat layout) → src layout
- **ADR-002**: Type validation library (attrs vs. pydantic vs. dataclasses)
- **ADR-003**: Documentation generator (mkdocs-material vs. sphinx)
- **ADR-004**: Test layout (tests/ alongside src vs. tests/ separate)
- **ADR-005**: Versioning scheme (semver from v0.1.0)
- **ADR-006**: License (Apache 2.0 vs. BSD-3)
- **ADR-007**: Python version support (3.10 minimum vs. 3.11 minimum)
- **ADR-008**: Astropy version pinning policy

Decisions I'll recommend on most of these below, but the ADRs capture
the reasoning so future contributors understand why.

## Visualization strategy

Every object in the type system has a `.plot(ax=None, **kwargs)` method.
Defaults produce a sensible inline Jupyter display; `ax` allows
composition into larger figures. Consistent handling of:

- Asinh stretch for astronomical images (via `astropy.visualization`)
- WCS-aware axes when WCS is present
- Colorbar with physical units from `Quantity`
- `log=True` option for flux maps

This is the hello-world payoff at end of week 1: loading any FITS file
through the package and calling `.plot()` produces a correct
astronomical display.

## Slow/fast path separation

Not implemented in Phase 1. Designed in the API from day 1 by convention:

- `ai.inject(...)` — the slow, correct path
- `ai.fast.inject(...)` — reserved namespace for future fast-path
  implementations

Phase 1 only implements the slow path. The namespace reservation
prevents breaking API changes later.

## Non-obvious design choices

**Why `InjectionResult` is a dataclass, not a subclass of `CCDData`.**
The injected image is a `CCDData`, but the result of injection is
richer — it includes the flux map, the mask, provenance. A dataclass
bundling multiple Astropy objects is cleaner than a custom subclass
that breaks duck-typing.

**Why parameters are in physical units, not pixels.** Satellites move
at physical angular velocities, not "pixels per exposure." A trail on
HSC is physically identical to a trail on ZTF; only the pixel
manifestation differs. Parameterizing in physical units makes the
injector instrument-portable. Pixel-space conversion happens inside
the injection code, using the WCS.

**Why a `provenance` dict rather than just trusting the parameters.**
Reproducing an injection requires the parameters *and* the library
version *and* the random seed *and* the instrument model version.
Bundling these explicitly prevents "it worked when I generated it last
year but I can't reproduce now" failures.

**Coadd-systematic metric.**
Family of pixel-space residual statistics plus
a power-spectrum check at trail frequencies. Precise mathematical form 
to be specified in Phase 3 once injection and stacking pipelines are real.