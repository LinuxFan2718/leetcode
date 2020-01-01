# The Gray code for decimal 15 rolls over to decimal 0 with only one switch change. 
# This is called the "cyclic" property of a Gray code. 
# 
# In the standard Gray coding the least significant bit follows a 
# repetitive pattern of 2 on, 2 off ( … 11001100 … ); the next digit a pattern 
# of 4 on, 4 off; and so forth. 
from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        grayCode = [0] * n # grayCode is 0 in Gray code
        SameBitLength = [2**i for i in range(n, 0, -1)]
        countdownUntilFlip = [x // 2 - 1 for x in SameBitLength]

        for _ in range(2**n - 1):
            indexToChange = countdownUntilFlip.index(0)

            countdownUntilFlip[indexToChange] = SameBitLength[indexToChange]
            countdownUntilFlip = [x - 1 for x in countdownUntilFlip]
            

            if grayCode[indexToChange] == 0:
                grayCode[indexToChange] = 1
            else:
                grayCode[indexToChange] = 0
            ans.append(int(''.join([str(x) for x in grayCode]),2))
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
pass
