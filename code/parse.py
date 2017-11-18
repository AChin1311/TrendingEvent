import json
import pandas as pd
import matplotlib.pyplot as plt
import sys
import time

tweets_data_path = sys.argv[1]

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
        #print(tweet['text'])
    except:
        continue

print("Total Msg:")
print(len(tweets_data))

tweets = pd.DataFrame()
tweets['text'] = list(map(lambda tweet: tweet.get('text'), tweets_data))
tweets['lang'] = list(map(lambda tweet: tweet.get('lang'), tweets_data))
tweets['created_at'] = list(map(lambda tweet: tweet.get('created_at'), tweets_data))
tweets['country'] = list(map(lambda tweet: tweet['place'].get('country') if tweet.get('place') != None else None, tweets_data))


for i in range(len(tweets_data)):
    time.sleep(1)
    print(tweets['text'][i])
    if(tweets['country'][i]!=None):
        print(tweets['country'][i])
    print(tweets['created_at'][i])
    

#Plot top 5 country
tweets_by_country = tweets['country'].value_counts()
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Country', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 Country', fontsize=15, fontweight='bold')
#tweets_by_country[:5].plot(ax=ax, kind='bar', color='red')
#plt.show()

