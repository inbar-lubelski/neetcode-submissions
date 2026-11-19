class MedianFinder:

    def __init__(self):
        self.max_heap=[]
        self.min_heap=[]
        

    def addNum(self, num: int) -> None:
        if self.min_heap and num>self.min_heap[0]:
            heapq.heappush(self.min_heap,num)
        else:
            heapq.heappush(self.max_heap,num*-1)
        
        if len(self.max_heap)>1+ len(self.min_heap):
            val= heapq.heappop(self.max_heap)*-1
            heapq.heappush(self.min_heap,val)
        if len(self.max_heap)+1< len(self.min_heap):
            val= heapq.heappop(self.min_heap)*-1
            heapq.heappush(self.max_heap,val)
            
        

    def findMedian(self) -> float:
        if len(self.max_heap)== len(self.min_heap):
            return ((self.max_heap[0]*-1)+self.min_heap[0])/2
        return self.max_heap[0]*-1 if len(self.max_heap)> len(self.min_heap) else self.min_heap[0]
        
        