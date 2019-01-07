"""
Count minimal number of jumps from position X to Y.
See https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/.
"""
import math

def solution(X, Y, D):
    """
    Given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or
    greater than Y.
    """
    return math.ceil((Y-X)/D)
