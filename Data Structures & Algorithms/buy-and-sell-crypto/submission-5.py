class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        l, r = 0, 1

        while r < len(prices):
            pnl = prices[r] - prices[l]
            maxx = max(maxx, pnl)
            if pnl <= 0:
                l = r
            r += 1

        return maxx