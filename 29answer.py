class Solution:
  # @return an integer
  # https://leetcode.com/problems/divide-two-integers/discuss/13403/Clear-python-code
  def divide(self, dividend, divisor):
      positive = (dividend < 0) is (divisor < 0)
      dividend, divisor = abs(dividend), abs(divisor)
      res = 0
      while dividend >= divisor:
          temp, i = divisor, 1
          while dividend >= temp:
              dividend -= temp
              res += i
              i <<= 1
              temp <<= 1
      if not positive:
          res = -res
      return min(max(-2147483648, res), 2147483647)

s = Solution()
print(s.divide(13, 3))
# print(s.divide(7, -3) == -2)
# print(s.divide(4, 4) == 1)
# print(s.divide(1, 1) == 1)

# a = s.divide(-2147483648, -1)
# print(a == 2147483647)
# b = s.divide(-2147483648, 1)
# print(b == -2147483648)