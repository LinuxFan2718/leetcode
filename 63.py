
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return 0

s = Solution()
obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
o = 2
ans = s.uniquePathsWithObstacles(obstacleGrid)
print(ans == o, ans)