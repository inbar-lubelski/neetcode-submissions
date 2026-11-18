class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
            
        for i in range(len(stones)):
            stones[i]=stones[i]* -1
        
        heapq.heapify(stones)
        while len(stones)>=2:
            s1= (heapq.heappop(stones))*-1
            s2= (heapq.heappop(stones))*-1
            if s1>s2:
                heapq.heappush(stones, (s1-s2)*-1)
            if s2>s1:
                heapq.heappush(stones, (s2-s1)*-1)
            
        if stones:
            return stones[0]*-1
        else:
            return 0
            


        