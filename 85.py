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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        if len(matrix) == 0:
          return maxArea
        for j in range(len(matrix[0])):
          heights = []
          for i in range(len(matrix)):
            n = 0
            while j + n < len(matrix[0]) and matrix[i][j + n] == "1":
              n += 1
            heights.append(n)
          area = self.largestRectangleArea(heights)
          if area > maxArea:
            maxArea = area
        return maxArea

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

input2 = [
  ["1","1","1","1","1"]
]
output2 = 5
ans = s.maximalRectangle(input2)
print(ans == output2, ans)

input3 = [
  ["1"],
  ["1"],
  ["1"],
  ["1"],
  ["1"]
]
output3 = 5
ans = s.maximalRectangle(input3)
print(ans == output3, ans)

input4 = []
output4 = 0
ans = s.maximalRectangle(input4)
print(ans == output4, ans)