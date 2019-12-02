from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
          return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        waysToEnd = []
        for _ in range(m):
            waysToEnd.append([None] * n)
        seenObstacleM = False
        for i in range(m-1, -1, -1):
            if obstacleGrid[i][n-1] == 1:
              seenObstacleM = True
            if seenObstacleM:
              waysToEnd[i][n-1] = 0
            elif seenObstacleM == False:
              waysToEnd[i][n-1] = 1
        seenObstacleN = False
        for j in range(n-1, -1, -1):
            if obstacleGrid[m-1][j] == 1:
              seenObstacleN = True
            if seenObstacleN:
              waysToEnd[m-1][j] = 0
            elif seenObstacleN == False:
              waysToEnd[m-1][j] = 1
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j] == 1:
                  waysToEnd[i][j] = 0
                elif obstacleGrid[i][j] == 0:
                  waysToEnd[i][j] = waysToEnd[i+1][j] + waysToEnd[i][j+1]

        return waysToEnd[0][0]

s = Solution()
obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
o = 2
ans = s.uniquePathsWithObstacles(obstacleGrid)
print(ans == o, ans)

obstacleGrid = [[0,1]]
o = 0
ans = s.uniquePathsWithObstacles(obstacleGrid)
print(ans == o, ans)

obstacleGrid = [[0,0],[1,1],[0,0]]
o = 0
ans = s.uniquePathsWithObstacles(obstacleGrid)
print(ans == o, ans)