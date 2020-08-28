# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num = (rand7()-1)*7 + rand7() - 1
        #Think of this as base 7 -- generating 0-48 numbers -- rand(0,6) * 7^1 + rand(0,6) * 7^0
        if num >= 40:
            return self.rand10()
        else:
            return (num%10)+1
            
#https://leetcode.com/problems/implement-rand10-using-rand7/discuss/816210/Python-rejection-sampling-2-lines-explained
