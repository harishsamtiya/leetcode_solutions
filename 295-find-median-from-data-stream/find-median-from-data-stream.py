class MedianFinder:

    def __init__(self):
        self.LeftHeap = []
        self.RightHeap = []
        self.LenL = 0
        self.LenR = 0

    def addNum(self, num: int) -> None:
        
        if not self.LeftHeap:
            heappush(self.LeftHeap, -num)
            self.LenL += 1
        else:
            leftTop = - self.LeftHeap[0]

            if leftTop < num:
                heappush(self.RightHeap, num)
                self.LenR += 1
                if self.LenL < self.LenR:
                    num = heappop(self.RightHeap)
                    self.LenR -= 1
                    heappush(self.LeftHeap, -num)
                    self.LenL += 1
            else:
                heappush(self.LeftHeap, -num)
                self.LenL += 1
                if self.LenL  > self.LenR + 1:
                    num = heappop(self.LeftHeap)
                    self.LenL -= 1
                    heappush(self.RightHeap, -num)
                    self.LenR += 1
            

    def findMedian(self) -> float:
        num1 = -self.LeftHeap[0]
        if self.LenL == self.LenR:
            num2 = self.RightHeap[0]
            return (num1 + num2)/2
        return num1
        



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()