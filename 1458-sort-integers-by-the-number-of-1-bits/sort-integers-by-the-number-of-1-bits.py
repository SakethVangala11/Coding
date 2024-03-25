import heapq
class Solution:
    def countBits(self,n):
        count = 0 
        for i in range(32):
            if (1<<i) & n:
                count+=1
        return count
    def sortByBits(self, arr: List[int]) -> List[int]:
        pq  = []
        for i in arr:
            count  = self.countBits(i)
            heapq.heappush(pq,(count,i))
        res = []
        while pq:
            x,y = heapq.heappop(pq)
            res.append(y)
        return res


        