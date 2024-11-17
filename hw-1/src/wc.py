import dataclasses

import click

__all__ = ["command_wc"]


@dataclasses.dataclass
class WCStats:
    lines: int
    words: int
    chars: int

    def __iadd__(self, other: "WCStats"):
        self.lines += other.lines
        self.words += other.words
        self.chars += other.chars
        return self


def count_stats(text: str) -> WCStats:
    lines = text.count("\n")
    words = len(text.split())
    chars = len(text)
    return WCStats(lines, words, chars)


def format_wc_stats(stats: WCStats, tag: str = "") -> str:
    formatted = f"{str(stats.lines).rjust(8)}{str(stats.words).rjust(8)}{str(stats.chars).rjust(8)}"
    if tag:
        formatted += f" {tag}"
    return formatted


@click.command()
@click.argument("files", type=click.File("r"), nargs=-1)
def command_wc(files):
    if not files:
        stdin_text = click.get_text_stream("stdin").read()
        stats = count_stats(stdin_text)
        click.echo(format_wc_stats(stats))
        return

    total_stats = WCStats(0, 0, 0)
    for file in files:
        text = file.read()
        stats = count_stats(text)
        click.echo(format_wc_stats(stats, file.name))
        total_stats += stats

    if len(files) > 1:
        click.echo(format_wc_stats(total_stats, "total"))


if __name__ == "__main__":
    command_wc()
