"""
https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem
"""
n = int(input().strip())
x = list(map(float, input().strip().split()))
y = list(map(float, input().strip().split()))


def get_rank(x, n):
    x_rank = {a: i+1 for i, a in enumerate(sorted(set(x)))}
    return [x_rank[a] for a in x]


rx = get_rank(x, n)
ry = get_rank(y, n)

d = [(rx[i] - ry[i])**2 for i in range(n)]
p = 1 - (6 * sum(d)) / (n * (n*n - 1))

print(f"{p:.3f}")
