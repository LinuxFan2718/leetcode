from typing import List
class Solution:
    def simplifyPath(self, path: str) -> str:
      ans = []
      for token in path.split('/'):
        if token in ['', '.']:
          pass
        elif token == '..':
          if len(ans) > 0:
            ans.pop()
        else:
          ans.append(token)
      return '/' + '/'.join(ans)


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

i = "/."
o = '/'
ans = s.simplifyPath(i)
print(ans == o, ans)

i = "/..."
o = "/..."
ans = s.simplifyPath(i)
print(ans == o, ans)

i = "/..hidden"
o = "/..hidden"
ans = s.simplifyPath(i)
print(ans == o, ans)

i = "/home/of/foo/../../bar/../../is/./here/."
o = "/is/here"