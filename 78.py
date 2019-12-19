from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []   
        ans = [[x] for x in range(0,1+n-k)]
        newAns = []
        while len(ans[-1]) < k:
            for combination in ans:
                for i in range(combination[-1]+1, n):
                    newAns.append(combination + [i])
            ans = newAns
            newAns = []
        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in range(len(nums)+1):
            ans += self.combine(len(nums), i)
        for combination in ans:
            combination[:] = [nums[j] for j in combination]
        return ans

s = Solution()
nums = [1,2,3]
o = [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
ans = s.subsets(nums)
print(sorted(ans) == sorted(o), ans)