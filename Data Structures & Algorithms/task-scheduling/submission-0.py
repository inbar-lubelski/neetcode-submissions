class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        freq_map={}
        for num in tasks:
            freq_map[num]= freq_map.get(num,0)+1

        count= [-val for val in freq_map.values()]
        heapq.heapify(count)
        q= collections.deque() 
        time=0
        while count or q:
            time+=1
            if count:
                cnt = heapq.heappop(count) +1
                if cnt!=0:
                    q.append([cnt, n+time])
            if q and q[0][1]== time:
                heapq.heappush(count,q.popleft()[0])
        return time

            
        