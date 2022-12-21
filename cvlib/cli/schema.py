import io

import click

from cvlib.schema import CurriculumVitae


@click.command()
@click.argument('output', type=click.File('w'), default='cv.json')
def schema(output: io.TextIOBase):
    output.write(CurriculumVitae.schema_json(indent=2))
