class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi, nextMaxi = 0, 0
        for i in nums:
            if i>maxi:
                maxi, nextMaxi = i, maxi
            elif i>nextMaxi:
                nextMaxi = i
        return (maxi-1)*(nextMaxi-1) 

        