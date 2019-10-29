from typing import List
class Solution:
  def combinationSum(self, candidates, target):
    res = []
    candidates.sort()
    self.dfs(candidates, target, 0, [], res)
    return res
    
  def dfs(self, nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return 
    for i in range(index, len(nums)):
        candidate = nums[i]
        self.dfs(nums, target-candidate, i, path+[candidate], res)

s = Solution()
candidates = [2,3,6,7]
target = 7
solution = sorted([
  [7],
  [2,2,3]
])
computed = s.combinationSum(candidates, target)
print(computed == solution, computed)

candidates = [2,3,5]
target = 8
solution = [
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
computed = s.combinationSum(candidates, target)
print(computed == solution, computed)
