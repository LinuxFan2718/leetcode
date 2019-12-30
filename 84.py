from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
          return 0
        elif len(heights) == 1:
          return heights[0]
        elif len(heights) == 2:
          return max(min(heights) * 2, heights[0], heights[1])
        pivot = heights.index(min(heights))
        return max(min(heights) * len(heights), self.largestRectangleArea(heights[:pivot]), self.largestRectangleArea(heights[pivot+1:]))
        
s = Solution()
i = [2,1,5,6,2,3]
o = 10
ans = s.largestRectangleArea(i)
print(o == ans, ans)

i = [5]
o = 5
ans = s.largestRectangleArea(i)
print(o == ans, ans)

i = [1,2,3,4,5,1,10,10]
o = 20
ans = s.largestRectangleArea(i)
print(o == ans, ans)

i = [0,1,0,2,0,3,0]
o = 3
ans = s.largestRectangleArea(i)
print(o == ans, ans)

i = [4,2,0,3,2,4,3,4]
o = 10
ans = s.largestRectangleArea(i)
print(o == ans, ans)

i = [5,5,1,7,1,1,5,2,7,6]
o = 12
ans = s.largestRectangleArea(i)
print(o == ans, ans)