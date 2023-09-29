"""Test cases for the CLI application."""
from typer.testing import CliRunner

from seasmoke.app import app

runner = CliRunner()


def test_app() -> None:
    """Test case for the CLI application."""
    result = runner.invoke(app, ["5"])
    assert result.exit_code == 0
