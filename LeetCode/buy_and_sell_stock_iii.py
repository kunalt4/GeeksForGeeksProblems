class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profits = []
        max_profit = 0
        curr_min = prices[0]
        for price in prices:
            curr_min = min(curr_min, price)
            max_profit = max(max_profit, price-curr_min)
            profits.append(max_profit)
            
        tot_max = 0
        max_profit = 0
        curr_max = prices[-1]
        i = len(prices)-1
        for price in prices[::-1]:
            curr_max = max(curr_max, price)
            max_profit = max(max_profit, curr_max-price)
            tot_max = max(tot_max, max_profit + profits[i])
            i-=1
        return tot_max
    
    
    #According to https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39743/Python-DP-solution-120ms
