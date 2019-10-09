from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        return [0]

solution = Solution()
s = "barfoothefoobarman",
words = ["foo","bar"]
correctAnswer = [0,9]
actualAnswer = solution.findSubstring(s, words)
print(correctAnswer == actualAnswer)

s = "wordgoodgoodgoodbestword",
words = ["word","good","best","word"]
correctAnswer = []
actualAnswer = solution.findSubstring(s, words)
print(correctAnswer == actualAnswer)