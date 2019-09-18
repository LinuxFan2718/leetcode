from typing import List
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        for length in range(len(s), 1, -1):
            for left_index in range(0, 1+len(s)-length):
                substring_to_check = s[left_index:left_index+length]
                if self.isPalindrome(substring_to_check):
                    return substring_to_check
        return s[0]

    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[-1-i]: 
                return False
        return True

solution = Solution()
a1 = solution.longestPalindrome("babad")
print(a1)
print(a1 in ["bab", "aba"])
s2 = solution.longestPalindrome("cbbd")
print(s2)
print(s2 == "bb")
print(solution.longestPalindrome(""))
print(solution.longestPalindrome("a"))
print(solution.longestPalindrome("aa"))
print(solution.longestPalindrome("aaa"))
print(solution.longestPalindrome("abcdefghijklomnopqrstuvwxyzz"))