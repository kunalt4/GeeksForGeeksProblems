class Solution:
    def isHappy(self, n: int) -> bool:
        set_val = set()
        while n!=1:
            n = sum([int(i)**2 for i in str(n)])
            if n in set_val:
                return False
            set_val.add(n)
        return True
