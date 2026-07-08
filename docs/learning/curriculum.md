The curriculum

Here's how I think about what you need to learn, organized by what unlocks what. This is a rough syllabus. We won't go through it linearly — we'll pull threads as the project demands them — but having the map helps.

Tier 1: Astronomy basics you need before any code (read this week, ~6 hours)
These are the things you should know cold before we touch trail physics.

Astronomical magnitudes. What does "apparent magnitude 7.5" mean physically? Why is the scale logarithmic and inverted? How do magnitudes relate to flux in physical units? Goal: explain in your own words why a magnitude-7 satellite is 100× brighter than a magnitude-12 satellite.
Coordinate systems. Right ascension and declination. The celestial sphere. World Coordinate System (WCS) in FITS files. How a pixel coordinate maps to a sky coordinate. Goal: given a FITS file in a notebook, use astropy.wcs to convert pixel (x, y) to (RA, Dec) and back, and explain what each transformation does.
The point spread function (PSF). Why does a point source on the sky become a blob on a detector? What's the difference between atmospheric seeing and the optical PSF? Why do PSFs vary across the field of view? Goal: simulate a Gaussian PSF, convolve a delta function with it, explain why the result is what it is.
FITS files. What's in them? Headers, HDUs, units, WCS keywords. Goal: open any FITS file in your test set and explain what every header keyword means. (Most you can ignore; some are load-bearing.)
Surface brightness vs. flux. Why is "brightness per unit area" a different thing than "total flux"? Why do astronomers care about this distinction? Goal: explain the LSB-wing problem in terms of surface brightness, not just flux.

Resources for Tier 1:

Astronomical Image and Data Analysis by Starck & Murtagh — old but the canonical "how astronomers think about images" reference. Skim chapters 1–3.
The Astropy tutorials at https://learn.astropy.org/ — work through "FITS-images", "FITS-tables", and "Coordinates" tutorials. These are excellent and hands-on.
Eric Bellm's lecture notes from the LSST DSFP school (Data Science Fellowship Program) on optical astronomy basics — search "DSFP optical photometry" on GitHub.

Tier 2: The physics of satellite trails (next two weeks, ~10 hours)
The actual content of astro-inject Phase 2.

Tyson et al. 2020. Read this in full. It's the load-bearing reference. The geometry of why LEO satellites produce wide trails on large telescopes (the near-field defocus argument) is the most important piece. Goal: explain in your own words why a Starlink satellite produces a 3-arcsecond-wide trail on Rubin but a much narrower trail on a 30cm telescope.
Hainaut & Williams 2020. Companion paper. Read for the broader survey-by-survey impact framing.
Hasan et al. 2022. The LSB-wing paper. Read sections 1, 2, and 4 in full. Goal: be able to explain to Ashish, in three sentences, what their key result was and why it justifies the coadd-systematic metric.
The trail brightness model. Why do trails vary in brightness along their length (solar phase angle), why do glints happen (specular reflections from flat surfaces), why do tumbling objects produce periodic brightening?
Atmospheric effects. How does seeing change a trail's profile? How does atmospheric scintillation affect the brightness modulation?

Resources for Tier 2:

The Tyson and Hasan papers above.
The IAU CPS (Centre for the Protection of the dark and quiet Sky from Satellite Constellation Interference) reports — these are accessible reviews of the field's current state.
Mallama 2021 on Starlink brightness modeling — technical but readable.

Tier 3: Python scientific computing patterns you need (parallel with Tiers 1-2)
These are the engineering foundations the package is built on. Not glamorous but load-bearing.

NumPy broadcasting and vectorization. When can you avoid a for-loop? Why does it matter? Goal: write a function that computes the distance from every pixel in an array to a given line, without any Python-level loops, and explain the broadcasting that makes it work.
Astropy units and quantities. Why is 5 * u.arcsec better than 5? How do unit conversions propagate? Goal: write a function whose inputs are physically-typed and demonstrate that unit errors are caught at function call time.
The CCDData / NDData type system. What does each carry? When do you use which? Goal: write a function that takes a CCDData, modifies its data array, and returns a new CCDData with WCS and uncertainty preserved.
Image visualization conventions. Asinh stretch, percentile cuts, colormap choice (and why "viridis on grayscale data" is a pet peeve in the field).

Resources for Tier 3:

The NumPy user guide on broadcasting.
The Astropy units documentation, specifically the "Equivalencies" section.
The Astropy visualization tutorial.

Tier 4: Machine learning fundamentals (deferred to Phase 3, but start reading now)
We will not write ML code in Phase 1 or 2. But you should be reading in the background. By the time we get to unstreak, you should have these cold.

Convolutional neural networks. Convolution as an operation, why it's translation-equivariant, why it's a good prior for images. Goal: implement a 2D convolution in NumPy from scratch, no PyTorch.
U-Net architecture. Why encoder-decoder, why skip connections, why it works for segmentation. Read the original Ronneberger et al. 2015 paper.
Loss functions for segmentation. Cross-entropy, Dice loss, focal loss, when each applies.
Why "predict a continuous flux map" is methodologically different from "predict a binary mask." This is the core technical claim of unstreak and you should be able to defend it.

Resources for Tier 4:

Dive into Deep Learning (d2l.ai) — free online, hands-on. Work through chapters 6 and 7 on CNNs.
Ronneberger et al. 2015 (the U-Net paper).
For the simulation-based-inference angle later: the SBI library docs at https://www.mackelab.org/sbi/.

Tier 5: Software engineering practices the package embodies (learn as you build)
You're already strong here, but a few things specific to scientific Python that are worth being deliberate about.

Why src layout, why hatchling, why ruff, why mypy strict. Be able to defend each.
Reproducibility patterns. Why explicit RNG, why provenance dicts, why content-addressable artifacts.
Semantic versioning in scientific software. Why scientific reproducibility puts more weight on version pinning than typical Python packages.
Astropy-affiliated package criteria. Read the requirements at https://www.astropy.org/affiliated/. This is your year-2 target.

What I'm assigning for this week
Concrete, before our next substantive session.
Reading (4-6 hours):

The two Astropy tutorials I named in Tier 1 (FITS-images, Coordinates).
Tyson et al. 2020, sections 1-3.
Skim Hasan et al. 2022 (just read the abstract and conclusion, full read comes later).

Hands-on (4-6 hours):

Write the eight ADRs. I'll suggest one per night for the next week. Don't just write the decisions I gave you — research each, briefly, before committing. For example, ADR-002 (attrs vs pydantic vs dataclasses): write a small test in a scratch notebook with each approach and decide based on what you actually liked, not what I told you. The ADRs are about thinking, not about transcribing.
Build a "FITS exploration" notebook in the repo as docs/notebooks/02_fits_basics.ipynb. Take any FITS file from your reconnaissance work. Open it. Print the header. Convert pixel coords to sky coords using WCS. Plot it with three different stretches (linear, log, asinh) and write up which is appropriate when. This is your "I understand what FITS files are" exercise.
Build a "magnitudes and fluxes" notebook as docs/notebooks/03_photometry_basics.ipynb. Implement: (a) magnitude-to-flux conversion from first principles, (b) a function that computes how many photons a magnitude-7 star produces in a 30-second exposure on a 1m telescope, (c) verify it against astropy.units.equivalencies. This is your "I can do photometric reasoning" exercise.