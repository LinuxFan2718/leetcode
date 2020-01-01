from typing import List
class Solution:
    def numDecodings(self, s: str) -> int:
        ans = 1 if any(x in s for x in '123456789') else 0
        i = 0
        while i < len(s):
          if s[i] == "0":
            i += 1
          elif s[i] == "1" and i+1 < len(s):
            if s[i+1] == "0":
              i += 2
            elif s[i+1] in "12":
              ans += 1
              i += 1
            elif s[i+1] in "3456789":
              ans += 2
              i += 2
          elif s[i] == "2" and i+1 < len(s):
            if s[i+1] == "0":
              i += 2
            elif s[i+1] in "12":
              ans += 1
              i += 1
            elif s[i+1] in "3456":
              ans += 2
              i += 2
            elif s[i+1] in "789":
              i += 2
          else:
            i += 1
        return ans

s = Solution()
i = "12"
o = 2
ans = s.numDecodings(i)
print(ans == o, ans)

i = "226"
o = 3
ans = s.numDecodings(i)
print(ans == o, ans)

i = "0"
o = 0
ans = s.numDecodings(i)
print(ans == o, ans)

i = "27"
o = 1
ans = s.numDecodings(i)
print(ans == o, ans)

i = "26"
o = 2
ans = s.numDecodings(i)
print(ans == o, ans)

i = "99"
o = 1
ans = s.numDecodings(i)
print(ans == o, ans)
