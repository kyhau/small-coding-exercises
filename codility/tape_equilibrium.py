"""
Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
See https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/.

Write an efficient algorithm for the following assumptions:
- N is an integer within the range [2..100000]
- each element of array A is an integer within the range -1000..1000
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def solution(A):
    """
    Given a non-empty array A of N integers, returns the minimal difference that can be achieved.
    """
    sum_1 = A[0]
    sum_2 = 0
    for i in range(1, len(A)):
        sum_2 += A[i]

    min_diff = abs(sum_1 - sum_2)

    for i in range(1, len(A)):
        sum_1 += A[i]
        sum_2 -= A[i]
        min_diff = min(abs(sum_1 - sum_2), min_diff)
        if min_diff == 0:
            break  # 0 is the smallest diff you can get, so no need to continue

    return min_diff
