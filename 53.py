from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      maxSum = currSum = nums[0]
      for i in range(1, len(nums)):
        currSum = max(nums[i], currSum + nums[i])
        maxSum = max(maxSum, currSum)
      return maxSum

s = Solution()
i = [-2,1,-3,4,-1,2,1,-5,4]
o = 6
ans = s.maxSubArray(i)
print(o == ans, ans)

i = [1]
o = 1
ans = s.maxSubArray(i)
print(o == ans, ans)

i =[-2,-1]
o = -1
ans = s.maxSubArray(i)
print(o == ans, ans)
i =[1,2,-1,-2,2,1,-2,1,4,-5,4]
o = 6
ans = s.maxSubArray(i)
print(o == ans, ans)