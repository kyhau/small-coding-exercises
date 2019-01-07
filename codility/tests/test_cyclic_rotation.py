import pytest
import cyclic_rotation

"""
For example, given
    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:
    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

For another example, given
    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given
    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]
"""


@pytest.mark.parametrize("test_inputs,expected", [
    (([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8]),
    (([0, 0, 0], 1), [0, 0, 0]),
    (([1, 2, 3, 4], 4), [1, 2, 3, 4]),
])
def test_cyclic_rotation_solution(test_inputs, expected):
    ori_array, rotate_times = test_inputs

    assert cyclic_rotation.solution(ori_array, rotate_times) == expected

