# The Gray code for decimal 15 rolls over to decimal 0 with only one switch change. 
# This is called the "cyclic" property of a Gray code. 
# 
# In the standard Gray coding the least significant bit follows a 
# repetitive pattern of 2 on, 2 off ( … 11001100 … ); the next digit a pattern 
# of 4 on, 4 off; and so forth. 
from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []
        return ans

s = Solution()
n = 2
o = [0,1,3,2]
ans = s.grayCode(n)
print(o == ans, ans)

n = 0
o = [0]
ans = s.grayCode(n)
print(o == ans, ans)
