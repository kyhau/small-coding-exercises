"""
Find value that occurs in odd number of elements.
See https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/.

A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element
of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, given array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7

Write an efficient algorithm for the following assumptions:
- N is an odd integer within the range [1..1,000,000];
- each element of array A is an integer within the range [1..1,000,000,000];
- all but one of the values in A occur an even number of times.
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def solution_simple(A):
    # Sort the list of integer first
    sorted_list = sorted(A)

    # Starting from left, comparing 2 elements at a time
    for i in range(0, len(sorted_list)-1, 2):
        if sorted_list[i] != sorted_list[i+1]:
            return sorted_list[i]

    # The last element is the odd occurrence
    return sorted_list[-1]


def solution(A):
    """
    Given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired
    element.
    """
    def func(array, start_pos, end_pos):
        """
        Find the mid point of start_pos and end_pos, find if the odd occurrence item is in the first or second half.
        """
        if start_pos == end_pos:
            return array[start_pos]

        # Find mid pos which is in odd position
        mid_pos = start_pos + int((end_pos-start_pos)/2)
        if mid_pos % 2 == 0:
            mid_pos += 1

        logging.debug(f"{start_pos}, {end_pos}, {mid_pos}")

        if array[mid_pos-1] == array[mid_pos]:
            # The odd occurrence is in between mid_pos+1 and end_pos
            return func(array, start_pos=mid_pos+1, end_pos=end_pos)

        # The odd occurrence is at mid_pos-1
        return array[mid_pos-1]

    # Sort the list of integer first
    sorted_list = sorted(A)
    logging.debug(sorted_list)

    return func(sorted_list, 0, len(sorted_list)-1)
