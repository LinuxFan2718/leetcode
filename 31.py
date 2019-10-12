from typing import List
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


s = Solution()
nums1 = [1,2,3]
s.nextPermutation(nums1)
nums1answer = [1,3,2]
print(nums1, nums1 == nums1answer)
nums2 = [3,2,1]
s.nextPermutation(nums2)
nums2answer = [1,2,3]
print(nums2, nums2 == nums2answer)
nums3 = [1,1,5]
s.nextPermutation(nums3)
nums3answer = [1,5,1]
print(nums3, nums3 == nums3answer)
nums4 = [1,1,5,2]
s.nextPermutation(nums4)
nums4answer = [1,2,1,5]
print(nums4, nums4 == nums4answer)
nums5 = [1,2]
s.nextPermutation(nums5)
nums5answer = [2,1]
print(nums5, nums5 == nums5answer)
nums6 = [1,3,2]
s.nextPermutation(nums6)
nums6answer = [2,1,3]
print(nums6, nums6 == nums6answer)
nums7 = [2,3,1]
s.nextPermutation(nums7)
nums7answer = [3,1,2]
print(nums7, nums7 == nums7answer)