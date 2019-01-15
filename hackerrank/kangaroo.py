"""
https://www.hackerrank.com/challenges/kangaroo/problem
"""

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    #     x1 + v1 * n = x2 + v2 * n
    # =>  n = (x1 - x2) / (v2 - v1)

    if v1 == v2:
        return "YES" if x1 == x2 else "NO"

    r1 = (x1 - x2) / (v2 - v1)
    r2 = (x1 - x2) // (v2 - v1)
    if r1 >= 0 and r1 - r2 == 0:
        return "YES"
    return "NO"
