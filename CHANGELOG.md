# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial scaffold: `src/astro_inject` package layout, `click`-based
  CLI with a `version` command, and stubs for `io`, `viz`, `types`,
  `trails`, `composition`, and `instruments.base`.
- Working `astro_inject.viz.plot_image` using astropy's asinh stretch
  + percentile interval.
- Test suite (`pytest`) with synthetic FITS fixtures, ruff lint +
  format config, mypy strict config, pre-commit hooks.
- MkDocs Material site with mkdocstrings API docs and an embedded
  hello-world Jupyter notebook.
- GitHub Actions workflows for CI (lint / type-check / test on
  Python 3.10, 3.11, 3.12) and docs deployment.

[Unreleased]: https://github.com/unstreak-lab/astro-inject/compare/HEAD
