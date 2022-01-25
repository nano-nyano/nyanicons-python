import pytest

from nyanicons.hls import HLS
from nyanicons.svg_util import SVGUtil


@pytest.mark.parametrize(
    "hls,exp_svg_format",
    [
        (HLS(0, 0, 0), "rgb(0, 0, 0)"),
        (HLS(0.5, 0.5, 0.5), "rgb(63, 191, 191)"),
        (HLS(1, 1, 1), "rgb(255, 255, 255)"),
        (HLS(0.1, 0.2, 0.3), "rgb(66, 54, 35)"),
    ]
)
def test_format_rgb_255(hls: HLS, exp_svg_format: str):
    assert SVGUtil.format_rgb_255(hls) == exp_svg_format


@pytest.mark.parametrize(
    "hls,exp_svg_format",
    [
        (HLS(0, 0, 0), "rgb(0%, 0%, 0%)"),
        (HLS(0.5, 0.5, 0.5), "rgb(25.0%, 75.0%, 75.0%)"),
        (HLS(1, 1, 1), "rgb(100%, 100.0%, 100.0%)"),
        (HLS(0.1, 0.2, 0.3), "rgb(26.0%, 21.2%, 14.0%)"),
    ]
)
def test_format_rgb_percent(hls: HLS, exp_svg_format: str):
    assert SVGUtil.format_rgb_percent(hls) == exp_svg_format
