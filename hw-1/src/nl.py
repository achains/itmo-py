import click
import sys

__all__ = ["command_nl"]


@click.command()
@click.argument("file", type=click.File("r"), required=False)
def command_nl(file):
    source = file or sys.stdin
    for i, line in enumerate(source, 1):
        click.echo(f"{i}\t{line}", nl=False)


if __name__ == "__main__":
    command_nl()
