from nyanicons.encoder import Encoder


class NanoEncoder(Encoder):
    """
    Nano uses custom base32, 1-9A-Z excluding 0, 2, l, v
    """
    ALPHABET_NANO_BASE32 = "13456789abcdefghijkmnopqrstuwxyz"
    ALPHABET_STD_BASE32 = "0123456789ABCDEFGHIJKLMNOPQRSTUV"
    BASE = len(ALPHABET_NANO_BASE32)
    MAP_NANO_TO_STD = str.maketrans(ALPHABET_NANO_BASE32, ALPHABET_STD_BASE32)
    MAP_STD_TO_NANO = str.maketrans(ALPHABET_STD_BASE32, ALPHABET_NANO_BASE32)

    @property
    def base(self) -> int:
        return self.BASE

    def decode_int(self, encoded_val: str) -> int:
        std_b32_val: str = encoded_val.lower().translate(self.MAP_NANO_TO_STD)
        return int(std_b32_val, self.BASE)

    def encode_int(self, val: int) -> str:
        encoded = ""
        while val:
            encoded += self.ALPHABET_NANO_BASE32[val % self.BASE]
            val //= self.BASE
        return encoded[::-1] or self.ALPHABET_NANO_BASE32[0]
