class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        sumo = (n*(n+1))//2
        for i in range(n):
            cur = (i*(i+1))//2
            if cur == sumo-cur+i:
                return i
        return -1

        