from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
      totalWater = 0
      if len(height) < 2:
        return 0
      left = 0
      right = 1
      while right < len(height):
        if right + 1 < len(height) and height[right] > height[right + 1]:
          # found a local max
          thisHeight = min(height[left], height[right])
          thisWidth = right - left - 1
          waterWithoutDisplacement = thisHeight * thisWidth
          displacement = sum(height[left+1:right])
          totalWater += waterWithoutDisplacement - displacement
          left = right
          right += 1
        right += 1
      return totalWater

s = Solution()
input = [0,1,0,2,1,0,1,3,2,1,2,1]
output = 6
computed = s.trap(input)
print(computed, computed == output)