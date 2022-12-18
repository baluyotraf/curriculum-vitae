import re

from cvlib.card.optimizer import bound_optimization


def _word_bisector(word, font, limit):
    bounds = [
        int(limit // length)
        for length in [font.getlength('W'), font.getlength('.')]
    ]

    def func(idx):
        return font.getlength(word[:idx])

    split = bound_optimization(*bounds, func, limit,
                               tolerance=1, mid_transform=int)

    return [word[:split], word[split:]]


def word_splitter(word, font, limit):
    if font.getlength(word) > limit:
        splits = _word_bisector(word, font, limit)
        return [splits[0], *word_splitter(splits[1], font, limit)]
    else:
        return [word]


def wrap_text(text, font, limit):
    wrapped = []
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
