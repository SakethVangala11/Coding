class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq= []
        for i in nums:
            heapq.heappush(pq,-i)
        while(k):
            x = heapq.heappop(pq)
            k-=1
        return -x


        