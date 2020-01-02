from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTHelper(root, -float('inf'), float('inf'))

    def isValidBSTHelper(self, root: TreeNode, minimum, maximum) -> bool:
        if not root:
          return True
        elif minimum < root.val and root.val < maximum:
          if not root.left and not root.right:
            return True
          elif not root.left:
            return self.isValidBSTHelper(root.right, max(minimum, root.val), maximum)
          elif not root.right:
            return self.isValidBSTHelper(root.left, minimum, min(root.val, maximum))
          else: # both children exist
            return self.isValidBSTHelper(root.right, max(minimum, root.val), maximum) and self.isValidBSTHelper(root.left, minimum, min(root.val, maximum))
        else:
          return False

s = Solution()
h4 = TreeNode(2)
h4.left = TreeNode(1)
h4.right = TreeNode(3)
#   2
#  / \
# 1   3
o = True
ans = s.isValidBST(h4)
print(ans == o)

h3 = TreeNode(5)
h3.left = TreeNode(1)
h3.right = TreeNode(4)
h3.right.left = TreeNode(3)
h3.right.right = TreeNode(6)

#      5
#     / \
#    1   4
#       / \
#      3   6
o = False
ans = s.isValidBST(h3)
print(ans == o)
