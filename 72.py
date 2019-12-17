from typing import List
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        lastCharDifferent = 0
        if word1[-1] != word2[-1]:
            lastCharDifferent += 1
        return min(
            self.minDistance(word1, word2[:-1]) + 1,
            self.minDistance(word1[:-1], word2) + 1,
            self.minDistance(word1[:-1], word2[:-1]) + lastCharDifferent
            )

s = Solution()
word1 = "horse"
word2 = "ros"
o = 3
ans = s.minDistance(word1, word2)
print(ans == o, ans)

word1 = "intention"
word2 = "execution"
o = 5
ans = s.minDistance(word1, word2)
print(ans == o, ans)