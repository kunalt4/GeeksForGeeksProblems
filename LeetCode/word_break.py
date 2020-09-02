class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for word in wordDict:
                if dp[i-len(word)] and s[i-len(word):i]==word:
                    dp[i] = True
                if dp[-1]:
                    return True
        return dp[-1]
    
    
    # With help from https://leetcode.com/problems/word-break/discuss/43808/Simple-DP-solution-in-Python-with-description
