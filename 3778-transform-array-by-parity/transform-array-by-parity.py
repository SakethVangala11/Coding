class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        idx = 0
        for i in range(n):
            if nums[i]==0:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx+=1
        return nums


        