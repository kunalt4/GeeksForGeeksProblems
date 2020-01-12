class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s)==0 or len(s)==1):
            return s
        lenStr = len(s)
        lenMax = lenStr
        i = 0
        j = lenMax
        while(j!=lenStr+1):
            if(self.isPalindrome(s[i:j])):
                return s[i:j]
            i = i + 1
            j = j + 1
            if(j==lenStr+1):
                i = 0
                lenMax = lenMax-1
                j = lenMax
    
    def isPalindrome(self,s):
        if (s==s[::-1]):
            return True
        return False