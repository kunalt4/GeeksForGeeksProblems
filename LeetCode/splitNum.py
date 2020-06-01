class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def splitNum(num):
            num = [int(n) for n in num]
            power = len(num)-1
            result = []
            for n in num:
                result.append(n*10**power)
                power-=1
            return result
    
        num1 = splitNum(num1)
        num2 = splitNum(num2)
        return str(sum([a*b for a in num1 for b in num2]))