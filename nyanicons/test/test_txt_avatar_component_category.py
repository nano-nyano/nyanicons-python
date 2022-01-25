import pytest

from nyanicons.txt_avatar_component_category import TxtAvatarComponentCategory


@pytest.mark.parametrize(
    "component_dir,exp_component_cnt",
    [
        ("./resources/txt_avatar_components/01_head/", 2),
        ("./resources/txt_avatar_components/02_collar/", 4),
        ("./resources/txt_avatar_components/03_eyes/", 3),
        ("./resources/txt_avatar_components/04_mouth/", 6),
        ("./resources/txt_avatar_components/05_hat/", 9),
        ("./resources/txt_avatar_components/06_accessory/", 1),
    ]
)
def test_init(component_dir: str, exp_component_cnt: int):
    component_category = TxtAvatarComponentCategory(component_dir)
    assert len(component_category.components) == exp_component_cnt
