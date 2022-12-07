import click

from cvlib.cli.cv import cv
from cvlib.cli.schema import schema


@click.group()
def main():
    pass


main.add_command(cv)
main.add_command(schema)
