class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        arr = []
        for i in range(len(nums)):
            arr.append(nums[i])
        arr.sort()
        for i in range(len(nums)):
            for j in range(len(arr)):
                if nums[i] == arr[j]:
                    ans.append(j)
                    break
        return ans
        