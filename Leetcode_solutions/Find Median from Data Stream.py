class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list=[]
        

    def addNum(self, num: int) -> None:
        if len(self.list)==0:
            self.list.append(num)
        else:
            self.list.append(num)
            self.list.sort()
                    

    def findMedian(self) -> float:
        mid = len(self.list)//2
        if len(self.list)%2==0:
            return (self.list[mid] + self.list[mid-1])/2
        else:
            return self.list[mid]
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()