import tweepy
import config
import csv

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
query = 'safa -has:links  -is:retweet lang:id'

# field names
fields = ['id', 'text']
	
# data rows of csv file
rows = [ ]
i=1
# name of csv file
file_name = "FinalSafa4.csv"

with open(file_name, 'w', encoding="utf-8") as filehandler:
    csvwriter = csv.writer(filehandler)

    csvwriter.writerow(fields)
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=10).flatten(limit=250):
        rows.append([i,tweet.text])
        i=i+1

    csvwriter.writerows(rows)





#query = 'GOTO TLKM -has:links  -is:retweet lang:id'
#query = '"umur 29" -has:links  -is:retweet lang:id'
#query = 'kapolda -has:links  -is:retweet lang:id'
query = 'safa -has:links lang:id'