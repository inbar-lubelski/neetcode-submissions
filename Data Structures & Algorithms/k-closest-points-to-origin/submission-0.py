class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []
        min_heap=[]
        for x,y in points:
            min_heap.append([(x**2+y**2), x, y])

        heapq.heapify(min_heap)
        res=[]
        while k>0:
            cur= heapq.heappop(min_heap)
            res.append([cur[1],cur[2]])
            k-=1
        return res
        
        