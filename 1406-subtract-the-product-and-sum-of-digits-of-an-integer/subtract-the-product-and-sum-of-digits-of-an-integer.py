class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumo = 0
        prod = 1
        while(n>0):
            rem = n%10
            sumo+=rem
            prod*=rem
            n = n//10
        return prod - sumo




        