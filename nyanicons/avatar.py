from typing import List

from svgutils.transform import SVGFigure

from nyanicons.color_scheme import ColorScheme
from nyanicons.nano_address import NanoAddress


class Avatar:
    def __init__(self, address: NanoAddress, color_scheme: ColorScheme, components: List[SVGFigure]):
        self._address: NanoAddress = address
        self._color_scheme: ColorScheme = color_scheme
        self._components: List[SVGFigure] = components

    def __hash__(self):
        vals = hash(self._address), hash(self._color_scheme), hash(set(self._components))
        return hash(vals)

    def __eq__(self, other):
        return hash(other) == hash(self)
