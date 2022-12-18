import os
from typing import Any

import yaml
import markupsafe
from mako.runtime import Context
from mako.lookup import TemplateLookup

import cvlib
from cvlib.schema import CurriculumVitae
from cvlib.card import create_card_from_cv


BASE_PATH = os.path.dirname(os.path.abspath(cvlib.__file__))
TEMPLATE_PATH = os.path.join(BASE_PATH, '../templates')
HTML_TEMPLATE_NAME = 'page/cv.html'
CSS_TEMPLATE_NAME = 'styles/cv.css'
HTML_OUTPUT_NAME = 'index.html'
CSS_OUTPUT_NAME = 'cv.css'
CARD_OUTPUT_NAME = 'card.png'


def escape(text):
    html_text = markupsafe.escape(text)
    return html_text.replace('\n', markupsafe.Markup('<br/>'))


TEMPLATE_LOOKUP = TemplateLookup(
    directories=[TEMPLATE_PATH],
    collection_size=500,
    filesystem_checks=True,
    default_filters=['escape'],
    imports=['from cvlib.template import escape']
)


def render_template(file, template, **kwargs):
    with open(file, 'w') as of:
        context = Context(of, **kwargs)
        template = TEMPLATE_LOOKUP.get_template(template)
        template.render_context(context)


def render_page(config, output_dir, web):
    with open(config) as cf:
        cv = CurriculumVitae(**yaml.safe_load(cf))

    html_path = os.path.join(output_dir, HTML_OUTPUT_NAME)
    render_template(html_path, HTML_TEMPLATE_NAME, cv=cv,
                    card_path=f'./{CARD_OUTPUT_NAME}')

    css_path = os.path.join(output_dir, CSS_OUTPUT_NAME)
    render_template(css_path, CSS_TEMPLATE_NAME, cv=cv, web_mode=web)

    card_path = os.path.join(output_dir, CARD_OUTPUT_NAME)
    card = create_card_from_cv(cv)
    card.save(card_path)
