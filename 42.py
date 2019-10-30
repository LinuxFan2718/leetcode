from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
      totalWater = 0
      if len(height) < 2:
        return 0

      leftHighest = [height[0]] + (len(height)-1) * [None]
      for i in range(1, len(height)):
        leftHighest[i] = max(leftHighest[i-1], height[i])

      rightHighest = (len(height) - 1) * [None] + [height[len(height) - 1]]
      for i in range(len(height) - 2, -1, -1):
        rightHighest[i] = max(rightHighest[i+1], height[i])

      for i in range(len(height)):
        totalWater += min(leftHighest[i], rightHighest[i]) - height[i]
      return totalWater

s = Solution()
input = [0,1,0,2,1,0,1,3,2,1,2,1]
output = 6
computed = s.trap(input)
print(computed, computed == output)

input = [2,0,2]
output = 2
computed = s.trap(input)
print(computed, computed == output)

input = [2,1,0,2]
output = 3
computed = s.trap(input)
print(computed, computed == output)

input = [5,4,1,2]
output = 1
computed = s.trap(input)
print(computed, computed == output)

input = [5,2,1,2,1,5]
output = 14
computed = s.trap(input)
print(computed, computed == output)