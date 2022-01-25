from typing import List

import pytest

from nyanicons.color_scheme import ColorScheme
from nyanicons.encoder import Encoder
from nyanicons.hls import HLS
from nyanicons.nano_encoder import NanoEncoder
from nyanicons.txt_avatar_generator import TxtAvatarGenerator


@pytest.fixture()
def encoder() -> Encoder:
    return NanoEncoder()


@pytest.mark.parametrize(
    "components_dir,exp_component_cnts",
    [
        ("./resources/txt_avatar_components/", [2, 4, 3, 6, 9, 1]),
    ]
)
def test_init(components_dir: str, exp_component_cnts: List[int], encoder: Encoder):
    txt_avatar_generator = TxtAvatarGenerator(components_dir, encoder)

    assert len(txt_avatar_generator.component_categories) == len(exp_component_cnts)
    for component_category, exp_cnt in zip(txt_avatar_generator.component_categories, exp_component_cnts):
        assert len(component_category.components) == exp_cnt


@pytest.mark.parametrize(
    "components_dir,nano_address,exp_primary_color,exp_components",
    [
        (
            "./resources/txt_avatar_components/",
            "nano_3arg3asgtigae3xckabaaewkx3bzsh7nwz7jkmjos79ihyaxwphhm6qgjps4",
            HLS(0.04, 0.469, 1),
            [
                'head_classic_stripes rgb(239, 57, 0) rgb(255, 178, 154)',
                'collar_striped_hor rgb(0, 239, 56) rgb(119, 119, 119) rgb(57, 0, 239)',
                'eyes_open',
                'mouth_smile',
                'hat_cap_backwards_solid rgb(0, 239, 56)',
                'acc_none',
            ]
        ),
        (
            "./resources/txt_avatar_components/",
            "nano_37imps4zk1dfahkqweqa91xpysacb7scqxf3jqhktepeofcxqnpx531b3mnt",
            HLS(0.037, 0.558, 1),
            [
                'head_classic_solid rgb(255, 79, 29)',
                'collar_solid rgb(29, 255, 78) rgb(79, 29, 255)',
                'eyes_shut_down',
                'mouth_serious',
                'hat_beanie_striped rgb(29, 255, 78) rgb(142, 142, 142)',
                'acc_none',
            ]
        ),
        (
            "./resources/txt_avatar_components/",
            "nano_1natrium1o3z5519ifou7xii8crpxpk8y65qmkih8e8bpsjri651oza8imdd",
            HLS(0.02, 0.668, 1),
            [
                'head_classic_solid rgb(255, 105, 85)',
                'collar_striped_vert rgb(85, 255, 105) rgb(170, 170, 170) rgb(106, 85, 255)',
                'eyes_shut_happy',
                'mouth_smile_2_teeth',
                'hat_paper',
                'acc_none',
            ]
        ),
    ]
)
def test_generate_avatar(components_dir: str,
                         nano_address: str,
                         exp_primary_color: HLS,
                         exp_components: List[str],
                         encoder: Encoder):
    generator = TxtAvatarGenerator(components_dir, encoder)
    avatar = generator.generate_avatar(nano_address)
    exp_color_scheme = ColorScheme(exp_primary_color)

    assert avatar.color_scheme == exp_color_scheme
    for c, exp_c in zip(avatar.components, exp_components):
        assert c == exp_c
