import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Heap Solution
        # pq = []
        # for (x,y) in points:
        #     dist = x*x+y*y
        #     if len(pq)<k:
        #         heapq.heappush(pq,(-dist,x,y))
        #     elif len(pq)==k:
        #         if dist < -pq[0][0]:
        #             heapq.heappushpop(pq,(-dist,x,y))
        # return [(x,y) for (dist,x,y) in pq]

        #Sorting solution
        points.sort(key = lambda x:x[0]**2+x[1]**2)
        return points[:k]
        
            


        