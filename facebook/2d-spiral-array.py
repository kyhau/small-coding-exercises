"""
Find the pattern and complete the function:
int[][] spiral(int n);
where n is the size of the 2D array.
"""

import numpy as np  # for printing 2D matrix only


def print_ret(ret):
    print(np.matrix(ret))


def spiral(n):

    # Note: [[foo]*10]*10 creates a list of the same object repeated 10 times.

    # x[:] is equivalent to list(X)
    ret = [x[:] for x in [[0] * n] * n]

    v = 1
    try:
        for i in range(round(n/2)):

            # Top unfilled row, left to right
            r = i
            for c in range(i, n-i):
                ret[r][c] = v
                v += 1

            # Rightmost unfilled col, top to bottom
            c = n-1-i
            for r in range(i+1, n-i):
                ret[r][c] = v
                v += 1

            # Bottom unfilled row, right to left
            r = n-1-i
            for c in range(n-i-2, i-1, -1):
                ret[r][c] = v
                v += 1

            # leftmost unfilled col, bottom to top, unfilled slot only
            c = i
            for r in range(n-i-2, i, -1):
                ret[r][c] = v
                v += 1

    except Exception as e:
        print(r, c, v)
        raise
    return ret


ret = spiral(8)
print_ret(ret)

"""
input = 3
123
894
765

input = 4
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07

input = 8
1 2 3 4 5 6 7 8
28 29 30 31 32 33 34 9
27 48 49 50 51 52 35 10
26 47 60 61 62 53 36 11
25 46 59 64 63 54 37 12
24 45 58 57 56 55 38 13
23 44 43 42 41 40 39 14
22 21 20 19 18 17 16 15
"""