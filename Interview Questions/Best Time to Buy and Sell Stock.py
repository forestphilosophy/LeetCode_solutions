class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_list = []
        
        if len(prices) == 1:
            return 0
        
        for i in range(0,len(prices)):
            if i == len(prices)-1:
                continue
                
            if prices[i] > max(prices[i+1:]):
                profit_list.append(0)
                continue
            else:
                profit_list.append(max(prices[i+1:])-prices[i])
                
        return max(profit_list)
    
#Efficient solution
def maxProfit(self, prices: List[int]) -> int:
        largest_profit = 0
        min_purchase = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - min_purchase > largest_profit:
                largest_profit = prices[i] - min_purchase
            if prices[i] < min_purchase:
                min_purchase = prices[i]
        return largest_profit
