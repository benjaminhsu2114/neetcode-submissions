class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_p = 0
        profit = 0
        n = len(prices)

        for r in range(n):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)
            else:
                l = r
  
        return max_p
        