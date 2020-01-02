from typing import List
class Solution:
    def valid(self, ip: str) -> bool:
        quads = ip.split('.')
        if len(quads) < 4:
            finishEarly = 1
        elif len(quads) == 4:
            finishEarly = 0
        for i in range(len(quads) - finishEarly):
            if not quads[i]:
                return False
            n = int(quads[i])
            if n > 255:
                return False
            if quads[i][0] == '0' and len(quads[i]) > 1:
                return False
        return True
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        if len(s) < 4 or len(s) > 12:
            return []
        
        return self.restoreIpAddressesHelper(s, ans)

    def restoreIpAddressesHelper(self, s: str, ans: List[str]) -> List[str]:
        quads = s.split('.')
        if len(quads) == 4 and self.valid(s):
            ans.append(s)
        else:
            if len(quads) in [2, 3]:
                lastDot = s.rindex('.')
                leftCandidate = s[:lastDot + 1]
                rightCandidateRaw = s[lastDot + 1:]
            elif len(quads) == 1:
                leftCandidate = ''
                rightCandidateRaw = s
            for i in range(1, min(len(rightCandidateRaw), 4)):
                rightCandidate = rightCandidateRaw[:i] + "." + rightCandidateRaw[i:]
                candidate = leftCandidate + rightCandidate
                if self.valid(candidate):
                    self.restoreIpAddressesHelper(candidate, ans)                

        return ans







s = Solution()
i = "25525511135"
o = ["255.255.11.135", "255.255.111.35"]
ans = s.restoreIpAddresses(i)
print(o == ans, ans)

i = "0000"
o = ["0.0.0.0"]
ans = s.restoreIpAddresses(i)
print(o == ans, ans)

i = "00000"
o = []
ans = s.restoreIpAddresses(i)
print(o == ans, ans)

i = "9"
o = []
ans = s.restoreIpAddresses(i)
print(o == ans, ans)

i = "1111"
o = ["1.1.1.1"]
ans = s.restoreIpAddresses(i)
print(o == ans, ans)

i = "11111"
o = ["11.1.1.1", "1.11.1.1", "1.1.11.1", "1.1.1.11", ]
ans = s.restoreIpAddresses(i)
print(sorted(o) == sorted(ans), ans)