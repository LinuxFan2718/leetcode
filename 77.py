from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []   
        ans = [[x] for x in range(1,2+n-k)]
        newAns = []
        while len(ans[-1]) < k:
            for combination in ans:
                for i in range(combination[-1]+1, n+1):
                    newAns.append(combination + [i])
            ans = newAns
            newAns = []
        return ans

s = Solution()
n = 4
k = 2
o = [
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
ans = s.combine(n,k)
print(sorted(o) == sorted(ans), ans)

ans = s.combine(4,1)
print(ans)

ans = s.combine(1,1)
print(ans)

ans = s.combine(4,4)
print(ans)
