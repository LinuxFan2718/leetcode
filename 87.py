from typing import List
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
      dp = {}
      return self.isScrambleHelper(s1, s2, dp)

    def isScrambleHelper(self, s1: str, s2: str, dp) -> bool:
        if (s1,s2) in dp:
          return dp[(s1,s2)]
        if sorted(s1) != sorted(s2):
          dp[(s1,s2)] = False
        elif len(s1) < 4:
          dp[(s1,s2)] = True
        else:
          for i in range(1, len(s1)):
            if (s1,s2) not in dp and self.isScrambleHelper(s1[i:], s2[i:], dp) and self.isScrambleHelper(s1[:i], s2[:i], dp) or self.isScrambleHelper(s1[:i], s2[-i:], dp) and self.isScrambleHelper(s1[i:], s2[:-i], dp):
              dp[(s1,s2)] = True
        if (s1,s2) not in dp:
          dp[(s1,s2)] = False
        return dp[(s1,s2)]

s = Solution()
s1, s2 = "great", "rgeat"
o = True
ans = s.isScramble(s1, s2)
print(o == ans)

s1, s2 = "abcde", "caebd"
o = False
ans = s.isScramble(s1, s2)
print(o == ans)

s1, s2 = "abb", "bba"
o = True
ans = s.isScramble(s1, s2)
print(o == ans)

s1, s2 = "abcdefghijklmnopq", "efghijklmnopqcadb"
o = False
ans = s.isScramble(s1, s2)
print(o == ans)

s1, s2 = "ccabcbabcbabbbbcbb", "bbbbabccccbbbabcba"
o = False
ans = s.isScramble(s1, s2)
print(o == ans)

s1, s2 = "xstjzkfpkggnhjzkpfjoguxvkbuopi", "xbouipkvxugojfpkzjhnggkpfkzjts"
o = False
ans = s.isScramble(s1, s2)
print(o == ans)