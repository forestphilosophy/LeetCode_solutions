class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0

        minimum = prices[0]
        
        for i in range(len(prices)):
            minimum = min(minimum,prices[i])
            profit = prices[i] - minimum
            max_profit = max(profit,max_profit)

        return max_profit
