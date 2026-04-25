# Design — astro-inject

> **Placeholder.** The detailed design document will be pasted in
> here. The high-level shape is sketched in the README and in the
> module layout under `src/astro_inject/`.

## Module map (current)

| Module | Status | Purpose |
|--------|--------|---------|
| `astro_inject.io` | minimal | FITS → `CCDData` loader. |
| `astro_inject.viz` | working | Asinh / percentile image display. |
| `astro_inject.types` | stub | `InjectionResult` dataclass. |
| `astro_inject.trails` | stub | `TrailParameters` dataclass. |
| `astro_inject.composition` | stub | Top-level `inject()` entry point. |
| `astro_inject.instruments` | stub | `Instrument` protocol. |

## Open questions

- Do we want artifact specs to be eagerly rasterized, or lazily
  evaluated during composition?
- How do we keep instrument descriptors lightweight enough that users
  can register their own without touching package internals?
- What's the ground-truth contract for downstream ML consumers?
