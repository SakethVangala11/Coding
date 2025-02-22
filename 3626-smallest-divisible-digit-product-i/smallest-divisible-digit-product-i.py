class Solution:
    def digitsProduct(self, n:int) -> int:
        prod = 1
        while(n>0):
            rem = n%10
            prod*=rem
            n=n//10
        return prod

    def smallestNumber(self, n: int, t: int) -> int:
        while(True):
            num = self.digitsProduct(n)
            if num%t==0:
                return n
            else:
                n+=1    