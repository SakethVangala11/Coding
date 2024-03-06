import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <=0:
            return False
        x  = math.log(n,2)/2
        if x.is_integer():
            return True
        else:
            return False

        