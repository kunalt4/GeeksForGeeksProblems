class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        cur = [0,1,2,3,4,5,6,7,8,9]
        for i in range(N-1):
            cur_temp = []
            for x in cur:
                y = x % 10
                if x>0 and y+K<10:
                    cur_temp.append(x*10+y+K)
                if x>0 and y-K>=0:
                    cur_temp.append(x*10+y-K)
            cur = cur_temp
        return set(cur)
