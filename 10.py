from typing import List
import string
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) == 0:
            return True
        if len(p) == 0:
            return False
        if p[0] in string.ascii_lowercase:
            if len(p) > 1 and p[1] == '*': # a*
                if p[0] != s[0]:
                    return self.isMatch(s, p[2:])
                else: # a* a...



            elif p[0] == s[0]:
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        elif p[0] == '.':
            if len(p) > 1 and p[1] == '*': # .*

            else:
                return self.isMatch(s[1:], p[1:])
            
        elif p[0] == '*':
            raise Exception(s, p, "p[0] == *")
        else:
            raise Exception(s, p, 'unrecognized character')


        

solution = Solution()
print(solution.isMatch('', '.*') == True)
print(solution.isMatch('aa', 'a') == False)
print(solution.isMatch('aa', 'a*') == True)
print(solution.isMatch('aab', 'c*a*b') == True)
print(solution.isMatch('mississippi', 'mis*is*p*.') == True)
