class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        
        res = []
        intervals = sorted(intervals, key=lambda i: i[0])
        for i in range(len(intervals)-1):
            if intervals[i+1][0] <= intervals[i][1]:
                intervals[i+1][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
            else:
                res.append(intervals[i])
        
        if res and intervals[-1][0] <= res[-1][1]:
            res[-1][0] = min(intervals[-1][0], res[-1][0])
            res[-1][1] = max(intervals[-1][1], res[-1][1])
        else:
            res.append(intervals[-1])
        return res
#Sort with start val, compare with next
# Handle last value seperately.
