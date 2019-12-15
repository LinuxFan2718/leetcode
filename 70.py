from typing import List
class Solution:
    def climbStairs(self, n: int) -> int:
      dp = { 
        0: 1,
        1: 1,
        2: 2,
        3: 3
        }
      return self.climbStairsHelper(n, dp)

    def climbStairsHelper(self, n, dp):
      if n not in dp.keys():
        dp[n] = self.climbStairsHelper(n-1, dp) + self.climbStairsHelper(n-2, dp)
      return dp[n] 

s = Solution()
i = 2
o = 2
ans = s.climbStairs(i)
print(ans == o, ans)

i = 3
o = 3
ans = s.climbStairs(i)
print(ans == o, ans)