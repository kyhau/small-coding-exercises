import pytest

# Convert decimal to binary with bin(), which returns result with prefix `0b`.
decimal_to_binary = lambda x : int(bin(x)[2:])


@pytest.mark.parametrize("test_input,expected", [
    (9, 1001),
    (15, 1111),
    (20, 10100),
    (32, 100000),
    (529, 1000010001),
    (1041, 10000010001),
    (2147483647, 1111111111111111111111111111111),
])
def test_binary_gap_solution(test_input, expected):
    assert decimal_to_binary(test_input) == expected
