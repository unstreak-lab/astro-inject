# References

## Foundational physics

- Tyson, J. A. et al. 2020. "Mitigation of LEO Satellite Brightness
  and Trail Effects on the Rubin Observatory LSST." AJ 160, 226.
  https://arxiv.org/abs/2006.12417
  — The load-bearing reference for trail physics on 8m-class telescopes.

- Hainaut, O. R. & Williams, A. P. 2020. "Impact of satellite
  constellations on astronomical observations with ESO telescopes."
  A&A 636, A121. https://arxiv.org/abs/2003.01992
  — Complementary broader review.

## Residual flux and coadd systematics

- Hasan, I. et al. 2022. "The impact of satellite trails on
  Hyper Suprime-Cam survey data." https://arxiv.org/abs/2201.05591
  — The LSB-wing problem quantified. Justifies the coadd-systematic metric.

## Detection methods

- Kim, D.-W. 2016. "ASTRiDE: Automated Streak Detection for
  Astronomical Images." https://github.com/dwkim78/ASTRiDE
  — The classical baseline. Documented failure modes in our Phase 0 notebook.

- Paillassa, M., Bertin, E. & Bouy, H. 2020. "MaxiMask and MaxiTrack:
  two new tools for identifying contaminants in astronomical images."
  A&A 634, A48. https://arxiv.org/abs/1907.08298
  — Multi-class CNN artifact detector; Bertin is the SExtractor author.

- Hasan, I. et al. 2024. "ASTA: a tool for satellite trail detection."
  A&A, in press. [check arXiv for latest]
  — Strongest published detector; U-Net + probabilistic Hough.

- Chatterjee, S. et al. 2024. "SatStreaks: Towards Supervised Learning
  for Delineating Satellite Streaks." CRV 2024.
  https://github.com/jijup/SatStreaks
  — Largest annotated real-image dataset (3,130 images).

## Packaging precedents

- Medford, M. S. et al. 2022. "Removing Atmospheric Fringes from Zwicky Transient Facility i-Band Images using PCA." https://arxiv.org/abs/2102.10738
  — `fringez` package; the template for what we're building.

## Astropy ecosystem

- Astropy Collaboration et al. 2022. "The Astropy Project: Sustaining
  and Growing a Community-oriented Open-source Project and the Latest
  Major Release (v5.0) of the Core Package." ApJ 935, 167.
  — The ecosystem keystone.

## Instrument references

- HSC-SSP DR3: https://hsc-release.mtk.nao.ac.jp/doc/
- MeerLICHT: https://www.meerlicht.org/
- ZTF: https://www.ztf.caltech.edu/
- HST ACS/WFC: https://www.stsci.edu/hst/instrumentation/acs

## Tool ecosystem to know

- `photutils` — Astropy-affiliated, source detection/photometry.
- `astroscrappy` — cosmic ray detection (future integration point).
- `galsim` — galaxy and PSF simulation.
- `pyradon` — existing trail injection tool (the thing we're replacing).
- `synphot` - synthetic photometry.

## Related software Links

- [Astropy](https://www.astropy.org/) — core stack we build on.
- [photutils](https://photutils.readthedocs.io/) — source detection
  and photometry helpers.
- [synphot](https://synphot.readthedocs.io/) — synthetic photometry.
