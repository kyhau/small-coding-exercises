"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler007
"""
import sys

inputs0 = []
t = int(input().strip())
for a0 in range(t):
    inputs0.append(int(input().strip()))

inputs1 = sorted(inputs0)

def is_prime(n):
    if n==2:
        return True
    p1, p2 = 2, n
    while p1 < p2:
        if n % p1 == 0:
            return False
        p2 = n // p1
        p1 += 1
    return True

max_value = inputs1[-1]
primes = []

i = 2
cnt = 0
while cnt < max_value:
    if is_prime(i):
        primes.append(i)
        cnt += 1
    i += 1

for i in inputs0:
    print(primes[i-1])
