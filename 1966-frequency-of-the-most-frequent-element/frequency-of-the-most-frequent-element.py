class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, 0
        sumo = 0
        maxi = 0
        n = len(nums)
        while(j<n):
            sumo+=nums[j]
            while((j-i+1)*nums[j] > sumo+k):
                sumo-=nums[i]
                i+=1
            maxi = max(maxi,(j-i+1))
            j+=1    
        return maxi
        

        