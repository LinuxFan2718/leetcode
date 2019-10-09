from typing import List
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
          return 0
        for i in range(len(haystack)- len(needle) +1):
          if haystack[i:i+len(needle)] == needle:
            return i
        return -1
s = Solution()
haystack = "hello"
needle = "ll"
print(s.strStr(haystack, needle) == 2)
haystack = "aaaaa"
needle = "bba"
print(s.strStr(haystack, needle) == -1)
haystack = "hello"
needle = "lo"
print(s.strStr(haystack, needle) == 3)