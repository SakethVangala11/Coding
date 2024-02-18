class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq=[]
        for i in stones:
            heapq.heappush(pq,-i)
        while(len(pq)>1):
            print(pq)
            x = -heapq.heappop(pq)
            y = -heapq.heappop(pq)
            if x!= y:
                heapq.heappush(pq,-abs(x-y))
        if(pq):
            return -pq[0]
        else:
            return 0




        