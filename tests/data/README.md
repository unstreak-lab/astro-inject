# Test data

This directory is reserved for FITS files used by the test suite.

The default tests synthesize images on the fly via fixtures in
`tests/conftest.py`, so no external data is required to run `pytest`.

If you want to add larger or instrument-specific fixtures:

1. Drop the FITS file into this directory (it will be ignored by git
   thanks to `.gitignore`).
2. Add a fixture in `conftest.py` that loads it via
   `astro_inject.io.load_fits`.
3. Document the provenance of the file (instrument, program, archive
   URL) at the top of the new fixture so future contributors can
   reproduce or replace it.

Do not commit raw FITS frames to the repository — they are large and
licensing varies by archive.
