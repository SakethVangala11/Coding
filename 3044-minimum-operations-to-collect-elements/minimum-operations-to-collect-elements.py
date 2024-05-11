class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        l = set()
        n = len(nums)
        while(nums):
            x = nums.pop()
            if x<=k:
                l.add(x)
                
            if len(l) == k:
                return n - len(nums)
    

        