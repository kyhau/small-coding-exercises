# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def func(nodes, ret, depth):
            if not nodes:
                return

            deq = []  # deq = deque([])   # current level's values
            new_nodes = []  # new nodes of next level, from left to right
            for n in nodes:
                if depth % 2 == 0:  # left to right
                    deq.append(n.val)
                else:
                    deq.insert(0, n.val)
                    # deq.appendleft(n.val)
                if n.left:
                    new_nodes.append(n.left)
                if n.right:
                    new_nodes.append(n.right)
            ret.append(deq)

            func(new_nodes, ret, depth + 1)

        ret = []
        nodes = [] if root is None else [root]
        func(nodes, ret, depth=0)
        return ret
