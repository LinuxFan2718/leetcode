from typing import List
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return False

s = Solution()
s1, s2 = "great", "rgeat"
o = True
ans = s.isScramble(s1, s2)
print(o == ans)

s1, s2 = "abcde", "caebd"
o = False
ans = s.isScramble(s1, s2)
print(o == ans)