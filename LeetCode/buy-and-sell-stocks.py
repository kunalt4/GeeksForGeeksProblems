class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        maxi = 0
        low = prices[0]
        for i in range(len(prices)):
            low = min(low, prices[i])
            maxi = max(maxi,prices[i]-low)
        return maxi