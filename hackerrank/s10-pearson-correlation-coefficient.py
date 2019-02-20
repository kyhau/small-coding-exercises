"""
https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem
"""
n = int(input().strip())
x = list(map(float, input().strip().split()))
y = list(map(float, input().strip().split()))


def pearson_correlation_coefficient(x, y, n):
    mean = lambda x: sum(a for a in x)/n
    mean_x = mean(x)
    mean_y = mean(y)

    std = lambda s, mean: (sum([(a - mean)**2 for a in s])/n)**0.5
    std_x = std(x, mean_x)
    std_y = std(y, mean_y)

    return sum([(x[i]-mean_x) * (y[i]-mean_y) for i in range(n)]) / (n * std_x * std_y)


p = pearson_correlation_coefficient(x, y, n)
print(f"{p:.3f}")

