import pytest

from easy.chuck_norris import norris_binary
from easy.temperatures import closest_to_zero

TEST_TEMPERATURE = [([1, -2, -8, 4, 5], 1),
                    ([-12, -5, -137], -5),
                    ([42, -5, 12, 21, 5, 24], 5),
                    ([42, 5, 12, 21, -5, 24], 5),
                    ([-5, -4, -2, 12, -40, 4, 2, 18, 11, 5], 2)]


TEST_CHUCK_NORRIS = [("C", "0 0 00 0000 0 00"),
                     ("CC", "0 0 00 0000 0 000 00 0000 0 00"),
                     ("%", "00 0 0 0 00 00 0 0 00 0 0 0"),
                     ("Chuck Norris' keyboard has 2 keys: 0 and white space.", "0 0 00 0000 0 0000 00 0 0 0 00 000 0 000 00 0 0 0 00 0 0 000 00 000 0 0000 00 0 0 0 00 0 0 00 00 0 0 0 00 00000 0 0 00 00 0 000 00 0 0 00 00 0 0 0000000 00 00 0 0 00 0 0 000 00 00 0 0 00 0 0 00 00 0 0 0 00 00 0 0000 00 00 0 00 00 0 0 0 00 00 0 000 00 0 0 0 00 00000 0 00 00 0 0 0 00 0 0 0000 00 00 0 0 00 0 0 00000 00 00 0 000 00 000 0 0 00 0 0 00 00 0 0 000000 00 0000 0 0000 00 00 0 0 00 0 0 00 00 00 0 0 00 000 0 0 00 00000 0 00 00 0 0 0 00 000 0 00 00 0000 0 0000 00 00 0 00 00 0 0 0 00 000000 0 00 00 00 0 0 00 00 0 0 00 00000 0 00 00 0 0 0 00 0 0 0000 00 00 0 0 00 0 0 00000 00 00 0 0000 00 00 0 00 00 0 0 000 00 0 0 0 00 00 0 0 00 000000 0 00 00 00000 0 0 00 00000 0 00 00 0000 0 000 00 0 0 000 00 0 0 00 00 00 0 0 00 000 0 0 00 00000 0 000 00 0 0 00000 00 0 0 0 00 000 0 00 00 0 0 0 00 00 0 0000 00 0 0 0 00 00 0 00 00 00 0 0 00 0 0 0 00 0 0 0 00 00000 0 000 00 00 0 00000 00 0000 0 00 00 0000 0 000 00 000 0 0000 00 00 0 0 00 0 0 0 00 0 0 0 00 0 0 000 00 0")]


@pytest.mark.parametrize("temps,output", TEST_TEMPERATURE)
def test_temperatures(temps, output):
    closest_to_zero(temps)
    assert closest_to_zero(temps) == output


@pytest.mark.parametrize("input,output", TEST_CHUCK_NORRIS)
def test_norris_binary(input, output):
    assert norris_binary(input) == output