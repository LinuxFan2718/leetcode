from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return max(heights)

s = Solution()
i = [2,1,5,6,2,3]
o = 10
ans = s.largestRectangleArea(i)
print(o == ans, ans)