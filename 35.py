from typing import List
from bisect import bisect_left
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      return bisect_left(nums, target)
        

s = Solution()
nums, target = [1,3,5,6], 5
correctAnswer = 2
myAnswer = s.searchInsert(nums, target)
print(myAnswer, myAnswer == correctAnswer)

nums, target = [1,3,5,6], 2
correctAnswer = 1
myAnswer = s.searchInsert(nums, target)
print(myAnswer, myAnswer == correctAnswer)

nums, target = [1,3,5,6], 7
correctAnswer = 4
myAnswer = s.searchInsert(nums, target)
print(myAnswer, myAnswer == correctAnswer)

nums, target = [1,3,5,6], 0
correctAnswer = 0
myAnswer = s.searchInsert(nums, target)
print(myAnswer, myAnswer == correctAnswer)