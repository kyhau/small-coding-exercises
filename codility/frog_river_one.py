"""
Find the earliest time when a frog can jump to the other side of a river.
See https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/.
"""
import logging
import random

logging.basicConfig(level=logging.DEBUG)


# N (len of array A) and X are integers within the range [1..100,000];
random_int_100000 = lambda x : range(random.randint(1, 100000))

# Each element of array A is an integer within the range [1..X].
random_A = lambda X, N: [random.randint(1, X) for n in range(random.randint(1, N))]


def solution(X, A):
    """
    Given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump
    to the other side of the river.

    Write an efficient algorithm for the following assumptions:
    - N and X are integers within the range [1..100,000];
    - each element of array A is an integer within the range [1..X].
    """

    # Create int array to indicate if a number smaller than X is found.
    checked_nums = [0] * X

    i = 0
    while i < len(A):
        checked_nums[A[i]-1] = 1
        logging.debug(f"{i}, {A[i]}, {checked_nums}")

        if 0 not in checked_nums:
            break
        i += 1

    return -1 if i == len(A) else i
