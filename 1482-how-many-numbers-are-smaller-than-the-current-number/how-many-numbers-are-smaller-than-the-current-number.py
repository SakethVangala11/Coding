class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [0]*101
        for i in nums:
            arr[i]+=1
        res = []
        for i in range(1, len(arr)):
            arr[i]+= arr[i-1]
        for i in range(len(nums)):
            if nums[i]!=0:
                res.append(arr[nums[i]-1])
            else:
                res.append(0)
        return res





        
        