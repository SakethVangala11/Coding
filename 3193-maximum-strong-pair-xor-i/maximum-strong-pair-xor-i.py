class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        maxi = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if abs(nums[j] - abs(nums[i])) <=min(nums[j], nums[i]):
                    maxi = max(maxi, nums[j]^nums[i])
        return maxi
        