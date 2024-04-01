class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        if nums[l]<=nums[h]:
            return nums[l]
        while(l<h):
            
            m=(l+h)//2
            if nums[m]<=nums[l]:
                h=m
            else:
                l=m
            
        return nums[l+1]

