from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
      leftmostGoodIndex = len(nums) - 1
      for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= leftmostGoodIndex:
          leftmostGoodIndex = i
      return leftmostGoodIndex == 0

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
