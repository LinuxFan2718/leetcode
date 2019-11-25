from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        emptyBoard = ['.' * n] * n
        self.helper(n, emptyBoard, ans)
        return ans

    def validBoard(self, n: int, board: List[str]) -> bool:
      if any([row.count('Q') > 1 for row in board]): # rows
        return False
      occupiedColumns = [row.index('Q') for row in board if 'Q' in row]
      if len(occupiedColumns) != len(set(occupiedColumns)): # columns
        return False
      # downhill diagonals
      for offset in range(-n+2,n-1):
        diagonalTuples = [(x,x + offset) for x in range(n) if 0 <= x and 0 <= x + offset and x < n and x + offset < n]
        diagonal = [board[diagonalTuple[0]][diagonalTuple[1]] for diagonalTuple in diagonalTuples]
        if diagonal.count('Q') > 1:
          return False
      # uphill diagonals
      for offset in range(1,2 * n - 2):
        diagonalTuples = [(x,offset-x) for x in range(n) if 0 <= x and 0 <= offset - x and x < n and offset - x < n]
        diagonal = [board[diagonalTuple[0]][diagonalTuple[1]] for diagonalTuple in diagonalTuples]
        if diagonal.count('Q') > 1:
          return False
      return True
    
    def helper(self, n: int, board: List[str], ans: List[List[str]]) -> None:
      # assume board is valid and unfinished
      firstEmptyRow = 0
      while 'Q' in board[firstEmptyRow]:
        firstEmptyRow += 1
      availableColumns = list(set(range(n)) - set([row.index('Q') for row in board if 'Q' in row]))
      for column in availableColumns:
        board[firstEmptyRow] = '.' * column + 'Q' + '.' * (n - column - 1)
        if self.validBoard(n, board):
          if firstEmptyRow + 1 == n:
            ans.append(board[:])
          else:
            self.helper(n, board, ans)
        board[firstEmptyRow] = '.' * n
          



s = Solution()
i = 4
o = [
 [".Q..",  # Solution 1
  "...Q",
  "Q...",
  "..Q."],
 ["..Q.",  # Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
ans = s.solveNQueens(i)
print(ans == o, ans)