class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        num = bin(num)
        return num[2] == '1' and ('1' not in num[3:]) and len(num[3:])%2==0
