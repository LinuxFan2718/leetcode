from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans = []
        mi = 0
        ni = 0
        while mi < m and ni < n:
          if nums1[mi] < nums2[ni]:
            ans.append(nums1[mi])
            mi += 1
          elif nums1[mi] >= nums2[ni]:
            ans.append(nums2[ni])
            ni += 1
        if mi == m:
          ans += nums2[ni:]
        elif ni == n:
          ans += nums1[mi:m]

        nums1[:] = ans
        
s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
o = [1,2,2,3,5,6]
s.merge(nums1, m, nums2, n)
print(nums1 == o, nums1)

nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
o = [1,2]
s.merge(nums1, m, nums2, n)
print(nums1 == o, nums1)