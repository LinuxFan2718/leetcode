from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        return ans

s = Solution()
i = "25525511135"
o = ["255.255.11.135", "255.255.111.35"]
ans = s.restoreIpAddresses(i)
print(sorted(o) == sorted(ans), ans)