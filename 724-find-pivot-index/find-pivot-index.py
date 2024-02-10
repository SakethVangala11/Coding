class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumo = sum(nums)
        currSum = 0 
        for i in range(len(nums)):
            if currSum == sumo-currSum-nums[i]:
                return i
            currSum+=nums[i]
        return -1
            
        