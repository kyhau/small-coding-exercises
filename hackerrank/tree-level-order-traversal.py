"""
https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
"""


def levelOrder(root):
    from collections import deque
    q = deque()
    q.append(root)

    ret = []
    while q:
        i = q.popleft()
        ret.append(str(i.info))
        if i.left:
            q.append(i.left)
        if i.right:
            q.append(i.right)
    print(" ".join(ret))
