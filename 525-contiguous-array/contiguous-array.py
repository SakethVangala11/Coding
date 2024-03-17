class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sumo = 0
        d = {}
        maxi = 0
        for i in range(len(nums)):
            if nums[i]==0:
                sumo-=1
            else:
                sumo+=1
            if sumo == 0:
                maxi = i+1
            elif sumo in d:
                maxi = max(maxi,i-d[sumo]) 
            elif sumo not in d:
                d[sumo] = i
        return maxi

            

        