class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ps = [0]*len(nums)
        ps[0] = nums[0]
        for i in range(1,len(nums)):
            ps[i] = ps[i-1] + nums[i]
        
        mini = min(ps)
        if mini > 0:
            return 1
        else:
            return abs(mini)+1
        