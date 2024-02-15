class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums)<3:
            return -1
        nums.sort()
        sumo = nums[0]+nums[1]
        maxi = -1
        j_maxi = -1
        i=1
        j=2
        while(j<len(nums)):
            if sumo>nums[j]:
                maxi = sumo
                j_maxi = nums[j]
            i+=1
            j+=1
            sumo+=nums[i]
        if maxi == -1:
            return maxi
        else:
            return maxi+j_maxi

        