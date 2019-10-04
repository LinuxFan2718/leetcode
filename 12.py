from typing import List
class Solution:
    def intToRoman(self, num: int) -> str:
        romanNumerals = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], ['C', 100], ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]
        romanNumerals.reverse()
        answer = ''
        for pair in romanNumerals:
            thisNum = pair[1]
            romanNumeral = pair[0]
            numeralsToAdd = num // thisNum
            answer += romanNumeral * numeralsToAdd
            num -= numeralsToAdd * thisNum
            if num == 0:
                break
        return answer
s = Solution()
print(s.intToRoman(3) == "III")
print(s.intToRoman(4) == "IV")
print(s.intToRoman(9) == "IX")
print(s.intToRoman(58) == "LVIII", s.intToRoman(58))
print(s.intToRoman(1994) == "MCMXCIV",s.intToRoman(1994))
