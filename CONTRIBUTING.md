# Contributing to astro-inject

Thanks for your interest in contributing! This project is in an early,
load-bearing phase, so the contributor workflow is intentionally
lightweight but strict on quality gates.

## Development setup

```bash
# 1. Fork on GitHub, then clone your fork
git clone git@github.com:<you>/astro-inject.git
cd astro-inject

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# 3. Install the package with dev + docs extras
pip install -e ".[dev,docs]"

# 4. Install pre-commit hooks
pre-commit install
```

## Branch and PR workflow

1. Create a branch off `main`:

   ```bash
   git checkout -b fix/short-description
   ```

2. Make your changes. Keep them focused; avoid mixing refactors with
   feature work.

3. Run the local checks and make sure they pass:

   ```bash
   ruff check
   ruff format --check
   mypy src/
   pytest
   ```

4. Commit with a descriptive message. Pre-commit will lint and format
   on its own; if it modifies files, re-stage and commit again.

5. Push your branch and open a pull request. In the PR description:
   - Describe **what** changed and **why**.
   - Link any related issues.
   - Note any user-visible API changes (these belong in
     `CHANGELOG.md` under the next-release heading).

## Architecture decisions

Non-trivial architectural changes — new public modules, dependency
additions, breaking changes, or anything that affects multiple
subsystems — should be proposed as an Architecture Decision Record
(ADR) before implementation.

1. Copy `docs/decisions/000-template.md` to a new file numbered
   sequentially (`001-…`, `002-…`, etc.).
2. Fill in the Context, Decision, and Consequences sections.
3. Open a PR adding just the ADR. Discuss there, iterate, and merge
   the ADR before opening the implementation PR.

## Code style and conventions

- Format and lint with `ruff` (config in `pyproject.toml`).
- Type-check with `mypy --strict`. New code should ship with full
  annotations; per-module relaxations live in `[tool.mypy.overrides]`.
- Prefer `attrs` (`@define(frozen=True, slots=True)`) for value types.
- Follow Google-style docstrings on public functions; mkdocstrings
  picks them up for the reference docs.

## Tests

- New functionality requires a test.
- Use the synthetic fixtures in `tests/conftest.py` rather than
  committing FITS files.
- `pytest --cov` is wired up by default; coverage must stay above
  80 % (enforced in CI).

## Reporting bugs and requesting features

Use GitHub Issues. Bug reports should include:

- Operating system and Python version.
- `pip freeze` output (or at least the relevant dependencies).
- A minimal reproducer.

## Code of conduct

Be kind. Disagreements about technical choices are welcome; personal
attacks are not. Consult the project owners if you encounter
behaviour that does not meet this bar.
