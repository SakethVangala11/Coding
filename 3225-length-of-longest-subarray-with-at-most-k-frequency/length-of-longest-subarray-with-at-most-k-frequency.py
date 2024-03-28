class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = {}
        i, j =0, 0
        n = len(nums)
        res = 0
        while(j<n):
            if nums[j] in d:
                d[nums[j]]+=1
            else:
                d[nums[j]]=1
            while(d[nums[j]]>k):
                d[nums[i]]-=1
                i+=1
            res = max(res,j-i+1)
            j+=1
        return res

        