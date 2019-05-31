"""
https://www.hackerrank.com/challenges/pairs/problem
"""


def pairs(k, arr):
    return len(set(arr) & set(a+k for a in arr))
