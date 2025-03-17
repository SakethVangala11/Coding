class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set(nums)
        sumo = 0
        pos = False
        for i in s:
            if i > 0:
                pos = True
            if i>0:
                sumo+=i
        if not pos:
            return max(s)
        return sumo      