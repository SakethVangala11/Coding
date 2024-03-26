class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = []
        for i in range(1,n+1):
            l.append(i)
        idx = 0
        count = n
        while(count!=1):
            idx = (idx+k-1)%count
            l.pop(idx)
            count-=1
        return l[0]

        