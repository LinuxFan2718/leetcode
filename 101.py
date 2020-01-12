from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            if not root.left and not root.right:
                return True
            if not root.left or not root.right:
                return False

        return True

def inorder(root: TreeNode) -> TreeNode:
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

s = Solution()
h3 = TreeNode(1)
h3.left = TreeNode(2)
h3.left.left = TreeNode(3)
h3.left.right = TreeNode(4)
h3.right = TreeNode(2)
h3.right.left = TreeNode(4)
h3.right.right = TreeNode(3)
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

h4 = TreeNode(1)
h4.left = TreeNode(2)
h4.left.right = TreeNode(3)
h4.right = TreeNode(2)
h4.right.right = TreeNode(3)

#     1
#    / \
#   2   2
#    \   \
#    3    3

ans3 = s.isSymmetric(h3)
o3 = True
print(ans3 == o3)

ans4 = s.isSymmetric(h4)
o4 = False
print(ans4 == o4)
