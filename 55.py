from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currentIndex = 0
        while True:
          if currentIndex >= len(nums) - 1 or currentIndex + nums[currentIndex] >= len(nums) - 1:
            return True
          if nums[currentIndex] == 0:
            return False
          candidates = []
          for i in range(currentIndex + 1, currentIndex + nums[currentIndex] + 1):
            candidates.append(i + nums[i])
          currentIndex = max(candidates)

s = Solution()
i = [2,3,1,1,4]
o = True
ans = s.canJump(i)
print(o == ans)

i = [3,2,1,0,4]
o = False
ans = s.canJump(i)
print(o == ans)

i = [2,0]
o = True
ans = s.canJump(i)
print(o == ans)

i = [1,2,3]
o = True
ans = s.canJump(i)
print(o == ans)

i = [5,9,3,2,1,0,2,3,3,1,0,0]
o = True
ans = s.canJump(i)
print(o == ans)
