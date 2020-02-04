class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        carry = 0
        res = ""
        while a or b or carry:
            if a:
                carry = carry + int(a.pop())
            if b:
                carry = carry + int(b.pop())
            res += str(carry%2)
            carry = carry//2
        return res[::-1]