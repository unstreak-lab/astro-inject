# Learning journal


## 2026-09-21
A2 done — fresh venv, install, run pytest + ruff + mypy
cd astro-inject
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev,docs]"
pytest && ruff check && mypy src/

## 2026-09-20
Restarted the project after a break. Created TASKS.md / NEXT.md.
What I remember clearly: the four ASTRiDE failure modes exist.
What got fuzzy: which four they actually are.
