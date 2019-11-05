from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
      self.memo = {}
      return self.helper(s, p)

    def helper(self, s: str, p: str) -> bool:
      memo = self.memo
      if (s,p) in memo:
        return memo[(s,p)]
      if len(p) == 0:
        memo[(s,p)] = len(s) == 0
      elif len(p) - p.count('*') > len(s):
        memo[(s,p)] = False
      elif p[0] == "*":
        if len(s) > 0 and len(p) > 0 and p[-1] not in ['?', '*'] and s[-1] != p[-1]:
          memo[(s,p)] = False # ugly speed hack to check last chars match if both letters
        else:
          j = 0
          while j < len(p) and p[j] == "*":
            j += 1
          for i in range(len(s)+1):
            if self.helper(s[i:], p[j:]):
              memo[(s, p)] = True
          if (s,p) not in memo:
            memo[(s,p)] = False
      elif p[0] == "?":
        if len(s) == 0:
          memo[(s,p)] = False     
        else:
          memo[(s,p)] = self.helper(s[1:], p[1:])
      else: # p[0] is a letter
        if len(s) == 0 or p[0] != s[0]:
          memo[(s,p)] = False
        elif p[0] == s[0]:
          memo[(s,p)] = self.helper(s[1:], p[1:])
      return memo[(s,p)]

s = Solution()
examples = [
  {
    's': "hi",
    'p': "*?",
    'output': True
  },{
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
  },{
    's': "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb",
    'p': "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a",
    'output': False 
  },{
    's': "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
    'p': "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb",
    'output': None 
  }
]

for example in examples:
  computed = s.isMatch(example['s'],example['p'])
  if computed == example['output']:
    print('pass')
  else:
    print('fail', computed, example['s'], example['p'])