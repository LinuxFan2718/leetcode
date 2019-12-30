from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if 0 not in heights:
          maxArea = self.largestRectangleAreaHelper(heights)
        else:
          maxArea = 0
          while 0 in heights:
            zeroIndex = heights.index(0)
            thisList = heights[:zeroIndex]
            area = self.largestRectangleAreaHelper(thisList)
            if area > maxArea:
              maxArea = area
            heights = heights[zeroIndex+1:]
          area = self.largestRectangleAreaHelper(heights)
          if area > maxArea:
            maxArea = area
        return maxArea

    def largestRectangleAreaHelper(self, heights: List[int]) -> int:
        if not heights:
          return 0
        left = 0
        right = len(heights) - 1
        maxArea = 0
        width = right - left + 1

        while width > 1:
          width = right - left + 1
          height = min(heights[left:right + 1])
          area = width * height
          if area > maxArea:
            maxArea = area
          if heights[left] < heights[right]:
            left += 1
          else:
            right -= 1
        if max(heights[left], heights[right]) > maxArea:
          maxArea = max(heights[left], heights[right])
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