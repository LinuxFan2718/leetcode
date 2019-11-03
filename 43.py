from typing import List
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
      if len(num1) == 0 or len(num2) == 0:
        return '0'
      hashMultTable = {}
      for x in range(10):
          hashMultTable[str(x)] = {}
          for y in range(10):
              hashMultTable[str(x)][str(y)] = str(x * y)
      hashAddTable = {} # x from 0-82, y from 0-9, get x+y
      for x in range(82):
        hashAddTable[str(x)] = {}
        for y in range(10):
            hashAddTable[str(x)][str(y)] = str(x + y)
      res = [] # products from each digit of num2
      #   num1
      # * num2
      # ------
      #    res
      for i in enumerate(list(num2)[::-1]):
        thisRes = '0' * i[0]
        carry = '0'
        for j in list(num1)[::-1]:
          thisProduct = hashAddTable[hashMultTable[i[1]][j]][carry] # one or two-digit string
          if len(thisProduct) == 1:
            






      return res
        
s = Solution()
num1 = "2"
num2 = "3"
output = "6"
computed = s.multiply(num1, num2)
print(computed, computed == output)

num1 = "123"
num2 = "456"
output = "56088"
computed = s.multiply(num1, num2)
print(computed, computed == output)
