class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        res = high
        def isPossible(capacity):
            curSum = 0
            ships = 1
            for i in weights:
                if curSum+i<=capacity:
                    curSum+=i
                else:
                    curSum = 0
                    curSum+=i
                    ships+=1
            if ships<=days:
                return True

        while(low<=high):
            capacity = (low+high)//2
            if isPossible(capacity):
                res = min(res, capacity)
                high = capacity - 1
            else:
                low = capacity + 1

        return res

        