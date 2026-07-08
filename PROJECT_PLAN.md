# astro-inject — Project Plan

**Status:** Phase 1 (foundation), Week 0
**Owner:** Mandar Mulherkar
**Last updated:** 2026-04-24

## What this is

`astro-inject` is a Python library for physics-based injection of artifacts
into real astronomical images, returning contaminated images plus per-pixel
ground-truth flux contribution maps. v1 targets satellite trails; the
architecture extends to cosmic rays, ghosts, fringes, scattered light, and
diffraction spikes.

The library exists because every astronomy ML paper on artifact detection
needs synthetic training and evaluation data, and current practice is ad-hoc
per-group scripts that model artifacts as idealized linear features. This is
the canonical, physics-rich, extensible version.

## Companion projects

- `astro-artifacts-bench` — standardized benchmark and evaluation harness
  (Phase 2)
- `unstreak` — satellite trail detector using `astro-inject` for training
  (Phase 3)

All three are separate packages with clean boundaries; each is independently
useful.

## Non-goals

- Not a replacement for instrument-specific pipeline tools (Rubin's
  `maskStreaks`, `acstools.satdet`, etc.) — those operate inside pipelines
  we do not aim to replace.
- Not a general photometric simulation library — `galsim` already fills
  that role for galaxy and PSF simulation; we focus specifically on
  artifact injection with ground-truth flux maps.
- Not a model zoo — `unstreak` is a single reference detector, not a
  collection.

## Design principles

1. **Astropy-native types at API boundaries.** `CCDData` in, `CCDData`
   out, `NDData` for auxiliary outputs, `Quantity` for physical
   parameters. Users with existing Astropy workflows should not need
   conversion code.
2. **Physics parameterized in physical units, not pixels.** Trail width
   in arcseconds, brightness in magnitudes, angular velocity in deg/s.
   Pixel-space quantities are derived inside the library.
3. **Reproducibility by construction.** Every random operation takes an
   explicit `numpy.random.Generator`. No implicit global state.
4. **Slow path first, fast path on demand.** The reference
   implementation is correct and readable. Speed optimizations are
   isolated behind a separate API and only added when profiling
   demands.
5. **Artifact-agnostic core, artifact-specific modules.** The
   composition logic (image + artifact flux map → contaminated image +
   ground truth) is shared across all artifact types. Artifact-specific
   physics lives in its own module.
6. **Visual inspection is first-class.** Every major type has a
   `.plot()` method that produces a sensible Jupyter-inline
   visualization. Tutorials show images, not just numbers.
7. **Public-data-only.** No dependency on private institutional data
   for any core functionality.

## Phases

### Phase 0: Reconnaissance ✓

Completed. ASTRiDE failure modes characterized on real HST and MeerLICHT
images. See `docs/recon/recon.ipynb`.

### Phase 1: Foundation (weeks 1–4)

Package skeleton, CI, docs site, type system, visualization layer.
Week 1 deliverable is a hello-world that renders FITS files via the
package in a notebook. Week 4 deliverable is a trail-injection API
(stubbed physics) that exercises the full I/O and composition pipeline.

### Phase 2: Trail physics (weeks 5–8)

Replace stubbed injection with real physics per Tyson+20 and related
literature. Validate by injection-recovery against ASTRiDE on MeerLICHT
data.

### Phase 3: Benchmark (weeks 9–11)

Standalone `astro-artifacts-bench` package. Test sets, metrics,
baselines.

### Phase 4: Detector (weeks 12–15)

Standalone `unstreak` package. Train a reference detector on
injection-recovery data.

### Phase 5: Launch (week 16)

Preprint, PyPI releases, public announcement.

### Phase 6: Maintenance and growth (months 5–12)

Second instrument in month 6, cosmic-ray injection in month 9, plus
steady-state bug fixes and community support.

## Success metrics

### v1 (4 months from start)
- All three packages on PyPI with semantic versioning
- arXiv preprint
- ≥3 instruments supported in `astro-inject`
- ≥10 GitHub stars (weak signal but non-zero)

### v2 (12 months from start)
- ≥100 PyPI downloads per month sustained
- ≥1 external citation
- ≥2 artifact types in `astro-inject`
- ≥1 external contributor

### Aspirational (24 months)
- Astropy-affiliated-package status for `astro-inject`
- ≥10 citations across downstream papers
- Adoption as standard training-data pipeline by at least one external
  research group

## Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Simulation-to-real gap in injected trails | Medium | High | Validate by injection-recovery against ASTRiDE; compare ASTRiDE scores on synthetic vs. real trails; iterate physics until distributions match |
| Small user base, limited adoption | High | Medium | Injector-first framing targets the broadest user base; benchmark + detector are demonstrations; single-person maintenance is sustainable |
| Foundation model released that supersedes detector work | Medium | Low | Injector and benchmark remain useful regardless; detector is demonstration, not the main contribution |
| Key public datasets become inaccessible | Low | High | Cache copies; document download procedures; use multiple independent data sources |
| Engineering scope creep | High | Medium | Strict phase boundaries; `.plot()` methods are the only allowed "nice to have" before v1 |

## Key references

See `docs/references.md` for the full reading list. The load-bearing ones:

- Tyson et al. 2020 — physical trail model for LEO satellite streaks
- Hasan et al. 2022 — residual flux after masking, HSC/COSMOS
- Hasan et al. 2024 — ASTA, the strongest current published detector
- Chatterjee et al. 2024 — SatStreaks dataset
- Medford et al. 2022 — fringez, the packaging precedent
- Paillassa et al. 2020 — MaxiMask, multi-class artifact detection

## Decision log

Architectural decisions with rationale live in `docs/decisions/`, one
file per decision, ADR-style.
