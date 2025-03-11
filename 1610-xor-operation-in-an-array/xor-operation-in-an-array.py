class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = []
        i = 0
        while(i<n):
            res.append(start+2*i)
            i+=1
        ans = 0
        for i in range(n):
            ans^=res[i]
        return ans
        