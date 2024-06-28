class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        d = {}
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] in d:
                    d[nums[i][j]]+=1
                else:
                    d[nums[i][j]]=1
        for i in d:
            if d[i] == len(nums):
                ans.append(i)
        ans.sort()
        return ans



        