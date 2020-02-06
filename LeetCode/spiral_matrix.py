class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        res = []
        poprev = False
        while (len(res)!=m*n):
            res.extend(matrix.pop(0))
            if(len(res)==m*n):
                break
            matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]
        return res