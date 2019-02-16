"""
https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem
"""


def geometric_distribution(n, p):
    """
    :param n: the total number of trials
    :param p: the probability of success of 1 trial
    """
    return (1-p)**(n-1) * p

"""
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the first 5th inspection?
Sample input:
1 3
5
Sample output:
0.868
"""
defect_p, batch_size = list(map(int, input().strip().split()))
n = int(input().strip())
p = defect_p/batch_size

g = sum(geometric_distribution(n1, p) for n1 in range(1, n+1))
print(f"{g:.3f}")
