# 80. Remove Duplicates from Sorted Array II
# Medium

# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Given nums = [1,1,1,2,2,3],

# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

# It doesn't matter what you leave beyond the returned length.

# Example 2:

# Given nums = [0,0,1,1,1,1,2,3,3],

# Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

# It doesn't matter what values are set beyond the returned length.

# Clarification:

# Confused why the returned value is an integer but your answer is an array?

# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

# Internally you can think of this:

# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);

# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 1
        numFound = 1
        current = nums[0]
        while i < len(nums):
            if current == nums[i]:
                numFound += 1
            else:
                numFound = 1
                current = nums[i]

            if numFound == 3:
                while i < len(nums) and nums[i] == current:
                    nums.pop(i)
            else:
                i += 1
        return len(nums)

s = Solution()
nums = [1,1,1,2,2,3]
o = 5
ans = s.removeDuplicates(nums)
print(ans == o, ans, nums)

nums = [0,0,1,1,1,1,2,3,3]
o = 7
ans = s.removeDuplicates(nums)
print(ans == o, ans, nums)

nums = [1]
o = 1
ans = s.removeDuplicates(nums)
print(ans == o, ans, nums)

nums = [1,1,1,2,2,2,3,3]
o = 6
ans = s.removeDuplicates(nums)
print(ans == o, ans, nums)