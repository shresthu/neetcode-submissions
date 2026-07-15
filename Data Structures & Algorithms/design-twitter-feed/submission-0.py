class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetmap = defaultdict(list) #here it is list, going from oldest -> latest
        self.followmap = defaultdict(set) #here it is set

    def postTweet(self, userId: int, tweetId: int) -> None:
        #to post the tweet it will be creation of a tweet
        self.tweetmap[userId].append([self.count,tweetId])
        self.count -= 1 #this way we are going to build a list of negative timestamp values of tweets

    def getNewsFeed(self, userId: int) -> List[int]:
        #this will be done in 2 steps, first we will need to essentially build a heap of the latest tweets
        #and the next extract the top 10 ones from the start
        res = [] #this will hold the final 10 tweets
        minheap = [] #this will be the minHeap which holds the tweets in order from which we will extract

        #build the minHeap
        self.followmap[userId].add(userId)

        #travers the list of followers
        for followeeid in self.followmap[userId]: 
            if followeeid in self.tweetmap: #if no tweets by this user ignore it
                index = len(self.tweetmap[followeeid]) - 1 #go from the last tweet(the latest tweet)
                count, tweetid = self.tweetmap[followeeid][index] #extract the last tweet
                minheap.append([count,tweetid,followeeid,index-1])
        #so now at this point we are storing the last tweets across all the followers
        # [[last tweet from user 2],[last tweet from user 3], [last tweet from user 1]] for user 1
        heapq.heapify(minheap) #this will make is so the most -ve val (latest tweet across users) will be at top

        #now that we have a heap of the latest tweets, lets extract the top and keep adding to heap until we have 10
        while minheap and len(res) < 10:
            #now we extract the top tweet
            count, tweetid, followeeid, index = heapq.heappop(minheap) #pop the latest tweet
            #lets add the tweet to the list
            res.append(tweetid)

            #now lets extract the next latest tweet from the user whose tweet we just consumed
            if index >= 0: #if the user has more tweets
                count, tweetid = self.tweetmap[followeeid][index]
                heapq.heappush(minheap,[count,tweetid,followeeid,index-1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        #this would mean the followee id gets added to followmap
        self.followmap[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
