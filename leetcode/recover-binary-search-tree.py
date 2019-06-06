# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def func(node, smallest, largest):
            if node is None:
                return
            
            print(f"node={node.val} smallest={smallest.val if smallest else None} largest={largest.val if largest else None}")
            
            if smallest and node.val > smallest.val:
                node.val, smallest.val = smallest.val, node.val
                print(f"swapped {node.val} {smallest.val}")
                return
            if largest and node.val < largest.val:
                node.val, largest.val = largest.val, node.val
                print(f"swapped {node.val} {largest.val}")
                return
            
            if node.left:
                smallest = smallest if smallest and smallest.val < node.val else node
                func(node.left, smallest, largest)
            
            if node.right:
                largest = largest if largest and largest.val < node.val else node
                func(node.left, smallest, largest)
        
        func(root, None, None)


root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)
Solution().recoverTree(root)
assert root.left.val == 3
assert root.left.right == 2

"""
# Test case 1:
# Input: [1,3,null,null,2]
   1
  /
 3
  \
   2
# Expected: [3,1,null,null,2]
   3
  /
 1
  \
   2

# Test case 2:
# Input: [3,1,4,null,null,2]
  3
 / \
1   4
   /
  2
# Expected: [2,1,4,null,null,3]
  2
 / \
1   4
   /
  3

# Test case 3:
# Input: [2,3,1]
  2
 / \
3   1
# Expected: [2,1,3]
  2
 / \
1   3
"""
