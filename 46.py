from typing import List
from math import factorial
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
      """
      Do not return anything, modify nums in-place instead.
      """
      if len(nums) < 2:
        return
      for i in range(len(nums) - 1, 0, -1): # right to left
        if nums[i - 1] < nums[i]: # ascending
          # swap nums[i - 1] with the smallest number larger than it to its right
          swap = (-1, 1000000000) # index, value
          for j in range(len(nums) - 1, i - 1, -1):
            if nums[i - 1] < nums[j] and nums[j] < swap[1]:
              swap = (j, nums[j])
          nums[i - 1], nums[swap[0]] = nums[swap[0]], nums[i - 1]
          # reverse nums to the right of nums[i - 1]
          nums[i:] = nums[:i-1:-1]
          return
      nums.reverse()
    # nums are distinct
    def permute(self, nums: List[int]) -> List[List[int]]:
      permutations = [nums]
      numPermutations = factorial(len(nums))
      while len(permutations) < numPermutations:
        nextAnswer = permutations[-1][:]
        self.nextPermutation(nextAnswer)
        permutations += [nextAnswer]
      return permutations

s = Solution()
i = [1,2,3]
o = [
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

computed = s.permute(i)
print(computed == o, computed)
