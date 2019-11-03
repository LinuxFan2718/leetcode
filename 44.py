from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
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
  }
]
for example in examples:
  computed = s.isMatch(example['s'],example['p'])
  if computed == example['output']:
    print('pass')
  else:
    print('fail', example['s'], example['p'])