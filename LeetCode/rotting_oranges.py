#Help from https://leetcode.com/problems/rotting-oranges/discuss/563686/Python-Clean-and-Well-Explained-(faster-than-greater-90)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        
        if rows == 0:
            return 0
        
        cols = len(grid[0])
        
        num_fresh = 0
        
        rotten = []
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    num_fresh += 1
        
        minutes = 0
        while len(rotten) > 0 and num_fresh > 0:
            
            for _ in range(len(rotten)):
                
                x,y = rotten.pop(0)
                
                for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    
                    xx = x+dx
                    yy = y+dy
                    
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy]==2:
                        continue
                    grid[xx][yy]=2
                    num_fresh-=1
                    rotten.append((xx,yy))
                
            minutes+=1
        
        return minutes if num_fresh == 0 else -1
