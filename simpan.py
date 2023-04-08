import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
query = 'papua -has:links  -is:retweet'

file_name = 'tweets.csv'

with open(file_name, 'a+', encoding="utf-8") as filehandler:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=10).flatten(limit=100):
        #print(tweet)
        filehandler.write('%s\n' % tweet)
        #filehandler.write('%s\n' % tweet.text)