import click

from cvlib.cli import (
    cv,
    schema,
)


@click.group()
def main():
    pass


main.add_command(cv.html)
main.add_command(cv.print)
main.add_command(schema.schema)
