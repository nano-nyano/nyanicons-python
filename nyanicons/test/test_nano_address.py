import pytest

from nyanicons.nano_address import InvalidNanoAddress, NanoAddress


@pytest.mark.parametrize(
    "address,exp_valid",
    [
        ('nano_3arg3asgtigae3xckabaaewkx3bzsh7nwz7jkmjos79ihyaxwphhm6qgjps4', True),
        ('nano_1ookerz3adg5rxc4zwwoshim5yyyihf6dpogjihwwq6ksjpq7ea4fuam5mmc', True),
        ('xrb_3arg3asgtigae3xckabaaewkx3bzsh7nwz7jkmjos79ihyaxwphhm6qgjps4', True),
        ('xrb_1ookerz3adg5rxc4zwwoshim5yyyihf6dpogjihwwq6ksjpq7ea4fuam5mmc', True),
        ('foo_3arg3asgtigae3xckabaaewkx3bzsh7nwz7jkmjos79ihyaxwphhm6qgjps4', False),
        ('nano_3arg3asgtigae3xckabaaewkx3bzsh7nz7jkmjos79ihyaxwphhm6qgjps4', False),
        ('nano_1ookerz3adg5rxc4zwwosim5yyyihf6dpogjihwwq6ksjpq7ea4fuam5mmc', False),
        ('nano_3arg3asgtigae3xckabaaewkx3bzsh7nwz7jkmjos79ihyaxwphhm6qgjps4x', False),
        ('nano_1ookerz3adg5rxc4zwwoshim5yyyihf6dpogjihwwq6ksjpq7ea4fuam5mmcx', False),
        ('nano_3arg3asgtigae3xckabaaewkx3bzsh7nwz7j===kmjos79ihyaxwphhm6qgjps4', False),
        ('nano_1ookerz3adg5rxc4zwwoshim5yyyihf6dpog===jihwwq6ksjpq7ea4fuam5mmc', False),
    ]
)
def test_valid(address: str, exp_valid: bool):
    if exp_valid:
        NanoAddress(address)
    else:
        with pytest.raises(InvalidNanoAddress):
            NanoAddress(address)


@pytest.mark.parametrize(
    "address,exp_prefix,exp_pub_key,exp_checksum",
    [
        ('nano_3arg3asgtigae3xckabaaewkx3bzsh7nwz7jkmjos79ihyaxwphhm6qgjps4', 'nano', '3arg3asgtigae3xckabaaewkx3bzsh7nwz7jkmjos79ihyaxwphh', 'm6qgjps4'),
        ('xrb_3arg3asgtigae3xckabaaewkx3bzsh7nwz7jkmjos79ihyaxwphhm6qgjps4', 'xrb', '3arg3asgtigae3xckabaaewkx3bzsh7nwz7jkmjos79ihyaxwphh', 'm6qgjps4'),
        ('nano_1ookerz3adg5rxc4zwwoshim5yyyihf6dpogjihwwq6ksjpq7ea4fuam5mmc', 'nano', '1ookerz3adg5rxc4zwwoshim5yyyihf6dpogjihwwq6ksjpq7ea4', 'fuam5mmc'),
        ('xrb_1ookerz3adg5rxc4zwwoshim5yyyihf6dpogjihwwq6ksjpq7ea4fuam5mmc', 'xrb', '1ookerz3adg5rxc4zwwoshim5yyyihf6dpogjihwwq6ksjpq7ea4', 'fuam5mmc'),
    ]
)
def test_parts(address: str, exp_prefix: str, exp_pub_key: str, exp_checksum: str):
    address = NanoAddress(address)

    assert address.prefix == exp_prefix
    assert address.pub_key == exp_pub_key
    assert address.checksum == exp_checksum
