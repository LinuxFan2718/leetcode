from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
          return []
        ans = []
        currentRow = [root]
        while currentRow:
          ans.append([node.val for node in currentRow])
          newCurrentRow = []
          for node in currentRow:
            if node.left:
              newCurrentRow.append(node.left)
            if node.right:
              newCurrentRow.append(node.right)
          currentRow = newCurrentRow
        return ans

        

def inorder(root: TreeNode) -> TreeNode:
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

s = Solution()
h1 = TreeNode(3)
h1.left = TreeNode(9)
h1.right = TreeNode(20)
h1.right.left = TreeNode(15)
h1.right.right = TreeNode(7)
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3


ans1 = s.levelOrder(h1)
o1 = [
  [3],
  [9,20],
  [15,7]
]
print(ans1 == o1)
