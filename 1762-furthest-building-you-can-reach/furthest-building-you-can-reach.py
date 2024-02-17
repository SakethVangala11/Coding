class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        for i in range(len(heights)-1):
            diff = heights[i+1]-heights[i]
            if diff<=0:
                continue
            bricks-=diff
            heapq.heappush(pq,-diff)
            if bricks<0:
                x = heapq.heappop(pq)
                bricks+=-x
                ladders-=1
            if ladders<0:
                return i
        return len(heights)-1
            

        