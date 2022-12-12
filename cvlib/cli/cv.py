import os

import click

from cvlib import template


def _html(input, output, web):
    os.makedirs(output, exist_ok=True)

    template.render_html(input, os.path.join(output, 'index.html'))
    template.render_css(os.path.join(output, 'cv.css'), web=web)


@click.command()
@click.argument('input', type=click.Path(exists=True), default='cv.yaml')
@click.argument('output', type=click.Path(), default='site')
def html(input, output):
    _html(input, output, True)


@click.command()
@click.argument('input', type=click.Path(exists=True), default='cv.yaml')
@click.argument('output', type=click.Path(), default='print')
def print(input, output):
    # Should be replaced by PDF option once there's a light weight library
    # that supports HTML5/CSS3
    _html(input, output, False)
