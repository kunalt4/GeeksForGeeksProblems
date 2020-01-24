class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        N = (N)%14
        if N==0:
            N = 14
        newList = [0]*len(cells)
        for day in range(N):
            for cell in range(len(cells)):
                if cell == 0 or cell == (len(cells)-1):
                    newList[cell] = 0
                elif(cells[cell-1]^cells[cell+1]==0):
                    newList[cell] = 1
                else:
                    newList[cell] = 0
            cells = newList.copy()
            
        return cells