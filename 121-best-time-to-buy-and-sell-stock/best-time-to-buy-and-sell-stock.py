class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = prices[-1]
        res = 0
        for i in range(len(prices)-2,-1,-1):
            res = max(res, maxi - prices[i])
            maxi = max(prices[i], maxi)
        return res
        