from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      length = 0
      index = 0
      while True:
        if nums[index+1:] == []:
          break
        if nums[index] == nums[index+1]:
          del(nums[index+1])
        else:
          index += 1
          length += 1
      return length + 1


s = Solution()
nums = [1,1,2]
print(s.removeDuplicates(nums) == len(set(nums)))
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums) == len(set(nums)))