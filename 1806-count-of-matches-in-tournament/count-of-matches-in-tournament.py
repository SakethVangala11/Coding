import math
class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while(n>1):
            ans+=n//2
            n = math.ceil(n/2)
        return ans
        