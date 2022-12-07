import click

from cvlib.schema import CurriculumVitae


@click.group()
def schema():
    pass


@schema.command()
@click.argument('output', type=click.File('w'))
def create(output):
    output.write(CurriculumVitae.schema_json(indent=2))
