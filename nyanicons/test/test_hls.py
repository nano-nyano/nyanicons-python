from typing import Tuple

import pytest

from nyanicons.hls import HLS


@pytest.mark.parametrize(
    "hls",
    [
        (HLS(0, 0, 0)),
        (HLS(0.5, 0.5, 0.5)),
        (HLS(1, 1, 1)),
    ]
)
def test_to_tuple(hls: HLS):
    assert hls.to_tuple() == (hls.h_val, hls.l_val, hls.s_val)


@pytest.mark.parametrize(
    "hls,exp_compliments",
    [
        (HLS(0, 0, 0), (HLS(0.333, 0, 0), HLS(0.667, 0, 0))),
        (HLS(0.5, 0.5, 0.5), (HLS(.833, 0.5, 0.5), HLS(0.167, 0.5, 0.5))),
        (HLS(1, 1, 1), (HLS(0.333, 1, 1), HLS(0.667, 1, 1))),
    ]
)
def test_triadic_complements(hls: HLS, exp_compliments: Tuple[HLS, HLS]):
    for t, e in zip(hls.triadic_complements(), exp_compliments):
        assert t == e


@pytest.mark.parametrize(
    "hls,exp_compliment",
    [
        (HLS(0, 0, 0), HLS(0, 0.333, 0)),
        (HLS(0.5, 0.5, 0.5), HLS(0.5, 0.167, 0.5)),
        (HLS(0.49, 0.49, 0.49), HLS(0.49, 0.823, 0.49)),
        (HLS(1, 1, 1), HLS(1, 0.667, 1)),
    ]
)
def test_monochrome_compliment(hls: HLS, exp_compliment: HLS):
    assert hls.monochrome_compliment() == exp_compliment


@pytest.mark.parametrize(
    "hls,exp_desaturated",
    [
        (HLS(0, 0, 0), HLS(0, 0, 0)),
        (HLS(0.5, 0.5, 0.5), HLS(0.5, 0.5, 0)),
        (HLS(1, 1, 1), HLS(1, 1, 0)),
    ]
)
def test_desaturate(hls: HLS, exp_desaturated: HLS):
    assert hls.desaturate() == exp_desaturated
