from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        currentIndex = 0
        while currentIndex + 1 < len(intervals):
          if intervals[currentIndex][1] >= intervals[currentIndex+1][0]:
            # combine
            intervals[currentIndex] = [
              min(intervals[currentIndex][0], intervals[currentIndex+1][0]),
              max(intervals[currentIndex][1], intervals[currentIndex+1][1])
            ]
            # drop intervals[currentIndex+1]
            intervals = intervals[:currentIndex+1] + intervals[currentIndex+2:]
            # do not increase currentIndex
          else:
            currentIndex += 1
        return intervals

s = Solution()
i = [[1,3],[2,6],[8,10],[15,18]]
o = [[1,6],[8,10],[15,18]]
ans = s.merge(i)
print(ans == o, ans)

i = [[1,4],[4,5]]
o = [[1,5]]
ans = s.merge(i)
print(ans == o, ans)