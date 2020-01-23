class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        if x < 0:
            return False
        n = x
        while x!=0:
            res = res*10 + x%10
            x = x//10
    
        if n == res:
            return True
        
        return False
