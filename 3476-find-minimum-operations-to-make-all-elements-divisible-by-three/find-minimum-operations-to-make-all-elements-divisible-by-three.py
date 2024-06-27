class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            d = i%3
            ans+=min(3-d, d)
        return ans
        