from typing import List
class Solution:
    def countAndSay(self, n: int) -> str:
        say = '1'
        i = 1
        while i < n:
          i += 1
          newSay = ''
          startRun = 0
          while startRun < len(say):
            lenRun = 1
            while (startRun + lenRun) < len(say) and say[startRun] == say[startRun + lenRun]:
              lenRun += 1
            newSay += str(lenRun) + say[startRun]
            startRun += lenRun
          say = newSay
        return say
        
s = Solution()
# input = 1
# output = "1"
# answer = s.countAndSay(input)
# print(answer == output, answer)

# input = 4
# output = "1211"
# answer = s.countAndSay(input)
# print(answer == output, answer)


for i in range(30):
  answer = s.countAndSay(i)
  print(i, len(answer))