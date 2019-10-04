from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
      i = 0
      j = len(height)-1
      maxSoFar = self.area(height, i, j)
      while i < j:
        if height[i] < height[j]: # left line shorter
          i += 1
        else:
          j -= 1
        thisArea = self.area(height, i, j)
        if thisArea > maxSoFar:
          maxSoFar = thisArea
      return maxSoFar
        
    def area(self, height, i, j) -> int:
      return (j - i) * min(height[i], height[j])

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49)