from typing import List
import string
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) == 0:
            return True
        if len(p) == 0:
            return False
        
        if p[0] in string.ascii_lowercase: # we are matching a letter not . or *
            if len(p) > 1 and p[1] == '*': # a*
                if p[0] != s[0]: # matched 0 chars from string
                    return self.isMatch(s, p[2:]) # drop wildcard a* from p and move on
                else: # a* matched 1+ a's
                    while len(s) > 0 and s[0] == p[0]:
                        if self.isMatch(s, p[2:]):
                            return True
                        s = s[1:] # drop all identical characters
                        if len(s) == 0:
                            return True
                    if self.isMatch(s, p[2:]): # check one more time with all a's removed from 
                        return True
                    return False
            elif len(s) == 0:
                return False
            elif p[0] == s[0]:
                return self.isMatch(s[1:], p[1:])
            else:
                return False

        elif p[0] == '.':
            if len(p) > 1 and p[1] == '*': # .*
                    while len(s) > 0:
                        if self.isMatch(s, p[2:]):
                            return True
                        s = s[1:] # drop all characters
                    return True
            else:
                return self.isMatch(s[1:], p[1:])
            
        elif p[0] == '*':
            raise Exception(s, p, "p[0] == *")
        else:
            raise Exception(s, p, 'unrecognized character')


        

solution = Solution()
print(1, solution.isMatch('', '.*') == True)
print(2, solution.isMatch('aa', 'a') == False)
print(3, solution.isMatch('aa', 'aa') == True)
print(4, solution.isMatch('aa', 'aaa') == False)
print(5, solution.isMatch('aa', 'a.') == True)
print(6, solution.isMatch('aa', '.a') == True)
print(7, solution.isMatch('aa', 'a*') == True)
print(8, solution.isMatch('aab', 'c*a*b') == True)
print(9, solution.isMatch('mississippi', 'mis*is*p*.') == False)
