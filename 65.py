from typing import List
class Solution:
    def isNumber(self, s: str) -> bool:
        digits = '1234567890'
        s = s.strip()
        if len(s) == 0:
            return False
        seenE = False
        for i in range(len(s)-1):
            if s[i] not in '1234567890-+.e':
                return False
            if s[i] in '-+' and i != 0 and s[i-1] != 'e':
                return False
            if s[i] == '.' and (i == 0 or s[i-1] not in digits or s[i+1] not in digits or seenE):
                return False
            if s[i] == 'e':
                if seenE:
                    return False
                seenE = True
                if i == 0 or s[i-1] not in digits or s[i+1] not in '1234567890-+':
                    return False
        if s[-1] not in digits:
            return False
        return True
            



s = Solution()

o = {
        "0": True,
        " 0.1 ": True,
        "abc": False,
        "1 a": False,
        "2e10": True,
        " -90e3   ": True,
        " 1e": False,
        "e3": False,
        " 6e-1": True,
        " 99e2.5 ": False,
        "53.5e93": True,
        " --6 ": False,
        "-+3": False,
        "95a54e53": False
    }

for k in o:
    ans = s.isNumber(k)
    if ans != o[k]:
        print(k, o[k])