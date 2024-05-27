class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(0,1000):
            count = 0
            for j in range(len(nums)):
                if nums[j] >= i:
                    count+=1
            if count == i:
                return i
        return -1





        

        