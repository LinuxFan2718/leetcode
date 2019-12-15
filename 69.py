# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Binary_numeral_system_(base_2)

from typing import List
import math
class Solution:
    def mySqrt(self, x: int) -> int:
      if x == 0:
        return x
      candidate1 = int(math.exp(0.5*math.log(x)))
      candidate2 = candidate1 + 1
      if candidate2 * candidate2 <= x:
        return candidate2
      else:
        return candidate1

s = Solution()
i = 4
o = 2
ans = s.mySqrt(i)
print(ans == o)

i = 8
o = 2
ans = s.mySqrt(i)
print(ans == o)

i = 2147395600
o = 46340
ans = s.mySqrt(i)
print(ans == o, ans)