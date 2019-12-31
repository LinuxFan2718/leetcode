from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stack.append(-1)
        maxarea = 0
        for i in range(len(heights)):
            while (stack[-1] != -1 and heights[stack[-1]] >= heights[i]):
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] -1))
        return maxarea

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