import heapq
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pq = []
        res = []
        for i in range(len(heights)):
            heapq.heappush(pq, (-1*heights[i], i))
        
        while(pq):
            x = heapq.heappop(pq)
            res.append(names[x[1]])
        
        return res
            
        