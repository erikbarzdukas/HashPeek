import tweepy

api = tweepy.API()
tweets = api.public_timeline()

for tweet in tweets:
    print tweet
