from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.small,self.large = [], []
        
    def addNum(self, num: int) -> None:
        #Push any element directly into small first
        heappush(self.small,-1*num)
        #Make sure that small array is small than large
        if self.small and self.large:
            if -1*self.small[0]>(self.large[0]):
                x = heappop(self.small)
                heappush(self.large,-1*x)
        #Make sure length of two arrays is almost equal
        if abs(len(self.small)-len(self.large))>1:
            if len(self.large)>len(self.small):
                x = heappop(self.large)
                heappush(self.small,-1*x)
            else:
                x = heappop(self.small)
                heappush(self.large,-1*x)
        
        
    def findMedian(self) -> float:
        #If both are equal length then small array max ele and large array min ele will be median
        if len(self.small)==len(self.large):
            return ((-1*self.small[0])+self.large[0])/2
        #Small array max ele is median
        elif len(self.small)>len(self.large):
            return -1*self.small[0]
        #large array min ele is median
        else:
            return self.large[0]
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()