from typing import List
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
      minAnswer = -2**31
      maxAnswer = 2**31 - 1
      if dividend == 0:
        return 0
      negativeDivident = dividend < 0
      negativeDivisor = divisor < 0
      negativeAnswer = negativeDivident ^ negativeDivisor
      dividend = abs(dividend)
      divisor = abs(divisor)
      if divisor == 1:
        if negativeAnswer:
          return max(-dividend, minAnswer)
        else:
          return min(dividend, maxAnswer)
      i = 0
      while dividend - divisor >= 0 and i < maxAnswer:
        dividend -= divisor
        i += 1
      if i >= maxAnswer:
        return maxAnswer
      
      if negativeAnswer:
        i = -i
      return i


        
s = Solution()
# print(s.divide(10, 3) == 3)
# print(s.divide(7, -3) == -2)
# print(s.divide(4, 4) == 1)
# print(s.divide(1, 1) == 1)

# a = s.divide(-2147483648, -1)
# print(a == 2147483647)
b = s.divide(-2147483648, 1)
print(b == -2147483648)
