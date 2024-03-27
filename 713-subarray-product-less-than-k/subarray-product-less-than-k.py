class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        i, j = 0, 0
        product = 1
        res = 0
        n = len(nums)
        while(j<n):
            product*=nums[j]
            while(product>=k):
                product//=nums[i]
                i+=1
            res+=j-i+1
            j+=1
        return res     