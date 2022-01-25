from abc import ABC, abstractmethod


class Encoder(ABC):
    @property
    @abstractmethod
    def base(self) -> int: pass

    @abstractmethod
    def decode_int(self, encoded_val: str) -> int: pass

    @abstractmethod
    def encode_int(self, val: int) -> str: pass

    def max_value_for_encoded(self, encoded_val: str) -> int:
        return self.base ** len(encoded_val)
