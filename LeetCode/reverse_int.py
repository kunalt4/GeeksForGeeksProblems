class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        x_neg = 1
        if x < 0:
            x_neg = -1
        x = abs(x)
        while x!=0:
            res = res*10 + x%10
            x = x//10
    
        res = x_neg*res
        
        if res < -2**31 or res > 2**31 - 1:
            return 0
        
        return res
        