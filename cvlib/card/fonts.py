import re
import io

import requests
from PIL import ImageFont


FONTS_REGEX = re.compile(
    br"""{.+?"""
    br"""font-family: ['"](.+?)['"];.+?"""
    br"""src: url\((.+?)\).+?"""
    br"""}""",
    re.DOTALL
)
FONTS_URL_FMT = 'https://fonts.googleapis.com/css?family={fonts}'


class GoogleFontLoader:

    def __init__(self, font_names, url_fmt=FONTS_URL_FMT):
        self.font_names = font_names
        self.url = url_fmt.format(fonts='|'.join(self.font_names))

    def load_bytes_dict(self):
        css = requests.get(self.url).content
        font_info = re.findall(FONTS_REGEX, css)
        return {
            fname.decode(): requests.get(furl).content
            for fname, furl in font_info
        }

    def load_font_dict(self):
        return {
            fname: ImageFont.truetype(io.BytesIO(fbytes))
            for fname, fbytes in self.load_bytes_dict().items()
        }
