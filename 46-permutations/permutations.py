class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # print("permute(" + str(nums) +")")
        result = []
        if len(nums) == 1:
            # print("return " + str([nums[:]]))
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            # print(n)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result