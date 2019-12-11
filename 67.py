from typing import List
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        carry = '0'
        if len(a) > len(b):
          short = b[::-1]
          long = a[::-1]
        else:
          short = a[::-1]
          long = b[::-1]
        for i in range(len(short)):
          if short[i] == long[i]:
            ans += carry
            carry = short[i]
          else:
            if carry == '0':
              ans += '1'
            else:
              ans += '0'
        i += 1
        while i < len(long):
          if carry == '0':
            ans += long[i]
          else:
            if long[i] == '0':
              ans += carry
              carry = '0'
            else:
              ans += '0'
          i += 1
        if carry == '1':
          ans += '1'
          carry = '0'
        return ans[::-1]

s = Solution()
a = "11"
b = "1"
o = "100"
ans = s.addBinary(a,b)
print(ans == o, ans)

a = "1010"
b = "1011"
o = "10101"
ans = s.addBinary(a,b)
print(ans == o, ans)

a = "100"
b = "110010"
o = '110110'
ans = s.addBinary(a,b)
print(ans == o, ans)