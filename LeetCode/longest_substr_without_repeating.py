# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        li = list(s)
        if(len(li)==0 or len(li)==1):
            return len(li)
        lenStr = len(li)
        lenMax = len(set(li))
        i = 0
        j = lenMax
        while(j!=lenStr+1):
            if(len(li[i:j])==len(set(li[i:j]))):
                return len(li[i:j])
            i = i + 1
            j = j + 1
            if(j==lenStr+1):
                i = 0
                lenMax = lenMax-1
                j = lenMax