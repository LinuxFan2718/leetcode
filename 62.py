from typing import List
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[(0,0)]]
        while paths[0][-1] != (m-1, n-1):
            newPaths = []
            for path in paths:
                if path[-1][0]+1 < m:
                    newPaths.append(path + [(path[-1][0]+1, path[-1][1])])
                if path[-1][1]+1 < n:
                    newPaths.append(path + [(path[-1][0], path[-1][1]+1)])
            paths = newPaths

        return len(paths)
    
s = Solution()
# m = 3
# n = 2
# o = 3
# ans = s.uniquePaths(m, n)
# print(ans == o, ans)

# m = 7
# n = 3
# o = 28
# ans = s.uniquePaths(m, n)
# print(ans == o, ans)

for i in range(1, 11):
    print(s.uniquePaths(1, i), s.uniquePaths(2, i), s.uniquePaths(3, i), s.uniquePaths(4, i))

# m = 23
# n = 12
# o = None
# ans = s.uniquePaths(m, n)
# print(ans == o, ans)
