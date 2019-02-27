"""
https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem
"""

def whatFlavors(cost, money):
    pos = 0
    d = {}
    while pos < len(cost):
        price = cost[pos]
        diff = money - price
        if diff in d:
            print(d[diff]+1, pos+1)
            return
        d[price] = pos
        pos += 1
