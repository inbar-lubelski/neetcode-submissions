import collections
class Twitter:

    def __init__(self):
        self.map_follow= collections.defaultdict(set)
        self.map_post = collections.defaultdict(list)
        self.count =0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.map_post[userId].append((self.count,tweetId))
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        max_heap= []
        sources = set(self.map_follow[userId])
        sources.add(userId)
        for f in sources:
            if f in self.map_post:
                idx= len(self.map_post[f])-1
                post= self.map_post[f][idx]
                max_heap.append([post[0],post[1],f ,idx-1])
        heapq.heapify(max_heap)
        while max_heap and len(res)<10:
            count,tweetId,followeeId, idx=  heapq.heappop(max_heap)
            res.append(tweetId)
            if idx>=0:
                next_post = self.map_post[followeeId][idx]
                to_add= [next_post[0],next_post[1],followeeId ,idx-1]
                heapq.heappush(max_heap,to_add)
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.map_follow[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.map_follow[followerId].discard(followeeId)

        
