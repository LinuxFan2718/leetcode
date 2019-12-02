from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        lowestCostPath = []
        m = len(grid)
        if m == 0:
          return 0
        n = len(grid[0])
        if n == 0:
          return 0
        for _ in range(m):
            lowestCostPath.append([None] * n)
        lowestCostPath[-1][-1] = grid[-1][-1]
        for i in range(m-2, -1, -1):
          lowestCostPath[i][-1] = lowestCostPath[i+1][-1] + grid[i][-1]
        for j in range(n-2, -1, -1):
          lowestCostPath[-1][j] = lowestCostPath[-1][j+1] + grid[-1][j]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
              lowestCostPath[i][j] = grid[i][j] + min(lowestCostPath[i+1][j], lowestCostPath[i][j+1])
        return lowestCostPath[0][0]

s = Solution()
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
o = 7
ans = s.minPathSum(grid)
print(ans == o, ans)

grid = [
  [1,3,1]
]
o = 5
ans = s.minPathSum(grid)
print(ans == o, ans)

grid = [
  [1],
  [1],
  [4]
]
o = 6
ans = s.minPathSum(grid)
print(ans == o, ans)

grid = [
  [99]
]
o = 99
ans = s.minPathSum(grid)
print(ans == o, ans)

grid = [[]]
o = 0
ans = s.minPathSum(grid)
print(ans == o, ans)