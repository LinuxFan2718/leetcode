from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      for c in s:
        if c in ['(', '[', '{']:
          stack.append(c)
        elif c in [')', ']', '}']:
          if len(stack) == 0:
            return False
          stackPop = stack.pop()
          if c == ')':
            if stackPop != '(':
              return False
          if c == ']':
            if stackPop != '[':
              return False
          if c == '}':
            if stackPop != '{':
              return False
        else:
          raise("invalid character", c, stack) 
      return len(stack) == 0
        


s = Solution()
print(s.isValid("()") == True)
# print(s.isValid('()[]\{\}') == True)
print(s.isValid("(]") == False)
print(s.isValid("([)]") == False)
print(s.isValid("{[]}") == True)

