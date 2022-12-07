import os
import shutil
import glob

import click

from cvlib.template import (
    render_template,
    TEMPLATE_PATH,
)


@click.group()
def cv():
    pass

@cv.command()
@click.argument('input', type=click.Path(exists=True), default='cv.yaml')
@click.argument('output', type=click.Path(), default='site')
def generate(input, output):
    os.makedirs(output, exist_ok=True)

    render_template(input, os.path.join(output, 'index.html'))

    for css in glob.glob(os.path.join(TEMPLATE_PATH, '*.css')):
        shutil.copy2(css, output)
