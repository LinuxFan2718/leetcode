from typing import List
class Solution:
  def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    answersSet = set()
    for i in range(len(nums)-3):
      for j in range(i+1, len(nums)-2):
        if target > 0 and nums[i] > target:
          break
        left = j + 1
        right = len(nums) - 1
        # two pointers are left, right
        while left < right:
          candidate = nums[i] + nums[j] + nums[left] + nums[right]
          if candidate == target:
            answersSet.add((nums[i], nums[j], nums[left], nums[right]))
            left += 1
            right -= 1
          elif candidate < target: # needs to get bigger
            left += 1
          elif candidate > target: # needs to get smaller
            right -= 1
    return [list(answer) for answer in answersSet]

s = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
answer = [
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

# computed = s.fourSum(nums, target)
# print(sorted(computed) == sorted(answer))

nums = [1,-2,-5,-4,-3,3,3,5]
target = -11
answer = [[-5,-4,-3,1]]

computed = s.fourSum(nums, target)
print(sorted(computed) == sorted(answer))
