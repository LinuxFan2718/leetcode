from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
      ans = []
      while len(words) > 0:
        lineWords = []
        while len(words) > 0 and sum([len(word)+1 for word in lineWords + [words[0]]]) - 1 <= maxWidth:
          lineWords.append(words.pop(0))
        if len(words) == 0 or len(lineWords) == 1: # last line or one-word line, left justify
          formattedLine = ' '.join(lineWords)
          ans.append(formattedLine + ' ' * (maxWidth - len(formattedLine)))
        else: # not last line, fully justify
          numChars = sum([len(word) for word in lineWords])
          numSpacesTotal = maxWidth - numChars
          numGroupSpaces = len(lineWords) - 1
          smallSpacesLength, numExtraSpaces = divmod(numSpacesTotal, numGroupSpaces)
          thisLine = ''
          while len(lineWords) > 1:
            thisSpace = ' ' * smallSpacesLength
            if numExtraSpaces > 0:
              thisSpace += ' '
              numExtraSpaces -= 1
            thisLine += lineWords.pop(0) + thisSpace
          thisLine += lineWords.pop(0)
          ans.append(thisLine)
      return ans

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