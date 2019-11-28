from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return intervals

s = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
output = [[1,5],[6,9]]
ans = s.insert(intervals, newInterval)
print(ans == output, ans)
