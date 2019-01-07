import pytest
import odd_occurrences_in_array


SAMPLE_1 = [9, 3, 9, 3, 9, 7, 9]
SAMPLE_2 = [111, 11, 1111, 1111, 11, 1111, 111, 1, 1, 1111, 1111]
SAMPLE_3 = [1, 3, 5, 7, 9, 11, 13, 15, 1, 3, 5, 7, 9, 11, 13, 15, 12]

@pytest.mark.parametrize("test_input,expected", [
    (SAMPLE_1, 7),
    (SAMPLE_2, 1111),
    (SAMPLE_3, 12),
])
def test_odd_occurrences_in_array(test_input, expected):

    assert odd_occurrences_in_array.solution(test_input) == expected

    assert odd_occurrences_in_array.solution_simple(test_input) == expected
