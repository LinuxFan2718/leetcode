from typing import List, Dict
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      # { ((candidates), target): solutionSet }
      memo = {}
      return self.combinationSumHelper(candidates, target, memo)

    def combinationSumHelper(self, candidates: List[int], target: int, memo: Dict) -> List[List[int]]:
      theseArgs = (tuple(candidates), target)
      if theseArgs in memo.keys():
        return memo[theseArgs]
      for candidate in candidates:
        if target - candidate == 0:
          
      return [1]

s = Solution()
candidates = [2,3,6,7]
target = 7
solution = [
  [7],
  [2,2,3]
]
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
