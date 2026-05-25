class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 1
        maxP = 0
        while R > L and R < len(prices):
            if prices[R] - prices[L] > maxP:
                profit = prices[R] - prices[L]
                maxP = max(maxP, profit)
            if prices[R] < prices[L]:
                L = R
            R += 1
        return maxP

            

            
            
