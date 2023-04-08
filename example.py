import tweepy
import config
import csv

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
query = 'papua -has:links  -is:retweet'
	
# field names
fields = ['id', 'text']
	
# data rows of csv file
rows = [ ]
i=1
# name of csv file
file_name = "data_twitter_dummy.csv"


with open(file_name, 'a+', encoding="utf-8") as filehandler:
    csvwriter = csv.writer(filehandler)

    csvwriter.writerow(fields)
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=10).flatten(limit=100):
        #print(tweet)
        rows.append([i,tweet.text])
        i=i+1
        #filehandler.write('%s\n' % tweet)
        #filehandler.write('%s\n' % tweet.text)

    csvwriter.writerows(rows)