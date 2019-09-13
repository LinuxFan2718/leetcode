from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        other_half = {}
        if len(nums) < 2: return []
        
        for i in range(len(nums)):
            num = nums[i]
            if nums[i] in other_half:
                return [other_half[num], i]
            other_half[target - num] = i

        print("should never get here")

solution = Solution()
nums = [2, 7, 11, 15]
target = 9
a = solution.twoSum(nums, target)
print(a)