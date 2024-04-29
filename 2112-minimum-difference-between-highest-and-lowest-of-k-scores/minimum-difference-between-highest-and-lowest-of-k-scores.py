class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0 
        j = k - 1
        mini = float('inf')
        while(j<len(nums)):
            mini = min(mini, nums[j]-nums[i])
            i+=1
            j+=1
        return mini

        