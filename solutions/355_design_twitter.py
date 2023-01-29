from collections import defaultdict, heapq


class Twitter:

    def __init__(self):
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.count = 0

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.tweet_map[user_id].append((self.count, tweet_id))
        self.count += 1

    def getNewsFeed(self, user_id: int) -> List[int]:
        feed = []

        max_heap = []

        self.follow_map[user_id].add(user_id)

        for followee_id in self.follow_map[user_id]:
            for count, tweet_id in self.tweet_map[followee_id]:
                heapq.heappush(max_heap, (-count, tweet_id))

        while len(feed) < 10 and max_heap:
            feed.append(heapq.heappop(max_heap)[1])

        return feed

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.follow_map[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if followee_id in self.follow_map[follower_id]:
            self.follow_map[follower_id].remove(followee_id)