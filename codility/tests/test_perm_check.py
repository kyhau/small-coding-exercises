import pytest
import perm_check


@pytest.mark.parametrize("test_input,expected", [
    ([4, 1, 3, 2], 1),
    ([4, 1, 3], 0),
])
def test_perm_check_solution(test_input, expected):
    assert perm_check.solution(test_input) == expected
