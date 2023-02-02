import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.userIdTweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userIdTweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        feed.extend(self.userIdTweets[userId])
        # print(self.userIdTweets)
        for followId in self.follows[userId]:
            feed.extend(self.userIdTweets[followId])
        heapq._heapify_max(feed)
        return([x[1] for x in heapq.nlargest(10, feed)])

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        print(self.follows[followerId])
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)