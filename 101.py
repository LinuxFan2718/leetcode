from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSymmetricHelper(root.left, root.right)

    def isSymmetricHelper(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if left and right:
            return (left.val == right.val
                and self.isSymmetricHelper(left.left, right.right)
                and self.isSymmetricHelper(right.left, left.right))
        return False
        

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

h5 = TreeNode(1)
h5.left = TreeNode(2)
h5.left.right = TreeNode(3)
h5.right = TreeNode(2)
h5.right.left = TreeNode(3)

# [1,2,2,null,3,3]
#     1
#    /    \
#   2      2
#  /    \ / \
# None  3 3  

ans3 = s.isSymmetric(h3)
o3 = True
print(ans3 == o3)

ans4 = s.isSymmetric(h4)
o4 = False
print(ans4 == o4)

ans5 = s.isSymmetric(h5)
o5 = True
print(ans5 == o5)
