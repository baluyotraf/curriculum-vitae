import abc
import functools
from typing import Tuple, Optional, Iterable

from PIL import Image, ImageDraw, ImageFont

from cvlib.card import wrap
from cvlib.typing import Number, Box


MDRAW = ImageDraw.Draw(Image.new('RGB', (0, 0)))


class TextLike(metaclass=abc.ABCMeta):

    def measure(self, coords: Tuple[int, int]=(0, 0)) -> Box:
        raise NotImplementedError()

    def render(self, draw: ImageDraw.ImageDraw,
               coords: Tuple[int, int], fill: str) -> None:
        raise NotImplementedError

    def resize(self, font_size: Number = 1.0,
               wrap_width: Number = 1.0) -> "TextLike":
        raise NotImplementedError


class Text(TextLike):

    def __init__(self, text: str, font: ImageFont.FreeTypeFont,
                 wrap_width: Optional[Number] = None):
        self.text = text
        self.font = font
        self.wrap_width = wrap_width

    @property
    @functools.lru_cache
    def wrapped(self):
        if self.wrap_width is None:
            return self.text
        else:
            return wrap.wrap_text(self.text, self.font, self.wrap_width)

    @property
    @functools.lru_cache
    def _offset(self) -> int:
        bbox = MDRAW.multiline_textbbox((0, 0), self.wrapped, font=self.font)
        return -bbox[1]

    def _offset_coords(self, coords: Tuple[int, int]):
        return (
            coords[0],
            coords[1] + self._offset
        )

    def measure(self, coords: Tuple[int, int]=(0, 0)) -> Box:
        coords = self._offset_coords(coords)
        return MDRAW.multiline_textbbox(coords, self.wrapped, self.font)

    def render(self, draw: ImageDraw.ImageDraw,
               coords: Tuple[int, int], fill: str) -> None:
        coords = self._offset_coords(coords)
        draw.multiline_text(
            coords,
            self.wrapped,
            font=self.font,
            fill=fill
        )

    def _apply_scale(self, base: Number, factor: Number) -> Number:
        if isinstance(factor, int):
            return factor
        else:
            return int(base * factor)

    def resize(self, font_size: Number = 1.0,
               wrap_width: Optional[Number] = 1.0) -> "TextLike":
        font_size = self._apply_scale(self.font.size, font_size)

        if wrap_width is None or self.wrap_width is None:
            wrap_width = None
        else:
            wrap_width = self._apply_scale(self.wrap_width, wrap_width)

        font = self.font.font_variant(size=int(font_size))
        return Text(self.text, font, wrap_width)


class MultiText(TextLike):

    def __init__(self, texts: Iterable[TextLike], spacing: int):
        self.texts = texts
        self.spacing = spacing

    def measure(self, coords: Tuple[int, int]=(0, 0)) -> Box:
        left, top = coords
        bottom = top
        right = 0

        for text in self.texts:
            bbox = text.measure((left, bottom))

            bottom = bbox[3] + self.spacing
            right = max(bbox[2], right)

        return (left, top, right, bottom - self.spacing)

    def render(self, draw: ImageDraw.ImageDraw,
               coords: Tuple[int, int], fill: str) -> None:
        left, top = coords
        for text in self.texts:
            text.render(draw, (left, top), fill)
            bbox = text.measure((left, top))
            top = bbox[3] + self.spacing

    def resize(self, font_size: Number = 1.0,
               wrap_width: Number = 1.0) -> "TextLike":
        return MultiText(
            [t.resize(font_size, wrap_width) for t in self.texts],
            self.spacing
        )
