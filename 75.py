from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = [0, 0 ,0]
        for n in nums:
            ans[n] += 1
        nums[:] = [0] * ans[0] + [1] * ans[1] + [2] * ans[2]

s = Solution()  
i = [2,0,2,1,1,0]
o = [0,0,1,1,2,2]
s.sortColors(i)
print(i == o)