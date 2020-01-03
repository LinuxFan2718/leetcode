from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root: TreeNode) -> List[int]:
      return self.inorder(root.left) + [root] + self.inorder(root.right) if root else []

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inOrderList = self.inorder(root)
        sortedinOrderList = sorted(inOrderList, key = lambda x: x.val )
        if len(inOrderList) < 2:
          return
        wrongIndex = []
        for i in range(len(inOrderList)):
          if sortedinOrderList[i] != inOrderList[i]:
            wrongIndex.append(i)
        temp = inOrderList[wrongIndex[0]].val
        inOrderList[wrongIndex[0]].val = inOrderList[wrongIndex[1]].val
        inOrderList[wrongIndex[1]].val = temp

        
        

s = Solution()

before = TreeNode(1)
before.left = TreeNode(3)
before.left.right = TreeNode(2)

after = TreeNode(3)
after.left = TreeNode(1)
after.left.right = TreeNode(2)

def checkTreeRough(h1, h2):
  return h1.val == h2.val and h1.left.val == h2.left.val

s.recoverTree(before)
print(checkTreeRough(before, after), before.val, after.val)

h4before = TreeNode(3)
h4before.left = TreeNode(1)
h4before.right = TreeNode(4)
h4before.right.left = TreeNode(2)

h4 = TreeNode(2)
h4.left = TreeNode(1)
h4.right = TreeNode(4)
h4.right.left = TreeNode(3)

s.recoverTree(h4before)
print(checkTreeRough(h4before, h4), h4before.val, h4.val)
