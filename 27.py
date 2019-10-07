from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      length = 0
      index = 0
      while True:
        if nums[index:] == []:
          break
        if nums[index] == val:
          del(nums[index])
        else:
          index += 1
          length += 1
      return length


s = Solution()
nums = [1,1,2]
print(s.removeElement(nums, 1))
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeElement(nums, 3))
nums = [3,2,2,3]
val = 3
print(s.removeElement(nums, val) == 2)
nums = [0,1,2,2,3,0,4,2]
val = 2
print(s.removeElement(nums, val) == 5)