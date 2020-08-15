class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) <= 1: return 0
        
        intervals.sort(key= lambda x:x[1])
        i = 0
        num = 0
        for j in range(1,len(intervals)):
            if intervals[j][0] < intervals[i][1]:
                num += 1
            else:
                i=j
    
        return num
