class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0 
        sumo = 0
        prefix_dict = {0:1}
        for num in nums:
            sumo+=num
            if sumo - goal in prefix_dict:
                count+=prefix_dict[sumo-goal]
            if sumo in prefix_dict:
                prefix_dict[sumo]+=1
            else:
                prefix_dict[sumo]=1
        return count
        