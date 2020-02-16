class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def remove_one(i,j):
            if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0 or grid[i][j]=='0':
                return
            else:
                grid[i][j]='0'
                remove_one(i,j+1)
                remove_one(i+1,j)
                remove_one(i-1,j)
                remove_one(i,j-1)
        
        count = 0
        for i in range(0,len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]=='1':
                    remove_one(i,j)
                    count+=1
        return count
        
        