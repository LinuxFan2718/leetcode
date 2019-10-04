from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
      nums.sort()
      bestAnswerInts = [nums[0], nums[1], nums[2]]
      bestAnswerDifference = abs(sum(bestAnswerInts) - target)
      for i in range(len(nums)-2):
        left = i + 1
        right = len(nums) - 1
        # two pointers are left, right
        while left < right:
          candidate = nums[i] + nums[left] + nums[right]
          if candidate == target:
            return candidate
          if abs(candidate - target) < bestAnswerDifference: # new winner
            bestAnswerInts = [nums[i], nums[left], nums[right]]
            bestAnswerDifference = abs(candidate - target)
          elif candidate < target: # needs to get larger
            left += 1
          elif target < candidate: # needs to get smaller
            right -= 1
      return sum(bestAnswerInts)

s = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(s.threeSumClosest(nums, target) == 2)
nums =  [0,2,1,-3]
target = 1
print(s.threeSumClosest(nums, target) == 0)