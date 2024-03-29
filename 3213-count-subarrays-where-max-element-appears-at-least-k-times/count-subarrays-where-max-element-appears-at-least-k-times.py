class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        i, j = 0, 0
        maxi = max(nums)
        n = len(nums)
        res = 0
        while(j<n):
            while(count<k and j<n):
                if nums[j] == maxi:
                    count+=1
                j+=1
            while(count>=k):
                res+=n-j+1
                if nums[i] == maxi:
                    count-=1
                i+=1
        return res