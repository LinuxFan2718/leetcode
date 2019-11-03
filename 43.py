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
      res = '0'
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
            thisRes = thisProduct + thisRes
            carry = '0'
          elif len(thisProduct) == 2:
            thisRes = thisProduct[1] + thisRes
            carry = thisProduct[0]
        if carry != '0':
          thisRes = carry + thisRes

        # add thisRes to res
        if len(res) > len(thisRes):
          thisRes = thisRes.rjust(len(res), '0')
        else:
          res = res.rjust(len(thisRes), '0')
        newRes = ''
        carry = '0'
        for k in range(len(res)-1, -1, -1):
          total = hashAddTable[hashAddTable[res[k]][thisRes[k]]][carry]
          if len(total) == 1:
            newRes = total + newRes
            carry = '0'
          if len(total) == 2:
            newRes = total[1] + newRes
            carry = total[0]
        if carry != '0':
          newRes = carry + newRes
        res = newRes
      while len(res) > 1 and res[0] == '0':
        res = res[1:]
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

num1 = "1"
num2 = "456"
output = "456"
computed = s.multiply(num1, num2)
print(computed, computed == output)

num1 = "999999999999"
num2 = "4999999999956"
output = "4999999999951000000000044"
computed = s.multiply(num1, num2)
print(computed, computed == output)

num1 = "9133"
num2 = "0"
output = "0"
computed = s.multiply(num1, num2)
print(computed, computed == output)
