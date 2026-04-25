"""Visualization helpers for astronomical images."""

from __future__ import annotations

from typing import Any

from astropy.nddata import CCDData
from astropy.visualization import AsinhStretch, ImageNormalize, PercentileInterval
from matplotlib.axes import Axes
from matplotlib.figure import Figure


def plot_image(
    image: CCDData,
    ax: Axes | None = None,
    stretch: str = "asinh",
    percentile: float = 99.0,
    cmap: str = "gray",
    **imshow_kwargs: Any,
) -> Axes:
    """Display an astronomical image with a perceptual stretch.

    Args:
        image: The image to display, as a `CCDData` instance.
        ax: Optional matplotlib `Axes` to draw on. A new figure is
            created when omitted.
        stretch: Stretch family to apply. Currently only `'asinh'` is
            implemented.
        percentile: Percentile interval used for clipping (e.g. 99.0
            stretches between the 0.5th and 99.5th percentiles).
        cmap: Matplotlib colormap name.
        **imshow_kwargs: Forwarded to `Axes.imshow`.

    Returns:
        The `Axes` containing the rendered image.

    Raises:
        ValueError: If `stretch` is not a supported value.
    """
    if stretch != "asinh":
        raise ValueError(f"Unsupported stretch {stretch!r}; only 'asinh' is implemented.")

    if ax is None:
        fig: Figure
        fig, ax = _new_figure()
        del fig  # held by the Axes; not returned to keep the API minimal

    norm = ImageNormalize(
        image.data,
        interval=PercentileInterval(percentile),
        stretch=AsinhStretch(),
    )
    ax.imshow(image.data, origin="lower", cmap=cmap, norm=norm, **imshow_kwargs)
    ax.set_xlabel("x [pix]")
    ax.set_ylabel("y [pix]")
    return ax


def _new_figure() -> tuple[Figure, Axes]:
    """Create a default figure for `plot_image`."""
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(6, 6))
    return fig, ax
