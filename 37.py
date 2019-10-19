from time import time
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      # Each row must contain the digits 1-9 without repetition.
      for row in board:
        temp = [x for x in row if len(x) == 1]
        if len(set(temp)) != len(temp):
          return False
      # Each column must contain the digits 1-9 without repetition.
      for i in range(9):
        temp = [x[i] for x in board if len(x[i]) == 1]
        if len(set(temp)) != len(temp):
          return False        
      # Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
      for i in range(0, 9, 3):
        for j in range(0, 9, 3):
          temp = [x[i:i+3] for x in board[j:j+3]]
          flatTemp = [item for sublist in temp for item in sublist if len(item) == 1]
          if len(set(flatTemp)) != len(flatTemp):
            return False          
      return True

    def nextEmptyCell(self, board: List[List[str]]) -> List[int]:
      for i in range(9):
        for j in range(9):
          if len(board[i][j]) > 1:
            return [i,j]
      return [-1, -1]

    def solveSudoku(self, board: List[List[str]]) -> None:
      for i in range(len(board)):
        board[i] = ['123456789' if x == '.' else x for x in board[i]]
      self.prunePossibilities(board)
      self.solveSudokuHelper(board)
      return
    
    def prunePossibilities(self, board: List[List[str]]) -> None:
      for i in range(len(board)):
        for j in range(len(board[0])):
          if len(board[i][j]) > 1:
            rowTaken = [x for x in board[i] if len(x) == 1]

            colTaken = []
            for k in range(len(board)):
              thisUnit = board[k][j]
              if len(thisUnit) == 1:
                colTaken.append(thisUnit)
              
            mStart = 3 * (i // 3) # 0,3,6
            nStart = 3 * (j // 3) # 0,3,6
            squareTaken = []
            for m in range(3):
              for n in range(3):
                thisUnit = board[mStart + m][nStart + n]
                if len(thisUnit) == 1:
                  squareTaken.append(thisUnit)

            allTaken = list(set(rowTaken + colTaken + squareTaken))
            for e in allTaken:
              board[i][j] = board[i][j].replace(e, '')

    def solveSudokuHelper(self, board: List[List[str]]) -> bool:
      i, j = self.nextEmptyCell(board)
      if [i, j] == [-1, -1]:
        return True
      possibleValues = board[i][j]
      for e in possibleValues:
        board[i][j] = e
        if self.isValidSudoku(board):
          if self.solveSudokuHelper(board):
            return True
      board[i][j] = possibleValues
      return False

    def printSudoku(self, board: List[List[str]]) -> None:
      for line in board:
        print(line)

s = Solution()
beforeTime1 = time()
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
s.printSudoku(board1)
s.solveSudoku(board1)
print(s.isValidSudoku(board1))
s.printSudoku(board1)
print(round(time() - beforeTime1, 1), 'seconds')
print('-' * 40)
beforeTime2 = time()
board2 = [
  [".",".",".",".",".","7",".",".","9"],
  [".","4",".",".","8","1","2",".","."],
  [".",".",".","9",".",".",".","1","."],
  [".",".","5","3",".",".",".","7","2"],
  ["2","9","3",".",".",".",".","5","."],
  [".",".",".",".",".","5","3",".","."],
  ["8",".",".",".","2","3",".",".","."],
  ["7",".",".",".","5",".",".","4","."],
  ["5","3","1",".","7",".",".",".","."]
]
s.printSudoku(board2)
s.solveSudoku(board2)
print(s.isValidSudoku(board2))
s.printSudoku(board2)
print(round(time() - beforeTime2, 1), 'seconds')