class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        ans = [0]*len(prices)
        maxi = prices[-1]

        for i in range(len(prices)-2,-1,-1):
            ans[i] = maxi
            maxi = max(prices[i], maxi)
        
        res = 0
        for i in range(len(prices)):
            diff = ans[i] - prices[i]
            if diff>0:
                res = max(res, diff)
        
        return res





        