from typing import List
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        ans = ""
        thisInterval = {}
        needle = {}
        for c in t:
            if c in needle.keys():
                needle[c] += 1
            else:
                needle[c] = 1
                thisInterval[c] = 0
        for right in range(len(s)):
            if s[right] in needle.keys():
                thisInterval[s[right]] += 1
            while all([thisInterval[k] >= needle[k] for k in needle.keys()]):
                if ans == "" or len(ans) > right - left:
                    ans = s[left:right+1]
                if s[left] in needle.keys():
                    thisInterval[s[left]] -= 1
                left += 1
        return ans


solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
o = "BANC"
ans = solution.minWindow(s, t)
print(o == ans, ans)

s = "bba"
t = "ab"
o = "ba"
ans = solution.minWindow(s, t)
print(o == ans, ans)