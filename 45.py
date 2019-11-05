from typing import List
class Solution:

    def jump(self, nums: List[int]) -> int:
      jumps = 0
      position = 0
      while position < len(nums) - 1:
        jumps += 1
        maxJump = nums[position]
        if position + maxJump >= len(nums) - 1:
          position = len(nums) - 1
        else:
          maxSoFar = 0
          newPosition = None
          for i in range(position+1, position+maxJump+1):
            if nums[i] >= maxSoFar:
              maxSoFar = nums[i]
              newPosition = i
          position = newPosition
      return jumps

s = Solution()
i = [2,3,1,1,4]
o = 2
computed = s.jump(i)
print(computed == o, computed)

i = [1,2,1,1,1]
o = 3
computed = s.jump(i)
print(computed == o, computed)

i = [10,9,8,7,6,5,4,3,2,1,1,0]
o = 2
computed = s.jump(i)
print(computed == o, computed)