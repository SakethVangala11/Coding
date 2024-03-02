import heapq
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [None]*len(nums)
        i = 0
        j = len(nums)-1
        for idx in range(len(nums)-1,-1,-1):
            if abs(nums[i]) > abs(nums[j]):
                result[idx] = nums[i]**2
                i+=1
            else:
                result[idx] = nums[j]**2
                j-=1
        return result


        