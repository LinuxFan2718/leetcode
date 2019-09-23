from typing import List
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        output = []
        for _ in range(numRows):
            output.append([])
        sequence = [x for x in range(numRows)] # on the way down
        sequence.extend([x for x in range(numRows - 2, 0, -1)]) # up
        i = 0
        sequence_length = len(sequence)
        for c in s:
            output[sequence[i]].append(c)
            i = (i + 1) % sequence_length
        return ''.join([char for outputrow in output for char in outputrow])

solution = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(solution.convert(s, numRows) == "PAHNAPLSIIGYIR")
s = "PAYPALISHIRING"
numRows = 4
print(solution.convert(s, numRows) == "PINALSIGYAHRPI")