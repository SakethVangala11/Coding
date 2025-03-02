class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        if k==1:
            maxi = -1
            for i in nums:
                if d[i]==1 and i>maxi:
                    maxi = max(maxi, i)
            return maxi
        else:
            maxi = max(nums[0], nums[-1])
            mini = min(nums[0], nums[-1])
            if d[maxi] == 1:
                return maxi
            elif d[mini] == 1:
                return mini
            return -1
        