# https://en.wikipedia.org/wiki/Levenshtein_distance
from typing import List
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        return self.minDistanceHelper(word1, word2, dp)

    def minDistanceHelper(self, word1: str, word2: str, dp: dict) -> int:
        if (word1, word2) in dp.keys():
            return dp[(word1,word2)]
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        lastCharDifferent = 0
        if word1[-1] != word2[-1]:
            lastCharDifferent += 1
        dp[(word1,word2)] = min(
            self.minDistanceHelper(word1, word2[:-1], dp) + 1,
            self.minDistanceHelper(word1[:-1], word2, dp) + 1,
            self.minDistanceHelper(word1[:-1], word2[:-1], dp) + lastCharDifferent
            )
        return dp[(word1,word2)]

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