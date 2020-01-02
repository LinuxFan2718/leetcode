from typing import List
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
      dp = {}
      return self.isInterleaveHelper(s1, s2, s3, dp)

    def isInterleaveHelper(self, s1: str, s2: str, s3: str, dp: dict) -> bool:
        if (s1,s2,s3) in dp.keys():
          return dp[(s1,s2,s3)]
        elif not s1:
          dp[(s1,s2,s3)] = s2 == s3
        elif not s2:
          dp[(s1,s2,s3)] = s1 == s3
        elif s1[0] == s2[0] == s3[0]:
          dp[(s1,s2,s3)] = self.isInterleaveHelper(s1[1:], s2, s3[1:], dp) or self.isInterleaveHelper(s1, s2[1:], s3[1:], dp)
        elif s1[0] == s3[0]:
          dp[(s1,s2,s3)] = self.isInterleaveHelper(s1[1:], s2, s3[1:], dp)
        elif s2[0] == s3[0]:
          dp[(s1,s2,s3)] = self.isInterleaveHelper(s1, s2[1:], s3[1:], dp)
        else:
          dp[(s1,s2,s3)] = False
        return dp[(s1,s2,s3)]

s = Solution()
s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac"
o = True
ans = s.isInterleave(s1,s2,s3)
print(ans == o)

s1, s2, s3 = "aabcc", "dbbca", "aadbbbaccc"
o = False
ans = s.isInterleave(s1, s2, s3)
print(ans == o)

s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
o = False
ans = s.isInterleave(s1, s2, s3)
print(ans == o)