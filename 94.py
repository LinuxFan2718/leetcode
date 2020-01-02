from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.helper(root, ans)
        return ans

    def helper(self, root: TreeNode, ans: List[int]) -> None:
        if root == None:
          return
        self.helper(root.left, ans)
        ans.append(root.val)
        self.helper(root.right, ans)



s = Solution()
i = TreeNode(1)
i.left = None
i.right = TreeNode(2)
i.right.left = TreeNode(3)
o = [1,3,2]
ans = s.inorderTraversal(i)
print(ans == o, ans)
