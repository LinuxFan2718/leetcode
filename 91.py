from typing import List
class Solution:
  def numDecodings(self, s): 
    if len(s) == 0:
      return 0
    dp = [0] * (len(s) + 1)
    dp[0] = 1

    for i in range(1, len(s) + 1):
      if s[i-1] in '123456789':
        dp[i] += dp[i-1]
      if i != 1 and 10 <= int(s[i-2:i]) and int(s[i-2:i]) <= 26:
        dp[i] += dp[i-2]
    return dp[-1]

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

i = "01"
o = 0
ans = s.numDecodings(i)
print(ans == o, ans)

i = "110"
o = 1
ans = s.numDecodings(i)
print(ans == o, ans)