from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      res = []
      candidates.sort()
      self.combinationSumHelper(candidates, target, [], 0, res)
      return [list(x) for x in set(tuple(x) for x in res)]

    def combinationSumHelper(self, candidates: List[int], target: int, partialSolution: List[int], index: int, res: List[List[int]]) -> None:
      if target < 0:
        return # bail once this path is not working
      if target == 0:
        res.append(partialSolution)
        return
      for i in range(index, len(candidates)):
        considering = candidates[i]
        self.combinationSumHelper(candidates, target - considering, partialSolution + [considering], i+1, res)

s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
solution = [
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
computed = s.combinationSum2(candidates, target)
print(sorted(computed) == sorted(solution), computed)

candidates = [2,5,2,1,2]
target = 5
solution = [
  [1,2,2],
  [5]
]
computed = s.combinationSum2(candidates, target)
print(sorted(computed) == sorted(solution), computed)
