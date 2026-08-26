class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        max = 0
        while r <= len(prices) - 1:
            diff = prices[r] - prices[l]
            if diff > max:
                max = diff
            if prices[r] < prices[l]:
                l = r
            r += 1
        return max
