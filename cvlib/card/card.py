from typing import Tuple, Optional

from PIL import Image, ImageDraw

from cvlib.card.text import TextLike
from cvlib.card.optimizer import bound_optimization


class Card:

    def __init__(self, size: Tuple[int, int], foreground: str, background: str,
                 margin: Optional[int] = None):
        self.size = size
        self.foreground = foreground
        self.background = background
        self.margin = margin or size[0] // 20

    def _optimize_content_size(self, content: TextLike,
                               area: Tuple[int, int]) -> TextLike:
        content = content.resize(wrap_width=area[0])

        cbbox = content.measure()
        content_ratio = area[1] / cbbox[3]
        if content_ratio >= 1.0:
            return content
        else:
            def func(resize_ratio: float) -> int:
                cbbox = content.resize(resize_ratio).measure()
                return cbbox[3]

            size = bound_optimization(content_ratio, 1.0, func,
                                      limit=area[1], tolerance=0.5)
            return content.resize(size)

    def render(self, content: TextLike) -> Image.Image:
        img = Image.new('RGB', self.size, color=self.background)
        draw = ImageDraw.Draw(img)
        area = tuple(d - 2 * self.margin for d in self.size)

        content = self._optimize_content_size(content, area)
        cbbox = content.measure()

        offset = (area[1] - cbbox[3]) // 2
        content.render(draw, (self.margin, self.margin + offset),
                       fill=self.foreground)
        return img
