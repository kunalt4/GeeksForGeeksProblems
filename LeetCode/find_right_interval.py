class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        l = sorted((num[0], i) for i, num in enumerate(intervals))
        res = []
        for interval in intervals:
            re = bisect.bisect_left(l, (interval[1],))
            if re < len(l):
                res.append(l[re][1])
            else:
                res.append(-1)
        return res
        
# Help from https://leetcode.com/problems/find-right-interval/discuss/91806/Python-O(nlogn)-short-solution-with-explanation
