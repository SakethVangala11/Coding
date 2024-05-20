class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        subset = []

        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return 
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        
        dfs(0)
        sumo = 0
        print(res)
        for i in res:
            if i:
                xo = 0
                for j in i:
                    xo^=j
                print(xo)
                sumo+=xo
        return sumo



        