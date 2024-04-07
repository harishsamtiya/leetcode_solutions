class Twitter:

    def __init__(self):
        self.users = [([], set()) for _ in range(500)]
        self.tweetTime = 2**31 - 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweets, followees = self.users[userId-1] 
        tweets.append((self.tweetTime, tweetId))
        self.tweetTime -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets, followees = self.users[userId-1] 
        followeesTweets = [] + tweets

        for followeId in followees:
            followeesTweets += self.users[followeId-1][0]
        
        heapify(followeesTweets)

        count = 0
        result = []
        while count < 10 and followeesTweets:
            tweetTime, tweetId = heappop(followeesTweets)
            result.append(tweetId)
            count += 1
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId-1][1].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId-1][1].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)