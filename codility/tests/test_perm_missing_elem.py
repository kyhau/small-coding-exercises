import pytest
import perm_missing_elem


@pytest.mark.parametrize("test_input,expected", [
    ([2, 3, 1, 5], 4),
    ([2, 3, 1, 5, 4, 6, 8, 7, 10], 9),
])
def test_perm_missing_elem_solution(test_input, expected):
    assert perm_missing_elem.solution(test_input) == expected
