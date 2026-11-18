class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
            
        for i in range(len(stones)):
            stones[i]=stones[i]* -1
        
        heapq.heapify(stones)
        while len(stones)>=2:
            s1= (heapq.heappop(stones))
            s2= (heapq.heappop(stones))
            if s1<s2:
                heapq.heappush(stones, (s1-s2))
            
        heapq.heappush(stones,0)
        return stones[0]*-1