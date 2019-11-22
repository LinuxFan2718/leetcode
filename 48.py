from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) < 2:
          return
        x = len(matrix) // 2
        y = x + len(matrix) % 2
        for i in range(x):
          for j in range(y):
            ul = i, j
            ur = j, len(matrix) - 1 - i
            lr = len(matrix) - 1 - i, len(matrix) - 1 - j
            ll = len(matrix) - 1 - j, i
            matrix[ul[0]][ul[1]], matrix[ur[0]][ur[1]], matrix[lr[0]][lr[1]], matrix[ll[0]][ll[1]] = matrix[ll[0]][ll[1]], matrix[ul[0]][ul[1]], matrix[ur[0]][ur[1]], matrix[lr[0]][lr[1]]

s = Solution()
i = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

for row in i:
  print(row)
print()

o = [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
s.rotate(i)
print(i == o)
for row in i:
  print(row)

i2 = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

for row in i2:
  print(row)
print()

o2 = [
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
s.rotate(i2)
print(i2 == o2)
for row in i2:
  print(row)