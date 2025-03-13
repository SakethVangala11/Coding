class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        for i in range(k):
            mini = 0 
            for j in range(n):
                if nums[j]<nums[mini]:
                    mini = j
            nums[mini]*=multiplier
        return nums
        