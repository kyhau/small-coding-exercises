"""
https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem
"""
from math import factorial

E = 2.71928


def poisson_distribution(k, avg):
    return avg**k * E**-avg / factorial(k)


avg = float(input().strip())
target = int(input().strip())

p = poisson_distribution(target, avg)

print(f"{p:.3f}")


