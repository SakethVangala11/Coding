class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1 for i in range(len(nums))]

        for i in range(len(nums)-2, -1, -1):
            tempmax = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    tempmax = max(tempmax, LIS[j])
            LIS[i] = max(1, 1+tempmax)
        return max(LIS)

        