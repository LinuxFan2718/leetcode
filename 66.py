from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return digits

s = Solution()
i = [1,2,3]
o = [1,2,4]
ans = s.plusOne(i)
print(ans == o, ans)

s = Solution()
i = [4,3,2,1]
o = [4,3,2,2]
ans = s.plusOne(i)
print(ans == o, ans)
