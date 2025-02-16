class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        sumo = 0
        n = len(nums)
        for i in range(n):
            flag=1
            if i-k>=0 and nums[i]<=nums[i-k]:
                flag=0
            if i+k<n and nums[i]<=nums[i+k]:
                flag=0
            if flag:
                sumo+=nums[i]
        return sumo 
            
        