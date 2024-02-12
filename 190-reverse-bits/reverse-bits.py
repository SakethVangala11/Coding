class Solution:
    def reverseBits(self, n: int) -> int:
        sumo = 0
        for i in range(32):
            if n&1<<i:
                sumo+=2**(31-i)
        return sumo
        