class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            j = i
            while(j < len(prices)):
                sell = prices[j]
                profit = max(sell - buy,profit)
                j+=1
        
        return profit 
