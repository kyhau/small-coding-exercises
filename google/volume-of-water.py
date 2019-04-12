"""
https://techdevguide.withgoogle.com/paths/advanced/sequence-2/volume-of-water/#!
https://leetcode.com/problems/trapping-rain-water/
"""


def func(x):
    # From left to right
    x1 = x.copy()
    max_left = 0
    for i in range(len(x1)):
        if max_left > x1[i]:
            x1[i] = max_left
        elif max_left < x1[i]:
            max_left = x1[i]

    # From right to left, also compare with x1, and calc the diff to x
    x2 = x.copy()
    max_right = 0
    for i in range(len(x2)-1, -1, -1):
        if x2[i] > max_right:
            max_right = x2[i]
        x2[i] = min(max_right, x1[i]) - x[i]

    # x  = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]
    # x1 = [1, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    # x2 = [0, 0, 1, 0, 3, 1, 3, 0, 0, 2, 2, 3, 0, 0, 0]
    return sum(x2)


ret = func([1,3,2,4,1,3,1,4,5,2,2,1,4,2,2])
assert ret == 15

ret = func([0,1,0,2,1,0,1,3,2,1,2,1])
assert ret == 6