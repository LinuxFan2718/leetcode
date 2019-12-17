from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        for row in rows:
            matrix[row] = [0] * len(matrix[row])
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0

s = Solution()
i = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
o = [
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
s.setZeroes(i)
print(i == o)

i = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
o = [
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
s.setZeroes(i)
print(i == o)