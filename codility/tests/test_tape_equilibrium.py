import pytest
import tape_equilibrium


@pytest.mark.parametrize("test_input,expected", [
    ([3, 1, 2, 4, 3], 1),
])
def test_tape_equilibrium_solution(test_input, expected):
    assert tape_equilibrium.solution(test_input) == expected
