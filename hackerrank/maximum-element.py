"""
https://www.hackerrank.com/challenges/maximum-element/problem
"""
from collections import deque

stack = deque()
m = 0

N = int(input().strip())
for i in range(N):
    inputs = list(map(int, input().strip().split()))
    if inputs[0] == 1:
        # Put current value, and max before inserting current value
        v = inputs[1]
        stack.appendleft((v, m))
        # Update current max
        m = max(m, v)
    elif inputs[0] == 2:
        # current max becomes max without `v` in the stack
        v, m = stack.popleft()
    elif inputs[0] == 3:
        v, m1 = stack[0]
        print(max(v, m1))