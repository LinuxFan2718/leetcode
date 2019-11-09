from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
      jumps = 0
      position = 0
      nums.reverse()
      while position <= len(nums) - 1:
        candidates = [(i,x) for i,x in enumerate(nums[position+1:], position + 1) if x >= i - position]
        if len(candidates) == 0:
          break
        else:
          jumps += 1
          position, _ = candidates.pop()
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

i = [1] * 25000
o = None
computed = s.jump(i)
print(computed == o, computed)