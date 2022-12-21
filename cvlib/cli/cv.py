import os

import click

from cvlib import template


DEF_CONFIG = 'cv.yaml'


def _html(config: str, output: str, web: bool):
    os.makedirs(output, exist_ok=True)
    template.render_page(config, output, web)


@click.command()
@click.argument('config', type=click.Path(exists=True), default=DEF_CONFIG)
@click.argument('output', type=click.Path(), default='site')
def html(config: str, output: str):
    _html(config, output, True)


@click.command()
@click.argument('config', type=click.Path(exists=True), default=DEF_CONFIG)
@click.argument('output', type=click.Path(), default='print')
def print(config: str, output: str):
    # Should be replaced by PDF option once there's a light weight library
    # that supports HTML5/CSS3
    _html(config, output, False)
