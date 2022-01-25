import pytest as pytest

from nyanicons.nano_encoder import NanoEncoder


@pytest.fixture()
def encoder() -> NanoEncoder:
    return NanoEncoder()


@pytest.mark.parametrize(
    "encoded_val,exp_decoded",
    [
        ('1', 0),
        ('a', 8),
        ('z', 31),
        ('a1', 256),
        ('zz', 1023),
        ('xno1', 971424),
        ('XNO1', 971424),
    ]
)
def test_decode_int(encoded_val: str, exp_decoded: int, encoder: NanoEncoder):
    assert encoder.decode_int(encoded_val) == exp_decoded


@pytest.mark.parametrize(
    "val,exp_encoded",
    [
        (0, '1'),
        (8, 'a'),
        (31, 'z'),
        (256, 'a1'),
        (1023, 'zz'),
        (971424, 'xno1'),
    ]
)
def test_encode_int(val: int, exp_encoded: str, encoder: NanoEncoder):
    assert encoder.encode_int(val) == exp_encoded
