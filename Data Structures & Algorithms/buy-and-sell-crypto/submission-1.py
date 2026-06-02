class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Mprofit = 0
        l,r = 0, 1

        while(r < len(prices)):
            if(prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                Mprofit = max(profit,Mprofit)
            else:
                l = r
            r += 1
        return Mprofit
