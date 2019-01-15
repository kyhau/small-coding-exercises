"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler005
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


# Get all primes smaller than n
get_primes = lambda x: [x for x in range(2, n + 1) if is_prime(x)]


def smallest_multiple(n):
    # M is divisible by all numbers from 1 to N iff M is equal to the product of all prime powers p^k
    # where p is prime and divides M, and p < N, and k is the largest integer such that p^k <= N.
    # For example, 2520 = 2^3 * 3^2 * 5 * 7.

    ret = []
    primes = get_primes(n)

    for base in primes:
        max_base_power = base
        for power in primes:
            if base ** power <= n:
                max_base_power = base ** power
            else:
                break
        ret.append(max_base_power)

    result = 1
    for i in ret:
        result *= i
    return result


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(smallest_multiple(n))
