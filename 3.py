from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        while left + longest < len(s):
            if self.withoutRepeating(s[left:left+longest+1]):
                longest += 1
            else:
                left += 1

        return longest
    
    def withoutRepeating(self, s: str) -> bool:
        return len(s) == len(set(list(s)))

solution = Solution()
print("abcabcbb", solution.lengthOfLongestSubstring("abcabcbb"))
print("bbbbb", solution.lengthOfLongestSubstring("bbbbb"))
print("pwwkew", solution.lengthOfLongestSubstring("pwwkew"))
print("", solution.lengthOfLongestSubstring(""))