"""
https://leetcode.com/problems/range-sum-of-bst/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        def func(root, L, R, total):
            if root is None:
                return total

            if L <= root.val <= R:
                total += root.val

            total = func(root.right, L, R, total)
            total = func(root.left, L, R, total)
            return total

        return func(root, L, R, 0)


#assert Solution().rangeSumBST(root = [10,5,15,3,7,None,18], L = 7, R = 15) == 32
#assert Solution().rangeSumBST(root = [10,5,15,3,7,13,18,1,None,6], L = 6, R = 10) == 23