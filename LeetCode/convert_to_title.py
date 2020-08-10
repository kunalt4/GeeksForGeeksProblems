class Solution:
    def convertToTitle(self, n: int) -> str:
        
        temp = []
        while n > 0:
            temp += chr(ord('A')+(n-1)%26)
            n = (n-1) // 26
        return ''.join(reversed(temp))
