class Solution:
    def calculate(self, s: str) -> int:
        preOp = "+"
        numStack = []
        num = 0
        s = s.replace(" ","")+"+0"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10+int(s[i])
            else:
                if preOp == "-": 
                    numStack.append(-num)
                elif preOp == "+":
                    numStack.append(num)
                elif preOp == "*":
                    numStack.append(numStack.pop()*num)
                else:
                    numStack.append(int(numStack.pop()/num))
                preOp = s[i]
                num = 0
        return sum(numStack)