class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1
        for i in nums:
            if i<0:
                pass
            elif i>0:
                if i>ans:
                    return ans
                else:
                    ans = i+1
        return ans



        
        
        