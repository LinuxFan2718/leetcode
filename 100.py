from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
          return True
        elif p and not q:
          return False
        elif q and not p:
          return False
        elif p.val != q.val:
          return False
        else: #both exist and have equal val
          return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

s = Solution()
h1 = TreeNode(1)
h1.left = TreeNode(2)
h1.right = TreeNode(3)

h2 = TreeNode(1)
h2.left = TreeNode(2)
h2.right = TreeNode(3)

ans = s.isSameTree(h1, h2)
o = True
print(ans == o)

h3 = TreeNode(1)
h3.left = TreeNode(2)

h4 = TreeNode(1)
h4.right = TreeNode(2)

ans = s.isSameTree(h3, h4)
o = False
print(ans == o)

h5 = TreeNode(1)
h5.left = TreeNode(2)
h5.right = TreeNode(1)

h6 = TreeNode(1)
h6.left = TreeNode(1)
h6.right = TreeNode(2)
ans = s.isSameTree(h5, h6)

o = False
print(ans == o)

h7 = TreeNode(1)
h7.left = TreeNode(1)

h8 = TreeNode(1)
h8.right = TreeNode(1)

ans = s.isSameTree(h7, h8)
o = False
print(ans == o)