import os

import click

from cvlib import template


DEF_CONFIG = 'cv.yaml'


def _html(config, output, web):
    os.makedirs(output, exist_ok=True)
    template.render_page(config, output, 1 if web else 0)


@click.command()
@click.argument('config', type=click.Path(exists=True), default=DEF_CONFIG)
@click.argument('output', type=click.Path(), default='site')
def html(config, output):
    _html(config, output, True)


@click.command()
@click.argument('config', type=click.Path(exists=True), default=DEF_CONFIG)
@click.argument('output', type=click.Path(), default='print')
def print(config, output):
    # Should be replaced by PDF option once there's a light weight library
    # that supports HTML5/CSS3
    _html(config, output, False)
