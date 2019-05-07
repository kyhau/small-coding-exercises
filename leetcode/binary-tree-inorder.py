

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # LNR
        def func(node, ret):
            if node is None:
                return
            func(node.left, ret)
            ret.append(node.val)
            func(node.right, ret)

        ret = []
        func(root, ret)
        return ret