class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_profit =0
        final_profit = 0
        for i in range(len(prices)-1):
            j = i+1
            if prices[i] < prices[j]:
                current_profit = prices[j] - prices[i]
                final_profit+= current_profit
                
            elif prices[i] > prices[j]:
                continue
