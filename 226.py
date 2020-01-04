from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

def inorder(root: TreeNode) -> TreeNode:
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

s = Solution()
h3 = TreeNode(4)
h3.left = TreeNode(2)
h3.left.left = TreeNode(1)
h3.left.right = TreeNode(3)
h3.right = TreeNode(7)
h3.right.left = TreeNode(6)
h3.right.right = TreeNode(9)

#       4
#     /   \
#   2       7
#  / \     / \
# 1   3   6   9

h4 = TreeNode(4)
h4.left = TreeNode(7)
h4.left.left = TreeNode(9)
h4.left.right = TreeNode(6)
h4.right = TreeNode(2)
h4.right.left = TreeNode(3)
h4.right.right = TreeNode(1)

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

ans = s.invertTree(h3)
ioans = inorder(ans)
io4 = inorder(h4)
print(ioans == io4, ioans)
