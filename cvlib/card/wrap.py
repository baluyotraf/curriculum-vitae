import re
from typing import List

from PIL.ImageFont import FreeTypeFont

from cvlib.typing import Number
from cvlib.card.optimizer import bound_optimization


def _word_bisector(word: str, font: FreeTypeFont, limit: Number) -> List[str]:
    bounds = [
        int(limit // length)
        for length in [font.getlength('W'), font.getlength('.')]
    ]

    def func(idx: int):
        return font.getlength(word[:idx])

    split = bound_optimization(bounds[0], bounds[1], func, limit,
                               tolerance=1, mid_transform=int)

    return [word[:split], word[split:]]


def word_splitter(word: str, font: FreeTypeFont, limit: Number) -> List[str]:
    if font.getlength(word) > limit:
        splits = _word_bisector(word, font, limit)
        return [splits[0], *word_splitter(splits[1], font, limit)]
    else:
        return [word]


def wrap_text(text: str, font: FreeTypeFont, limit: Number) -> str:
    wrapped: List[str] = []
    for word in re.split(r'\s', text):
        width = font.getlength(word)
        if width > limit:
            wrapped.extend(word_splitter(word, font, limit))
        else:
            try:
                prev = wrapped[-1]
            except IndexError:
                wrapped.append(word)
                continue

            words = f'{prev} {word}'
            widths = font.getlength(words)
            if widths > limit:
                wrapped.append(word)
            else:
                wrapped[-1] = words

    return '\n'.join(wrapped)
