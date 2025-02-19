class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxi = -1
        n = len(nums)
        for i in range(n-1):
            maxi = max(abs(nums[i]-nums[i+1]),maxi)
        maxi = max(abs(nums[0]-nums[-1]),maxi)
        return maxi
        