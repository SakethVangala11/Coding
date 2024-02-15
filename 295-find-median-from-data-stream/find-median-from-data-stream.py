class MedianFinder:

    def __init__(self):
        self.q = []
        self.length = 0
        
    def addNum(self, num: int) -> None:
        self.q.append(num)
        self.length+=1

    def findMedian(self) -> float:
        self.q.sort()
        if self.length%2==0:
            return (self.q[self.length//2] + self.q[(self.length//2)-1])/2
        else:
            return self.q[self.length//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()