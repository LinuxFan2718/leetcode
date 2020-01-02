from typing import List
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        return False

s = Solution()
s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac"
o = True
ans = s.isInterleave(s1,s2,s3)
print(ans == o)

s1, s2, s3 = "aabcc", "dbbca", "aadbbbaccc"
o = False
ans = s.isInterleave(s1, s2, s3)
print(ans == o)