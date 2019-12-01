from typing import List
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        waysToEnd = []
        for _ in range(m):
            waysToEnd.append([None] * n)
        for i in range(m):
            waysToEnd[i][n-1] = 1
        for j in range(n):
            waysToEnd[m-1][j] = 1
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                waysToEnd[i][j] = waysToEnd[i+1][j] + waysToEnd[i][j+1]

        return waysToEnd[0][0]

s = Solution()
m = 3
n = 2
o = 3
ans = s.uniquePaths(m, n)
print(ans == o, ans)

m = 7
n = 3
o = 28
ans = s.uniquePaths(m, n)
print(ans == o, ans)

m = 57
n = 2
o = 57
ans = s.uniquePaths(m, n)
print(ans == o, ans)

m = 23
n = 12
o = 193536720
ans = s.uniquePaths(m, n)
print(ans == o, ans)

m = 1
n = 2
o = 1
ans = s.uniquePaths(m, n)
print(ans == o, ans)