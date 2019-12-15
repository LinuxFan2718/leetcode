# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Binary_numeral_system_(base_2)

from typing import List
class Solution:
    def mySqrt(self, x: int) -> int:
      binaryString = bin(x)
      binaryLen = len(binaryString) - 2

s = Solution()
i = 4
o = 2
ans = s.mySqrt(i)
print(ans == o)

i = 8
o = 2
ans = s.mySqrt(i)
print(ans == o)
        