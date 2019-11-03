from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
      if len(p) == 0:
        return len(s) == 0
      if p[0] == "*":
        for i in range(len(s)+1):
          if self.isMatch(s[i:], p[1:]):
            return True
        return False
      elif p[0] == "?":
        if len(s) == 0:
          return False     
        else:
          return self.isMatch(s[1:], p[1:])
      else: # p[0] is a letter
        if len(s) == 0 or p[0] != s[0]:
          return False
        elif p[0] == s[0]:
          return self.isMatch(s[1:], p[1:])
      return True

s = Solution()
examples = [
  {
    's': "aa",
    'p': "a",
    'output': False
  },{
    's': "aa",
    'p': "*",
    'output': True   
  },{
    's': "cb",
    'p': "?a",
    'output': False   
  },{
    's': "adceb",
    'p': "*a*b",
    'output': True
  },{
    's': "acdcb",
    'p': "a*c?b",
    'output': False   
  },{
    's': "aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba",
    'p': "a*******b",
    'output': False 
  }
]
for example in examples:
  computed = s.isMatch(example['s'],example['p'])
  if computed == example['output']:
    print('pass')
  else:
    print('fail', example['s'], example['p'])