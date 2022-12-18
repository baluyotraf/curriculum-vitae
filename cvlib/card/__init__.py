from cvlib.schema import CurriculumVitae
from cvlib.card.fonts import GoogleFontLoader
from cvlib.card.text import Text, MultiText
from cvlib.card.card import Card


CARD_SIZE = (1200, 630)
NAME_SIZE = CARD_SIZE[0] // 10
TAGLINE_SIZE = CARD_SIZE[0] // 20
TEXT_SPACING = 20


def create_card_from_cv(cv: CurriculumVitae):
    texts = [
        (cv.theme.primary_font, cv.headline.name, NAME_SIZE),
        (cv.theme.secondary_font, cv.headline.tagline, TAGLINE_SIZE),
    ]

    fonts = GoogleFontLoader([t[0] for t in texts]).load_font_dict()
    card_texts = MultiText([
        Text(t[1], fonts[t[0]].font_variant(size=t[2]))
        for t in texts
    ], spacing=TEXT_SPACING)

    card = Card(
        CARD_SIZE,
        foreground=cv.theme.primary_color_text,
        background=cv.theme.primary_color
    )

    return card.render(card_texts)
