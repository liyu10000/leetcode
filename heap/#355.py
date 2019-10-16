import heapq

class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.feed = dict()
        self.followers = dict()
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.count += 1
        
        if userId not in self.feed:
            self.feed[userId] = []
            
            if userId not in self.followers:
                self.followers[userId] = set()
                
        self.feed[userId].append((self.count, tweetId))
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        return self.get_top_K_tweets(userId)
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.followers:
            self.followers[followerId] = set()
        
        if followeeId != followerId:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
            
            if len(self.followers[followerId]) == 0:
                del self.followers[followerId]
                
                
    def get_top_K_tweets(self, userId, k = 10):
        heap = []
        
        if userId in self.followers and len(self.followers[userId]) > 0:
            for followed in self.followers[userId]:
                if followed in self.feed:
                    f = self.feed[followed]
                    
                    i = len(f) - 1
                    heap.append((-1 * f[i][0], f[i][1], followed, i))
                        
        if userId in self.feed:
            f = self.feed[userId]

            i = len(f) - 1
            heap.append((-1 * f[i][0], f[i][1], userId, i))
                
        heapq.heapify(heap)
        
        res = []
        count = 0
        
        while count < k and heap:
            _, tweetId, user, idx = heapq.heappop(heap)
            
            res.append(tweetId)
            
            idx -= 1
            if idx >= max(0, len(self.feed[user]) - k):
                heapq.heappush(heap, (-1 * self.feed[user][idx][0], self.feed[user][idx][1], user, idx))
                
            count += 1
            
        return res


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)