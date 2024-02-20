class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumo=0
        for i in range(len(nums)):
            sumo^=i
            sumo^=nums[i]
        sumo^=len(nums)
        return sumo
        