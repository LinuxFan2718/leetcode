# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if not root:
            return 0
        currentLevel = [root]
        while currentLevel:
            depth += 1
            newCurrentLevel = []
            for node in currentLevel:
                if node.left:
                    newCurrentLevel.append(node.left)
                if node.right:
                    newCurrentLevel.append(node.right)
            currentLevel = newCurrentLevel
        return depth

s = Solution()
h1 = TreeNode(3)
h1.left = TreeNode(9)
r = h1.right = TreeNode(20)
r.left = TreeNode(15)
r.right = TreeNode(7)

o = s.maxDepth(h1)
ans = 3
print(o == ans, o)