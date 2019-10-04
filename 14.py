class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        if len(strs) == 0:
            return answer
        for i in range(len(strs[0])):
            thisLetter = strs[0][i]
            for s in strs:
                if i < len(s) and s[i] == thisLetter:
                    pass
                else:
                    return answer
            answer += thisLetter
        
        return answer