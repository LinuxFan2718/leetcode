from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      if len(matrix) == 0:
        return []
      ans = []
      directionOrder = ['right', 'down', 'left', 'up']
      directionDelta = {
        'right': (0, 1),
        'down': (1, 0),
        'left': (0, -1),
        'up': (-1, 0)
      }
      for i in range(len(matrix)): #(value, visited?)
        for j in range(len(matrix[0])):
          matrix[i][j] = [matrix[i][j], False]
      current = (0, 0)
      directionIndex = 0
      direction = directionOrder[directionIndex % 4]
      while len(ans) < len(matrix) * len(matrix[0]):
        ans.append(matrix[current[0]][current[1]][0])
        matrix[current[0]][current[1]][1] = True

        nextCurrentCandidate = [sum(x) for x in zip(current, directionDelta[direction])]
        if nextCurrentCandidate[0] >= len(matrix) or nextCurrentCandidate[1] >= len(matrix[0]) or matrix[nextCurrentCandidate[0]][nextCurrentCandidate[1]][1] == True:
          directionIndex += 1
          direction = directionOrder[directionIndex % 4]
          nextCurrentCandidate = [sum(x) for x in zip(current, directionDelta[direction])]
        current = nextCurrentCandidate
      return ans

s = Solution()
i = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
o = [1,2,3,6,9,8,7,4,5]
ans = s.spiralOrder(i)
print(ans == o, ans)

i = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
o = [1,2,3,4,8,12,11,10,9,5,6,7]
ans = s.spiralOrder(i)
print(ans == o, ans)

i = []
o = []
ans = s.spiralOrder(i)
print(ans == o, ans)