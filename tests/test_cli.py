"""Tests for the click-based CLI."""

from __future__ import annotations

from click.testing import CliRunner

from astro_inject import __version__
from astro_inject.cli import main


def test_version_command_prints_version() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["version"])
    assert result.exit_code == 0, result.output
    assert __version__ in result.output


def test_help_lists_version_command() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "version" in result.output
