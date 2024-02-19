class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        count=0
        for i in range(32):
            if(n&1<<i):
                count+=1
        if count==1:
            return True
        return False
        