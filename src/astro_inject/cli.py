"""Command-line interface for astro-inject."""

from __future__ import annotations

import click

from astro_inject._version import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def main() -> None:
    """astro-inject: inject synthetic artifacts into astronomical images."""


@main.command()
def version() -> None:
    """Print the installed astro-inject version and exit."""
    click.echo(f"astro-inject {__version__}")


if __name__ == "__main__":  # pragma: no cover
    main()
