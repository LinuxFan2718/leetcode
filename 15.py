from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      target = 0
      nums.sort()
      answersSet = set()
      for i in range(len(nums)-2):
        if nums[i] > target:
          break
        left = i + 1
        right = len(nums) - 1
        # two pointers are left, right
        while left < right:
          candidate = nums[i] + nums[left] + nums[right]
          if candidate == target:
            answersSet.add((nums[i], nums[left], nums[right]))
            left += 1
            right -= 1
          elif candidate < 0: # needs to get bigger
            left += 1
          elif candidate > 0: # needs to get smaller
            right -= 1
      return [list(answer) for answer in answersSet]




s = Solution()
a = [-1, 0, 1, 2, -1, -4]
solutionSet = [
  [-1, 0, 1],
  [-1, -1, 2]
]
print(sorted(s.threeSum(a)) == sorted(solutionSet), s.threeSum(a))

input = [11,4,9,-7,-7,4,-6,13,12,-1,-5,-15,-2,-4,7,14,14,13,-2,-11,-9,-3,-15,6,-4,14,-7,-15,2,2,7,-10,13,-6,-1,14,5,8,12,3,14,-15,3,-10,-4,-12,-11,-4,-14,-6,-8,14,6,-15,5,10,14,13,10,-6,-8,-6,-1,-9,3,13,-10,-6,-1,9,4,-2,9,14,3,-9,-13,-1,-6,10,8,-7,9,-8,-7,-1,9,-15,-3,4,-6,5,13,8,3,-6,-1,8,-5,13,2,14,-12,-11,13,-1,-13,8,13,-4,3,-1,-4,-2,-2,5,12,-8,5,-13,3,14]

sorted(s.threeSum(input))