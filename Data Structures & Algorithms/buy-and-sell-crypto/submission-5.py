class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        
        for i in range(len(prices)):
            buy = prices[i]

            j = i + 1

            while (j < len(prices)):
                sell = prices[j]
                profit = sell - buy
                maxP = max(maxP,profit)
                j += 1
        return maxP


