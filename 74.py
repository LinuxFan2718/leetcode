from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        modulus = len(matrix[0])
        left = 0
        right = modulus * len(matrix)
        guess = (left + right) // 2
        while left < right:
            guessRow, guessCol = divmod(guess, modulus)
            candidate = matrix[guessRow][guessCol]
            if candidate == target:
                return True
            elif target < candidate:
                right = guess
            elif candidate < target:
                left = guess
            lastGuess = guess
            guess = (left + right) // 2
            if guess == lastGuess:
                return False
        return False

s = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
o = True
ans = s.searchMatrix(matrix, target)
print(ans == o)

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
o = False
ans = s.searchMatrix(matrix, target)
print(ans == o)

matrix = [[1]]
target = 1
o = True
ans = s.searchMatrix(matrix, target)
print(ans == o)