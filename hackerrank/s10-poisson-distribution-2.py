"""
https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem
"""
a, b = list(map(float, input().strip().split()))

ca = 160 + 40 * (a + a**2)
cb = 128 + 40 * (b + b**2)

print(f"{ca:.3f}")
print(f"{cb:.3f}")

# 226.176
# 286.100

