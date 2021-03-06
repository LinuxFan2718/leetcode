from typing import List
class Solution:
    def longestValidParentheses(self, s: str) -> int:
      longest = 0
      currentLength = 0
      stack = []
      for paren in enumerate(s):
        if paren[1] == '(':
          if paren[0] != 0 and s[paren[0] - 1] == '(':
            stack.append(paren[0])
          else:
            stack.append(paren[0] - currentLength)
        elif paren[1] == ')':
          if len(stack) > 0: # not an unmatched )
            currentLength = 1 + paren[0] - stack.pop()
          else:
            currentLength = 0 # unmatched ) resets current run
        if currentLength > longest:
          longest = currentLength
      return longest



s = Solution()
input = "(()"
output = 2
lvp = s.longestValidParentheses(input)
print(lvp, lvp == output)

input = ")()())"
output = 4
lvp = s.longestValidParentheses(input)
print(lvp, lvp == output)

input = ")"
output = 0
lvp = s.longestValidParentheses(input)
print(lvp, lvp == output)

input = "()(()"
output = 2
lvp = s.longestValidParentheses(input)
print(lvp, lvp == output)

input = "())()()(())((()(()()(((()))((((())((()(())()())(()((((()))()(()))(())()(())(()(((((())((((((()())())(()(()((())()))(()))))))()(()))((((())()()()))()()()(((()(()())(()()(()(()()(((()))))))()()))())())((()()))))))((()))(((()((())()(()()))((())))()()())))))))()))))(()))))()))()))()((())))((()))(()))))))(((()))))))))()(()()()(())((())()))()()(())))()()))(()())()))(((()())()))((())((((()))(()(()(()()()(((())()(((((()))((()(((((())(()()))((((((((()(()(()(()(())))(())(()())())(()((((()(())((()(())))(())))()(((((()(()()(())))))))())(())(())(()()(((())))((()))(((((()))))())))()((()))()))))())))))((())(((((()()))((((())))(((()(()(())())(((()(()(()()()())))())()))((()((())())()()()(((())(((((()((((((()((()())))((((())((()(((((((()(()((()()()(()(()())(()(()()((((())))()(((()())))(()()))()(()()()()(((((())(()))))((()))())))()((((((()))())))()(()))(())))((((()())(((((()()())(((((())(()())(()))))()(()()))()))))))())))(((())(()(()()))(()))()(((())))())((((()(((()))))))()(()(()))()()(()()))))))))((()))))))(())((()((()))()))((((((()())))))(()((())((((()))))(()(()()()()(()))()()(()(()))(()()(((((((()())(())(()())((())())()(()())((())()())())(()())))())))(())())())(())((()())(((()()))()))()()))()(()(())((((((((())))()((())((()((((((((((()))))(()(((((())(()(()())())))((())())))))()))(()((()()))((()((())()()()((()(())())((())())(()()(((())))))())()()(()))()())(()(()((())))((((()()(())))())(())(()(()(())())())(()()())()(())())))(()()(((())))((()()(((())()()(()())((((()()(()())(()((((()(()()(()(()(((()((()())(()()))(()((((()(((((()))))()()))(((()((((((()(()()()()())()))(()(())))))((()(((()())())))(((()()))(()(()(((((((()()))(()(())))())()(())())(())(()))(())(()))()()(()()())))))()))()((())(((()((((((((())()()))())))((()())("
output = 310
lvp = s.longestValidParentheses(input)
print(lvp, lvp == output)
