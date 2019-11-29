from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) < 2:
          return
        for i in range(len(nums) - 1, 0, -1): # right to left
          if nums[i - 1] < nums[i]: # ascending
            # swap nums[i - 1] with the smallest number larger than it to its right
            swap = (-1, 10000000000000) # index, value
            for j in range(len(nums) - 1, i - 1, -1):
              if nums[i - 1] < nums[j] and nums[j] < swap[1]:
                swap = (j, nums[j])
            nums[i - 1], nums[swap[0]] = nums[swap[0]], nums[i - 1]
            # reverse nums to the right of nums[i - 1]
            nums[i:] = nums[:i-1:-1]
            return
        nums.reverse()
    def getPermutation(self, n: int, k: int) -> str:
        ans = [1]
        for i in range(2, n+1):
          ans.append(i)
        for _ in range(1, k):
          self.nextPermutation(ans)
        return ''.join([str(x) for x in ans])

s = Solution()
n = 3
k = 3
o = "213"
ans = s.getPermutation(n, k)
print(ans == o, ans)

n = 9
k = 206490
o = None
ans = s.getPermutation(n, k)
print(ans == o, ans)