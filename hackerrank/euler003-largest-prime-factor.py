#!/bin/python3
"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler003
"""
import sys


def is_prime(n):
    if n == 2:
        return True
    p1, p2 = 2, n
    while p1 < p2:
        if n % p1 == 0:
            return False
        p2 = n // p1
        p1 += 1
    return True


def largest_prime_factor(n):
    max_prime = n
    p1, p2 = 2, n
    while p1 < p2:
        p2 = n // p1
        if n % p1 == 0:
            if is_prime(p2):
                # Largest prime (from right)
                return p2
            if is_prime(p1):
                # largest prime so far (from left)
                max_prime = p1
        p1 += 1
    return max_prime


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_prime_factor(n))
