from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        return 1

s = Solution()
input = [0,1,0,2,1,0,1,3,2,1,2,1]
output = 6
computed = s.trap(input)
print(computed, computed == output)