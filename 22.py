from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      for c in s:
        if c == '(':
          stack.append(c)
        elif c == ')':
          if len(stack) == 0:
            return False
          stackPop = stack.pop()
          if c == ')':
            if stackPop != '(':
              return False
        else:
          raise("invalid character", c, stack) 
      return len(stack) >= 0
    def generateParenthesis(self, n: int) -> List[str]:
      answers = ["("]
      for _ in range(2*n-1):
        newAnswers = []
        for answer in answers:
          candidates = []
          if answer.count("(") < n:
            candidates.append(answer + "(")
          if answer.count(")") < n:
            candidates.append(answer + ")")
          for candidate in candidates:
            if self.isValid(candidate):
              newAnswers.append(candidate)
        answers = newAnswers
      return answers


        
s = Solution()
answer = ["((()))", "(()())", "(())()", "()(())", "()()()"]
answer.sort()

q = s.generateParenthesis(3)
print(sorted(q) == answer)
pass