from math import pow
import pytest
import binary_gap


@pytest.mark.parametrize("test_input,expected_values", [
    (9, (1001, 2)),
    (15, (1111, 0)),  # all 1s
    (20, (10100, 1)),
    (32, (100000, 0)),
    (529, (1000010001, 4)),
    (1041, (10000010001, 5)),
    (1107312642, (1000010000000000100000000000010, 12)),
    (2147483647, (1111111111111111111111111111111, 0)),
])
def test_binary_gap_solution(test_input, expected_values):
    expected_binary, expected_binary_gap = expected_values

    assert binary_gap.decimal_to_binary(test_input) == expected_binary

    assert binary_gap.solution(test_input) == expected_binary_gap
