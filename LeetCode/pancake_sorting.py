#Find max position, move it to last
# repeat for rest

class Solution:
    
    def pancakeSort(self, A: List[int]) -> List[int]:
        end, max_pos = len(A)-1, 0
        res = []
        
        while end != 0:
            
            max_pos = A.index(max(A[:end+1])) #Find max
            if max_pos == 0:
                A[:end+1] = A[:end+1][::-1]
                res.append(end+1)
                end-=1
            elif max_pos == end:
                end-=1
            else:
                A[:max_pos+1] = A[:max_pos+1][::-1]
                res.append(max_pos+1)
        return res
