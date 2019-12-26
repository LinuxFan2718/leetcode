# 79. Word Search
# Medium

# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0 or len(board[0]) == 0 or len(word) == 0:
          return False
        for i in range(len(board)):
          for j in range(len(board[0])):
            if board[i][j] == word[0]:
              if self.existHelper(board, word, [(i,j)]):
                return True
        return False

    def existHelper(self, board: List[List[str]], word: str, used: List[tuple]) -> bool:
      if len(word) == len(used):
        return True
      current = used[-1]
      adjacentCells = (current[0], current[1]-1), (current[0]-1, current[1]), (current[0], current[1]+1), (current[0]+1, current[1])
      for cell in adjacentCells:
        if 0 <= cell[0] and cell[0] < len(board) and 0 <= cell[1] and cell[1] < len(board[0]):
          if board[cell[0]][cell[1]] == word[len(used)] and (cell[0], cell[1]) not in used:
            if self.existHelper(board, word, used + [(cell[0], cell[1])]):
              return True


s = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
o = True
ans = s.exist(board, word)
print(ans == o)
word = "SEE"
o = True
ans = s.exist(board, word)
print(ans == o)
word = "ABCB"
o = False
ans = s.exist(board, word)
print(ans == o)