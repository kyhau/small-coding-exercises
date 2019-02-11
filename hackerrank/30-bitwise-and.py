"""
https://www.hackerrank.com/challenges/30-bitwise-and/problem
"""


def bitwise_and(n, k):
    """
    When k is odd, k-1 is even, k-1 can always be reached by (k-1) & k.

    k   = 11
    k-1 = 10
    k-1 == (k-1) & k

    When k is even, k-1 is odd, k-1 can only be reached if and only if ((k-1) | k) <= n

    k   = 10110
    k-1 = 10101
    pos = 10111
    k-1 == (k-1) & pos
    pos = (k-1) | k
    """
    return k-1 if ((k-1) | k) <= n else k-2


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        print(bitwise_and(n, k))
