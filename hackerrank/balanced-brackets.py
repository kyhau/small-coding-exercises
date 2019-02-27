"""
https://www.hackerrank.com/challenges/balanced-brackets/problem
"""

from collections import deque

def isBalanced(s):
    d1 = deque()
    d2 = deque(s)

    pos = 0
    while pos < len(d2):
        x = d1[-1] if d1 else None
        y = d2.popleft()

        if (x == "(" and y == ")") or (x == "[" and y == "]") or (x == "{" and y == "}"):
            d1.pop()
        elif y in [")", "}", "]"]:
            return "NO"
        else:
            d1.append(y)

    return "NO" if d1 else "YES"
