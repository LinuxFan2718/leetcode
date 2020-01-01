from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [sorted(nums)]
        for i in range(len(nums) - 1, -1, -1):
          for subset in [subset for subset in ans if len(subset) == i + 1]:
            for j in range(len(subset)):
              candidateSubset = subset[:j] + subset[j+1:]
              if candidateSubset not in ans:
                ans.append(candidateSubset)
        return ans

s = Solution()
i = [1,2,2]
o = [
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
ans = s.subsetsWithDup(i)
print(sorted(o) == sorted(ans), ans)

i = [1]
o = [
  [1],
  []
]
ans = s.subsetsWithDup(i)
print(sorted(o) == sorted(ans), ans)

i = []
o = [[]]
ans = s.subsetsWithDup(i)
print(sorted(o) == sorted(ans), ans)

i = [4,4,4,1,4]
o = [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
ans = s.subsetsWithDup(i)
print(sorted(o) == sorted(ans), ans)