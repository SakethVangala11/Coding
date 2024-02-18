class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []
        nums.sort(reverse = True)
        count=0
        for i in nums:
            if(k):
                heapq.heappush(self.pq,i)
                k-=1

    def add(self, val: int) -> int:
        if len(self.pq)!=self.k:
            heapq.heappush(self.pq,val)
        elif val>self.pq[0]:
            heapq.heappop(self.pq)
            heapq.heappush(self.pq,val)
        return self.pq[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)