from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      res = []
      candidates.sort()
      self.combinationSumHelper(candidates, target, [], 0, res)
      return res

    def combinationSumHelper(self, candidates: List[int], target: int, partialSolution: List[int], index: int, res: List[List[int]]) -> None:
      if target < 0:
        return # bail once this path is not working
      if target == 0:
        res.append(partialSolution)
        return
      for i in range(index, len(candidates)):
        considering = candidates[i]
        self.combinationSumHelper(candidates, target - considering, partialSolution + [considering], i, res)
      
      

s = Solution()
candidates = [2,3,6,7]
target = 7
solution = [
  [7],
  [2,2,3]
]
computed = s.combinationSum(candidates, target)
print(sorted(computed) == sorted(solution), computed)

candidates = [2,3,5]
target = 8
solution = [
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
computed = s.combinationSum(candidates, target)
print(computed == solution, computed)
