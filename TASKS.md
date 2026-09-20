# TASKS.md — path to Tier 1 re-quiz and Phase 2 readiness

Work top to bottom. End EVERY session by: (1) committing, (2) updating
NEXT.md with the next unchecked task. One task per session is a win.

## A. Restart (all ⚡)

- [ ] A1 ⚡ Create NEXT.md (one line: current task) and docs/ideas.md
      (park Ashish's sky-app + streaks idea, 2 sentences). Commit.
- [ ] A2 ⚡ Fresh venv, `pip install -e ".[dev,docs]"`, run pytest +
      ruff + mypy. Note any breakage in the journal; fix or flag.
- [ ] A3 ⚡ Run hello-world notebook top to bottom. Confirm the image
      renders. One journal line: what plot_image() does and why asinh.
- [ ] A4 ⚡ Re-read your recon takeaways (the 4 ASTRiDE failure modes).
      Journal: which of the four you still remember unprompted.
- [ ] A5 ⚡ If PROJECT_PLAN.md / design doc are still placeholders,
      paste in the real content. Commit.
- [ ] A6 ⚡ Design doc: add "trail brightness model parameterized by
      bandpass; v1 = optical, spectral dimension reserved (per Ashish,
      IR surveys like Gattini-IR/WINTER)." Add Gattini-IR + WINTER
      links to docs/references.md. Commit.

## B. Notebook 02 — FITS basics (docs/notebooks/02_fits_basics.ipynb)

- [ ] B1 ⚡ Cell 1: imports; load one recon FITS file; markdown on
      where it came from.
- [ ] B2 ⚡ Cell 2: fits.open(), hdul.info(); explain HDUs in your words.
- [ ] B3 ⚡ Cell 3: print header; annotate NAXIS/BITPIX/BUNIT/EXPTIME/
      INSTRUME/FILTER/DATE-OBS in your words.
- [ ] B4 ⚡ Cell 4: data shape/dtype/min/max/mean/std. Answer in
      markdown: what physical quantity are these numbers? (Check BUNIT.
      They are NOT magnitudes — this was your quiz gap.)
- [ ] B5 ⚡ Cell 5: display with linear, log, asinh stretches
      (ImageNormalize + PercentileInterval). Markdown: when each fits.
- [ ] B6 ⚡ Cell 6: WCS(header); identify reference pixel, reference
      sky position, pixel scale, projection type.
- [ ] B7 ⚡ Cell 7: pixel↔sky round trip; move 1 arcmin, compute pixel
      scale by hand, verify vs header.
- [ ] B8 ⚡ Cell 8: plot with projection=wcs, sky gridlines.
- [ ] B9 ⚡ Cell 9: overlay a SkyCoord marker. Cell 10: reflection
      paragraph → also into journal. Commit the finished notebook.

## C. ADR-001 — package layout (docs/decisions/001-package-layout.md)

- [ ] C1 📖 Read PyPUG src-vs-flat discussion + Hynek's "Testing &
      Packaging". One journal sentence each.
- [ ] C2 ⚡ Check layout of 5 astro repos (astropy, photutils,
      lightkurve, ccdproc, astroquery) + 3 general (numpy, pytest,
      attrs). Tally in a scratch note.
- [ ] C3 ⚡ Write the ADR (200–400 words) from YOUR notes: context,
      decision, consequences, honest alternatives. Commit.

## D. Reading — trail physics (notes go in docs/learning/)

- [ ] D1 ⚡ Create docs/learning/tyson2020.md with the 3-section
      skeleton (says / didn't understand / means for astro-inject).
- [ ] D2 📖 Tyson+20 §1 (intro). Fill in notes as you read.
- [ ] D3 🧠 Tyson+20 §2 — the core physics: why LEO satellites make
      WIDE trails on LARGE telescopes (near-field defocus). Read
      slowly, sketch the geometry by hand in your notes. This is THE
      load-bearing hour of the whole list.
- [ ] D4 ⚡ Self-check, no peeking: write 3–4 sentences answering
      "why is a Starlink trail wider on Rubin than on a 30 cm scope?"
      If you can't → journal that honestly, redo D3 next session.
- [ ] D5 📖 Tyson+20 §3. Notes.
- [ ] D6 📖 Hasan+22 abstract + conclusions only. New notes file,
      same skeleton. One sentence: what result justifies our
      coadd-systematic metric?

## E. Notebook 03 — photometry (docs/notebooks/03_photometry_basics.ipynb)

- [ ] E1 ⚡ Cells 1–2: flux_ratio(m1, m2) from scratch (no astropy).
      Tests: (7,12)→100, (0,5)→100, (0,1)→~2.512. Markdown: derive
      from "5 mag = 100×" — this nails your quiz gap permanently.
- [ ] E2 📖 Cell 3: zero points — what they are, why needed;
      magnitude_to_flux_jansky(m).
- [ ] E3 🧠 Cells 4–5: flux → photon rate → photons_in_exposure().
      Full unit chain, written out step by step, no skipping. Test:
      mag 7, 1 m telescope, 30 s. THE injector calculation.
- [ ] E4 ⚡ Cell 6: verify vs astropy (u.ABmag → u.Jy equivalencies).
- [ ] E5 ⚡ Cell 7: surface brightness → flux per pixel. Markdown:
      restate compact-vs-diffuse correctly (your quiz miss, inverted).
- [ ] E6 🧠 Cell 8: the trail estimate — mag-5 Starlink, 2 s crossing,
      30 s exposure, 0.2"/px, 3" wide trail → photons per pixel.
      Reason it through stepwise. Cells 9–10: reflection. Commit.

## F. Re-quiz gate

- [ ] F1 ⚡ Tell Claude: "ready for the Tier 1 re-quiz." Target gaps:
      the −2.5 factor, FITS pixel values, surface brightness
      direction, atmospheric seeing.
- [ ] F2 (after passing) Tier 2 quiz — trail physics — then Phase 2:
      real injection code begins.
