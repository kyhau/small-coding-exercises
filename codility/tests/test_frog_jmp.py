import pytest
import frog_jmp

@pytest.mark.parametrize("test_inputs,expected", [
    ([10, 85, 30], 3),
    ([10, 101, 30], 4),
])
def test_frog_jmp_solution(test_inputs, expected):
    x, y, d = test_inputs
    assert frog_jmp.solution(x, y, d) == expected
