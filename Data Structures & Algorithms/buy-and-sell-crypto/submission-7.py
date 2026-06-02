class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0

        l,r = 0,1

        while r < len(prices):
            profit = prices[r] - prices[l]
            maxp = max(maxp,profit)

            if prices[r] < prices[l]:
                l = r
            else:
                r += 1
        return maxp