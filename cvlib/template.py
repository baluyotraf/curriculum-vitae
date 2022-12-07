import os
from typing import Any

import yaml
from mako.runtime import Context
from mako.lookup import TemplateLookup

import cvlib
from cvlib.schema import CurriculumVitae


BASE_PATH = os.path.dirname(os.path.abspath(cvlib.__file__))
TEMPLATE_PATH = os.path.join(BASE_PATH, '../templates')
TEMPLATE_LOOKUP = TemplateLookup(
    directories=[TEMPLATE_PATH],
    collection_size=500,
    filesystem_checks=True,
    default_filters=['h']
)
TEMPLATE_NAME = 'cv.html'


def render_template(config, output):

    with open(config) as cf:
        cv = CurriculumVitae(**yaml.safe_load(cf))

    with open(output, 'w') as of:
        context = Context(of, cv=cv)
        template = TEMPLATE_LOOKUP.get_template(TEMPLATE_NAME)
        template.render_context(context)