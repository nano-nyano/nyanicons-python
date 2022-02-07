import os
from typing import List

from nyanicons import svg_util
from nyanicons.color_scheme import ColorScheme
from nyanicons.encoder import Encoder
from nyanicons.hls import HLS
from nyanicons.nano_address import NanoAddress
from nyanicons.txt_avatar import TxtAvatar
from nyanicons.txt_avatar_component_category import TxtAvatarComponentCategory


class TxtAvatarGenerator:

    def __init__(self, components_dir: str, encoder: Encoder):
        self._components_dir: str = os.fsdecode(components_dir)
        self.component_categories: List[TxtAvatarComponentCategory] = self._load_components(self._components_dir)
        self._encoder: Encoder = encoder

    @staticmethod
    def _load_components(components_dir: str) -> List[TxtAvatarComponentCategory]:
        paths = [os.path.join(components_dir, p) for p in os.listdir(components_dir)]
        paths.sort()  # Sort alphanumerically (default) so that components are appended in correct order
        component_category_dirs = [p for p in paths if os.path.isdir(p)]

        component_categories = [TxtAvatarComponentCategory(d) for d in component_category_dirs]

        return component_categories

    def generate_avatar(self, address: str) -> TxtAvatar:
        nano_address = NanoAddress(address)
        pub_key = nano_address.pub_key

        chunk_cnt = len(self.component_categories) + 1  # +1 for base color chunk
        pub_key_chunks: List[str] = [pub_key[i:i + chunk_cnt] for i in range(0, len(pub_key), chunk_cnt)]

        primary_color_chunk = pub_key_chunks.pop(0)
        primary_color: HLS = self._generate_primary_color(primary_color_chunk)
        color_scheme = ColorScheme(primary_color)

        component_chunks = zip(self.component_categories, pub_key_chunks)
        components: List[str] = []
        for component_category, chunk in component_chunks:
            component: str = self._generate_component(component_category, chunk, color_scheme)
            components.append(component)

        return TxtAvatar(nano_address, color_scheme, components)

    def _generate_primary_color(self, primary_color_chunk: str) -> HLS:
        h_chunk = primary_color_chunk[:int(len(primary_color_chunk)/2)]
        l_chunk = primary_color_chunk[int(len(primary_color_chunk)/2):]
        h_max = self._encoder.max_value_for_encoded(h_chunk)
        l_max = self._encoder.max_value_for_encoded(l_chunk)

        h_val = self._encoder.decode_int(h_chunk) / h_max
        s_val = 1  # use full saturation
        l_val = 0.25 + 0.5 * (self._encoder.decode_int(l_chunk) / l_max)  # normalize lightness between 0.25 & 0.75

        return HLS(h_val, l_val, s_val)

    def _generate_component(self,
                            component_category: TxtAvatarComponentCategory,
                            chunk: str,
                            color_scheme: ColorScheme) -> str:
        raw_value: int = self._encoder.decode_int(chunk)
        max_raw_value: int = self._encoder.max_value_for_encoded(chunk)
        max_component_idx: int = len(component_category.components) - 1

        component_idx: int = int(round(max_component_idx * raw_value / max_raw_value))
        component: str = component_category.components[component_idx]
        component = self._colorize_component(component, color_scheme)

        return component

    @staticmethod
    def _colorize_component(component: str, color_scheme: ColorScheme) -> str:
        component = component.replace('COLOR_PRIMARY', svg_util.format_rgb_255(color_scheme.primary))
        component = component.replace('COLOR_SECONDARY', svg_util.format_rgb_255(color_scheme.secondary))
        component = component.replace('COLOR_TERTIARY', svg_util.format_rgb_255(color_scheme.tertiary))
        component = component.replace('COLOR_MONOCHROME', svg_util.format_rgb_255(color_scheme.monochrome))
        component = component.replace('COLOR_GRAYSCALE', svg_util.format_rgb_255(color_scheme.grayscale))

        return component
