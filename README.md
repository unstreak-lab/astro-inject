# astro-inject

[![PyPI](https://img.shields.io/badge/pypi-not%20yet%20released-lightgrey)](https://pypi.org/project/astro-inject/)
[![Docs](https://img.shields.io/badge/docs-mkdocs-blue)](https://unstreak-lab.github.io/astro-inject/)
[![CI](https://github.com/unstreak-lab/astro-inject/actions/workflows/ci.yml/badge.svg)](https://github.com/unstreak-lab/astro-inject/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-pending-lightgrey)](https://codecov.io/gh/unstreak-lab/astro-inject)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

Inject synthetic artifacts (satellite trails, cosmic rays, …) into
astronomical images for ML training and data-reduction pipeline
evaluation.

> **Status:** pre-alpha scaffold. Public API is not stable. The
> physics modules are intentionally stubbed in this release — only the
> visualization helper is wired through.

## Installation

```bash
pip install astro-inject  # not yet on PyPI
```

For development, install from source with the `dev` and `docs` extras
(see [Development](#development)).

## Quick example

```python
import numpy as np
from astropy.nddata import CCDData

from astro_inject.viz import plot_image

rng = np.random.default_rng(0)
data = rng.normal(100.0, 5.0, size=(256, 256)).astype("float32")
image = CCDData(data, unit="adu")

ax = plot_image(image)
ax.figure.savefig("preview.png")
```

The full hello-world walkthrough lives at
[`docs/tutorials/01_hello_world.ipynb`](docs/tutorials/01_hello_world.ipynb).

## Documentation

Full documentation is built with [MkDocs Material] and deployed to
GitHub Pages. The high-level entry points are:

- **Design** — overall architecture and the contracts between modules.
- **Decisions** — per-decision ADRs with the rationale behind each
  choice.
- **Tutorials** — runnable notebooks, starting with `01_hello_world`.
- **References** — papers, surveys, and related software.

## Citation

If you use `astro-inject` in published work, please cite it. A real
DOI will be issued at the first tagged release; until then, please use:

```bibtex
@software{astro_inject,
  author       = {{astro-inject contributors}},
  title        = {astro-inject: synthetic artifact injection for
                  astronomical images},
  year         = {2026},
  url          = {https://github.com/unstreak-lab/astro-inject},
  note         = {Pre-release; see CITATION.cff after v0.1.0.}
}
```

## Development

```bash
git clone https://github.com/unstreak-lab/astro-inject.git
cd astro-inject
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev,docs]"
pre-commit install
```

Common commands:

```bash
ruff check                  # lint
ruff format --check         # formatting
mypy src/                   # type-check (strict)
pytest                      # run the test suite with coverage
mkdocs serve                # preview docs at http://127.0.0.1:8000/
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contributor
workflow.

## License

Apache 2.0 © astro-inject contributors. See [LICENSE](LICENSE).

[MkDocs Material]: https://squidfunk.github.io/mkdocs-material/
