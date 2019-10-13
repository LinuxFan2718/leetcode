from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
      try:
        return [nums.index(target), len(nums) - 1 - nums[::-1].index(target)]
      except ValueError:
        return [-1, -1]

s = Solution()
nums = [5,7,7,8,8,10]
target = 8
correctAnswer = [3,4]
myAnswer = s.searchRange(nums, target)
print(myAnswer, myAnswer == correctAnswer)

nums = [5,7,7,8,8,10]
target = 6
correctAnswer = [-1,-1]
myAnswer = s.searchRange(nums, target)
print(myAnswer, myAnswer == correctAnswer)
