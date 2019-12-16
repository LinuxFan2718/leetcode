from typing import List
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return -1

s = Solution()
word1 = "horse"
word2 = "ros"
o = 3
ans = s.minDistance(word1, word2)
print(ans == o)

word1 = "intention"
word2 = "execution"
o = 5
ans = s.minDistance(word1, word2)
print(ans == o)