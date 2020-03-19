class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0,len(s)):
            for j in range(2):
                left = i
                right = left + j
                while left >=0 and right < len(s) and s[left]==s[right]:
                    count+=1
                    left-=1
                    right+=1
        return count