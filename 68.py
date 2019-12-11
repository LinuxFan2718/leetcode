from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        return words

s = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
o = [
   "This    is    an",
   "example  of text",
   "justification.  "
]
ans = s.fullJustify(words, maxWidth)
print(ans == o)

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
o = [
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
ans = s.fullJustify(words, maxWidth)
print(ans == o)

words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
o = [
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
ans = s.fullJustify(words, maxWidth)
print(ans == o)