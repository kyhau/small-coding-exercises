"""
https://www.hackerrank.com/challenges/flipping-bits/problem
"""
import math
import os
import random
import re
import sys


# Complete the flippingBits function below.
def flippingBits(n):

    #def decimal_to_binary(n):
    #    return bin(n)[2:]

    #def binary_to_decimal(n):
    #    return int(n,2)

    #b = decimal_to_binary(n)
    #b = f'{b:0>{32}}'

    # Simpler
    return n ^ 0xffffffff

