#!/bin/python3
"""
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
"""


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):

    # Absolute min must be from the pair that the 2 numbers are closest.
    # So sort arr first, then compare a number only with the next one on the list
    arr.sort()

    abs_min = None
    for i in range(len(arr)-1):
        m = abs(arr[i]-arr[i+1])
        abs_min = m if abs_min is None else min(m, abs_min)

    return abs_min
