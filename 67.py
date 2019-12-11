from typing import List
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = a
        return ans

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