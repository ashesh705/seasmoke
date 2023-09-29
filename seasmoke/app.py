"""
Entry point of the application.

1. Initialize the CLI app.
2. Read and parse all the inputs.
"""
from typing import Annotated

import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def _(arg: Annotated[int, typer.Argument()]) -> None:
    """Parse all the inputs and redirect for processing."""
    typer.echo(f"Received argument {arg}")
