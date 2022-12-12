import os

import click

from cvlib import template


@click.group()
def cv():
    pass

@cv.command()
@click.argument('input', type=click.Path(exists=True), default='cv.yaml')
@click.argument('output', type=click.Path(), default='site')
def generate(input, output):
    os.makedirs(output, exist_ok=True)

    template.render_html(input, os.path.join(output, 'index.html'))
    template.render_css(os.path.join(output, 'cv.css'))
