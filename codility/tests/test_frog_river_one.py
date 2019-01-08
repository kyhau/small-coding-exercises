import pytest
import frog_river_one


@pytest.mark.parametrize("test_input,expected", [
    ((5, [1, 3, 1, 4, 2, 3, 5, 4]), 6),
    ((5, [1, 5, 1, 4, 2, 2, 5, 4]), -1),
])
def test_frog_river_one_solution(test_input, expected):
    x, a = test_input
    assert frog_river_one.solution(x, a) == expected
