from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxRectangle = 0

        return maxRectangle

s = Solution()
input1 = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
output1 = 6
ans = s.maximalRectangle(input1)
print(ans == output1, ans)