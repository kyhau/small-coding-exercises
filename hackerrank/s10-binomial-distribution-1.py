"""
https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

We define a binomial process to be a binomial experiment meeting the following conditions:
1. The number of successes is x.
2. The total number of trials is n.
3. The probability of success of 1 trial is p.
4. The probability of failure of 1 trial q, where q = 1 - p.
5. b(x, n, p) is the binomial probability, meaning the probability of having exactly  successes out of  trials.

The binomial random variable is the number of successes, x, out of n trials.

The binomial distribution is the probability distribution for the binomial random variable, given by the following
probability mass function:

b(x, n, p) = n! / (x! (n-x)!) * p**x * q ** (n-x)

"""
from math import factorial


def binomial_distribution(x, n, p):
    return factorial(n) / factorial(x) / factorial(n-x) * p**x * (1-p)**(n-x)

# What proportion of Russian families with exactly 6 children will have at least 3 boys
# The ratio of boys to girls for babies born in Russia is 1.09:1.
# Sample input: 1.09 1
# Sample output: 0.696
boy, girl = list(map(float, input().strip().split()))

n = 6
p = boy/(boy+girl)
b = 0
for x in range(3, n+1):
    b += binomial_distribution(x, n, p)

print(f"{b:.3f}")
