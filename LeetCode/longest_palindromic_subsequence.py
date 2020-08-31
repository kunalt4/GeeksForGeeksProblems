class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        srev = s[::-1]
        dp = [[0] * (len(srev) + 1) for _ in range(len(s) + 1)]
        
        for i, char1 in enumerate(s):
            for j, char2 in enumerate(srev):
                if char1 == char2:
                    dp[i+1][j+1] = 1+dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]
