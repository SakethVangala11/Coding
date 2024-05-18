import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = []

        for i in gifts:
            heapq.heappush(pq, -1*i)
        
        while(k):
            x = heapq.heappop(pq)
            heapq.heappush(pq, -1*(math.floor(math.sqrt(-1*x))))
            k-=1
        return -1*sum(pq)


        