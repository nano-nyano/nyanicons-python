import re


class InvalidNanoAddress(ValueError):
    pass


class NanoAddress:
    NANO_ADDRESS_REGEX = re.compile("^(nano|xrb)_[13]{1}[13456789abcdefghijkmnopqrstuwxyz]{59}$")

    def __init__(self, address: str):
        address = address.lower()
        if self.NANO_ADDRESS_REGEX.match(address) is None:
            raise InvalidNanoAddress(f"{address} is not a valid Nano address")

        self._full_address = address
        self._prefix, pub_key_and_checksum = address.split('_')
        self._pub_key = pub_key_and_checksum[:52]
        self._checksum = pub_key_and_checksum[-8:]

    @property
    def full_address(self) -> str:
        return self._full_address

    @property
    def prefix(self) -> str:
        return self._prefix

    @property
    def pub_key(self) -> str:
        return self._pub_key

    @property
    def checksum(self) -> str:
        return self._checksum
