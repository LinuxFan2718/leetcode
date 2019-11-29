from typing import List
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        ans = 0
        current = len(s) - 1
        while current >= 0:
          if s[current] == ' ':
            break
          ans += 1
          current -= 1
        return ans

solution = Solution()
s = "Hello World"
o = 5
ans = solution.lengthOfLastWord(s)
print(ans == o, ans)

s = "World"
o = 5
ans = solution.lengthOfLastWord(s)
print(ans == o, ans)

s = "a   World       "
o = 5
ans = solution.lengthOfLastWord(s)
print(ans == o, ans)

s = "      "
o = 0
ans = solution.lengthOfLastWord(s)
print(ans == o, ans)