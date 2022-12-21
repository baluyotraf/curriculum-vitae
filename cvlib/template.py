import os
from typing import (
    Any,
)

import yaml
import markupsafe
from mako.runtime import Context # type: ignore
from mako.lookup import TemplateLookup, # type: ignore

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


def escape(text: str) -> markupsafe.Markup:
    html_text = markupsafe.escape(text)
    return html_text.replace('\n', markupsafe.Markup('<br/>')) # type: ignore


TEMPLATE_LOOKUP = TemplateLookup( # type: ignore
    directories=[TEMPLATE_PATH],
    collection_size=500,
    filesystem_checks=True,
    default_filters=['escape'],
    imports=['from cvlib.template import escape']
)


def render_template(file: str, template_name: str, **kwargs: Any) -> None:
    with open(file, 'w') as of:
        context = Context(of, **kwargs) # type: ignore
        template = TEMPLATE_LOOKUP.get_template(template_name) # type: ignore
        template.render_context(context) # type: ignore


def render_page(config: str, output_dir: str, web: bool) -> None:
    with open(config) as cf:
        cv = CurriculumVitae(**yaml.safe_load(cf))

    html_path = os.path.join(output_dir, HTML_OUTPUT_NAME)
    render_template(html_path, HTML_TEMPLATE_NAME, cv=cv,
                    card_path=CARD_OUTPUT_NAME)

    css_path = os.path.join(output_dir, CSS_OUTPUT_NAME)
    render_template(css_path, CSS_TEMPLATE_NAME, cv=cv, web_mode=int(web))

    card_path = os.path.join(output_dir, CARD_OUTPUT_NAME)
    card = create_card_from_cv(cv)
    card.save(card_path)
