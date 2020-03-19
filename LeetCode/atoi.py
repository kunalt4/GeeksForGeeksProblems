class Solution:
    def myAtoi(self, str: str) -> int:

        str = str.lstrip()
        if not str:
            return 0

        sign = 1
        if str[0] == "+":
            sign = 1
            str = str[1:]
        elif str[0] == "-":
            sign = -1
            str = str[1:]
        str = re.split(r"[^0-9]", str)[0]
        print(str)
        str = str.split(" ", 1)[0]
        res = 0
        for char in str:
            if char.isnumeric():
                res = res*10 + int(char)
            else:
                break

        res = sign * res
        if res < -2**31:
            return -2**31
        if res > 2**31-1:
            return 2**31-1

        return res
