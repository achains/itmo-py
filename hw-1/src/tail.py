import click
import sys

__all__ = ["command_tail"]

TAIL_STDIN_LINES = 17
TAIL_FILE_LINES = 10


def find_tail(source, num_lines):
    return "".join(source.readlines()[-num_lines:])


@click.command()
@click.argument("files", type=click.File("r"), nargs=-1)
def command_tail(files):
    if not files:
        tail_lines = find_tail(sys.stdin, TAIL_STDIN_LINES)
        click.echo(tail_lines)
    else:
        show_headers = len(files) > 1
        for file in files:
            tail_lines = find_tail(file, TAIL_FILE_LINES)
            if show_headers:
                click.echo(f"==> {file.name} <==")
            click.echo(tail_lines)


if __name__ == "__main__":
    command_tail()
