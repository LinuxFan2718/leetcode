from typing import List
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
      hashMultTable = {}
      for x in range(10):
          hashMultTable[str(x)] = {}
          for y in range(10):
              hashMultTable[str(x)][str(y)] = str(x * y)
      hashAddTable = {}
      for x in range(10):
        hashAddTable[str(x)] = {}
        for y in range(10):
            hashAddTable[str(x)][str(y)] = str(x + y)
      res = ''

      if len(num1) < len(num2):
        num1, num2 = num2, num1
      # num1 always longer or equal length
      listNum1, listNum2 = list(num1), list(num2)
      carry = '0'
      while len(listNum2) > 0:
        thisNum1, thisNum2 = listNum1.pop(), listNum2.pop()
        thisProductPreCarry = hashMultTable[thisNum1][thisNum2]
        thisProductPostCarry = ''
        if len(thisProductPreCarry) == 1:
          thisProductPostCarry = hashAddTable[thisProductPreCarry][carry]
        elif len(thisProductPreCarry) == 2:
          onesDigit, tensDigit = thisProductPreCarry[1], thisProductPreCarry[0]
          temp = hashAddTable[onesDigit][carry]
          if len(temp) == 1:
            thisProductPostCarry = hashAddTable[temp][carry]
          elif len(temp) == 2:
            tempOnesDigit, tempTensDigit = temp[1], temp[0]
            temp2 = hashAddTable[tempOnesDigit][carry]
            temp2OnesDigit, temp2TensDigit = temp2[1], temp2[0]
            temp3TensDigit = hashAddTable[tempTensDigit][temp2TensDigit]
            thisProductPostCarry = temp3TensDigit + temp2OnesDigit
          if len(thisProductPostCarry) == 1:
            carry = tensDigit
            res += thisProductPostCarry
          elif len(thisProductPostCarry) == 2:
            thisProductPostCarryOnes, thisProductPostCarryTens = thisProductPostCarry[1], thisProductPostCarry[0]
            carry = hashAddTable[tensDigit][thisProductPostCarryTens]
            res += thisProductPostCarryOnes



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
