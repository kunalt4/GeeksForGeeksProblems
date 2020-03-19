class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        i = 0
        while i < len(prices)-1:
            currlow = prices[i]
            while (i<len(prices)-1) and (prices[i+1]>prices[i]):
                i+=1
            maxi += prices[i] - currlow
            i+=1
        return maxi