"""
Find the missing element in a given permutation.
See https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/.
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def solution(A):
    """
    Given an array A, returns the value of the missing element.
    """
    def func(array, start_pos, end_pos):
        """Binary search Best/Average/Worst: O(1)/O(log n)/O(log n)
        """
        if start_pos >= end_pos:
            return array[start_pos]-1

        mid_pos = start_pos + int((end_pos-start_pos)/2)
        logging.debug(f"{start_pos}, {end_pos}, {mid_pos}")

        if mid_pos == array[mid_pos]-1:
            return func(array, start_pos=mid_pos+1, end_pos=end_pos)

        return func(array, start_pos=start_pos, end_pos=mid_pos-1)

    # Sort the list of integer first
    sorted_array = sorted(A)
    logging.debug(sorted_array)

    return func(sorted_array, 0, len(sorted_array)-1)
