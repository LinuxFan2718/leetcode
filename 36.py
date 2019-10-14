from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      # Each row must contain the digits 1-9 without repetition.
      for row in board:
        temp = [x for x in row if x != '.']
        if len(set(temp)) != len(temp):
          return False
      # Each column must contain the digits 1-9 without repetition.
      for i in range(9):
        temp = [x[i] for x in board if x[i] != '.']
        if len(set(temp)) != len(temp):
          return False        
      # Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
      for i in range(0, 9, 3):
        for j in range(0, 9, 3):
          temp = [x[i:i+3] for x in board[j:j+3]]
          flatTemp = [item for sublist in temp for item in sublist if item != '.']
          if len(set(flatTemp)) != len(flatTemp):
            return False          
      return True

s = Solution()
board1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
correctAnswer1 = True
print(correctAnswer1 == s.isValidSudoku(board1))
board2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
correctAnswer2 = False
print(correctAnswer2 == s.isValidSudoku(board2))