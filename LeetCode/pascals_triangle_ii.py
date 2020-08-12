class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            for j in range(rowIndex):
                res = [x+y for x,y in zip([0]+res, res+[0])]
        return res
