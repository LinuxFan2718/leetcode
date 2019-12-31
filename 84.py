from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
      stack = [] # smaller heights than current index
      maxArea = 0
      i = 0
      while i < len(heights):
        if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
          stack.append(i)
          i += 1
        else: # heights[i] is smaller than top of stack
          heightIndex = stack.pop()
          if len(stack) == 0: # rectangle from left edge to current index with height top of stack
            leftIndex = 0
          elif len(stack) > 0: # rectangle from left second element from top of stack to top of stack
            leftIndex = stack[-1] + 1
          width = i - leftIndex
          height = heights[heightIndex]
          area = width * height
          if area > maxArea:
            maxArea = area
      while stack: # check rectangles where right edge is end of histogram
        heightIndex = stack.pop()
        if len(stack) == 0:
          leftIndex = 0
        elif len(stack) > 0:
          leftIndex = stack[-1] + 1
        width = len(heights) - leftIndex
        height = heights[heightIndex]
        area = width * height
        if area > maxArea:
          maxArea = area        
      return maxArea

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

i = [50,0,5,1,7,1,1,5,2,7,6]
o = 50
ans = s.largestRectangleArea(i)
print(o == ans, ans)

i = [0,50,0,5,1,7,1,1,5,2,7,6]
o = 50
ans = s.largestRectangleArea(i)
print(o == ans, ans)