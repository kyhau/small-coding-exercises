"""
https://www.hackerrank.com/challenges/diagonal-difference/problem
"""


# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    w = len(arr)
    s1 = sum(arr[i][i] for i in range(w))
    s2 = sum(arr[i][w-1-i] for i in range(w))
    return abs(s1-s2)
