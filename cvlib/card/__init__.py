import dataclasses as dc
from typing import Optional

from PIL import Image

from cvlib.schema import CurriculumVitae
from cvlib.card.fonts import GoogleFontLoader
from cvlib.card.text import Text, MultiText
from cvlib.card.card import Card


CARD_SIZE = (1200, 630)
NAME_SIZE = CARD_SIZE[0] // 10
TAGLINE_SIZE = CARD_SIZE[0] // 20
TEXT_SPACING = 20


@dc.dataclass
class CardText:
    text: str
    font: str
    font_size: int
    width: Optional[float] = None


def create_card_from_cv(cv: CurriculumVitae) -> Image.Image:
    texts = [
        CardText(
            cv.headline.name, 
            cv.theme.primary_font, 
            NAME_SIZE
        ),
        CardText(
            cv.headline.tagline, 
            cv.theme.secondary_font, 
            TAGLINE_SIZE, 
            CARD_SIZE[1]
        ),
    ]

    fonts = GoogleFontLoader([ct.font for ct in texts]).load_font_dict()
    card_texts = MultiText([
        Text(
            ct.text, 
            fonts[ct.font].font_variant(size=ct.font_size), 
            wrap_width=ct.width
        )
        for ct in texts
    ], spacing=TEXT_SPACING)

    card = Card(
        CARD_SIZE,
        foreground=cv.theme.primary_color_text,
        background=cv.theme.primary_color
    )

    return card.render(card_texts)
