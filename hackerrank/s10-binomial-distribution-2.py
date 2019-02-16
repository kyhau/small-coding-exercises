"""
https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

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

# Sample input denoting the respective percentage of defective pistons and the size of the current batch of pistons
# Sample input: 12 10
# Sample output:
#   0.891
#   0.342
# Print the answer to each question on its own line:
# 1. the probability that a batch of  pistons will contain no more than 2 rejects.
# 2. the probability that a batch of  pistons will contain at least 2 rejects.
defect_p, batch_size = list(map(int, input().strip().split()))

n = batch_size
p = defect_p/100
b1 = sum(binomial_distribution(x, n, p) for x in range(0, 2+1))
b2 = sum(binomial_distribution(x, n, p) for x in range(2, n+1))
print(f"{b1:.3f}")
print(f"{b2:.3f}")