from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
      if n == 0:
        return []
      return self.helper(1, n)

    def helper(self, low, high) -> TreeNode:
      if high - low < 0:
        return [None]
      elif high - low == 0:
        return [TreeNode(low)]
      elif high - low == 1:
        h1 = TreeNode(low)
        h1.right = TreeNode(high)
        h2 = TreeNode(high)
        h2.left = TreeNode(low)
        return [h1, h2]
      else:
        ans = []
        for i in range(low, high+1):
          lefts = self.helper(low, i-1)
          rights = self.helper(i+1, high)
          for left in lefts:
            for right in rights:
              thisHead = TreeNode(i)
              thisHead.left = left
              thisHead.right = right
              ans.append(thisHead)
        return ans
      
def checkTreesRough(h1, h2):
  return sorted([x.val for x in h1]) == sorted([x.val for x in h2])


s = Solution()
n = 3

h1 = TreeNode(1)
h1.right = TreeNode(3)
h1.right.left = TreeNode(2)

h2 = TreeNode(3)
h2.left = TreeNode(2)
h2.left.left = TreeNode(1)

h3 = TreeNode(3)
h3.left = TreeNode(1)
h3.left.right = TreeNode(2)

h4 = TreeNode(2)
h4.left = TreeNode(1)
h4.right = TreeNode(3)

h5 = TreeNode(1)
h5.right = TreeNode(2)
h5.right.right = TreeNode(3)

o = [h1, h2, h3, h4, h5]
ans = s.generateTrees(n)

print(len(ans) == 5)
print(checkTreesRough(o, ans))

n = 0
o = []
ans = s.generateTrees(n)

print(checkTreesRough(o, ans))

n = 4

lenCorrect = 14
ans = s.generateTrees(n)
print(len(ans) == lenCorrect)

myOutput = [
  [1,None,2,1,3,None,None,None,4],
  [1,None,2,1,4,None,None,3],
  [1,None,3,1,4,None,2],
  [1,None,3,2,4,1],
  [1,None,4,1,None,None,2,None,3],
  [1,None,4,1,None,None,3,2],
  [1,None,4,2,None,1,3],
  [1,None,4,3,None,1,None,None,2],
  [1,None,4,3,None,2,None,1],
  [2,1,3,None,None,None,4],
  [2,1,4,None,None,3],
  [3,1,4,None,2],
  [3,2,4,1],
  [4,1,None,None,2,None,3],
  [4,1,None,None,3,2],
  [4,2,None,1,3],
  [4,3,None,1,None,None,2],
  [4,3,None,2,None,1]
]

correctOutput = [
  [1,None,2,None,3,None,4],
  [1,None,2,None,4,3],
  [1,None,3,2,4],
  [1,None,4,2,None,None,3],
  [1,None,4,3,None,2],
  [2,1,3,None,None,None,4],
  [2,1,4,None,None,3],
  [3,1,4,None,2],
  [3,2,4,1],
  [4,1,None,None,2,None,3],
  [4,1,None,None,3,2],
  [4,2,None,1,3],
  [4,3,None,1,None,None,2],
  [4,3,None,2,None,1]
]