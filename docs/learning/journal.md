# Learning journal

## 2026-09-23
Why asinh stretch - linear and logarithmic to preserve image being
washed out by bright pixels. Asinh behaves linearly for faint values
and logarithmically for bright ones, compressing the bright end so
faint structure stays visible

Moved the recon notebook to this repo. Recalled the failure modes for ASTRiDE.

Failure modes for ASTRiDE:
1. closed contours, trails exiting the frame/sensor/chip are missed.
2. Faintness floor, changing (lowering) it causes more fragments, not longer trails.
3. No fragmetn linking (why?)
4. False positives on bleed trails.
5. May miss wings.

1. What is line hypothesis (Hough transform)

What a tool can do differently
1. Detect wings - start from a line hypothesis 
2. + Radial growth till you hit background for wings
3. Link colinear fragments
4. Understand bleed trails and spikes.

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
