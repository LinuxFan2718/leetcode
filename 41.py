from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
          while nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] -1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
          if nums[i] != i+1:
            return i+1
        return len(nums)+1

s = Solution()
Input = [1,2,0]
Output = 3
computed = s.firstMissingPositive(Input)
print(computed,computed == Output)

Input = [3,4,-1,1]
Output = 2
computed = s.firstMissingPositive(Input)
print(computed,computed == Output)

Input = [7,8,9,11,12]
Output = 1
computed = s.firstMissingPositive(Input)
print(computed,computed == Output)

input = [-1,4,2,1,9,10]
output = 3
computed = s.firstMissingPositive(input)
print(computed,computed == output)