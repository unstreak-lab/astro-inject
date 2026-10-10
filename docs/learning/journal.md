# Learning journal

## 2026-10-10
Instrument ≠ spectral regime
Instrument provides the property and spectral regime determines how the
light is produced - reflected sunlight or thermal emission.
Ashish mentioned astro-inject may not be useful to him if its in visual band.
Which camera, and which wavelength matter because the magnitudes are different
in the wavelength of the instrument. So they’re independent, and the code keeps
them separate: the engine never assumes a band.

Added learnings from Liu et al for denoising ccd images.

Quantity vs. floats
I chose astropy Quantity to allow for units to be attached to the numbers.
This prevents any confusion and prevents wrong conversion bugs. e.g., passing
a pixel scale in pixels/arcsec instead of arcsec/pixel now fails loudly.

mypy python_version
venv (using the mac version) was set to 3.14, the highest version, but we
need to set it to a lower floor. mypy was set to 3.10. On that 3.14 venv,
pip installed a newer numpy whose type files use 3.12+ syntax, which
mypy-in-3.10-mode rejected. Pre 3.14 Numpy syntax caused errors, so we
develop with the low floor, which can be the same as astropy, and CI/CD
will check for the range from 3.11 to 3.14. The fix was recreating the venv
on 3.11. That pulled in a numpy mypy accepts, so python_version = "3.11" now works.

Real backgrounds and simulation-to-real
In a synthetic image, the background is very real, we only inject a physics based
artifact with GT. With a real background, we will still maintain real background
noise and uncertainties. We are not introducing another variable for learning.
The one thing that needs to be correct is the physics of the trails. We wll get real
noise, stars, and detector quirks for free. We also get to see if running ASTRiDE on
the injected trails, and on the ASTA trails will "struggle the same way".

Instrument ≠ exposure
Exposure porperties will vary every night based on local temperature, Seeing (how much
the atmosphere blurs stars that night) and Sky background (how bright the sky glows that
night, from the moon, clouds, city light)

## 2026-09-25
mypy's python_version setting controls what syntax it accepts everywhere,
including third-party stubs. Learned my venv silently used 3.14."

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
