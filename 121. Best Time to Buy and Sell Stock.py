class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        dayBought, daySold = 0, 1

        while daySold < len(prices):
            curProfit = prices[daySold] - prices[dayBought]
            profit = max(profit, curProfit)

            if prices[dayBought] >= prices[daySold]:
                dayBought = daySold
                
            daySold += 1
            
        return profit
                
