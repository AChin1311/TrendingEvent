import json
import pandas as pd
import sys
import time
from kw import features as kw_features

tweets_data_path = sys.argv[1]

tweets_data = []
tweets_text = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_text.append(tweet['text'].lower())
        tweets_data.append(tweet)
        
        print(tweet['text'])
    except:
        continue

print("Total Msg:")
print(len(tweets_data))


vectors = []
for tw in tweets_text:
    li = ['disaster','date','month','entertainment','holiday','action','price','time','logistics','sport','location']
    features ={}
    for l in li:
        features[l] = 0

    for w in tw.split():
        for l in li:
            if w in kw_features[l]:
                features[l] += 1

    tmp = []
    for l in features:
        tmp.append(features[l])
    if sum(tmp) == 0:
        continue
    vectors.append(tmp)
print(vectors)