class Solution:
    def arrangeCoins(self, n: int) -> int:
        sumo = 0
        i = 1
        while(sumo<n):
            sumo+=i
            i+=1
        if sumo == n:
            return i-1
        return i-2

        