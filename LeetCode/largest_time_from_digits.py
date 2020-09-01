class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        A.sort()
        for h in range(23,-1,-1):
            for m in range(59,-1,-1):
                time = [h//10, h%10, m//10, m%10]
                if A == sorted(time):
                    return str(time[0])+str(time[1])+":"+str(time[2])+str(time[3])
        return ""
#https://leetcode.com/problems/largest-time-for-given-digits/discuss/536484/Python3-Easy-understanding-(With-explanation)
