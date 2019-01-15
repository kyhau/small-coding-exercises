#!/bin/python3
"""
https://www.hackerrank.com/challenges/crush/problem
"""

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

    # Instead of storing the actual values in the array, store the difference between the current element
    # and the previous element.

    ret = [0]*(n+1)
    for q in queries:
        a, b, k = q
        ret[a] += k
        if b+1<=n:
            ret[b+1] -= k

    max_value, tmp = 0, 0
    for i in ret:
        tmp += i
        max_value = max(max_value, tmp)
    return max_value
