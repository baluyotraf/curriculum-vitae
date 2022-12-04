from typing import Any

import yaml
from mako.runtime import Context
from mako.lookup import TemplateLookup

from schema import CurriculumVitae


lookup = TemplateLookup(
    directories=['templates'],
    collection_size=500,
    filesystem_checks=True,
    default_filters=['h']
)


def serve_template(name: str, context: Context):
    template = lookup.get_template(name)
    template.render_context(context)


with open('cv.yaml') as f:
    cv = CurriculumVitae(**yaml.safe_load(f))

with open('result.html', 'w') as f:
    serve_template('cv.html', Context(f, cv=cv))
