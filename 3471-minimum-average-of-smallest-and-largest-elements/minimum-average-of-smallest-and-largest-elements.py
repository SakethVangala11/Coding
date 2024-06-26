class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []

        nums.sort()

        while(nums):
            x = nums.pop()
            y = nums.pop(0)
            averages.append((x+y)/2)
        return min(averages)
        