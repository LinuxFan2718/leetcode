from typing import List
class Solution:
    def myPow(self, x: float, n: int) -> float:
      if n == 0:
        return 1.0
      if n == 1:
        return x
      if n < 0:
        n = -n
        x = 1/x
      half = self.myPow(x, n // 2)
      if n % 2 == 0:
        return half * half
      elif n % 2 == 1:
        return half * half * x

s = Solution()
x, n = 2.00000, 10
o = 1024.00000
ans = s.myPow(x,n)
print(round(ans,4) == round(o,4), ans, o)

x, n = 2.10000, 3
o = 9.26100
ans = s.myPow(x,n)
print(round(ans,4) == round(o,4), ans, o)
x, n = 2.00000, -2
o = 0.25000
ans = s.myPow(x,n)
print(round(ans,4) == round(o,4), ans, o)

x, n = 0.00001, 2147483647
o = 0.0
ans = s.myPow(x,n)
print(round(ans,4) == round(o,4), ans, o)