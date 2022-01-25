import colorsys
from typing import Tuple


class HLS:
    def __init__(self, h_val: float, l_val: float, s_val: float):
        self.h_val: float = h_val
        self.l_val: float = l_val
        self.s_val: float = s_val

    def __hash__(self):
        vals = round(self.h_val, 3), round(self.l_val, 3), round(self.s_val, 3)
        return hash(vals)

    def __eq__(self, other):
        return hash(other) == hash(self)

    def to_tuple(self) -> Tuple[float, float, float]:
        return self.h_val, self.l_val, self.s_val

    def triadic_complements(self) -> ('HLS', 'HLS'):
        """
        Returns the triadic compliments to this color. Adds/subtracts 0.333 to H value.
        :return:
        """
        h1 = (self.h_val + 0.333) % 1
        h2 = (self.h_val - 0.333) % 1

        return HLS(h1, self.l_val, self.s_val), HLS(h2, self.l_val, self.s_val)

    def monochrome_compliment(self) -> 'HLS':
        """
        Returns a monochromatic compliment to this color. Adds 0.333 to L if L<.5 or subtracts 0.333.
        from L if L>=.5
        :return:
        """
        ml = self.l_val
        ml += 0.333 if ml < 0.5 else -0.333

        return HLS(self.h_val, ml, self.s_val)

    def desaturate(self) -> 'HLS':
        """
        Returns the desaturation of this color. Sets S to 0.
        :return:
        """
        return HLS(self.h_val, self.l_val, 0.0)
