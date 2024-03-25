class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mini = float('inf')
        sumo = 0
        for i in nums:
            sumo+=i
            mini = min(sumo,mini)
        if mini > 0:
            return 1
        else:
            return abs(mini)+1
        