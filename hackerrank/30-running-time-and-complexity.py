"""
https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True

    v, last = 2, n
    while v <= last:
        if n % v == 0:
            return False
        v += 1
        last = n // v
    return True

N = int(input().strip())

for i in range(N):
    num = int(input().strip())
    print("Prime" if is_prime(num) else "Not prime")
