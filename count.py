import tweepy
import config
#place_country:US
client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
query = 'papua -has:links  -is:retweet'

counts = client.get_recent_tweets_count(query=query, granularity='day')

for count in counts.data:
    print(count)