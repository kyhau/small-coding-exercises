"""
https://www.hackerrank.com/challenges/minimum-swaps-2/problem
"""
import math
import os
import random
import re
import sys

import logging
logging.basicConfig(level=logging.INFO)

# Ref: https://stackoverflow.com/questions/15152322/compute-the-minimal-number-of-swaps-to-order-a-sequence/15152602#15152602

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

# Complete the minimumSwaps function below.
def minimumSwaps(arr):

    # Semantically you sort the elements and then figure out how to put them to the initial state
    # via swapping through the leftmost item that is out of place.

    annotated = [*enumerate(arr)]
    logging.debug(annotated)
    # DEBUG:root:[(0, 7), (1, 1), (2, 3), (3, 2), (4, 4), (5, 5), (6, 6)]

    annotated.sort(key = lambda it: it[1])
    logging.debug(annotated)
    # DEBUG:root:[(1, 1), (3, 2), (2, 3), (4, 4), (5, 5), (6, 6), (0, 7)]

    count = 0
    i = 0
    while i < len(arr):
        if annotated[i][0] == i:
            # In the right position, no action required
            i += 1
            continue
        swap(annotated, i, annotated[i][0])
        count += 1

    return count


if __name__ == '__main__':
    arr = [7, 1, 3, 2, 4, 5, 6]
    res = minimumSwaps(arr)
    print(res)
