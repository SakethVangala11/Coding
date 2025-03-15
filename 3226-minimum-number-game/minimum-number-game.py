class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        n = len(nums)
        nums.sort()
        for i in range(1,n,2):
            arr.append(nums[i])
            arr.append(nums[i-1])
        return arr

        