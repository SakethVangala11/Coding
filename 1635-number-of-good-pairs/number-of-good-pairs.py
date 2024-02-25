class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d= {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l = list(d.values())
        total = 0
        for i in l:
            total+=(i*(i-1))//2
        return total
        