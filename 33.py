from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
      try:
        return nums.index(target)
      except ValueError:
        return -1
        
s = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
correctAnswer = 4
myAnswer = s.search(nums, target)
print(myAnswer == correctAnswer, myAnswer)

nums = [4,5,6,7,0,1,2]
target = 3
correctAnswer = -1
myAnswer = s.search(nums, target)
print(myAnswer == correctAnswer, myAnswer)
