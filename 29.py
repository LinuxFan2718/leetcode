from typing import List
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
      minAnswer = -(1<<31)
      maxAnswer = (1<<31) - 1
      negativeAnswer = -1 if (dividend < 0) ^ (divisor < 0) else 1
      dividend = abs(dividend)
      divisor = abs(divisor)
      quotient = 0
      temp = 0
      for i in range(31, -1, -1):
        if((divisor << i) <= dividend - temp):
          temp += divisor << i
          quotient |= 1 << i
      return max(minAnswer, min(maxAnswer, negativeAnswer * quotient))

    # test down from the highest  
    # bit and accumulate the  
    # tentative value for valid bit 
    def ignoreme(self, dividend: int, divisor: int) -> int:
      for i in range(31, -1, -1): 
          if (temp + (divisor << i) <= dividend): 
              temp += divisor << i
              quotient |= 1 << i
        
s = Solution()
print(s.divide(10, 3) == 3)
c = s.divide(7, 3)
print(c == 2,c)
d = s.divide(7, -3)
print(d == -2,d)
print(s.divide(4, 4) == 1)
print(s.divide(1, 1) == 1)

a = s.divide(-2147483648, -1)
print(a == 2147483647)
b = s.divide(-2147483648, 1)
print(b == -2147483648)
