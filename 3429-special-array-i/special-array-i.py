class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if i == 0:
                pass
            else:
                if (nums[i]%2 == 0 and nums[i-1]%2==1) or (nums[i]%2==1 and nums[i-1]%2==0):
                    pass
                else:
                    return False
        return True

            
        

        