class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        low = 1
        high = x

        while(low<=high):
            mid = (low+high)//2
            if low == mid:
                return low
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                high = mid
            else:
                low = mid
        
        