from typing import List
from math import factorial
from functools import reduce
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if 1 in (m, n):
            return 1
        r = min(m,n) - 1
        n = max(m,n)
        #  n! / r! / (n-r)!
        # ans = len(list(combinations_with_replacement(range(large), small)))
        # (n+r-1)! / r! / (n-1)!
        numerator = set(range(1, n+r))
        denominator1 = int(factorial(r))
        denominator2 = set(range(1, n))

        multiplierNums = numerator - denominator2
        product = int(reduce((lambda x,y: x*y), list(multiplierNums)))
        return int(product / denominator1)

s = Solution()
m = 3
n = 2
o = 3
ans = s.uniquePaths(m, n)
print(ans == o, ans)

m = 7
n = 3
o = 28
ans = s.uniquePaths(m, n)
print(ans == o, ans)

m = 57
n = 2
o = 57
ans = s.uniquePaths(m, n)
print(ans == o, ans)

m = 23
n = 12
o = 193536720
ans = s.uniquePaths(m, n)
print(ans == o, ans)

m = 1
n = 2
o = 1
ans = s.uniquePaths(m, n)
print(ans == o, ans)