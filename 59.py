from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
      ans = []
      for _ in range(n):
        ans.append([None] * n)
      directionOrder = ['right', 'down', 'left', 'up']
      directionDelta = {
        'right': (0, 1),
        'down': (1, 0),
        'left': (0, -1),
        'up': (-1, 0)
      }
      current = (0, 0)
      directionIndex = 0
      direction = directionOrder[directionIndex % 4]
      i = 0
      while i < n**2:
        i += 1
        ans[current[0]][current[1]] = i

        nextCurrentCandidate = [sum(x) for x in zip(current, directionDelta[direction])]
        if nextCurrentCandidate[0] >= n or nextCurrentCandidate[1] >= n or ans[nextCurrentCandidate[0]][nextCurrentCandidate[1]] != None:
          directionIndex += 1
          direction = directionOrder[directionIndex % 4]
          nextCurrentCandidate = [sum(x) for x in zip(current, directionDelta[direction])]
        current = nextCurrentCandidate
      return ans

s = Solution()
i = 3
o = [
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
ans = s.generateMatrix(i)
print(ans == o, ans)
pass