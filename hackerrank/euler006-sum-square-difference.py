"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler006
"""
import sys

"""
1) sum of first n natural numbers = n*(n+1)/2
2) sum of first n natural numbers individual squares = n*(n+1)*(2*n+1)/6
"""

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    sum1 = (n * (n + 1) // 2) ** 2
    sum2 = n * (n + 1) * (2 * n + 1) // 6
    print(abs(sum1 - sum2))