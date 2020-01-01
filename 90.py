from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        return ans

s = Solution()
i = [1,2,2]
o = [
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
ans = s.subsetsWithDup(i)
print(o == ans, ans)