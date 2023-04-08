import tweepy
import config
client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
#'papua -is:retweet'
query = 'papua -has:links  -is:retweet'

response = client.search_recent_tweets(query=query, max_results=10, tweet_fields=['created_at', 'lang'], expansions=['author_id'])

users = {u['id']: u for u in response.includes['users']}

for tweet in response.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        print("id: ", tweet.id)
        print("text: ", tweet.text)
        print("Nama: ", user.name)
        print("Username: ", user.username)
        print(" ")
        print(" ")

