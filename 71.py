from typing import List
class Solution:
    def simplifyPath(self, path: str) -> str:
        return path

s = Solution()
i = "/home/"
o = "/home"
ans = s.simplifyPath(i)
print(ans == o, ans)

i = "/../"
o = "/"
ans = s.simplifyPath(i)
print(ans == o, ans)

i = "/home//foo/"
o = "/home/foo"
ans = s.simplifyPath(i)
print(ans == o, ans)

i =  "/a/./b/../../c/"
o = "/c"
ans = s.simplifyPath(i)
print(ans == o, ans)

i = "/a/../../b/../c//.//"
o = "/c"
ans = s.simplifyPath(i)
print(ans == o, ans)

i = "/a//b////c/d//././/.."
o = "/a/b/c"
ans = s.simplifyPath(i)
print(ans == o, ans)
