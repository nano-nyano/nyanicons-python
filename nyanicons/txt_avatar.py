from typing import List

from nyanicons.color_scheme import ColorScheme
from nyanicons.nano_address import NanoAddress


class TxtAvatar:
    def __init__(self, address: NanoAddress, color_scheme: ColorScheme, components: List[str]):
        self.address: NanoAddress = address
        self.color_scheme: ColorScheme = color_scheme
        self.components: List[str] = components

    def __hash__(self):
        vals = hash(self.address), hash(self.color_scheme), hash(set(self.components))
        return hash(vals)

    def __eq__(self, other):
        return hash(other) == hash(self)
