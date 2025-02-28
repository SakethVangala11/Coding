class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set()
        res = 0
        for i in jewels:
            s.add(i)
        for i in stones:
            if i in s:
                res+=1
        return res
        
        