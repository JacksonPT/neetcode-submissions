class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Base case#
        if prices == sorted(prices,reverse=True):
            return 0
    
        #Set buy and sell day#
        profit = 0 
        #Arithmetic#
        for i in range(len(prices)):
            buyPrice = prices[i]
            for j in range(i+1,len(prices)):
                sellPrice = prices[j]
                profit = max(profit,sellPrice-buyPrice)

        return profit

        
        