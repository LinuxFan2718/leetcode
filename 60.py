from typing import List
from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        sortedNums = list(range(1, n+1))
        ans = []
        k -= 1

        while len(sortedNums) > 0:
          chunkSize = factorial(n-1)
          chunksToSkip, _ = divmod(k, chunkSize)
          digitToAdd = sortedNums.pop(chunksToSkip)
          ans.append(digitToAdd)
          n -= 1
          k -= chunksToSkip * chunkSize
        
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