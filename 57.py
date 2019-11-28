from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find where to insert newInterval using bisect
        if len(intervals) == 0:
          return [newInterval]
        left = 0
        right = len(intervals) - 1
        mid = (left + right) // 2
        insertAt = mid + 1
        while True:
          if intervals[mid][0] == newInterval[0]: # left bisect
            insertAt = mid + 1
            break
          if left >= right-1:
            if newInterval[0] < intervals[left][0]:
              insertAt = left
            elif intervals[left][0] < newInterval[0] and newInterval[0] < intervals[right][0]:
              insertAt = left + 1
            elif intervals[right][0] < newInterval[0]:
              insertAt = right + 1
            break
          elif intervals[mid][0] < newInterval[0]:
            left = mid
          elif newInterval[0] < intervals[mid][0]:
            right = mid
          mid = (left + right) // 2
        intervals = intervals[:insertAt] + [newInterval] + intervals[insertAt:]

        # traverse intervals as normal
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
intervals = [[1,3],[6,9]]
newInterval = [2,5]
output = [[1,5],[6,9]]
ans = s.insert(intervals, newInterval)
print(ans == output, ans)

intervals = [[1,5]]
newInterval = [6,8]
output = [[1,5],[6,8]]
ans = s.insert(intervals, newInterval)
print(ans == output, ans)

intervals = [[2,6],[7,9]]
newInterval = [15,18]
output = [[2,6],[7,9],[15,18]]
ans = s.insert(intervals, newInterval)
print(ans == output, ans)

intervals = []
newInterval = [5,7]
output = [[5,7]]
ans = s.insert(intervals, newInterval)
print(ans == output, ans)