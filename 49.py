from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      answers = {}
      for i in range(len(strs)):
        sortedWord = ''.join(sorted(strs[i]))
        if sortedWord in answers.keys():
          answers[sortedWord].append(strs[i])
        else:
          answers[sortedWord] = [strs[i]]
      return [x for x in answers.values()]
        
s = Solution()
i = ["eat", "tea", "tan", "ate", "nat", "bat"]
o = [
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
answer = s.groupAnagrams(i)
print(answer == o)
print(answer)
print(o)