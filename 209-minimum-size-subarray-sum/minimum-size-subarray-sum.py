class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini = float('inf')
        i, j = 0, 0
        n = len(nums)
        sumo = 0
        while(j < n):
            sumo+=nums[j]
            if sumo>=target:
                mini = min(mini,j-i+1)
            while(sumo>=target):
                sumo-=nums[i]
                i+=1
                if sumo >=target:
                    mini = min(mini,j-i+1)
            j+=1
        if mini==float('inf'):
            return 0
        return mini


        
        