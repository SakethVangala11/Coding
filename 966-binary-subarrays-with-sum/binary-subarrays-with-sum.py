class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0 
        sumo = 0
        prefix_dict = {0:1}
        for num in nums:
            sumo+=num
            if sumo - goal in prefix_dict:
                count+=prefix_dict[sumo-goal]
            prefix_dict[sumo] = prefix_dict.get(sumo,0)+1
        return count
        