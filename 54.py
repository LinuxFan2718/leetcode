from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return []

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