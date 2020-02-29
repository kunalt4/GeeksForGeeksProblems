class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if (dividend <= -2147483648 and divisor == -1): return 2147483647
        
        if (divisor == 1):
            if dividend > 2147483647 or dividend < -2147483648:
                return 2147483647
            else:
                return dividend
                
        
        negative = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        the_sum = divisor
        
        while the_sum <= dividend:
            current_quotient = 1
            while (the_sum + the_sum) <= dividend:
                the_sum += the_sum
                current_quotient += current_quotient
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient
            
        
        return -quotient if negative else quotient
