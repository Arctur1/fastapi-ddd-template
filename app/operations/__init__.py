import click

from .commands import cli

cli_commands = click.CommandCollection(sources=[cli])

__all__ = ("cli_commands",)
