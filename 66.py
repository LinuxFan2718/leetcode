from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      carry = 0
      for i in range(len(digits) -1, -1, -1):
        if digits[i] == 9:
          digits[i] = 0
          carry = 1
        else:
          digits[i] += 1
          carry = 0
          break
      if carry == 1:
        digits = [1] + digits

      return digits

s = Solution()
i = [1,2,3]
o = [1,2,4]
ans = s.plusOne(i)
print(ans == o, ans)

i = [0]
o = [1]
ans = s.plusOne(i)
print(ans == o, ans)

s = Solution()
i = [4,3,2,1]
o = [4,3,2,2]
ans = s.plusOne(i)
print(ans == o, ans)

s = Solution()
i = [9,9,9,9,9]
o = [1,0,0,0,0,0]
ans = s.plusOne(i)
print(ans == o, ans)

s = Solution()
i = [1,0,9,9,9,9,9]
o = [1,1,0,0,0,0,0]
ans = s.plusOne(i)
print(ans == o, ans)