"""
Check whether array A is permutation.
See https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/.
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def solution(A):
    """
    Given an array A, returns 1 if array A is a permutation and 0 if it is not.
    """
    sorted_array = sorted(A)
    logging.debug(sorted_array)
    return 1 if sorted_array[0] == 1 \
                and sorted_array[-1] == len(sorted_array) \
                and list(set(A)) == sorted_array \
        else 0
