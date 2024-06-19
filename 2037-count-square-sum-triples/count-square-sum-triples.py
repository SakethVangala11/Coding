import math
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1,n+1):
            for b in range(1,n+1):
                c = math.sqrt(a**2 + b**2) 
                if c.is_integer() and c<=n:
                    count+=1

                
        return count
        