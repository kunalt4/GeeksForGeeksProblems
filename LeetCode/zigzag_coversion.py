class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 0 or len(s) == 1 or numRows < 2:
            return s
        row = [''] * numRows
        index = 0
        for i in range(len(s)):
            row[index] = row[index] + s[i]
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index = index + step
        return ''.join(row)