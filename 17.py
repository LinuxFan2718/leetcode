from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
      if digits == "":
        return []
      phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
      }
      output = [""]
      for c in digits:
        newOutput = []
        for e in output:
          for newLetter in phone[c]:
            newOutput.append(e + newLetter)
        output = newOutput
      return output

s = Solution()
print(s.letterCombinations("23"))